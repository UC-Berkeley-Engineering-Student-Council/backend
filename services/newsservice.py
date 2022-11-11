#newssservice.py
# @author: Amol Budhiraja

def news_service(app):
    """News Feature Routes"""

    @app.route("/news/<string:title>", methods=["GET"])
    def news(title: str) -> str:
        title = title.upper()
        return f"<p>News Title: {title}!</p>"

