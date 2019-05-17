from django.conf.urls import include, url

from . import views

urlpatterns = [
	url('<int:id>/', views.detail, name='detail'),
]
