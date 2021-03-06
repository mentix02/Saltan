from .models import Salt, Profile, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg', 'gif']


def salts(request):
	if not request.user.is_authenticated:
		return redirect('salt:login')
	else:
		users_salts = Salt.objects.filter(creator=Profile.objects.get(user=request.user))
		context = {"salts": users_salts}
		return render(request, 'salt/salts.html', context)


class AddSalt(View):
	template_name = 'salt/add_salt.html'

	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('salt:login')
		context = {}
		return render(request, str(self.template_name), context)

	def post(self, request):
		user = request.user
		creator = Profile.objects.get(user=user)
		title = request.POST['title']
		description = request.POST['description']
		image = request.FILES['img']
		# print(image)
		# print(type(image))
		str_image = str(image)
		image_type = str_image.split('.')[-1]
		# print(image_type)
		if image_type not in IMAGE_FILE_TYPES:
			return render(request, str(self.template_name), {"error": 
				"Image file type should be jpg, jpeg, gif or png!"})
		else:
			try:
				new_salt = Salt(
					creator=creator,
					title=title,
					description=description,
					image=image,
				)
				new_salt.save()
			except:
				return render(request, str(self.template_name), {"error": 
					"Something went wrong! Please try again!"})
			return redirect('salt:salts')


class SaltDetail(View):
	template_name = 'salt/detail.html'

	def get(self, request, salt_id):
		if not request.user.is_authenticated:
			return redirect('salt:login')
		else:
			user = Profile.objects.get(user=request.user)
			salt = Salt.objects.get(pk=salt_id)
			comments = Comment.objects.filter(salt=salt)
			context = {"salt": salt, "comments": comments, "user": user}
			return render(request, self.template_name, context)

	def post(self, request, salt_id):
		user = Profile.objects.get(user=request.user)
		salt = Salt.objects.get(pk=salt_id)
		comment = request.POST['comment']
		if len(comment) == 0:
			user = Profile.objects.get(user=request.user)
			salt = Salt.objects.get(pk=salt_id)
			comments = Comment.objects.filter(salt=salt)
			context = {
				"salt": salt,
				"comments": comments,
				"user": user,
				"error": "Can't have blank comments!",
			}
			return render(request, self.template_name, context)
		the_comment = Comment(
				user=user,
				salt=salt,
				comment=comment,
			)
		the_comment.save()
		return HttpResponseRedirect('/salt/'+str(salt_id))


class DeleteSalt(DeleteView):
	model = Salt
	success_url = reverse_lazy('salt:salts')
	# return HttpResponseRedirect('/salts/')

def delete_salt(request, pk):
	user = request.user
	salt = get_object_or_404(Salt, pk=pk)

	if salt.creator.user == user:
		salt.delete()
		return redirect('salt:salts')
	else:
		return redirect('salt:salts')
