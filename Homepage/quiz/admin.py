from django.contrib import admin
from .models import Answer, Category, Question, Quiz
# Register your models here.


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Category)
