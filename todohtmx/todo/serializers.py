from rest_framework import serializers
from .models import Faq, Statistics

# Constants for validation limits and messages
QUESTION_MIN_LENGTH = 10
ANSWER_MIN_LENGTH = 5
QUESTION_ERROR = f"Question must be at least {QUESTION_MIN_LENGTH} characters in length"
ANSWER_ERROR = f"Answer must be at least {ANSWER_MIN_LENGTH} characters in length"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ["question", "answer"]

    def validate_question(self, value):
        if len(value) < QUESTION_MIN_LENGTH:
            raise serializers.ValidationError(QUESTION_ERROR)
        return value

    def validate_answer(self, value):
        if len(value) < ANSWER_MIN_LENGTH:
            raise serializers.ValidationError(ANSWER_ERROR)
        return value


class StatisticsSerializer(serializers.ModelSerializer):
    total_count = serializers.SerializerMethodField()
    completed_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Statistics
        fields = [
            "pending_count",
            "in_progress_count",
            "completed_count",
            "total_count",
            "archived_count",
            "completed_percentage",
        ]
        read_only_fields = ["total_count", "completed_percentage"]

    def get_total_count(self, obj):
        return (
            obj.pending_count
            + obj.in_progress_count
            + obj.completed_count
            + obj.archived_count
        )

    def get_completed_percentage(self, obj):
        total_count = self.get_total_count(obj)
        done_count = obj.completed_count + obj.archived_count
        return (done_count / total_count * 100) if total_count > 0 else 0
