from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app
from .constants import ip_address, overall_facebook_spending, overall_facebook_spending_chloro, dashboard

router = Blueprint('router', __name__)

overall_facebook_spending_addr = f"{ip_address}:{overall_facebook_spending}"
overall_facebook_spending_chloro_addr = f"{ip_address}:{overall_facebook_spending_chloro}"
dashboard_addr = f"{ip_address}:{dashboard}"

@router.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html', title="GridCast")

@router.route("/forecast_dashboard", methods=["GET", "POST"])
def forecast_dashboard():
    return render_template('forecast_dashboard.html', title="GridCast - Forecast", iframesrc=dashboard_addr)

@router.route("/national_report", methods=["GET", "POST"])
def national_report():
    return render_template('national_report.html', title="GridCast - National Report", iframesrc=overall_facebook_spending_addr, iframesrc_map=overall_facebook_spending_chloro_addr)

@router.route("/static/num_accidents.geojson", methods=["GET", "POST"])
def traffic_data():
    f = open("./data/num_accidents.geojson", "r")
    return f.read()