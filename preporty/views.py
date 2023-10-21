from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView
from .models import Property, Category

def my_view(request):
    # Your view logic here
    x = Category.objects.all()
    context = {'bb':"HEllo it's me"}
    return render(request, 'index.html', context)

class PropertyList(ListView):
    model=Property
#filter

class PropertyDetail(DetailView):
    pass
#book




