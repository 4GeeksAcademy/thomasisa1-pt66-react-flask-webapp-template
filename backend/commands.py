import click
from .models import db, User, People, Planet
from faker import Faker

fake = Faker()

def setup_commands(app):
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users")  # name of our command
    @click.argument("count")  # argument of our command
    def insert_test_users(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@test.com"
            user.password = "123456"
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")
        print("All test users created")

    @app.cli.command("insert-test-people")  # name of our command
    @click.argument("count")  # argument of our command
    def insert_test_people(count):
        print("Creating test people")
        for x in range(1, int(count) + 1):
            person = People()
            person.name = fake.name()
            person.birth_year = fake.year()
            person.gender = fake.random_element(elements=("male", "female"))
            db.session.add(person)
            db.session.commit()
            print("Person: ", person.name, " created.")
        print("All test people created")

    @app.cli.command("insert-test-planets")  # name of our command
    @click.argument("count")  # argument of our command
    def insert_test_planets(count):
        print("Creating test planets")
        for x in range(1, int(count) + 1):
            planet = Planet()
            planet.name = fake.word().capitalize() + " Planet"
            planet.climate = fake.random_element(elements=("temperate", "tropical", "arid", "frozen"))
            planet.terrain = fake.random_element(elements=("mountains", "forest", "desert", "ocean"))
            db.session.add(planet)
            db.session.commit()
            print("Planet: ", planet.name, " created.")
        print("All test planets created")

    @app.cli.command("insert-test-data")
    def insert_test_data():
        print("Inserting test data")
        insert_test_users(5)
        insert_test_people(5)
        insert_test_planets(5)
        print("All test data inserted")
