from django.shortcuts import render
from .forms import ImageForm
# Create your views here.
def home(req):
    form = ImageForm()
    return render(req, 'home/home.html', {'form': form})