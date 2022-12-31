from src.infra.db import engine
from sqlmodel import SQLModel
import asyncio

def main():
    SQLModel.metadata.create_all(engine)



if __name__=="__main__":
    main()
