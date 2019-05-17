from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url('tmc/', include('TMC.urls')),
    url('admin/', admin.site.urls),
]
