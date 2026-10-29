import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from backend.models.schemas import DialectResponse

router = APIRouter(prefix="/dialect", tags=["Regional Kannada"])
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "dialects.json"

def read_dialects():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

@router.get("")
def list_dialects():
    data = read_dialects()
    return {"dialects": [{"key": k, "name": v["name"], "description": v["description"]}
                         for k, v in data.items()]}

@router.get("/{key}", response_model=DialectResponse)
def get_dialect(key: str):
    data = read_dialects()
    if key not in data:
        raise HTTPException(status_code=404, detail="Dialect not found. Use uttara, coastal, mysuru or malnad.")
    return {"key": key, **data[key]}
