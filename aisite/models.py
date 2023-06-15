from django.db import models


class Site(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='sites', verbose_name="تصویر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "سایت‌ها"
