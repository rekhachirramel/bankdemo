from django.contrib import admin
from .models import Branch
from .models import District
from .models import ProcessData
# Register your models here.
admin.site.register(Branch)
admin.site.register(District)
admin.site.register(ProcessData)