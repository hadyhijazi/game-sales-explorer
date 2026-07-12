import pandas as pd

# load dataset
df = pd.read_csv("data/vgsales.csv")

def get_all_games():
    return df.to_dict(orient="records")

def get_games_by_platform(platform):
    filtered = df[df["Platform"].str.lower() == platform.lower()]
    return filtered.to_dict(orient="records")

def get_games_by_year(year):
    filtered = df[df["Year"] == year]
    return filtered.to_dict(orient="records")

def get_games_by_genre(genre):
    filtered = df[df["Genre"].str.lower() == genre.lower()]
    return filtered.to_dict(orient="records")

def get_games_by_publisher(publisher):
    filtered = df[df["Publisher"].str.lower() == publisher.lower()]
    return filtered.to_dict(orient="records")

def get_stats():
    total_games = len(df)
    top_genre = df["Genre"].value_counts().idxmax()
    best_selling = df.loc[df["Global_Sales"].idxmax()]["Name"]
    return {
        "total_games": total_games,
        "most_common_genre": top_genre,
        "best_selling_game": best_selling
    }

def get_top_games(n):
    top_games = df.sort_values(by="Global_Sales", ascending=False).head(n)
    return top_games.to_dict(orient="records")

def search_games(name):
    filtered = df[df["Name"].str.contains(name, case=False)]
    return filtered.to_dict(orient="records")

def filter_games(platform=None, genre=None, sort=None):
    filtered = df
    if platform:
        filtered = filtered[filtered["Platform"].str.lower() == platform.lower()]
    if genre:
        filtered = filtered[filtered["Genre"].str.lower() == genre.lower()]
    if sort == "top_sales":
        filtered = filtered.sort_values(by="Global_Sales", ascending=False)
    elif sort == "newest":
        filtered = filtered.sort_values(by="Year", ascending=False)
    elif sort == "oldest":
        filtered = filtered.sort_values(by="Year", ascending=True)
    return filtered.to_dict(orient="records")