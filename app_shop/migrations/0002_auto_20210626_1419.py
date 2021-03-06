# Generated by Django 3.2.4 on 2021-06-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='detail_text',
            new_name='Detail_text',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='old_price',
            new_name='old_Price',
        ),
        migrations.AlterField(
            model_name='product',
            name='mainimage',
            field=models.ImageField(upload_to=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview_text',
            field=models.TextField(max_length=250, verbose_name='Preview Text'),
        ),
    ]
