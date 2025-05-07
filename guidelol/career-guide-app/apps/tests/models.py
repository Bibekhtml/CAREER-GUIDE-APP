from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class UserTest(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.title}"