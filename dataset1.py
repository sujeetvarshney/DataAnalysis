import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('en_IN')

# Generate 800 records
records = []
for _ in range(800):
    name = fake.name()
    age = random.randint(22, 60)
    salary = random.randint(20000, 100000)
    joining_date = fake.date_between(start_date='-5y', end_date='today')
    dob = fake.date_of_birth(minimum_age=22, maximum_age=60)
    incremented_salary = salary + random.randint(5000, 20000)
    health_insurance = random.choice(['Yes', 'No'])
    gender = random.choice(['Male', 'Female'])
    working_profile = fake.job()
    city = fake.city()
    
    records.append([name, age, salary, joining_date, dob, incremented_salary, health_insurance, gender, working_profile, city])

# Write records to a CSV file
with open('indian_employees.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Salary', 'Joining Date', 'Date of Birth', 'Incremented Salary', 'Health Insurance', 'Gender', 'Working Profile', 'City'])
    writer.writerows(records)
