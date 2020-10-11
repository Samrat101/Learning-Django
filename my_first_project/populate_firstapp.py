import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_first_project.settings')
import django
django.setup()
import random
from first_app.models import Accessrecord ,webpage,topic
from faker import  Faker
fakegen=Faker()
topics=['social' , 'market' , 'news' , 'cricket']
def add_topic():
    t=topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top=add_topic()

        # create the fake data for the entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.name()

        # create new webpage entry
        webpg=webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create new Accessrecord entry
        acc_rec=Accessrecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ =='__main__':
    print("populating script!")
    populate(20)
    print("populated")
