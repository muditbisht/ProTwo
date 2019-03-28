import os
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')
django.setup()

import random
from AppTwo.models import AccessRecord,Topic,Webpage
from faker import Faker
import sys

fake = Faker()
topics = ['Search','Social Network','MarketPlace','News','Games','Music','Streaming','Educational']
domain = ['.in','.co','.co.in','.com','.co','.en','.is'] 
def name2url(name):
	name=name.split()
	url=''
	for a in name:
		url+=a
	return url
def add_topic():
    t = Topic.objects.get_or_create(topic=random.choice(topics))[0]
    t.save()
    return t
def populate(N):
	for i in range(N):
		top = add_topic() 
		fake_name=fake.company()
		fake_name=name2url(fake_name)
		fake_url='www.'+fake_name
		
		if str(top)=='Educational':
			dom=random.choice([random.choice(domain),'.edu'])
		else:
			dom=random.choice(domain)
		fake_url+=dom

		web = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

		acc_record = AccessRecord.objects.get_or_create(name=web,date=fake.date())[0]
if __name__ == '__main__':
	print("populating script!")
	N=5
	if len(sys.argv)>1:
		N=int(sys.argv[1])
	populate(N)
	print("Populated")
