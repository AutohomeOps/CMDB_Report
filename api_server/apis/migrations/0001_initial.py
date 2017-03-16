# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certname', models.CharField(max_length=50, unique=True)),
                ('sn', models.CharField(max_length=100, unique=True, verbose_name='SN')),
                ('manufactory', models.CharField(max_length=50, verbose_name='\u670d\u52a1\u5668\u5382\u5546')),
                ('productname', models.CharField(max_length=50, verbose_name='\u670d\u52a1\u5668\u4ea7\u54c1\u540d\u79f0')),
                ('model', models.CharField(max_length=50, verbose_name='\u670d\u52a1\u5668\u578b\u53f7')),
                ('os_type', models.CharField(max_length=10, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7c7b\u578b')),
                ('os_distribution', models.CharField(max_length=10, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u53d1\u884c\u7248\u672c')),
                ('os_release', models.CharField(max_length=10, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c\u53f7')),
                ('cpu_count', models.IntegerField(default=0, verbose_name='CPU\u7269\u7406\u4e2a\u6570')),
                ('cpu_core_count', models.IntegerField(default=0, verbose_name='CPU\u903b\u8f91\u6838\u6570')),
                ('cpu_model', models.CharField(max_length=50, verbose_name='CPU\u578b\u53f7')),
                ('nic_count', models.IntegerField(default=0, verbose_name='\u7f51\u5361\u4e2a\u6570')),
                ('nic', jsonfield.fields.JSONField(verbose_name='\u7f51\u5361\u4fe1\u606f')),
                ('raid_adaptor_count', models.IntegerField(verbose_name='Raid\u5361\u63a7\u5236\u5668\u4e2a\u6570')),
                ('raid_adaptor', jsonfield.fields.JSONField(null=True, verbose_name='Raid\u5361\u63a7\u5236\u5668\u7ea4\u7ec6\u4fe1\u606f')),
                ('raid_type', models.CharField(max_length=50, null=True, verbose_name='Raid\u7c7b\u578b')),
                ('physical_disk_driver', jsonfield.fields.JSONField(null=True, verbose_name='\u786c\u76d8\u8be6\u7ec6\u4fe1\u606f')),
                ('ram_size', models.IntegerField(default=0, verbose_name='\u5185\u5b58\u603b\u5bb9\u91cf')),
                ('ram_slot', jsonfield.fields.JSONField(null=True, verbose_name='\u5185\u5b58\u8be6\u7ec6\u4fe1\u606f')),
                ('setuptime', models.DateTimeField(blank=True, null=True, verbose_name='\u7cfb\u7edf\u5b89\u88c5\u65f6\u95f4')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
