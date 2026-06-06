from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chelsea Woods & Co. - NovaReign Core")

# This allows your visual frontend to talk to this backend securely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "online", "company": "Chelsea Woods & Co.", "system": "NovaReign Active"}
