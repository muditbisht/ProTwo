from django.shortcuts import render
from django.http import HttpResponse,Http404
from random import randint
from AppTwo.models import Topic,Webpage,AccessRecord
from AppTwo.Forms import User_Forms,web_form
from json import loads
from time import sleep
from os import path
from faker import Faker
from Users.views import picture


BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
file = path.join(BASE_DIR,"AppTwo","StatesIndia.json") 
State_DIR=loads(open(file).read())



def non(request):
	X=Faker()
	text=X.text()
	print(request.user,picture(request))
	return render(request,'Non.htm',context={'text':text,'Name':'non','Image':picture(request)})
def index(request):
	print(request.user,picture(request))
	Q=[]
	for _ in range(10):
		i=randint(0,len(State_DIR)-1)
		Q.append(i)
	Q=set(Q)
	States=[]
	for i in Q:
		States.append({'state':State_DIR[i]['name'],'code' : State_DIR[i]['code']})
	# Create your views here.
	my_dict={'States' : States,'Name':'Index'}
	return  render(request,'AppTwo/Index.htm',context=my_dict)
def help(request):
	print(request.user,picture(request))
	return render(request,'AppTwo/help.htm',context={'Name':'Help'})

def Topic_list(request):
	print(request.user,picture(request))
	topic_list=Topic.objects.order_by('topic')
	topic_list={'record' : topic_list,'Name':'Topic_List'}
	return render(request,'AppTwo/TopicList.htm',context=topic_list)

def Webpage_list(request):
	print(request.user,picture(request))
	web_list = {'record' : Webpage.objects.order_by('name'),'Name':'web_list'}
	return render(request,'AppTwo/WebpageList.htm',context=web_list)

def AccessRecord_list(request):
	print(request.user,picture(request))
	acc_list={'record' : AccessRecord.objects.order_by('name'),'Name': 'Access_List'}
	return render(request,'AppTwo/AccessList.htm',context=acc_list)
def form_view(request):
	form = User_Forms()
	print(request.user,picture(request))
	if request.method == 'POST':
		form = User_Forms(request.POST)
		if form.is_valid():
			print("Validation Success")
			return HttpResponse('<h1>Success</h1>')
	else:
		print("method is not POST")
	return render(request,'AppTwo/Form.htm',{'form' : form,'Name':'Form'})

def webForm(request):
	form = web_form()
	print(request.user,picture(request))
	if request.method == 'POST':
		form = web_form(request.POST)
		if form.is_valid():
			form.save(commit=True)
			print("Successful")
			return HttpResponse('<h1>Submited</h1>')
	else:
		print("Method not POST")
	return render(request,'AppTwo/webForm.htm',{'form':form,'Name':'WebForm'})



