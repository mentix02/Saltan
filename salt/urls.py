from django.conf.urls import url, include
from . import views, salt
from django.contrib.auth.views import logout

app_name = 'salt'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^visitor/', include('salt.visitor_urls')),
	url(r'^profile/', include('salt.profile')),
	url(r'^salts/$', salt.salts, name='salts'),
	url(r'^add_salt/$', salt.AddSalt.as_view(), name='add_salt'),
	url(r'^salt/(?P<salt_id>[0-9]+)/$', salt.SaltDetail.as_view(), name='detail'),
	url(r'^salt/delete/(?P<pk>[0-9]+)/$', salt.delete_salt, name='delete_salt'),
	url(r'^logout/$', logout, {'template_name': 'salt/index.html', 'next_page': '/'}, name='logout'),
]
