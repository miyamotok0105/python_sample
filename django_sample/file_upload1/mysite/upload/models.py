# -*- coding: utf-8 -*-
from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Document(models.Model):
    #フォルダに入れるバージョン
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    #============================
    #サムネイルに表示する時バージョン
    origin = models.ImageField(upload_to="documents/%Y/%m/%d/", default='documents/None/no-img.jpg')

    big = ImageSpecField(source="origin", processors=[ResizeToFill(1280, 1024)],
                         format='JPEG')

    thumbnail = ImageSpecField(source='origin',
                            processors=[ResizeToFill(250,250)], format="JPEG",
                            options={'quality': 60})

    middle = ImageSpecField(source='origin',
                        processors=[ResizeToFill(600, 400)], format="JPEG",
                        options={'quality': 75})

    small = ImageSpecField(source='origin',
                            processors=[ResizeToFill(75,75)], format="JPEG",
                            options={'quality': 50})