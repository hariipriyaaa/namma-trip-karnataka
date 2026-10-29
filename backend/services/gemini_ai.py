"""Optional Gemini adapter. Curated ground data remains the reliable fallback."""
import json
from typing import Optional
from backend.config import GEMINI_API_KEY, GEMINI_MODEL

def generate_with_gemini(grounded_itinerary: dict, user_preferences: dict) -> Optional[dict]:
    """Ask Gemini to improve descriptive text while retaining the grounded stop list/costs.

    This function intentionally returns None if the key/library/network is unavailable.
    It does not invent live opening hours, ticket prices, transport timetables or bookings.
    """
    if not GEMINI_API_KEY:
        return None
    try:
        from google import genai
        client = genai.Client(api_key=GEMINI_API_KEY)
        prompt = (
            "You are a careful Karnataka travel writing assistant. Rewrite only the "
            "description and stop descriptions in the supplied itinerary to be helpful and "
            "culturally respectful. Do not change stop names, stop count, costs, day order, "
            "transit advice, foods, or notes. Do not claim live availability or exact current "
            "timetables. Return valid JSON with the same schema. User preferences: "
            + json.dumps(user_preferences, ensure_ascii=False)
            + "\nGrounded itinerary JSON:\n"
            + json.dumps(grounded_itinerary, ensure_ascii=False)
        )
        response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
        text = (response.text or "").strip()
        if text.startswith("```"):
            text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
        candidate = json.loads(text)
        # Preserve trusted structural and numerical fields from curated data.
        # Preserve the curated itinerary structure. Models can accidentally cross-wire
        # a stop description with another stop, invent a stop, or alter the schedule.
        # Keep all stop names, order, day grouping, descriptions and costs grounded.
        for field in ("circuit_id", "circuit_name", "region", "days", "max_days", "requested_days",
                      "style", "interests", "transit_recommendation", "estimated_total",
                      "daily_budget", "estimated_total_min", "estimated_total_max", "budget_breakdown",
                      "foods", "days_schedule", "notes", "generated_by"):
            if field in grounded_itinerary:
                candidate[field] = grounded_itinerary[field]
        candidate["generated_by"] = "curated-ground-data+gemini-description"
        return candidate
    except Exception:
        return None
