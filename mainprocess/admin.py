# from django.contrib import admin
# from .models import Profile,Java,Python,C,Cpp,ConnectRequest,Message
# # Register your models here.

# from tinymce.widgets import TinyMCE

# class CAdmin(admin.ModelAdmin):
#     formfield_overides={
#         models.TextField:{'widget':TinyMCE()},
#     }
from django.contrib import admin

# Register your models here.
from .models import *
from tinymce.widgets import TinyMCE

class CAdmin(admin.ModelAdmin):


    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Profile)
admin.site.register(C,CAdmin)
admin.site.register(Cpp)
admin.site.register(Java)
admin.site.register(Python)
admin.site.register(ConnectRequest)
admin.site.register(Message)
