from flask import Flask
from config import Config
from models import db
from routes import register_routes
import logging
from monitoring import setup_metrics

app = Flask(__name__)
app.config.from_object(Config)

setup_metrics(app)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("Starting Product Service...")

db.init_app(app)

with app.app_context():
    db.create_all()

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=8080)