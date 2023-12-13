from faker import Faker
from src.config.data import NewUser

Faker.seed()
fake = Faker('en-US')


def generated_data():
    yield NewUser(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        address=fake.address(),
        city=fake.city(),
        state=fake.state(),
        zip_code=fake.zipcode(),
        phone_number=fake.phone_number(),
        ssn=fake.ssn(),
        username=fake.user_name(),
        password=fake.password(),
        email=fake.email()
    )
