from rest_framework import Serializers
from .models import Faq


class FaqSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faq
        fields = ["id", "question", "answer"]
