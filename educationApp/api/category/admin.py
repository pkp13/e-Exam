from django.contrib import admin
from .models import Subject, Topic, Difficulty, Source
# Register your models here.

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Difficulty)
admin.site.register(Source)