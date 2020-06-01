from django.db import models

# Create your models here.

class Show(models.Model):
    SEASON_CHOICES = [
        ('winter', 'Winter'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
    ]

    mal_id = models.PositiveIntegerField("MyAnimeList ID", primary_key=True, unique=True, blank=False)
    name = models.CharField("Name", max_length=250, blank=False)
    year = models.PositiveIntegerField("Year", blank=False, default=1960)
    season = models.CharField("Season", max_length=250, choices=SEASON_CHOICES, blank=False, default='winter')

    def __str__(self):
        return self.name

    @property
    def release_date(self):
        return '%s %s' % (self.season, str(self.year))

class Theme(models.Model):
    name = models.CharField("Name", max_length=250, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    theme_type = models.CharField("Type", max_length=250, blank=False)
    url = models.URLField("WebM URL", blank=False)
    priority = models.IntegerField("Priority", blank=False, default=0)
    notes = models.CharField("Notes", max_length=250, blank=True, default="")

    def __str__(self):
        return self.name

    @property
    def listed_name(self):
        return '%s (%s)' % (self.theme_type, self.notes)

    @property
    def show_name(self):
        return self.show.name
