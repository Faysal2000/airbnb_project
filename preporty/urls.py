from django.urls import path
from .views import PropertyDetail,PropertyList
from . import views


app_name='property'

urlpatterns = [
    
    # path('',PropertyList.as_view()),
    path('', views.my_view, name='my_view')
]
