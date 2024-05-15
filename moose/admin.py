from django.contrib import admin
from .models import About,Blog,Subscription,Contact,Tag,Comments,Contacts
# Register your models here.


admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Subscription)
admin.site.register(Contact)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Contacts)