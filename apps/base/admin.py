from django.contrib import admin
from apps.base import models
from django.contrib.auth.models import User, Group
# Register your models here.
class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'phone', 'email')
    search_fields = ('title', 'phone', 'email')

class SlideImage1Inline(admin.TabularInline):
    model = models.SlideImage1
    extra = 1

class SlideImage2Inline(admin.TabularInline):
    model = models.SlideImage2
    extra = 1


class SlideFilterAdmin(admin.ModelAdmin):
    list_display = ("title", )
    list_filter = ('title', )
    search_fields = ('title', )
    inlines = (SlideImage1Inline,SlideImage2Inline)

class NumbersFilterAdmin(admin.ModelAdmin):
    list_filter = ('client', 'team', 'experience', 'critical', 'review' )
    search_fields = ('client', 'team', 'experience', 'critical', 'review' )

class AboutFilterAdmin(admin.ModelAdmin):
    list_filter = ('descriptions', )
    search_fields = ('descriptions', )

admin.site.register(models.Numbers, NumbersFilterAdmin)
admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.About, AboutFilterAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
