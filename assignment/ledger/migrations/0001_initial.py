# Generated by Django 4.1.5 on 2023-01-04 14:29

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
            name='Url_Mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('original_url', models.CharField(max_length=256)),
                ('hash', models.CharField(max_length=10)),
                ('validity', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('amount', models.IntegerField(default=0, verbose_name='금액')),
                ('place', models.CharField(max_length=100, verbose_name='사용처')),
                ('memo', models.CharField(max_length=500, verbose_name='메모')),
                ('ledger_type', models.CharField(choices=[('EXP', '지출'), ('INC', '수입')], max_length=3, verbose_name='지출or수입 여부')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]