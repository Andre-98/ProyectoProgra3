from __future__ import unicode_literals

from __future__ import absolute_import

from django.conf.urls import url, include

from apps.Animal.views import index, Animal_view

#app_name='Animal'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', Animal_view, name='Animal_crear'),
]