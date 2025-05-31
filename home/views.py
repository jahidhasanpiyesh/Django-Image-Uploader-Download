from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.
def home(req):
    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm() 
    img = Image.objects.all()
    return render(req, 'home/home.html', {'img':img, 'form': form}) 

