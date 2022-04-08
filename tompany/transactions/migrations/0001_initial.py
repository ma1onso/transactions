# Generated by Django 3.2.12 on 2022-04-08 23:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_time', models.DateTimeField(help_text='Date and time of transaction')),
                ('status', models.CharField(choices=[('closed', 'Closed'), ('reversed', 'Reversed'), ('pending', 'Pending')], default='pending', max_length=20)),
                ('approval_status', models.CharField(choices=[('charged', 'Charged'), ('not_charged', 'Not Charged')], default='not_charged', max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='companies.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
