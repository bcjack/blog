from django.contrib import admin
from miniblog.models import *

admin.site.register(Style)
admin.site.register(Reply)
admin.site.register(Blog,BlogAdmin)

