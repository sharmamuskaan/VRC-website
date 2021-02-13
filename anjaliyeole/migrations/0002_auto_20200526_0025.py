# Generated by Django 3.0.6 on 2020-05-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anjaliyeole', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AreasofExpertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='buy_link',
            field=models.URLField(default='default'),
        ),
        migrations.AddField(
            model_name='books',
            name='picture',
            field=models.ImageField(max_length=255, null=True, upload_to='pictures'),
        ),
        migrations.AddField(
            model_name='books',
            name='published',
            field=models.DateField(auto_now=True),
        ),
    ]
