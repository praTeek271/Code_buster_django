from django.contrib import admin
from resources.models import Team,FeedBack,FAQ,Resourses
# Register your models here.

admin.site.site_header="Code Busters"
admin.site.site_title="Code Busters"
admin.site.index_title="Code Busters"

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
    list_display=("name","category","subject", "show")
    list_filter = ("category","subject","image",)
    search_fields = ("category","name","image", )
    editable_list = ('show','category')
    action_list=('show')

    

    # show.boolean=True