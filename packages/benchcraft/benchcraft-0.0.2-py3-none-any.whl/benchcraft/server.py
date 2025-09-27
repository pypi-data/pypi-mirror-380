from flask import Flask
import benchcraft


def main():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/static",
    )

    app.register_blueprint(
        benchcraft.www.api.api.api_blueprint,
        url_prefix="/api",
    )

    app.register_blueprint(
        benchcraft.www.create.create.create_blueprint,
        url_prefix="/",
    )

    app.register_blueprint(
        benchcraft.www.run.run.run_blueprint,
        url_prefix="/run",
    )

    app.register_blueprint(
        benchcraft.www.review.review.review_blueprint,
        url_prefix="/review",
    )

    app.run(debug=True)


if __name__ == "__main__":
    main()
