from flask import Blueprint, render_template
from flask_login import current_user, login_required

from .portfolio import project_list
from .site import SITE_CONFIG
main = Blueprint("main", __name__)


# Routes
@main.route("/")
def index():
    return render_template("index.html", project_list=project_list, site=SITE_CONFIG)


@main.route("/privacy")
def privacy():
    return render_template("privacy.html", site=SITE_CONFIG)


@main.route("/about")
def about():
    return render_template("about.html", site=SITE_CONFIG)


@main.route("/projects")
def projects():
    return render_template("projects.html", project_list=project_list, site=SITE_CONFIG)


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user, site=SITE_CONFIG)
