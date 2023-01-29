from django.contrib import admin

# Register your models here.
from .models import Parties,Poll

admin.site.register([Poll,Parties])
