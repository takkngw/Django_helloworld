# Generated by Django 4.2.13 on 2024-06-17 07:27

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]
