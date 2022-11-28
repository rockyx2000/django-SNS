from django.contrib import admin
from .models import BoardModel, LikeModel, ReadModel

# Register your models here.

admin.site.register(BoardModel)
admin.site.register(LikeModel)
admin.site.register(ReadModel)
