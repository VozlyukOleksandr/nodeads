from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^group_list/', GroupList.as_view()),
    url(r'^create_group/', form),
    url(r'^create_element/(?P<group>[0-9]+)/', form_),
    url(r'^(?P<group_id>[0-9]+)/', ElementList.as_view())
]