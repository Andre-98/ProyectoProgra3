# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.contrib import admin

from apps.adopcion.models import Persona, Registro_produc

# Register your models here.
admin.site.register(Persona)
admin.site.register(Registro_produc)