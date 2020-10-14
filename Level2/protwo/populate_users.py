import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')
import django
django.setup()
import random
from apptwo.models import user
from faker import  Faker
fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=fakegen.email()

        #new entry
        use=user.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate(20)
    print("COMPLETE")
