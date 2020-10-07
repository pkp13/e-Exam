from django.db import models
from api.category.models import Subject, Topic, Difficulty, Source
# Create your models here.

class Question(models.Model):
    questionDescription = models.CharField(max_length = 250, blank = True, null = True)
    image = models.ImageField(upload_to = 'images', blank = True, null = True)
    equation = models.CharField(max_length=100, blank = True, null = True)

    equations_answere = models.BooleanField(default=False)
    optionA = models.CharField(max_length = 100, blank = True, null = True)
    optionB = models.CharField(max_length = 100, blank = True, null = True)
    optionC = models.CharField(max_length = 100, blank = True, null = True)
    optionD = models.CharField(max_length = 100, blank = True, null = True)
    answere = models.CharField(max_length = 1, blank = True, null = True)
    answereDescription = models.CharField(max_length = 250, blank = True, null = True)
    
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    difficulty = models.ForeignKey(Difficulty, on_delete = models.SET_NULL, blank = True, null = True)
    subject = models.ForeignKey(Subject, on_delete = models.SET_NULL, blank = True, null = True)
    category = models.ForeignKey(Topic, on_delete = models.SET_NULL, blank = True, null = True)
    source = models.ForeignKey(Source, on_delete = models.SET_NULL, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    
    def __str__(self):
        return self.questionDescription