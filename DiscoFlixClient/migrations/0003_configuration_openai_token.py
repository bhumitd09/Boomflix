# Generated by Django 5.1.2 on 2024-11-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiscoFlixClient', '0002_configuration_is_tagging_enabled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='openai_token',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='OpenAI Token'),
        ),
    ]
