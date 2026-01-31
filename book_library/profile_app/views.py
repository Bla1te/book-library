from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title': 'profile '
    }
	return render(request, 'profile_app/index.html', context)

