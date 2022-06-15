# Generated by Django 3.2.13 on 2022-04-19 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roycebulksms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_message', models.TextField()),
                ('phone_number', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('message_id', models.CharField(blank=True, max_length=250, null=True)),
                ('response_code', models.CharField(blank=True, max_length=250, null=True)),
                ('response_description', models.CharField(blank=True, max_length=250, null=True)),
                ('network_id', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_status', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_description', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_tat', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_network_id', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_time', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_response_description', models.CharField(blank=True, max_length=250, null=True)),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roycebulksms.senderid')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('other_name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=250)),
                ('alt_phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roycebulksms.group')),
            ],
        ),
    ]
