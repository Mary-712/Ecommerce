# Generated by Django 4.2.6 on 2023-11-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('contactnumber', models.IntegerField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
