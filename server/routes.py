from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app
from .constants import ip_address #, dashboard

router = Blueprint('router', __name__)

dashboard_addr = f"{ip_address}:{5000}/forecast_app"

@router.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html', title="GridCast")

@router.route("/forecast_dashboard", methods=["GET", "POST"])
def forecast_dashboard():
    return render_template('forecast_dashboard.html', title="GridCast - Forecast", iframesrc=dashboard_addr)

@router.route("/static/num_accidents.geojson", methods=["GET", "POST"])
def traffic_data():
    f = open("./data/num_accidents.geojson", "r")
    return f.read()