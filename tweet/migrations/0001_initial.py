# Generated by Django 3.2.3 on 2021-05-30 19:37

from django.db import migrations, models
import tweetRoot.utils.root_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(default='no_image.jpg', upload_to=tweetRoot.utils.root_utils.customer_image_file_path)),
            ],
            options={
                'db_table': 'tweet',
            },
        ),
    ]
