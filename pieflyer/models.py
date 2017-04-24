from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Score(models.Model):
    #score_list = []
    #def __str__(self):
    #    self.score_list = self.score_list.sorted()
    #    return [self.score_list[i] for i in xrange(0, len(self.score_list))] 
    score = 0
    def __str__(self):
        return self.score
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text