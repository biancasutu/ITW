# Generated by Django 4.1.2 on 2022-11-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='img_not_found', upload_to=''),
        ),
    ]
