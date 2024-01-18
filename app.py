from flask import Flask, render_template, request
from tmdbv3api import TMDb, Discover

app = Flask(__name__)

# Replace with your TMDb API key
tmdb_api_key = '0d6afa2db47ee5b63984d9baf1dd48a3'

tmdb = TMDb()
tmdb.api_key = tmdb_api_key

def get_movies(emotion):
    genre_ids = {
        "Sad": 18,         # Drama
        "Disgust": 10402,  # Music
        "Anger": 10751,    # Family
        "Anticipation": 53,  # Thriller
        "Fear": 10752,     # War
        "Enjoyment": 53,   # Thriller
        "Trust": 37,       # Western
        "Surprise": 10752  # War
    }

    # Get movies by genre
    genre_id = genre_ids.get(emotion)
    if genre_id:
        discover = Discover()
        movies = discover.discover_movies(
            {'with_genres': genre_id, 'sort_by': 'popularity.desc'})
        titles = [movie.title for movie in movies]
        return titles
    else:
        return []


   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    emotion = request.form['emotion']
    movies = get_movies(emotion)
    return render_template('recommend.html', emotion=emotion, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
