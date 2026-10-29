"""Geographic route continuity for NammaTrip itineraries.

Uses geocoding plus OSRM driving-road matrices only when enabled. It never
fabricates road distances: failed/ambiguous lookups leave the curated schedule
unchanged and explicitly mark the route as unverified.
"""
from __future__ import annotations

import os
from functools import lru_cache
from typing import Any

import httpx

NOMINATIM_URL = os.getenv("NAMMATRIP_GEOCODER_URL", "https://nominatim.openstreetmap.org/search")
OSRM_BASE_URL = os.getenv("NAMMATRIP_OSRM_URL", "https://router.project-osrm.org")
ENABLED = os.getenv("NAMMATRIP_ROUTE_OPTIMIZATION", "false").strip().lower() in {"1", "true", "yes", "on"}
PROVIDER = "OpenStreetMap Nominatim + OSRM"


@lru_cache(maxsize=512)
def _geocode(place: str, region: str) -> tuple[float, float] | None:
    """Resolve a stop name; cache results to reduce repeat requests."""
    query = f"{place}, {region}, Karnataka, India"
    try:
        response = httpx.get(
            NOMINATIM_URL,
            params={"q": query, "format": "jsonv2", "limit": 1, "countrycodes": "in"},
            headers={"User-Agent": "NammaTrip/1.0 (Karnataka travel route planning)"},
            timeout=5.0,
        )
        response.raise_for_status()
        rows = response.json()
        if not rows:
            return None
        row = rows[0]
        # Reject results outside Karnataka's broad geographic bounds to reduce
        # the risk of silently routing to a same-named place elsewhere.
        lon, lat = float(row["lon"]), float(row["lat"])
        if not (73.5 <= lon <= 78.8 and 11.0 <= lat <= 19.0):
            return None
        return lon, lat
    except (httpx.HTTPError, ValueError, KeyError, TypeError, IndexError):
        return None


def _road_table(coords: list[tuple[float, float]]) -> tuple[list[list[float | None]], list[list[float | None]]] | None:
    if len(coords) < 2:
        return ([[0.0]], [[0.0]])
    coord_text = ";".join(f"{lon},{lat}" for lon, lat in coords)
    try:
        response = httpx.get(
            f"{OSRM_BASE_URL.rstrip('/')}/table/v1/driving/{coord_text}",
            params={"annotations": "distance,duration"}, timeout=12.0,
        )
        response.raise_for_status()
        payload = response.json()
        if payload.get("code") != "Ok":
            return None
        distances, durations = payload.get("distances"), payload.get("durations")
        n = len(coords)
        if not (isinstance(distances, list) and isinstance(durations, list)
                and len(distances) == n and len(durations) == n
                and all(isinstance(r, list) and len(r) == n for r in distances)
                and all(isinstance(r, list) and len(r) == n for r in durations)):
            return None
        return distances, durations
    except (httpx.HTTPError, ValueError, TypeError):
        return None


def _nearest_global_order(distances: list[list[float | None]]) -> list[int] | None:
    """Nearest-neighbour global route, anchored at the first curated stop."""
    n = len(distances)
    if n <= 1:
        return list(range(n))
    remaining = set(range(1, n))
    order = [0]
    while remaining:
        current = order[-1]
        options = [(distances[current][j], j) for j in remaining
                   if distances[current][j] is not None]
        if not options:
            return None
        _, next_index = min(options, key=lambda pair: pair[0])
        order.append(next_index)
        remaining.remove(next_index)
    return order


def _two_opt(order: list[int], distances: list[list[float | None]], max_passes: int = 8) -> list[int]:
    """Improve route length without changing the anchored first stop."""
    best = order[:]
    def leg(a: int, b: int) -> float:
        value = distances[a][b]
        return float(value) if value is not None else float("inf")
    for _ in range(max_passes):
        changed = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best) - 1):
                a, b = best[i - 1], best[i]
                c, d = best[j], best[j + 1]
                if leg(a, c) + leg(b, d) + 0.001 < leg(a, b) + leg(c, d):
                    best[i:j + 1] = reversed(best[i:j + 1])
                    changed = True
        if not changed:
            break
    return best


def _unverified(result: dict[str, Any], status: str, message: str) -> dict[str, Any]:
    result["route_plan"] = {
        "status": status,
        "provider": PROVIDER,
        "distance_km": None,
        "message": message,
        "scope": "No verified road route is available; curated day and stop order is preserved.",
    }
    return result


