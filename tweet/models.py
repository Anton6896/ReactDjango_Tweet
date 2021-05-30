from django.db import models
from tweetRoot.utils.root_utils import customer_image_file_path


class Tweet(models.Model):
    content = models.TextField()
    image = models.ImageField(default="no_image.jpg", upload_to=customer_image_file_path)

    # def __str__(self):
    #     return

    class Meta:
        db_table = 'tweet'
