# Generated by Django 5.0.7 on 2024-08-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0004_alter_organization_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address_line_1',
            field=models.CharField(max_length=255, verbose_name='Address Line 1'),
        ),
    ]