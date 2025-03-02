# Generated by Django 2.1.11 on 2019-08-30 18:13

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
            name='Cancellation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, verbose_name='reason')),
                ('date', models.DateField(verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('all_day', models.BooleanField(default=False, verbose_name='all day')),
                ('repeat', models.CharField(choices=[('NEVER', 'Never'), ('DAILY', 'Every Day'), ('WEEKDAY', 'Every Weekday'), ('WEEKLY', 'Every Week'), ('BIWEEKLY', 'Every 2 Weeks'), ('MONTHLY', 'Every Month'), ('YEARLY', 'Every Year')], default='NEVER', max_length=15, verbose_name='repeat')),
                ('end_repeat', models.DateField(blank=True, null=True, verbose_name='end repeat')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('background_color', models.CharField(choices=[('eeeeee', 'gray'), ('ff0000', 'red'), ('0000ff', 'blue'), ('00ff00', 'green'), ('000000', 'black'), ('ffffff', 'white')], default='eeeeee', max_length=10, verbose_name='background color')),
                ('background_color_custom', models.CharField(blank=True, help_text='Must be a valid hex triplet. Default is gray (eeeeee)', max_length=6, verbose_name='background color custom')),
                ('font_color', models.CharField(choices=[('eeeeee', 'gray'), ('ff0000', 'red'), ('0000ff', 'blue'), ('00ff00', 'green'), ('000000', 'black'), ('ffffff', 'white')], default='000000', max_length=10, verbose_name='font color')),
                ('font_color_custom', models.CharField(blank=True, help_text='Must be a valid hex triplet. Default is black (000000)', max_length=6, verbose_name='font color custom')),
                ('categories', models.ManyToManyField(blank=True, to='happenings.Category', verbose_name='categories')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('address_line_1', models.CharField(blank=True, max_length=255, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=255, verbose_name='Address Line 2')),
                ('address_line_3', models.CharField(blank=True, max_length=255, verbose_name='Address Line 3')),
                ('state', models.CharField(blank=True, max_length=63, verbose_name='State / Province / Region')),
                ('city', models.CharField(blank=True, max_length=63, verbose_name='City / Town')),
                ('zipcode', models.CharField(blank=True, max_length=31, verbose_name='ZIP / Postal Code')),
                ('country', models.CharField(blank=True, max_length=127, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ManyToManyField(blank=True, to='happenings.Location', verbose_name='locations'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, to='happenings.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='cancellation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancellations', related_query_name='cancellation', to='happenings.Event'),
        ),
    ]
