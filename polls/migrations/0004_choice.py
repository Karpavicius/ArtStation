# Generated by Django 2.0.13 on 2019-04-28 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('polls', '0003_auto_20190428_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]