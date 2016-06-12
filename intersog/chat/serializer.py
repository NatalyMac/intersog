from swampdragon.serializers.model_serializer import ModelSerializer


class ChatSerializer(ModelSerializer):
    class Meta:
        model = "chat.Chat"
        publish_fields = ('text', 'user_sent')

