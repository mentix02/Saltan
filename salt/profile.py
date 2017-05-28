from django.conf.urls import url
from . import user

urlpatterns = [
	url(r'^me/$', user.UserDetail.as_view(), name='profile'),
    url(r'^people/$', user.PeopleList.as_view(), name='people'),
	url(r'^(?P<username>[\w.@+-]+)/$', user.PersonDetail.as_view(), name='person'),
	url(r'^me/edit/$', user.EditView.as_view(), name='edit_profile'),
	url(r'^me/deactivate/$', user.deactivate, name='deactivate'),
]
