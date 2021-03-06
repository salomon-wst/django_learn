# Generated by Django 2.2 on 2019-05-13 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email_id', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('user_type', models.DecimalField(decimal_places=0, max_digits=2)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
