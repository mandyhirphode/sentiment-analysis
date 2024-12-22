from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
import pandas as pd
from io import StringIO
from textblob import TextBlob
import csv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
origins = ["http://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class SentimentResult(BaseModel):
    id: int
    text: str
    sentiment: str

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...), token: str = Depends(oauth2_scheme)):
    print(file.content_type)
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type, please upload a CSV file")

    contents = await file.read()
    csv_data = contents.decode('utf-8')
    df = pd.read_csv(StringIO(csv_data))

    if 'id' not in df.columns or 'text' not in df.columns:
        raise HTTPException(status_code=400, detail="CSV file must contain 'id' and 'text' columns")

    results = []
    for index, row in df.iterrows():
        text = row['text']
        sentiment = TextBlob(text).sentiment.polarity
        sentiment_label = 'positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral'
        results.append(SentimentResult(id=row['id'], text=text, sentiment=sentiment_label))

    return results

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "admin":
        return {"access_token": "fake-token", "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
