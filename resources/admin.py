from django.contrib import admin
from resources.models import Team,FeedBack,FAQ,Resourses,event
# Register your models here.

admin.site.site_header="Code Busters"
admin.site.site_title="Code Busters"
admin.site.index_title="Code Busters"

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position")

@admin.register(FeedBack)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("subject","name","date")

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
   list_display = ("que","category")

@admin.register(Resourses)
class ResoursesAdmin(admin.ModelAdmin):
    list_display=("name","category","subject", "show")
    list_filter = ("category","subject","image",)
    search_fields = ("category","name","image", )
    editable_list = ('show','category')
    action_list=('show')

    
@admin.register(event)
class EventsAdmin(admin.ModelAdmin):
    list_display=("title","category","thumbnail_img", "show")
    list_filter = ("category","show",)
    search_fields = ("category","title","show", )
    editable_list = ('show','category')
    action_list=('show')

    

    # show.boolean=True