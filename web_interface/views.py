from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from api.models import User
from .forms import UserForm

class IndexView(View):

	def get(self, request, *args, **kwargs):
		# users = User.objects.all()
		# return render(request, 'web_interface/index.html', {'users': users})
		form = UserForm()
		return render(request, 'web_interface/add_user.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = UserForm(request.POST)
		print(str(form))
		if form.is_valid():
			form.save()
			return HttpResponse("You have been added to the db")
		else:
			return HttpResponse("Woops something went wrong!")




def show_users(request):
	print("All is called")
	users = User.objects.all()
	for user in users:
		print(str(user))
	return render(request, 'web_interface/show_users.html', {'users': users})