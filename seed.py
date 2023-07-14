import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import datetime
import random

from faker import Faker
from validate_docbr import CPF

from school.models import Course, Enrollment, Student


def creating_students(quantity_of_people):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity_of_people):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        cpf = cpf.generate()
        date_birth = fake.date_between(start_date='-18y', end_date='today')
        s = Student(name = name, rg = rg, cpf = cpf, date_birth = date_birth)
        s.save()

def creating_courses(quantity_of_courses):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantity_of_courses):
        code_course = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        descs = ['Python Basics', 'Python Intermediate','Python Advanced', 'Python for Data Science', 'Python/React']
        description = random.choice(descs)
        descs.remove(description)
        level = random.choice("BIA")
        c = Course(code_course = code_course, description = description, level = level)
        c.save()


creating_students(200)
creating_courses(5)