# Generated by Django 2.2.13 on 2020-06-05 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tgjf",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sdasf", models.BigIntegerField(blank=True, null=True)),
                ("safasdf", models.BigIntegerField(blank=True, null=True)),
                ("erett", models.BigIntegerField(blank=True, null=True)),
                ("tyjyuj", models.BigIntegerField(blank=True, null=True)),
                ("ikiol", models.BigIntegerField(blank=True, null=True)),
                ("qwsqwswqq", models.BigIntegerField(blank=True, null=True)),
                ("wdwdwe", models.BigIntegerField(blank=True, null=True)),
                ("dewdwee", models.BigIntegerField(blank=True, null=True)),
                ("efrfrfrf", models.BigIntegerField(blank=True, null=True)),
                ("erfrgth", models.BigIntegerField(blank=True, null=True)),
                (
                    "cfgsf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tgjf_cfgsf",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
