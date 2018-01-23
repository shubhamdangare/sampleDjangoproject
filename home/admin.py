from django.contrib import admin

# Register your models here.
from home.models import Friendlist, Datastrore

admin.site.register(Datastrore)
admin.site.register(Friendlist)