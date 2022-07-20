from django.db import models
from django.urls import reverse
from datetime import date

GENRES = (
  ('A', 'Action/Adventure'),
  ('F', 'FPS'),
  ('3', '3D Platformer'),
  ('2', '2D Platformer'),
  ('W', 'WRPG'),
  ('J', 'JRPG'),
  ('P', 'Puzzle'),
  ('R', 'Rhythm'),
  ('S', 'Stealth'),
  ('4', '4x Strategy'),
  ('O', 'Open World'),
  ('V', 'Visual Novel'),
  ('C', 'Competitive Fighting Game'),
  ('M', 'MOBA'),
  ('L', 'Life Sim'),
  ('I', 'Immersive Sim'),
  ('G', 'General Simulation')
)


class Dev(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('devs_detail', kwargs={'pk': self.id})


class Game(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(
    max_length=1,
    choices=GENRES,
    default=GENRES[0][0]
  )
  release = models.PositiveIntegerField(default=1970)
  description = models.TextField(max_length=250)
  devs = models.ManyToManyField(Dev)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id': self.id})

  def played_today(self):
    return self.playtime_set.filter(date=date.today()).count() > 0

class Playtime(models.Model):
  date = models.DateField('Playtime Date')
  hours = models.PositiveIntegerField()

  game = models.ForeignKey(
    Game,
    on_delete=models.CASCADE
  )

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"{self.hours} played on {self.date}"
