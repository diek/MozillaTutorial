# Generated by Django 3.0.2 on 2020-01-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200127_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Book availability', max_length=1),
        ),
        migrations.AddConstraint(
            model_name='bookinstance',
            constraint=models.CheckConstraint(check=models.Q(status__in=['m', 'o', 'a', 'r']), name='loan_status_valid'),
        ),
    ]
