from rest_framework import Serializers
from .models import Faq, Statistics


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = ["question", "answer"]


class StatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistics
        fields = ["pending_count", "in_progress_count", "completed_count"]
