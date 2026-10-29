from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_circuits_endpoint_returns_ten_circuits():
    response = client.get("/api/itinerary/circuits")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 10
    assert len(data["circuits"]) == 10

def test_itinerary_has_requested_days_and_unique_stops():
    response = client.post("/api/itinerary/generate", json={
        "circuit": "wildlife", "days": 4, "style": "Comfort",
        "interests": ["Ghats, Falls & Treks"]
    })
    assert response.status_code == 200
    data = response.json()
    assert 1 <= data["days"] <= 4
    assert len(data["days_schedule"]) == data["days"]
    names = [stop["name"] for day in data["days_schedule"] for stop in day["stops"]]
    assert names and len(names) == len(set(names))
    assert all(any(word in (stop["name"] + " " + stop["category"]).lower()
                   for word in ("nature", "waterfall", "falls", "forest", "lake", "viewpoint",
                                "wildlife", "coast", "beach", "island", "dam", "landscape",
                                "bird", "rainforest", "river", "hill station", "scenic",
                                "garden", "sanctuary"))
               for day in data["days_schedule"] for stop in day["stops"])

def test_invalid_duration_rejected():
    response = client.post("/api/itinerary/generate", json={
        "circuit": "wildlife", "days": 11, "style": "Comfort", "interests": []
    })
    assert response.status_code == 422

def test_dialect_endpoint():
    response = client.get("/api/dialect/uttara")
    assert response.status_code == 200
    assert response.json()["key"] == "uttara"
    assert response.json()["phrases"]


def test_coastal_duration_is_limited_and_no_generic_fillers():
    response = client.post("/api/itinerary/generate", json={
        "circuit": "coastal", "days": 7, "style": "Comfort", "interests": []
    })
    assert response.status_code == 200
    data = response.json()
    assert data["days"] == 4
    names = [stop["name"] for day in data["days_schedule"] for stop in day["stops"]]
    assert len(names) == 12 and len(names) == len(set(names))
    assert not any("sunset viewpoint" in name.lower() or "market walk" in name.lower() or "local coastal" in name.lower() for name in names)


def test_mysuru_royal_route_supports_seven_days_with_named_stops():
    response = client.post("/api/itinerary/generate", json={
        "circuit": "royal", "days": 7, "style": "Comfort", "interests": []
    })
    assert response.status_code == 200
    data = response.json()
    assert data["days"] == 7
    names = [stop["name"] for day in data["days_schedule"] for stop in day["stops"]]
    assert len(names) == 21 and len(names) == len(set(names))
    assert not any("local food stop" in name.lower() or "flexible buffer" in name.lower() for name in names)


def test_all_circuit_duration_caps_and_unique_stops():
    from backend.services.ground_data import CIRCUITS, CIRCUIT_MAX_DAYS, build_grounded_itinerary

    for circuit_id, circuit in CIRCUITS.items():
        cap = CIRCUIT_MAX_DAYS[circuit_id]
        result = build_grounded_itinerary({
            "circuit": circuit_id, "days": 7, "style": "Comfort", "interests": []
        })
        assert result["days"] <= cap, circuit_id
        names = [stop["name"] for day in result["days_schedule"] for stop in day["stops"]]
        assert len(names) == len(set(names)), circuit_id
        assert all(name.strip() for name in names), circuit_id
        assert len(names) == result["days"] * 3, circuit_id

def test_budget_breakdown_is_itemised_and_ticket_costs_do_not_scale_with_style():
    comfort = client.post("/api/itinerary/generate", json={
        "circuit": "hoysala", "days": 4, "style": "Comfort", "interests": []
    }).json()
    budget = comfort["budget_breakdown"]
    assert budget["meals"]["breakfast"]
    assert budget["meals"]["lunch"]
    assert budget["meals"]["dinner"]
    assert budget["nights_assumed"] == 3
    assert comfort["estimated_total_min"] < comfort["estimated_total_max"]
    assert comfort["days_schedule"][0]["stops"][0]["cost"] == 0  # Belur temple darshan: no admission fee included

    premium = client.post("/api/itinerary/generate", json={
        "circuit": "hoysala", "days": 4, "style": "Premium", "interests": []
    }).json()
    comfort_palace = next(s for day in comfort["days_schedule"] for s in day["stops"] if s["name"] == "Mysore Palace")
    premium_palace = next(s for day in premium["days_schedule"] for s in day["stops"] if s["name"] == "Mysore Palace")
    assert comfort_palace["cost"] == premium_palace["cost"] == 120
