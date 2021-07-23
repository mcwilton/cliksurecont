from django.conf.urls import url 
from contacts import views 
 
urlpatterns = [ 
    url(r'^api/contacts$', views.contacts_list),
    url(r'^api/contacts/(?P<pk>[0-9]+)$', views.contacts_detail),
    url(r'^api/contacts/published$', views.contacts_list_published),
]
