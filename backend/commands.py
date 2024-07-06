from flask import current_app as app
from backend.models import db, User, People, Planet, Favorite

def insert_sample_data():
    with app.app_context():
        db.create_all()

        try:
            # Create sample user
            user = User.query.filter_by(email="alice_smith@example.com").first()
            if not user:
                user = User(
                    email="alice_smith@example.com",
                    password="securepassword",
                    first_name="Alice",
                    last_name="Smith",
                    is_active=True
                )
                db.session.add(user)
                db.session.commit()
                print("User: alice_smith@example.com created.")
            
            # Create sample people
            sample_people = [
                {"name": "Luke Skywalker", "birth_year": "19BBY", "gender": "male"},
                {"name": "Leia Organa", "birth_year": "19BBY", "gender": "female"},
                {"name": "Han Solo", "birth_year": "29BBY", "gender": "male"},
                {"name": "Yoda", "birth_year": "896BBY", "gender": "male"}
            ]
            for person_data in sample_people:
                person = People.query.filter_by(name=person_data["name"]).first()
                if not person:
                    person = People(
                        name=person_data["name"],
                        birth_year=person_data["birth_year"],
                        gender=person_data["gender"]
                    )
                    db.session.add(person)
                    db.session.commit()
                    print(f"Person: {person_data['name']} created.")
            
            # Create sample planet
            planet = Planet.query.filter_by(name="Tatooine").first()
            if not planet:
                planet = Planet(
                    name="Tatooine",
                    climate="arid",
                    terrain="desert"
                )
                db.session.add(planet)
                db.session.commit()
                print("Planet: Tatooine created.")
            
            # Link favorites
            favorite_person = Favorite.query.filter_by(user_id=user.id, people_id=person.id).first()
            if not favorite_person:
                favorite_person = Favorite(user_id=user.id, people_id=person.id)
                db.session.add(favorite_person)
            
            favorite_planet = Favorite.query.filter_by(user_id=user.id, planet_id=planet.id).first()
            if not favorite_planet:
                favorite_planet = Favorite(user_id=user.id, planet_id=planet.id)
                db.session.add(favorite_planet)
            
            db.session.commit()
            print("Favorites for alice_smith@example.com created.")
        except Exception as e:
            print(f"Error inserting sample data: {e}")