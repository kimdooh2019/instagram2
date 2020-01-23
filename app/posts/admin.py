from django.contrib import admin

# Register your models here.
from posts.models import Post, PostComment, Images, PostLike


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1


class PostCommentInline(admin.TabularInline):
    model = PostComment
    extra = 1

#### admin customize document 보기
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'create')
    list_display_links = ('title',)
    inlines = [
        ImagesInline,
        PostCommentInline,
    ]


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass
