from rest_framework import serializers
from .tasks import upload_to_ai

class BotSerializer(serializers.Serializer):
    questions = serializers.ListField(required=True, write_only=True)
    user_info = serializers.CharField(required=True, write_only=True)
    merchant = serializers.CharField(required=True, write_only=True)
    user_id = serializers.IntegerField(required=True, write_only=True)

    def create(self, validated_data):
        # call ai and run async
        upload_to_ai(validated_data['questions'], validated_data['user_info'], validated_data['merchant'], validated_data['user_id'])
        return "successfull"
