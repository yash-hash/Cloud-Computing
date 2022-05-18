from django.db import models


class Category(models.Model):
    """Category Model"""
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Answer(models.Model):
    """Answer Model"""
    answer_txt = models.CharField(max_length=150)

    def __str__(self):
        return self.answer_txt


class Question(models.Model):
    """Question Model"""
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    question_txt = models.CharField(max_length=200)
    answer = models.OneToOneField('Answer', on_delete=models.CASCADE, related_name='correcta_answer', null=True, blank=True)
    choices = models.ManyToManyField('Answer',related_name = 'choices' )

    def __str__(self):
        return self.question_txt


class Quiz(models.Model):
    """Quiz Model"""
    category = models.ManyToManyField('Category', related_name ='category')
    quiz_name = models.CharField(max_length=200)
    question = models.ManyToManyField(Question, blank=True)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.quiz_name
