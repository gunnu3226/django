# Generated by Django 4.2.3 on 2024-08-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
            ],
            options={
                "verbose_name": "채팅",
                "verbose_name_plural": "채팅",
                "db_table": "chat",
                "ordering": ["-updated_at", "-created_at"],
            },
        ),
    ]
