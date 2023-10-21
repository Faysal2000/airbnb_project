from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView
from .models import Property

def my_view(request):
    # Your view logic here
    
    return render(request, 'index.html', {})

class PropertyList(ListView):
    model=Property
#filter

class PropertyDetail(DetailView):
    pass
#book




