# Generated by Django 2.2.12 on 2022-07-20 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('A', 'Action/Adventure'), ('R', 'RPG'), ('F', 'FPS'), ('3', '3d Platformer'), ('2', '2d Platformer'), ('P', 'Puzzle'), ('R', 'Rhythm'), ('S', 'Strategy'), ('O', 'Open World'), ('V', 'Visual Novel'), ('C', 'Competitive Fighting Game'), ('M', 'MOBA')], default='A', max_length=1)),
                ('release', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=250)),
                ('devs', models.ManyToManyField(to='main_app.Dev')),
            ],
        ),
        migrations.CreateModel(
            name='Playtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Playtime Date')),
                ('hours', models.PositiveIntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Game')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
