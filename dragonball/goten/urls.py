from django.urls import path
from . import views
urlpatterns = [
	path('drag', views.drag, name='drag')
]