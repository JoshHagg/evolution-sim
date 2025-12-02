from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from simulation import Simulation

sim = Simulation()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/world")
def get_world():
    return sim.tick()

@app.get("/")
def root():
    return RedirectResponse(url="/world")

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "backend running"}

