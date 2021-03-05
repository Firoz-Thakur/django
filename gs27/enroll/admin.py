from django.contrib import admin
from enroll.models import student


@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stupass','stumail')




#admin.site.register(student,studentAdmin)