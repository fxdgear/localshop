from django.contrib import admin

from localshop.apps.packages import models

admin.site.register(models.Package)
