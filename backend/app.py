from fastapi import FastAPI
from model import summarizer

app = FastAPI()

@app.get("/summarize")
async def summarize(text: str):
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]['summary_text']