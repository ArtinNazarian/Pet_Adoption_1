from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "123password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
app.app_context().push()

@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = PetForm()
    if form.validate_on_submit():     
       
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)       
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_pet.html', form=form)
    
@app.route('/pet/<int:pet_id>')
def pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    return render_template('pet_information.html', pet=pet, form=form)

@app.route('/pet/<int:pet_id>/edit', methods=["GET", "POST"])
def edit(pet_id):    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():   
        pet.photo_url = form.photo_url.data   
        pet.notes = form.notes.data
        pet.avilable = form.avilable.data
        db.session.commit()
        return redirect('/')
    else:        
        return render_template('edit_pet_form.html', form=form, pet=pet)

   

    






