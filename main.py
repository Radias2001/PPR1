from typing import Union
from fastapi import FastAPI
from transformers import pipeline


app = FastAPI()


@app.get("/{seq}")
def word(seq: str):
    classifier = pipeline("fill-mask")
    ans = classifier(seq)
    return ans
