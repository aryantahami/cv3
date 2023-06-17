from django.db import models
from django.urls import reverse


class Site(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='sites', verbose_name="تصویر")

    def get_absolute_url(self):
        return reverse('site_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "سایت‌ها"
