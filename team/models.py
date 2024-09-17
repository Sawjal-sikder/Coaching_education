from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=55, verbose_name="Team Member Name")
    title = models.CharField(max_length=255, verbose_name="Team Member Title")
    thumbnail = models.ImageField(upload_to='team_thumbnails/', verbose_name="Profile Image")
    description = models.TextField(verbose_name="Team Member Description")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"