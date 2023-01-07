from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','Item_name','Total_Stock_In_KG','Price_Per_KG')

