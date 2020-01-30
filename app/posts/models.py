from django.db import models

from members.models import User
import re


class Post(models.Model):
    TAG_PATTERN = re.compile(r'#(\w+)')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    content_html = models.TextField(blank=True)
    heart = models.ManyToManyField(
        User,
        through='PostLike',
        related_name='like_post_set')
    create = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        'Tag', verbose_name='해시태그 목록', related_name='posts', blank=True,
    )

    # comment = models.ManyToManyField('PostComment')
    # images = models.ManyToManyField('Images')
    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return self.title

    def _save_html(self):
        self.content_html = re.sub(
            self.TAG_PATTERN,
            r'<a href="/explore/tags/\g<1>\">#\g<1></a>',
            self.content,
        )

    def _save_tags(self):
        tag_name_list = re.findall(self.TAG_PATTERN, self.content)
        tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_name_list]
        self.tags.set(tags)

    def save(self, *args, **kwargs):
        self._save_html()
        super().save(*args, **kwargs)
        self._save_tags()


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images')


class PostLike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class PostComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ('-pk',)


class Tag(models.Model):
    name = models.CharField('태그명', max_length=100)

    def __str__(self):
        return self.name
