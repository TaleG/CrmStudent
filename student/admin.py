from django.contrib import admin

# Register your models here.
from student import models

admin.site.register(models.Customer)
admin.site.register(models.ConsultRecord)
admin.site.register(models.ClassList)
admin.site.register(models.CouresRecord)
admin.site.register(models.StudyRecord)
admin.site.register(models.UserProfile)
admin.site.register(models.Course)
admin.site.register(models.School)