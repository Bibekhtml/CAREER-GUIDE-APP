from django.db import models

class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    career = models.ForeignKey(Career, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class TopicTest(models.Model):
    career = models.ForeignKey(Career, related_name='tests', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    questions = models.JSONField()  # Store questions in JSON format
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Certificate(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return f"{self.user.username} - {self.career.title}"

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    videos = models.ManyToManyField(Video, related_name='playlists')

    def __str__(self):
        return self.title