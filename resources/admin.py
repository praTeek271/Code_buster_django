from django.contrib import admin
from resources.models import Team,FeedBack,FAQ,Resourses
# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position")

@admin.register(FeedBack)
class FeedbackAdmin(admin.ModelAdmin):
    pass

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
   pass

@admin.register(Resourses)
class ResoursesAdmin(admin.ModelAdmin):
    list_display=("category","name", "show")
    list_filter = ("category",)
    search_fields = ("category","name", )

