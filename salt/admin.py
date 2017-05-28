from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Salt)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(Pepper)
