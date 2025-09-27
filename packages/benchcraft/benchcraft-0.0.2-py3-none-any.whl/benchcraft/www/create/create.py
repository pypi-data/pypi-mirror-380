from flask import Blueprint, render_template


create_blueprint = Blueprint(
    "create",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
    url_prefix="/",
)


@create_blueprint.route("/")
def index():
    """Renders the main HTML page."""
    return render_template("create.html", page_context="create")
