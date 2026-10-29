# Namma Trip Karnataka 🚌

**Discover Karnataka. Plan your trip. Explore more.**

Namma Trip Karnataka is a travel planning website that helps students and travellers explore destinations across Karnataka, organize their travel itineraries, and discover Kannada phrases and regional dialects.

Whether you're planning a weekend getaway with friends, exploring during semester breaks, or discovering Karnataka for the first time, Namma Trip helps you get started.

## ✨ Features

- **Travel Itinerary Planning:** Generate travel itineraries to help organize your journey.
- **Explore Karnataka:** Discover destinations and plan your next adventure.
- **Kannada Phrasebook:** Explore Kannada phrases and regional dialects.
- **Simple Web Interface:** Access travel planning features through a browser.

## 🛠️ Requirements

Before running the project, make sure you have:

- Python installed.
- Git installed to clone the repository.
- A modern web browser.
- An internet connection for cloning the repository and installing dependencies.

## 🚀 How to Run the Project

### 1. Download the project

Open a terminal and run:

```bash
git clone https://github.com/hariipriyaaa/namma-trip-karnataka.git
cd namma-trip-karnataka
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4. Install the required dependencies

```bash
python -m pip install -r backend/requirements.txt
```

### 5. Start the backend

From the project root, run:

```bash
python -m uvicorn backend.main:app --reload --port 8000
```

The backend will be available at:

http://127.0.0.1:8000

### 6. Start the frontend

Keep the backend terminal running. Open a **second terminal** in the project root, activate the virtual environment if needed, and run:

```bash
python -m http.server 5500 --directory frontend
```

Open the website in your browser:

**http://127.0.0.1:5500**

Keep both terminal windows running while using the website.

## 🧪 Running the Tests

To run the project's automated tests, install the test runner:

```bash
python -m pip install pytest
```

Then run:

```bash
python -m pytest
```

## 📁 Project Structure

```text
namma-trip-karnataka/
├── backend/       # Application backend and travel planning logic
├── frontend/      # Website interface, styles and JavaScript
├── scripts/       # Development helper scripts
├── tests/         # Automated tests
├── .env.example   # Example configuration
├── .gitignore     # Files excluded from Git
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🌱 Our Goal

To make exploring Karnataka more accessible and enjoyable by bringing travel planning and local language discovery together in one place.

---

**Made with ❤️ for explorers of Karnataka.**
