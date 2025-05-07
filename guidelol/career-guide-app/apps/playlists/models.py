from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='teachers/')

    def __str__(self):
        return self.name

class Playlist(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, related_name='playlists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title