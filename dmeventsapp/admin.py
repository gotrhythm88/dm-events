from django.contrib import admin
from .models import Event, Question, Participant, Answer

admin.site.register(Event)
admin.site.register(Question)
admin.site.register(Participant)
admin.site.register(Answer)