import csv
import random
from faker import Faker

fake = Faker('uk_UA')  # Українська локалізація

# Генеруємо дані для 2000 співробітників
num_employees = 2000
employees = []

for _ in range(num_employees):
    gender = 'Чоловіча' if random.random() > 0.4 else 'Жіноча'
    first_name = fake.first_name_male() if gender == 'Чоловіча' else fake.first_name_female()
    last_name = fake.last_name_male() if gender == 'Чоловіча' else fake.last_name_female()
    middle_name = fake.middle_name_male() if gender == 'Чоловіча' else fake.middle_name_female()
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85)
    job_title = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    employees.append([last_name, first_name, middle_name, gender, birth_date, job_title, city, address, phone, email])

# Записуємо дані у CSV файл
with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])
    writer.writerows(employees)
