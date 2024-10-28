from flask_frozen import Freezer
from app import app  # Importe seu app Flask

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()