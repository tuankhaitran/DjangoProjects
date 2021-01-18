from django.contrib import admin
from groups import models
# Register your models here.


# Allow to utilize django admin interface to edit model in the same page as the parent model
# Our GroupMember is 
class GroupMemberInline(admin.TabularInline):
    model=models.GroupMember



admin.site.register(models.Group)