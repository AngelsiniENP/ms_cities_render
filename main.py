# main.py (raíz)
from ms_cities.app import app

@app.get("/health")
def health():
    return {"status": "ok", "service": "ms_categories"}