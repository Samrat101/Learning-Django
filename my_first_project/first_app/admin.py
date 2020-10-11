from django.contrib import admin

from first_app.models import topic,webpage,Accessrecord
# Register your models here.
admin.site.register(topic)
admin.site.register(webpage)
admin.site.register(Accessrecord)
