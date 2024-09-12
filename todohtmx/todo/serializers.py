from rest_framework import serializers
from .models import Faq, Statistics, Message


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = ["question", "answer", "question_length"]

    def get_question_length(self, obj):
        return len(obj.question)

    def validate_question(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Question must be at least 10 characters length"
            )
        return value

    def validate_answer(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Answer must be at least 10 characters in length"
            )
        return value


class StatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistics
        fields = [
            "pending_count",
            "in_progress_count",
            "completed_count",
            "total_count",
            "archived_count",
        ]
        read_only_fields = ["total_count", "completed_percentage"]

    def get_total_count(self, obj):
        return (
            obj.pending_count
            + obj.progress_count
            + obj.completed_count
            + obj.archived_count
        )

    def get_completed_percentage(self, obj):
        total_count = self.get_total_count(obj)
        done_count = obj.completed_count + obj.archived_count
        return (done_count / total_count * 100) if total_count > 0 else 0


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["content", "timestamp"]
