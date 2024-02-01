# Generated by Django 4.2.7 on 2024-02-01 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0002_rename_member1_name_ideagen_member_2_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgpt',
            name='teamLeadPhone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{11}$')]),
        ),
        migrations.AlterField(
            model_name='chatgpt',
            name='teamLeadStudentID',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')]),
        ),
        migrations.AlterField(
            model_name='ideagen',
            name='teamLeadPhone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{11}$')]),
        ),
        migrations.AlterField(
            model_name='ideagen',
            name='teamLeadStudentID',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')]),
        ),
        migrations.AlterField(
            model_name='linefollow',
            name='teamLeadPhone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{11}$')]),
        ),
        migrations.AlterField(
            model_name='linefollow',
            name='teamLeadStudentID',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')]),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='teamLeadPhone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{11}$')]),
        ),
        migrations.AlterField(
            model_name='roborace',
            name='teamLeadStudentID',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')]),
        ),
        migrations.AlterField(
            model_name='soccerbot',
            name='teamLeadPhone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{11}$')]),
        ),
        migrations.AlterField(
            model_name='soccerbot',
            name='teamLeadStudentID',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(regex='^[0-9]{8}$')]),
        ),
    ]
