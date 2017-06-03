from django.conf.urls import url
from . import views


app_name = "email_validate"

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^success$', views.success, name='success'),
]
