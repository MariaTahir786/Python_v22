from app import app

from app.controllers import star_war_controller,like_controller

if __name__ == "__main__":
    app.run(debug=True)