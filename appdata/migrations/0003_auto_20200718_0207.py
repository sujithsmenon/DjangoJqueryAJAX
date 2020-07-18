# Generated by Django 2.2.7 on 2020-07-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0002_auto_20200718_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='integerbox_A',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='integerbox_B',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='integerbox_C',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='integerbox_D',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friend',
            name='new_check_box_A',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='friend',
            name='new_check_box_B',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='friend',
            name='new_check_box_C',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='friend',
            name='new_check_box_D',
            field=models.BooleanField(),
        ),
    ]
