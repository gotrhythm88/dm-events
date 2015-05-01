from django.shortcuts import render
from dmeventsapp.models import Event, Question, Participant, Answer
from rest_framework import viewsets
from dmeventsapp.serializers import EventSerializer, QuestionSerializer, ParticipantSerializer, AnswerSerializer
from rest_framework.response import Response

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):

	queryset = Event.objects.all()
	serializer_class = EventSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
	
	queryset = Participant.objects.all()
	def list(self, request, domain_pk=None):
		queryset = self.queryset.filter(domain=domain_pk)
		serializer = ParticipantSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None, domain_pk=None):
		queryset = self.queryset.get(pk=pk, domain=domain_pk)
		serializer = ParticipantSerializer(queryset)
		return Response(serializer.data)

class AnswerViewSet(viewsets.ModelViewSet):
	
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class QuestionViewSet(viewsets.ViewSet):
	queryset = Question.objects.all()

	def list(self, request, event_pk=None):
		queryset = self.queryset.filter(event=event_pk)
		serializer = QuestionSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None, event_pk=None):
		queryset = self.queryset.get(pk=pk, event=event_pk)
		serializer = QuestionSerializer(queryset)
		return Response(serializer.data)