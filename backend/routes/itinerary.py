from fastapi import APIRouter
from backend.models.schemas import ItineraryRequest, ItineraryResponse
from backend.services.ground_data import CIRCUITS, build_grounded_itinerary, get_circuit_list
from backend.services.gemini_ai import generate_with_gemini
from backend.services.route_planner import optimize_itinerary_routes

router = APIRouter(prefix="/itinerary", tags=["Itinerary"])

@router.get("/circuits")
def list_circuits():
    return {"count": len(CIRCUITS), "circuits": get_circuit_list()}

@router.post("/generate", response_model=ItineraryResponse)
def generate_itinerary(request: ItineraryRequest):
    payload = request.model_dump()
    itinerary = build_grounded_itinerary(payload)
    ai_result = generate_with_gemini(itinerary, payload)
    if ai_result:
        itinerary = ai_result
    return optimize_itinerary_routes(itinerary)
