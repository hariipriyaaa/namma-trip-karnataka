# Namma Trip (ನಮ್ಮ ಟ್ರಿಪ್) — AI Karunadu Grand Circuit

A responsive, Kannada-aware travel planner for exploring Karnataka. Built for the **Kannada Technology Challenge — Problem Statement 06**, Namma Trip helps travellers create day-by-day itineraries across curated regional circuits, explore regional Kannada phrases, estimate trip expenses, and save or print their plans.

> **Travel information notice:** This project provides curated planning guidance and indicative cost estimates. It does not provide live traffic, transport schedules, ticket availability, or confirmed bookings. Check current prices, opening hours, weather, access rules, and local safety guidance before travelling. Gemini integration is optional; the app can fall back to curated content.

## Table of contents

- [Highlights](#highlights)
- [Technology stack](#technology-stack)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Getting started](#getting-started)
  - [Windows](#windows)
  - [macOS and Linux](#macos-and-linux)
  - [Run the frontend](#run-the-frontend)
- [Optional Gemini integration](#optional-gemini-integration)
- [API reference](#api-reference)
- [Run tests](#run-tests)
- [Run with Docker](#run-with-docker)
- [Deployment](#deployment)
- [Budget estimates and limitations](#budget-estimates-and-limitations)
- [Security notes](#security-notes)

## Highlights

- **Curated Karnataka circuits:** Ten regional circuits spanning coastal Karnataka, Malnad, heritage destinations, North Karnataka, Bengaluru, Mysuru/Kodagu, and Uttara Kannada.
- **Day-by-day itineraries:** Generate trips from 1 to 7 days, subject to each circuit's supported duration and available curated stops.
- **Three stops per day:** Itinerary generation uses named curated attractions and avoids repeating stop names within a generated trip.
- **Travel styles:** Budget, Comfort, and Premium planning estimates.
- **Regional Kannada phrasebook:** Phrase groups for Uttara Karnataka, coastal Karnataka, Mysuru, and Malnad.
- **Browser text-to-speech:** Listen to phrases when a Kannada voice is available in the browser.
- **Save and print:** Save itineraries in browser `localStorage`, track checked-stop costs, and print or save a trip as PDF through the browser print dialog.
- **Itemised budget guidance:** Indicative estimates for meals, accommodation, local transport, and listed activities.
- **FastAPI backend:** Validated request schemas, API endpoints, CORS configuration, and interactive OpenAPI documentation.
- **Optional Gemini enhancement:** Gemini can enhance descriptive text; curated itinerary data remains the source of truth, with fallback content when the service is unavailable.
- **Frontend fallback:** The frontend can be opened directly for a basic demo without running the backend.

## Technology stack

| Area | Technologies |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| API documentation | OpenAPI / Swagger UI |
| Optional AI integration | Gemini API |
| Testing | pytest, HTTPX |
| Local persistence | Browser `localStorage` |
| Containerisation | Docker, Docker Compose |

## Project structure

```text
namma-trip-karnataka/
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── itinerary.py
│   │   └── dialect.py
│   ├── services/
│   │   ├── gemini_ai.py
│   │   └── ground_data.py
│   ├── data/
│   │   └── dialects.json
│   └── requirements.txt
├── tests/
│   └── test_api.py
├── scripts/
│   ├── run_dev.sh
│   └── run_dev.bat
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Requirements

- Python **3.11 or 3.12**
- A modern web browser
- Git (recommended)
- Docker and Docker Compose, only if you want to run the backend in a container
- A Gemini API key only if you want to enable the optional Gemini enhancement

## Getting started

Run these commands from the **project root directory**.

### Windows

1. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

2. Activate it:

   ```powershell
   .venv\Scripts\activate
   ```

3. Install the backend dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r backend\requirements.txt
   ```

4. Start the API server:

   ```powershell
   python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
   ```

5. Open the API documentation:

   **http://127.0.0.1:8000/docs**

### macOS and Linux

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r backend/requirements.txt
   ```

3. Start the API server:

   ```bash
   python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
   ```

4. Open **http://127.0.0.1:8000/docs**.

### Run the frontend

You can open `frontend/index.html` directly in a browser for a basic demo. To serve the frontend locally, open a **second terminal** at the project root.

**Windows:**

```powershell
py -m http.server 5500 --directory frontend
```

**macOS/Linux:**

```bash
python3 -m http.server 5500 --directory frontend
```

Then visit **http://127.0.0.1:5500**.

#### Connect the frontend to the local API

If the frontend is served separately, configure its API base URL before using backend-powered features. In the browser developer console, run:

```javascript
window.NAMMA_TRIP_API = "http://127.0.0.1:8000";
location.reload();
```

For a persistent local setting, update the `API_BASE` constant near the top of `frontend/js/app.js` to:

```javascript
const API_BASE = "http://127.0.0.1:8000";
```

If you deploy the frontend and backend separately, set the API base to the deployed backend URL and configure the backend's `FRONTEND_ORIGINS` environment variable for the deployed frontend origin.

## Optional Gemini integration

Gemini is optional. The curated itinerary data remains the source of truth for attraction names, itinerary structure, route notes, and estimated costs. Gemini is used only to enhance descriptive text. If no API key is configured or the service is unavailable, the app can use curated fallback content.

1. Copy `.env.example` to `.env`.
2. Add your own key to the `GEMINI_API_KEY` setting.
3. Install the backend dependencies and restart the API.

Keep `.env` private and never commit API keys to a public repository. Leave the key unset if you do not need Gemini-enhanced descriptions.

## API reference

When the backend is running, interactive API documentation is available at **http://127.0.0.1:8000/docs**.

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | API metadata |
| `GET` | `/health` | Health check |
| `GET` | `/api/itinerary/circuits` | List the ten curated circuits |
| `POST` | `/api/itinerary/generate` | Generate an itinerary from a circuit, duration, style, and interests |
| `GET` | `/api/dialect` | List available Kannada phrase groups |
| `GET` | `/api/dialect/{key}` | Retrieve a phrase group |
| `GET` | `/docs` | Interactive Swagger UI |

Supported phrase-group keys include `uttara`, `coastal`, `mysuru`, and `malnad`.

### Example itinerary request

```json
{
  "circuit": "wildlife",
  "days": 3,
  "style": "Comfort",
  "interests": [
    "UNESCO & Architecture",
    "Ghats, Falls & Treks"
  ]
}
```

The API may adjust the requested number of days to match the selected circuit's supported duration.

## Run tests

From the project root, activate your virtual environment and run:

```bash
python -m pip install pytest httpx
python -m pytest -q
```

Review the test output to confirm which tests passed or failed in your environment.

## Run with Docker

Ensure Docker and Docker Compose are installed and running. From the project root, execute:

```bash
docker compose up --build
```

Then open **http://127.0.0.1:8000/docs**.

The supplied Docker configuration runs the API backend. Serve the `frontend/` directory separately using the local web-server instructions above or a static hosting service.

To stop the containers, press `Ctrl+C`. If you started them in detached mode, use:

```bash
docker compose down
```

## Deployment

The frontend and backend can be deployed separately.

### Frontend

Deploy the `frontend/` directory to a static hosting provider, such as Vercel or Netlify, or another suitable static web server.

### Backend

Deploy the Docker image or run the FastAPI application on a Python-compatible host. A typical start command is:

```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port "${PORT:-8000}"
```

Use the command and port configuration required by your hosting provider. If the provider expects a root-level `requirements.txt`, configure its build/install command to install `backend/requirements.txt`.

### Deployment checklist

- Configure `FRONTEND_ORIGINS` with the exact origin(s) of the deployed frontend.
- Store `GEMINI_API_KEY` as a backend environment secret only if Gemini is enabled.
- Update `API_BASE` in `frontend/js/app.js` to the deployed backend URL.
- Verify `/health`, `/docs`, itinerary generation, and dialect endpoints after deployment.
- Use HTTPS for public deployments.
- Never expose API keys or other secrets in frontend code or public repository files.

## Budget estimates and limitations

- Budget figures are indicative planning estimates, not live quotes.
- Food estimates vary by circuit and day area; accommodation and local transport estimates vary by location and travel style.
- Accommodation estimates assume two travellers sharing a room and count overnight stays as **trip days minus one**.
- The trip estimate excludes travel to and from the circuit start, shopping, and optional upgrades.
- A zero ticket estimate means no ticket amount was included in the calculation. It does **not** guarantee free entry, parking, guides, ferry services, or special activities.
- Stay-area suggestions are general area guidance, not verified accommodation listings or bookings.
- The planner does not include live transport timetables, real-time traffic, live ticketing, or booking integration.
- Browser text-to-speech depends on browser support and the availability of a Kannada voice.
- Saved trips use browser `localStorage` and are available only in the same browser and device.
- Confirm current entry fees, opening times, weather, access permissions, transport arrangements, and operator safety practices with official or local sources before departure.

### Price references

The original project documentation lists these references as inputs to some indicative estimates. Verify current information directly before relying on it:

- [Mysuru Palace — Karnataka Tourism](https://karnatakatourism.org/en/attractions/mysuru-palace/)
- [Mysuru Zoo — visitor information](https://www.mysuruzoo.info/public/visit)
- [Chennakeshava Temple, Belur — Karnataka HRCE](https://itms.kar.nic.in/hrcehome/index_temple.php?action=pooja_info&tid=3)
- [Mysuru cost-of-living reference — Numbeo](https://www.numbeo.com/cost-of-living/in/Mysore)
- [Mysuru local sightseeing pricing reference](https://www.travelmysore.com/pricing/)

These references do not constitute live price verification or endorsements.

## Security notes

- Do not commit `.env`, credentials, API keys, access tokens, or private configuration.
- Check that `.gitignore` excludes `.env` and local virtual-environment files.
- Keep secrets on the backend; never place private API keys in frontend JavaScript.
- Before publishing, inspect the repository for temporary files, personal documents, duplicate previews, and unintended secrets.
