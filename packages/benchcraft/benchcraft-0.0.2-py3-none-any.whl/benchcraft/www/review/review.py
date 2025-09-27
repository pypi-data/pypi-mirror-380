from flask import Blueprint, render_template


review_blueprint = Blueprint("review", __name__, template_folder="templates")


@review_blueprint.route("/")
def review_page():
    """Renders the review page."""
    return render_template("review.html")
