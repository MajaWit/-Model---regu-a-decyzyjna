from fastapi import FastAPI, Query
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/api/v1.0/predict")
def predict(x: Optional[float] = Query(0), y: Optional[float] = Query(0)):
    result = 1 if (x + y) > 5.8 else 0
    return {
        "prediction": result,
        "features": {"x": x, "y": y}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
