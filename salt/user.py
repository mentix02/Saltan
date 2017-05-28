from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


class PeopleList(ListView):
	template_name = 'salt/people.html'
	context_object_name = 'people'
	paginate_by = 8

	def get_queryset(self):
		return Profile.objects.all()


class LoginView(View):
	template_name = 'visitor/login.html'

	def get(self, request):
		if request.user.is_authenticated():
			return render(request, 'salt/index.html', {})
		else:
			return render(request, self.template_name, {})

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('salt:index')
			else:
				return render(request, self.template_name, {'error': "Sorry! User isn't active!"})
		else:
			return render(request, self.template_name, {'error': "Invalid login!"})


class RegisterView(View):
	template_name = 'visitor/register.html'

	def get(self, request):
		if request.user.is_authenticated():
			return render(request, 'salt/index.html', {})
		else:
			return render(request, self.template_name, {})

	def post(self, request):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		profile_pic = request.FILES['profile_pic']

		try:
			User.objects.get(username=username)
			return render(request, self.template_name, {"error": "Username taken or has been deactivated!"})
		except:
			if ' ' in username:
				return render(request, self.template_name, {"error": "No spaces in username!"})
			else:
				user = User.objects.create_user(
					first_name=first_name,
					last_name=last_name,
					username=username,
					password=password,
					email=email,
				)
				user.save()
				new_profile = Profile(
					user=user,
					profile_pic=profile_pic,
				)
				new_profile.save()

				message = "Welcome to Saltan. Hope you enjoy your visit, " + username

				send_mail('Welcome To Saltan!', message, settings.EMAIL_HOST_USER, [str(email)], fail_silently=True)

				the_user = authenticate(username=username, password=password)

				if the_user is not None:
					if the_user.is_active:
						login(request, the_user)
						return redirect('salt:index')
					else:
						return render(request, self.template_name, {'error': "User has been deactivated! Can't register again!"})
				else:
					return render(request, self.template_name, {'error': "Something went wrong! Sorry!"})


class UserDetail(View):
	template_name = "salt/profile.html"

	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('salt:login')
		user = Profile.objects.get(user=request.user)
		return render(request, self.template_name, {"user": user})

	def post(self, request):
		user = request.user
		profile = Profile.objects.get(user=user)
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		profile_pic = request.FILES['profile_pic']
		password = request.POST['password']
		no_passwords = [" "]
		if password in no_passwords:
			context = {
				"profile": profile,
				"password_error": "Can't set THAT password! :/",
			}
			return render(request, "salt/edit_profile.html", context)
		elif password == "":
			user(first_name=first_name, last_name=last_name, email=email)
			user.save()
			profile(user=user, profile_pic=profile_pic)
			profile.save()
			return render(request, self.template_name, {"user": profile})
		elif len(password) > 5:
			user(first_name=first_name, last_name=last_name, password=password, email=email)
			user.save()
			profile(user=user, profile_pic=profile_pic)
			profile.save()
			return render(request, self.template_name, {"user": profile})


class PersonDetail(View):
	template_name = 'salt/person.html'

	def get(self, request, username):
		try:
			user = User.objects.get(username=username)
			if user == request.user:
				return redirect('salt:profile')
		except User.DoesNotExist:
			raise Http404("Sorry! Couldn't find user!")
		profile = Profile.objects.get(user=user)
		context = {"profile": profile}
		return render(request, str(self.template_name), context)


class EditView(View):
	template_name = 'salt/edit_profile.html'

	def get(self, request):
		user = request.user
		profile = Profile.objects.get(user=user)
		return render(request, self.template_name, {"profile": profile})


def deactivate(request):
	user = request.user
	user.is_active = False
	user.save()
	logout(request)
	return redirect('salt:register')
