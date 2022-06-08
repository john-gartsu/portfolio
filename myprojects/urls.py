from django.urls import path

# import home/views to get home fn
from . import views

# list of url patterns
# changing to class based views add the class view with as_view() method
urlpatterns = [
    path('', views.MyProjectsView.as_view(), name='myprojects'),
]