# Generated by Django 2.1.5 on 2019-02-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtpmapapp', '0020_updatelog'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='mvc',
            index=models.Index(fields=['id', 'longitude', 'latitude'], name='dtpmapapp_m_id_0e0677_idx'),
        ),
    ]