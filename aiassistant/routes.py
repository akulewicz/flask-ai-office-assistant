from aiassistant import app, bcrypt, db
from aiassistant.forms import CorrectorForm, RegistrationForm, LoginForm
from aiassistant.services.text_corrector_service import TextCorrectorService
from aiassistant.models import User
from flask import render_template, send_from_directory, request, redirect, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required

text_corrector_service = TextCorrectorService()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/corrector", methods=['GET', 'POST'])
@login_required
def corrector():
    form = CorrectorForm()
    if form.validate_on_submit():
        corrected_text = text_corrector_service.correct_text(text=form.text.data, simplify=form.simplify.data)
        return render_template('corrector.html', form=form, corrected_text=corrected_text)
    return render_template('corrector.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
@login_required # Do przemyślenia, jak będzie wyglądała rejestracja
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Możesz się już zalogować', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Logowanie nieudane. Sprawdź e-mail i hasło', 'danger')    
    return render_template('login.html', form=form)
        
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
    
@app.route("/preline.js")
def serve_preline_js():
    return send_from_directory("../node_modules/preline/dist", "preline.js")