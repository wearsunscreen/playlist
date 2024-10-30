from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    current_app,
    url_for,
)
from movie_library.forms import MovieForm
from movie_library.models import Movie
from dataclasses import asdict


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    movie_data = current_app.db.movie.find({})
    movies = [Movie(**movie) for movie in movie_data]
    return render_template("index.html", title="Movies Watchlist", movies_data=movies)


@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = Movie(
            title=form.title.data, year=form.year.data, director=form.director.data
        )
        current_app.db.movie.insert_one(asdict(movie))
        return redirect(url_for(".index"))

    return render_template("new_movie.html", title="Add Movie", form=form)


@pages.get("/movie/<string:_id>")
def movie(_id):
    movie_data = current_app.db.movie.find_one({"_id": _id})
    if not movie_data:
        about(404)
    movie = Movie(**movie_data)
    return render_template("movie_details.html", movie=movie)


@pages.get("/toggle_theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    return redirect(request.args.get("current_page"))
