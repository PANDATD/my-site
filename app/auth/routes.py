from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm
from  ..main.site import SITE_CONFIG
auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data  # You should hash this in real apps
        )
        db.session.add(user)
        db.session.commit()
        flash('✅ Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', site=SITE_CONFIG, form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("main.index"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html", form=form, site=SITE_CONFIG,)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You’ve been logged out.", "info")
    return redirect(url_for("main.index"))
