# Generated by Django 2.2.12 on 2022-07-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20220720_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.CharField(choices=[('A', 'Action/Adventure'), ('R', 'RPG'), ('F', 'FPS'), ('3', '3D Platformer'), ('2', '2D Platformer'), ('P', 'Puzzle'), ('R', 'Rhythm'), ('S', 'Strategy'), ('O', 'Open World'), ('V', 'Visual Novel'), ('C', 'Competitive Fighting Game'), ('M', 'MOBA'), ('L', 'Life Sim'), ('I', 'Immersive Sim'), ('G', 'General Simulation')], default='A', max_length=1),
        ),
    ]