def optimize_itinerary_routes(itinerary: dict[str, Any]) -> dict[str, Any]:
    """Optimise stop order within days AND order stop clusters across days.

    Day stop counts are preserved. A global road route is ordered first, then
    split into the original day's stop counts; time labels are reassigned to
    morning/afternoon/evening so slots remain chronological.
    """
    result = dict(itinerary)
    source_days = result.get("days_schedule", [])
    if not ENABLED:
        return _unverified(
            result, "disabled",
            "Route continuity is implemented but live road optimisation is disabled. Set NAMMATRIP_ROUTE_OPTIMIZATION=true and configure a routing service to enable geographic ordering. No distances are claimed as verified.",
        )

    days = [dict(day) for day in source_days]
    all_stops = [dict(stop) for day in days for stop in day.get("stops", [])]
    if len(all_stops) < 2:
        return _unverified(result, "insufficient_stops", "At least two stops are needed to calculate a road route.")

    region = str(result.get("region") or result.get("circuit_name") or "Karnataka")
    coordinates = [_geocode(str(stop.get("name", "")), region) for stop in all_stops]
    if any(point is None for point in coordinates):
        return _unverified(
            result, "unverified",
            "One or more stop names could not be reliably located in Karnataka. The original itinerary is preserved; no distances are shown.",
        )
    coords = [point for point in coordinates if point is not None]
    table = _road_table(coords)
    if table is None:
        return _unverified(
            result, "unverified",
            "The road-routing service did not return a complete driving matrix. The original itinerary is preserved; no distances are shown.",
        )
    distances, durations = table
    order = _nearest_global_order(distances)
    if order is None:
        return _unverified(
            result, "unverified",
            "The road network could not connect every stop. The original itinerary is preserved; no distances are shown.",
        )
    order = _two_opt(order, distances)

    capacities = [len(day.get("stops", [])) for day in days]
    cursor = 0
    total_m = 0.0
    total_seconds = 0.0
    legs = []
    previous = None
    for day_idx, (day, capacity) in enumerate(zip(days, capacities), start=1):
        indexes = order[cursor:cursor + capacity]
        cursor += capacity
        day_stops = [all_stops[i] for i in indexes]
        slots = [str(s.get("time") or default) for s, default in zip(day_stops, ["Morning", "Afternoon", "Evening"] * ((len(day_stops) + 2) // 3))]
        # Keep the visible timeline chronological even when stops move between days.
        defaults = ["Morning", "Afternoon", "Evening"]
        for i, stop in enumerate(day_stops):
            stop["time"] = defaults[min(i, 2)]
        day["stops"] = day_stops
        if day_stops:
            day["title"] = f"Day {day_idx}: {day_stops[0].get('name', 'Regional route')}"
        day_legs = []
        for a, b in zip(indexes, indexes[1:]):
            metres, seconds = distances[a][b], durations[a][b]
            if metres is None or seconds is None:
                return _unverified(result, "unverified", "A road leg is missing from the routing matrix. The original itinerary is preserved; no distances are shown.")
            total_m += float(metres)
            total_seconds += float(seconds)
            day_legs.append({"from": all_stops[a].get("name"), "to": all_stops[b].get("name"), "distance_km": round(float(metres) / 1000, 1), "drive_minutes": round(float(seconds) / 60)})
        if day_legs:
            day["route_summary"] = {"legs": day_legs, "distance_km": round(sum(x["distance_km"] for x in day_legs), 1), "drive_minutes": sum(x["drive_minutes"] for x in day_legs)}
        else:
            day["route_summary"] = {"legs": [], "distance_km": 0, "drive_minutes": 0}
        if previous is not None and indexes:
            metres, seconds = distances[previous][indexes[0]], durations[previous][indexes[0]]
            if metres is None or seconds is None:
                return _unverified(result, "unverified", "The routing service could not verify the transfer between day clusters. The original itinerary is preserved; no distances are shown.")
            total_m += float(metres)
            total_seconds += float(seconds)
            day["transfer_from_previous_day"] = {"distance_km": round(float(metres) / 1000, 1), "drive_minutes": round(float(seconds) / 60), "note": "Estimated driving leg between day clusters; overnight accommodation and actual departure point must be confirmed."}
        if indexes:
            previous = indexes[-1]
    result["days_schedule"] = days
    result["route_plan"] = {
        "status": "optimised",
        "provider": PROVIDER,
        "distance_km": round(total_m / 1000, 1),
        "estimated_drive_minutes": round(total_seconds / 60),
        "distance_basis": "OSRM driving-road matrix. Includes within-day legs and transfers between consecutive day clusters; excludes travel to/from the circuit and live traffic delays.",
        "day_to_day_continuity": True,
        "message": "Stops are ordered as one continuous road sequence and then grouped into the planned days. Daily drive estimates are routing estimates, not live traffic. Confirm accommodation, opening hours, permits, seasonal access and route conditions before travel.",
    }
    return result
