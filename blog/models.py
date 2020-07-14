from django.db import models
from django.urls import reverse

import logging
logger = logging.getLogger(__name__)

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        logger.info('get_absolute_url 진입')
        logger.info('get_absolute_url 진입 :1 self :::')  #slug sdfsdfs
        logger.info('get_absolute_url 진입 :2 self.slug'+ str(self.slug))  #slug sdfsdfs
        logger.info('get_absolute_url 진입 :3 self.slug'+ self.slug)  #slug sdfsdfs
        # logger.info('get_absolute_url 진입 :4 '+ self.get())  #slug sdfsdfs
        logger.info('get_absolute_url 진입 :5 '+ self.slug)  #slug sdfsdfs
        logger.info('get_absolute_url 진입 :6 '+ self.Post)  #slug sdfsdfs
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

