from django.db import models
import datetime

#from django.db import models
from django.utils import timezone

# Create your models here.
# class SuankeChoiceQuestionSubmitDetailLog(models.Model):
#    is_true_answer = models.IntegerField()
#    submit_context = models.CharField(max_length=255, blank=True, null=True)
#    created_at = models.DateTimeField()
#    choice_question = models.ForeignKey('SuankeChoiceQuestions', models.DO_NOTHING)
#    user = models.ForeignKey('SuankeUser', models.DO_NOTHING)

#    class Meta:
#        managed = False
#        db_table = 'suanke_choice_question_submit_detail_log'


#class SuankeChoiceQuestionUserAnswerData(models.Model):
#    submit_count = models.SmallIntegerField()
#    is_true_answer = models.IntegerField()
#    first_submit_time = models.DateTimeField()
#    last_submit_time = models.DateTimeField()
#    choice_question = models.ForeignKey('SuankeChoiceQuestions', models.DO_NOTHING)
#    user = models.ForeignKey('SuankeUser', models.DO_NOTHING)

#    class Meta:
#        managed = False
#        db_table = 'suanke_choice_question_user_answer_data'


#class SuankeChoiceQuestions(models.Model):
#    title = models.CharField(max_length=50)
#    content = models.TextField()
#    course_path = models.CharField(max_length=20)
#    true_answer = models.CharField(max_length=5)
#    trigger_time = models.DateTimeField(blank=True, null=True)
#    is_send_now = models.IntegerField()
#    created_at = models.DateTimeField()
#    updated_at = models.DateTimeField()
#    is_delete = models.IntegerField()
#    creator = models.ForeignKey('SuankeUser', models.DO_NOTHING)
#    last_update_user = models.ForeignKey('SuankeUser', models.DO_NOTHING)
#    choice_analysis = models.TextField(blank=True, null=True)

#    class Meta:
#        managed = False
#        db_table = 'suanke_choice_questions'

#    def __str__(self):
#        return self.content
#    def question_Rate(self):
#        return true_answer / 100
#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#    def was_published_recently(self):
#        now = timezone.now()
#        return now - datetime.timedelta(days=1) <= self.updated_at <= now



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    question_rate = models.FloatField(default=0)
    question_right = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text
    def question_Rate(self):
        return question_rate / 100
#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Student(models.Model):
    question_number = models.CharField(max_length=32, default='title')
    student_name= models.TextField(null=True)



 
 
class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"
 
 
class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)
     
    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"
 
    def __str__(self):
        return self.name


