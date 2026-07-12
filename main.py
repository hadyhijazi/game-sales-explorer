from fastapi import FastAPI
from data_loader import get_all_games, get_games_by_platform, get_games_by_year, get_games_by_genre, get_games_by_publisher, get_stats, get_top_games, search_games, filter_games
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Game Sales API is running"}

@app.get("/games")
def games():
    return get_all_games()

@app.get("/games/platform/{platform}")
def games_by_platform(platform: str):
    return get_games_by_platform(platform)

@app.get("/games/year/{year}")
def games_by_year(year: int):
    return get_games_by_year(year)

@app.get("/games/genre/{genre}")
def games_by_genre(genre: str):
    return get_games_by_genre(genre)

@app.get("/games/publisher/{publisher}")
def games_by_publisher(publisher: str):
    return get_games_by_publisher(publisher)

@app.get("/games/stats")
def stats():
    return get_stats()

@app.get("/games/top/{n}")
def top_games(n: int):
    return get_top_games(n)

@app.get("/games/search")
def search(name: str):
    return search_games(name)

@app.get("/games/filter")
def filter(platform: str = None, genre: str = None, sort: str = None):
    return filter_games(platform, genre, sort)