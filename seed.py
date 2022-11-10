from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name="Sabrina", species="Cat", age="8y",
           notes="She loves snacks and looking outside.")
pet2 = Pet(name="Duke", species="Dog", age="4y",
           notes="He loves snacks and barking.")
pet3 = Pet(name="Lucky", species="Cat", age="3y",
           notes="He loves hugs and pets.")
pet4 = Pet(name="Milly", species="Dog", age="8y",
           notes="Loves everyone and everything.")


db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)

db.session.commit()
