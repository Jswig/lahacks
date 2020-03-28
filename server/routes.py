from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app

router = Blueprint('router', __name__)

@router.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html', title="PlaceHolder")

@router.route("/candidate_dashboard", methods=["GET", "POST"])
def candidate_dashboard():
    return render_template('candidate_dashboard.html', title="The Transparency Report - Candidate Dashboard")

@router.route("/national_report", methods=["GET", "POST"])
def national_report():
    return render_template('national_report.html', title="The Transparency Report - National Report")

