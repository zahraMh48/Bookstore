from django.contrib import admin
from .models import Book, Comment


# admin.site.register(Comment, CommentAdmin) # or write another way

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created','recomend','is_active')

admin.site.register(Book) #show Book on admin panel

