# Generated by Django 5.1.5 on 2025-02-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "dreamland_app",
            "0004_location_remove_property_acre_remove_property_cent_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Agent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                (
                    "agent_id",
                    models.CharField(editable=False, max_length=20, unique=True),
                ),
                ("username", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("personal_address", models.TextField()),
                ("district_place", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                ("contact_number", models.CharField(max_length=15)),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "allocated_locations",
                    models.ManyToManyField(
                        related_name="agents", to="dreamland_app.location"
                    ),
                ),
            ],
            options={
                "verbose_name": "Agent",
                "verbose_name_plural": "Agents",
                "db_table": "agent",
            },
        ),
    ]
