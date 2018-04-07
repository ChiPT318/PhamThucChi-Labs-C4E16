from models.service import Service
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

# print(measurement_numbers)

for i in range(10):
    # print("Saving service ", i+1)
    measurement_numbers = []
    for j in range(3):
        measurement_number = randint(60,90)
        measurement_numbers.append(measurement_number)

    new_service = Service(name=fake.name(),
                        yob=randint(1995,2000),
                        gender=randint(0,1),
                        height=randint(150,180),
                        phone=fake.phone_number(),
                        address=fake.address(),
                        status=choice([True, False]),
                        description=choice(["ngoan hien", "de thuong", "lễ phép với gia đình"]),
                        measurements= (measurement_numbers))
    new_service.save()
