
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, redirect, flash
from models import connect_db, Pet, db
from forms import AddPetForm


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_agency"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


connect_db(app)


@app.route("/")
def home_page():

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add", methods=["POST", "GET"])
def add_pet_form():
    """Display form to add a new pet"""
    form = AddPetForm()

    if form.validate_on_submit():

        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        newPet = Pet(name=name, species=species,
                     photo_url=photo_url, age=age, notes=notes)

        db.session.add(newPet)
        db.session.commit()
        flash("Pet added!")
        return redirect("/")
    else:

        return render_template("add.html", form=form)


@app.route('/pets/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    """display form to edit a pet"""
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():

        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        flash("Updated!")
        return redirect("/")
    else:

        return render_template("edit_pet.html", form=form, pet=pet)


@app.route('/pets/<int:id>/details', methods=["GET", "POST"])
def pet_details(id):
    """Display pet details"""
    pet = Pet.query.get_or_404(id)

    return render_template("details.html", pet=pet)
