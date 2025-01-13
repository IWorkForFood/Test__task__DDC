from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.images import get_image_dimensions
import uuid



class ResizeImageMixin:
    def resize(self, startImageField: models.ImageField, endImageField,  size:tuple):
        width, height = get_image_dimensions(startImageField)
        if width < height:
             size = (200, height)
        else:
            size = (width ,200)
        im = Image.open(startImageField)  # Catch original
        source_image = im.convert('RGB')
        source_image.thumbnail(size)  # Resize to size
        output = BytesIO()
        source_image.save(output, format='JPEG') # Save resize image to bytes
        output.seek(0)

        content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
        file = File(content_file)

        random_name = f'{uuid.uuid4()}.jpeg'
        endImageField.save(random_name, file, save=False)

def photo_directory_path(instance, filename):
    now = datetime.now().strftime('%Y/%m/%d/%H/%M/%S')
    return 'user_{0}/n/{1}/{2}'.format(instance.author.id, filename, now)

def edited_photo_directory_path(instance, filename):
    now = datetime.now().strftime('%Y/%m/%d/%H/%M/%S')
    return 'user_{0}/e/{1}/{2}'.format(instance.author.id, filename, now)

class NewsModel(ResizeImageMixin, models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок новости')
    main_image = models.ImageField(blank=True, null=True, upload_to=photo_directory_path)
    image_preview = models.ImageField(blank=True, null=True, upload_to=edited_photo_directory_path)
    text = models.TextField(verbose_name='Текст новости')
    publication_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.main_image:
            self.resize(self.main_image, self.image_preview, (200, 200))

        super().save(*args, **kwargs)

