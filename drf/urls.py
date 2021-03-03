from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(
        r'^api/v1/people/(?P<pk>[0-9]+)$',
        views.get_delete_update_person,
        name='get_delete_update_person'
    ),
    url(
        r'^api/v1/people/$',
        views.get_post_people,
        name='get_post_people'
    ),
    path('', views.index, name='home page'),
]
