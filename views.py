import os
from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.config.from_object("project.config.Config")

from .forms import PatientForm, MedicForm
from  .utils import *

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = PatientForm()

    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("index.html", title="Gloth", subtitle="test", patient_form=form, name="Ynov")
        else:
            data = request.args.get(form)
            return redirect(url_for('medic'), data=data)

    return render_template("index.html", title="Gloth", subtitle="subtitle", patient_form=form, name="Ynov")


@app.route('/medic', methods=["GET","POST"])
def medic():

    form = MedicForm(request.form)
    patho_id = (request.form.get("pathology"))
    user_id = (request.form.get("user"))
    user_name = getUserName(user_id)
    patho_name = getPathologyName(patho_id)
    results = getPathologyIcd10(patho_id)
    icd10_final = [str(icd10) for icd10 in results]

    return render_template("medic.html", name="Ynov", pathology=patho_name, user=user_name, icd=icd10_final)

