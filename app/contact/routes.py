from flask import Blueprint, flash, redirect, render_template, url_for

from .forms import ContactForm
from  ..main.site import SITE_CONFIG
contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print("Form Submitted:", form.name.data, form.email.data, form.message.data)
        flash("Your message has been sent!", "success")
        return redirect(url_for("main.index"))
    if form.errors:
        flash(
            "There were errors in your form. Please correct them and try again.",
            "danger",
        )
    return render_template("contact.html", form=form, site=SITE_CONFIG)
