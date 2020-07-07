from django.contrib import admin
from .models import Board, Topic


class TopicInlineModel(admin.StackedInline):
    model = Topic
    extra = 0


class BoardAdmin(admin.ModelAdmin):
    inlines = [TopicInlineModel]


admin.site.register(Topic, TopicInlineModel)
admin.site.register(Board, BoardAdmin)
