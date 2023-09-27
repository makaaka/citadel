from django.contrib import admin

# Register your models here.
from .models import Workshop, Participant

# Register your models here.
admin.site.register(Workshop)
admin.site.register(Participant)