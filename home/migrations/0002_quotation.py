# Generated by Django 3.1.1 on 2020-09-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('customer_email', models.EmailField(max_length=255)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
