from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from Users.models import UserProfileInfo
from Users.forms import UserForm,UserProfileInfoForm
# Create your views here.



from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def picture(request):
	cur_user = request.user
	pic='/media/profile_pic/noimage.jpg'
	if cur_user:
		print(cur_user)
		try :
			pic=cur_user.userprofileinfo.picture.url
			print(pic)
			return pic
		except:
			pass			
	return pic
	

def index(request):
	print(request.user,picture(request))
	return render(request,'Users/index.htm',context={'picture' : picture(request)})

def register(request):
	registered = False

	if request.method=='POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileInfoForm(request.POST)
		print(request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			print("UserForm Success!")

			profile = profile_form.save(commit=False) 
			profile.user = user
			
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			
			profile.save()
			registered = True
		else:
			print('Un-Successful',user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()
		print("METHOD not POST")
	return render(request,'Users/Register.htm',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return render(request,'Users/index.htm')
			else:
				HttpResponse("Account Inactive")
		else:
			print('Invalid User\nUsername : {} | Password : {}'.format(username,password))
			return HttpResponse("Invalid Username or password")
	else:
		print('Method is not POST')
		return render(request,'Users/Login.htm')

@login_required
def user_logout(request):
	print(request.user,picture(request))
	logout(request)
	return render(request,'Users/index.htm')






