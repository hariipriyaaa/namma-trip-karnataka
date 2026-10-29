from backend.services import route_planner as planner


def sample_itinerary():
    return {
        "region": "Malnad & Western Ghats",
        "circuit_name": "Malnad",
        "days": 2,
        "days_schedule": [
            {"day": 1, "title": "Day 1: A", "stops": [
                {"time": "Morning", "name": "A", "description": "a", "category": "Nature", "cost": 0},
                {"time": "Afternoon", "name": "B", "description": "b", "category": "Nature", "cost": 0},
            ]},
            {"day": 2, "title": "Day 2: C", "stops": [
                {"time": "Morning", "name": "C", "description": "c", "category": "Food", "cost": 0},
                {"time": "Evening", "name": "D", "description": "d", "category": "Adventure", "cost": 0},
            ]},
        ],
    }


def test_disabled_is_explicit_and_does_not_claim_distance(monkeypatch):
    monkeypatch.setattr(planner, "ENABLED", False)
    result = planner.optimize_itinerary_routes(sample_itinerary())
    assert result["route_plan"]["status"] == "disabled"
    assert result["route_plan"]["distance_km"] is None
    assert result["days_schedule"][0]["stops"][0]["name"] == "A"


def test_global_route_reorders_stops_across_day_clusters(monkeypatch):
    monkeypatch.setattr(planner, "ENABLED", True)
    points = {"A": (0.0, 0.0), "B": (1.0, 0.0), "C": (2.0, 0.0), "D": (3.0, 0.0)}
    monkeypatch.setattr(planner, "_geocode", lambda name, region: points[name])
    # Distances make A -> C -> B -> D the best global sequence, unlike source A -> B / C -> D.
    matrix = [
        [0, 90, 10, 100],
        [90, 0, 10, 10],
        [10, 10, 0, 90],
        [100, 10, 90, 0],
    ]
    durations = [[value * 60 for value in row] for row in matrix]
    monkeypatch.setattr(planner, "_road_table", lambda coords: (matrix, durations))
    result = planner.optimize_itinerary_routes(sample_itinerary())
    assert result["route_plan"]["status"] == "optimised"
    assert result["route_plan"]["day_to_day_continuity"] is True
    names = [[stop["name"] for stop in day["stops"]] for day in result["days_schedule"]]
    assert names == [["A", "C"], ["B", "D"]]
    assert result["days_schedule"][1]["transfer_from_previous_day"]["distance_km"] is not None
    assert [stop["time"] for stop in result["days_schedule"][0]["stops"]] == ["Morning", "Afternoon"]


def test_geocode_failure_preserves_original_schedule(monkeypatch):
    monkeypatch.setattr(planner, "ENABLED", True)
    monkeypatch.setattr(planner, "_geocode", lambda name, region: None if name == "C" else (76.0, 13.0))
    result = planner.optimize_itinerary_routes(sample_itinerary())
    assert result["route_plan"]["status"] == "unverified"
    assert result["route_plan"]["distance_km"] is None
    assert result["days_schedule"][1]["stops"][0]["name"] == "C"
