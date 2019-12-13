# coding:utf-8
from django.db import models


class NewsClass(models.Model):
    name = models.CharField("分类名称", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "资讯类别"
        verbose_name_plural = "资讯类别"


class News(models.Model):
    # 默认添加
    # id = models.AutoField(primary_key=True)
    title = models.CharField("文章标题", max_length=30)
    content = models.TextField("文章内容")
    date = models.DateTimeField("发布时间")
    show = models.BooleanField("是否显示")
    news_class = models.ForeignKey(
        NewsClass, verbose_name="文章分类", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "资讯"
        verbose_name_plural = "资讯"
