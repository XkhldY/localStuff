# Generated by Django 3.1.7 on 2021-04-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justmodels', '0003_auto_20210402_0513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='stock_name',
            new_name='symbol',
        ),
        migrations.AddField(
            model_name='stocks',
            name='company_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
