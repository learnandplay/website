# -*- coding: UTF-8 -*-
## @package models
# Modèles utilisés pour l'ORM de django
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

## Classe Subject\n
# Un sujet d'études (Maths, ...)
class Subject(models.Model):
    ## Le nom du sujet
    name = models.CharField(max_length=32)
    ## Reference du sujet
    reference = models.CharField(max_length=32)
    ## Données liées au sujet
    data = models.TextField()
    class Meta:
        db_table = 'lp_subject'
    def __str__(self):
        return self.name

## Classe Exercise\n
# Classe servant de base pour les exercices personnalisés
class Exercise(models.Model):
    ## Nom de l'exercice
    name = models.CharField(max_length=64)
    ## Sujet d'étude de l'exercice
    subject = models.ForeignKey(Subject)
    ## Reference de l'exercice
    reference = models.CharField(max_length=32)
    ## Données liées à l'exercice
    data = models.TextField()
    class Meta:
        db_table = 'lp_exercise'
    def __str__(self):
        return self.name

## Classe SchoolClass\n
# Représente une classe
class SchoolClass(models.Model):
    ## Nom de la classe
    name = models.CharField(max_length=64)
    ## Nom de l'établissement
    school_name = models.CharField(max_length=128)
    ## Mot de passe de la classe
    password = models.CharField(max_length=128)
    ## Date de création
    creation_date = models.DateTimeField(auto_now_add=True)
    ## Date de modification
    modification_date = models.DateTimeField(auto_now=True)
    ## Données liées à la classe
    data = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'lp_schoolclass'
    def __str__(self):
        return "Class '%s' from school '%s'" % (self.name, self.school_name)

## Classe SubjectConfig\n
# Classe servant à personnaliser un sujet d'étude
class SubjectConfig(models.Model):
    ## Nom de la configuration
    name = models.CharField(max_length=64)
    ## Sujet d'étude de base
    subject = models.ForeignKey(Subject)
    ## Classe pour laquelle le sujet est personnalisé
    school_class = models.ForeignKey(SchoolClass, blank=True, null=True)
    ## Date de début de mise en place de la configuration
    start_date = models.DateTimeField(null=True, blank=True)
    ## Date de fin de mise en place de la configuration
    end_date = models.DateTimeField(null=True, blank=True)
    ## Données de configuration
    data = models.TextField()
    class Meta:
        db_table = 'lp_subject_config'
    def __str__(self):
        return "Config %s for %s" % (self.subject, self.school_class)

## Classe ExerciseConfig\n
# Classe servant à personnaliser un exercice
class ExerciseConfig(models.Model):
    ## Nom de la configuration
    name = models.CharField(max_length=64)
    ## Exercice de base
    exercise = models.ForeignKey(Exercise)
    ## Classe pour laquelle l'exercice est personnalisé
    school_class = models.ForeignKey(SchoolClass, blank=True, null=True)
    ## Date de début de mise en place de la configuration
    start_date = models.DateTimeField(null=True, blank=True)
    ## Date de fin de mise en place de la configuration
    end_date = models.DateTimeField(null=True, blank=True)
    ## Données de configuration
    data = models.TextField()
    class Meta:
        db_table = 'lp_exercise_config'
    def __str__(self):
        return "Config %s for %s" % (self.exercise, self.school_class)

## Classe LPUser\n
# Classe utilisateur, étends l'utilisateur de base de django
class LPUser(models.Model):
    ## Avatar de l'utilisateur\n
    # Utilise django-imagekit
    avatar = ProcessedImageField(upload_to='avatars',
                                           null=True, blank=True,
                                           default='avatars/default.png',
                                           processors=[ResizeToFill(400, 400)],
                                           format='JPEG',
                                           options={'quality': 90})
    ## Utilisateur de base django
    user = models.OneToOneField(User, related_name='LPUser')
    ## Classes liées à l'utilisateur
    school_class = models.ManyToManyField(SchoolClass, null=True, blank=True)
    ## Données de configuration de l'utilisateur
    data = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'lp_user'
    def __str__(self):
        return self.user.username

## Classe Statistics\n
# Statisques de jeu
class Statistics(models.Model):
    ## Utilisateur lié
    user = models.ForeignKey(LPUser)
    ## Exercice lié
    exercise = models.ForeignKey(Exercise)
    ## Date de creation
    date = models.DateTimeField(default=datetime.now, blank=True)
    ## Données statistiques
    data = models.TextField()
    class Meta:
        db_table = 'lp_statistics'
    def __str__(self):
        return "Statistics for '%s': %s" % (self.user, self.data)
