from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from .models import Item
from .forms import AddItemForm

# Create your views here.
# home view
def home(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	return render(request, 'items/home.html')

# dashboard
@login_required(login_url="/accounts/login")
def dashboard(request):
	error = None
	form = AddItemForm(request.POST or None)

	if request.method == 'POST':
		try:
			if form.is_valid():
				instance = form.save(commit=False)
				instance.author = request.user
				instance.save()
		except AttributeError:
			error = "Ooops.... Couldn't get the name or price"
		except:
			error = "Something went wrong..."

	form = AddItemForm()

	items = Item.objects.filter(author=request.user)
	context = {
		'items': items,
		'form': form,
		'error': error
	}

	return render(request, 'items/dashboard.html', context)

# update prices
@login_required(login_url="/accounts/login")
def update(request):
	items = Item.objects.all()

	for item in items:
		item.save()
	return redirect('dashboard')

# delete item view
# @login_required(login_url="/accounts/login")
class DeleteItem(DeleteView):
	model = Item
	template_name = 'items/deleteItem.html'
	success_url = reverse_lazy('dashboard')