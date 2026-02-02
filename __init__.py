from flask import Flask
from .route import route as route_bp

app=Flask(__name__)

app.register_blueprint(route_bp)