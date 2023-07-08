# Generated by Django 4.2.3 on 2023-07-08 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("alias", models.SlugField(max_length=200, unique=True)),
                ("url", models.URLField(max_length=2048)),
                ("hits", models.PositiveBigIntegerField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-created", "alias"],
                "get_latest_by": "created",
                "indexes": [
                    models.Index(
                        fields=["created"], name="shortener_l_created_4cbdb9_idx"
                    ),
                    models.Index(
                        fields=["updated"], name="shortener_l_updated_6c760f_idx"
                    ),
                    models.Index(fields=["url"], name="shortener_l_url_793502_idx"),
                    models.Index(fields=["hits"], name="shortener_l_hits_d0418e_idx"),
                ],
            },
        ),
    ]
