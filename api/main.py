from fastapi import FastAPI

app = FastAPI()

@app("/")
async def root():
	return {"message": "Hello World"}
