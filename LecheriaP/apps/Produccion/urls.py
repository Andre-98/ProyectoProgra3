from __future__ import unicode_literals

from __future__ import absolute_import

from django.conf.urls import url

from apps.Produccion.views import index_Produccion

urlpatterns = [
    url(r'^$', index_Produccion),
]