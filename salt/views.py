from django.shortcuts import render, redirect
from django.views.generic import View
from random import shuffle
from .models import Salt


def index(request):
	if not request.user.is_authenticated:
		return redirect('salt:login')
	else:
		the_salts = Salt.objects.all()
		salts = list(the_salts)
		shuffle(salts)
		context = {"salts": salts}
		return render(request, 'salt/index.html', context)


class AboutView(View):

	template_name = 'salt/about.html'
	context = {}

	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('salt:login')
		return render(request, self.template_name, self.context)

	def post(self, request):
		return render(request, self.template_name, self.context)
