from django.db import models
from tweetRoot.utils.root_utils import customer_image_file_path
from PIL import Image


class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(default="no_image.jpg", upload_to=customer_image_file_path)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'tweet: {self.pk}'

    class Meta:
        db_table = 'tweet'

    def save(self, *args, **kwargs):
        super(Tweet, self).save(*args, **kwargs)

        try:
            img = Image.open(self.image.path)
            output_size = (300, 300)

            if img.height > 300 or img.width > 300:
                img.thumbnail(output_size)
                img.save(self.image.path)
        except IOError:
            print(f'save problem with file in Tweet model')
