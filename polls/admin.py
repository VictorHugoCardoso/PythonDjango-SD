from django.contrib import admin

from .models import Question
from .models import assinado

admin.site.register(Question)
admin.site.register(assinado)