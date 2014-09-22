from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        db_table = 'lp_subject'
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=64)
    subject = models.ForeignKey(Subject)
    data = models.TextField()
    class Meta:
        db_table = 'lp_exercise'
    def __str__(self):
        return self.name

class SchoolClass(models.Model):
    name = models.CharField(max_length=64)
    school_name = models.CharField(max_length=128)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    data = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'lp_schoolclass'
    def __str__(self):
        return "Class '%s' from school '%s'" % (self.name, self.school_name)

class SubjectConfig(models.Model):
    subject = models.ForeignKey(Subject)
    school_class = models.ForeignKey(SchoolClass)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    data = models.TextField()
    class Meta:
        db_table = 'lp_subject_config'
    def __str__(self):
        return "Config %s for %s" % (self.subject, self.school_class)

class ExerciseConfig(models.Model):
    exercise = models.ForeignKey(Exercise)
    school_class = models.ForeignKey(SchoolClass)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    data = models.TextField()
    class Meta:
        db_table = 'lp_exercise_config'
    def __str__(self):
        return "Config %s for %s" % (self.exercise, self.school_class)

class LPUser(models.Model):
    user = models.OneToOneField(User)
    school_class = models.ManyToManyField(SchoolClass, null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'lp_user'
    def __str__(self):
        return self.user.username

class Statistics(models.Model):
    user = models.ForeignKey(LPUser)
    subject = models.ForeignKey(Subject)
    exercise = models.ForeignKey(Exercise)
    data = models.TextField()
    class Meta:
        db_table = 'lp_statistics'
    def __str__(self):
        return "Statistics for '%s': %s" % (self.user, self.data)
