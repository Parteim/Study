from django.contrib import admin

from .models import Topic, Course, CourseLevel, MaterialLink, MaterialText, MaterialImage, Material

admin.site.register([Course, CourseLevel, Topic, Material, MaterialText, MaterialImage, MaterialLink, ])
