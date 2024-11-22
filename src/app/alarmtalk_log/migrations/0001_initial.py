# Generated by Django 4.2.3 on 2024-08-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AlarmTalkLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="생성일시")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일시")),
                ("to_set", models.JSONField(default=list, verbose_name="수신자")),
                ("template_code", models.CharField(max_length=32, verbose_name="템플릿코드")),
                ("title", models.CharField(max_length=128, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "status",
                    models.CharField(
                        choices=[("R", "대기"), ("S", "성공"), ("F", "실패")], default="R", max_length=1, verbose_name="상태"
                    ),
                ),
                ("fail_reason", models.TextField(blank=True, default="", verbose_name="실패사유")),
            ],
            options={
                "verbose_name": "알람톡 로그",
                "verbose_name_plural": "알람톡 로그",
                "db_table": "alarmtalk_log",
            },
        ),
    ]
