from django.contrib import admin
from .models import Student


admin.site.site_header = "Curd Project"
admin.site.index_title = "Curd Admin"

# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','roll','name','email','password')