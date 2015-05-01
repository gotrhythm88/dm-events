from rest_framework import serializers
from dmeventsapp.models import Event, Question, Participant, Answer

class AnswerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Question
		fields = ('id', 'tweetId', 'tweetText', 'scoring', 'judgeComments')


class ParticipantSerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True, required=False)

	class Meta:
		model = Participant
		fields = ('id', 'twitterHandle', 'answers')


class QuestionSerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True, required=False)

	class Meta:
		model = Question
		fields = ('id', 'qTitle', 'qExplanation', 'qType', 'qPoints', 'answers')


class EventSerializer(serializers.ModelSerializer):
	questions = QuestionSerializer(many=True, required=False)
	participants = ParticipantSerializer(many=True, required=False)

	class Meta:
		model = Event
		fields = ('id', 'title', 'description', 'hashtag',
			'startDate', 'endDate', 'instructions', 'prizes', 'link',
			'imagePath', 'visibility', 'noSocialSharing', 'password',
			'questions', 'participants')




