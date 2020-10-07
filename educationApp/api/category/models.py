from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length = 250, blank = True, null = True)
    
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length = 250, blank = True, null = True)
    
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    subject = models.ForeignKey(Subject, on_delete = models.SET_NULL, blank = True, null = True)
    higherCategory = models.ForeignKey("self", on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self):
        return self.name



class Difficulty(models.Model):
    difficultyLevel = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.difficultyLevel


class Source(models.Model):
    sourceName = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.sourceName

