from fastapi import FastAPI, UploadFile, File

app = FastAPI()

import auth, data, exercise, files, translate as tr

@app.get("/")
async def index():
    print ("function name: ", index.__name__)
    item = 'Available options: /register, /login, /download, /upload, /categories, /sentences, /exercise'
    return item

@app.get("/register")
async def register(login: str, password: str):
    return auth.add_user(login, password)

@app.get("/login")
async def login(login: str, password: str):
    return auth.autorisation(login, password)

@app.get("/download")
def download(filename: str):
    print ("function name: ", download.__name__)
    return files.download(filename)

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return files.upload(file)

@app.get("/categories")
async def categories():
    return data.get_categories()

@app.get("/sentences")
async def sentences(limit: int = 200, offset: int = 0):
    return data.get_sentences(limit, offset)

@app.get("/exercise")
async def get_exercise(token: str):
    return exercise.get_exercise(token)

@app.post("/translate")
async def translate(token: str,  exercise_id: int, translation: str):
    return tr.translate(token,  exercise_id, translation)