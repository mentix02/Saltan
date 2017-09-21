from django.conf.urls import url
from . import user, views

urlpatterns = [
	url(r'^register/$', user.RegisterView.as_view(), name='register'),
	url(r'^login/$', user.LoginView.as_view(), name='login'),
	url(r'^about/$', views.AboutView.as_view(), name='about'),
	url(r'^$', user.UserDetail.as_view(), name='user_detail'),
]
