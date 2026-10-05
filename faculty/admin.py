from django.contrib import admin

from faculty.models import Department, ExchangeProgram, MainPage, Program, Teacher

admin.site.register(MainPage)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(ExchangeProgram)
