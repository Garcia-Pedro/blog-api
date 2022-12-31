from src.infra.requests import api
from uvicorn import run

if __name__=="__main__":
    run(api)