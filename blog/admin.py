from django.contrib import admin
from blog.models import Post

@admin.register(Post)  # admin.site.register() 함수 사용해도 가능
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title','content')
    prepopulated_fields = {'slug':('title',)}