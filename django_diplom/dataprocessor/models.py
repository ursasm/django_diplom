import uuid

from django.db import models

class FileData(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    file = models.FileField(verbose_name='Файл с данными', upload_to='files/')