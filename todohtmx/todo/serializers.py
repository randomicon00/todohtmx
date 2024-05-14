from rest_framework import Serializers
from .models import Faq, Statistics


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = ["question", "answer", "question_length"]


    def get_question_length(self, obj):
        return len(obj.question)

    def validate_question(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("The question must be at least 10 characters length"
        return value

class StatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistics
        fields = ["pending_count", "in_progress_count", "completed_count", "total_count"]
        read_only_fields = ["total_count", "completed_percentage"]

    def get_total_count(self, obj):
        return obj.pending_count + obj.progress_count + obj.completed_count

    def get_completed_percentage(self, obj):
        total = self.get_total_count(obj)
        return (obj.completed_count / total * 100) if total > 0 else 0
