from django.urls import path, re_path
from django.conf.urls import include

from Register import views


urlpatterns = [
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]