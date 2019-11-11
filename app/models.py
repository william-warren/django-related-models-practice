from django.db import models


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    artist_name = models.TextField()


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    seconds = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    # Method for converting the songs total duration in
    # second to a M:SS format.

    def formatted_duration(self):
        minutes = self.seconds // 60
        leftover_seconds = self.seconds - (60 * minutes)
        if leftover_seconds == 0:
            leftover_seconds = "00"
        return f"{minutes}:{leftover_seconds}"
