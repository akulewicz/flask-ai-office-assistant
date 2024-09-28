from aiassistant import app
from flask import render_template, send_from_directory, request, redirect
from aiassistant.forms import CorrectorForm

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/corrector", methods=['GET', 'POST'])
def corrector():
    form = CorrectorForm()
    if form.validate_on_submit():
        return redirect('home')
    return render_template('corrector.html', form=form)

@app.route("/preline.js")
def serve_preline_js():
    return send_from_directory("../node_modules/preline/dist", "preline.js")