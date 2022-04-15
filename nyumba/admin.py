from django.contrib import admin
from .models import Agents, About, Comment, Photo, Video, Slide

# Register your models here.
admin.site.register(Agents)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Slide)