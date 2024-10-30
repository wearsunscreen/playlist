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
import uuid


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Movies Watchlist",
    )


@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = {
            "title": form.title.data,
            "year": form.year.data,
            "director": form.director.data,
            "_uid": uuid.uuid4().hex,
        }
        current_app.db.movie.insert_one(movie)
        return redirect(url_for(".index"))

    return render_template("new_movie.html", title="Add Movie", form=form)


@pages.get("/toggle_theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    return redirect(request.args.get("current_page"))
