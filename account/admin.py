from django.contrib import admin

# Register your models here.
from account.models import Userprofile


class AdminChange(admin.ModelAdmin):
    list_display = ('user', 'Info','city','phone')

    def get_queryset(self, request):
        query= super(AdminChange,self).get_queryset(request)
        query = query.order_by('city')
        return query

    def Info(self, obj):
        return obj.name


admin.site.register(Userprofile,AdminChange)
