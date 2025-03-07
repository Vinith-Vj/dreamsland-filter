# Generated by Django 5.1.5 on 2025-03-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamland_app', '0007_remove_agent_allocated_locations_alter_agent_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_owner_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bhk',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
