# Generated by Django 2.0.3 on 2018-04-08 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0008_auto_20180408_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='deal',
            old_name='keyword1',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='deal',
            old_name='keyword2',
            new_name='main_attraction',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='keyword3',
        ),
        migrations.AddField(
            model_name='deal',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='deal.Type'),
            preserve_default=False,
        ),
    ]
