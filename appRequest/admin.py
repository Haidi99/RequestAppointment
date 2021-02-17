from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Country, MyModelAdmin)
admin.site.register(Company, MyModelAdmin)
admin.site.register(Person, MyModelAdmin)
