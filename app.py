from config import create_app
from db import db

app = create_app()

with app.app_context():
    db.init_app(app)


if __name__ == '__main__':
    app.run()
