#!/root/.pyenv/versions/py3.4.1/bin/python3.4

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'home.views.home_page', name='home'),
    url(r'^total/', 'home.views.total_table', name='total_table')
]

