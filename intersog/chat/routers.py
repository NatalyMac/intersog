# coding: utf-8
from swampdragon import route_handler
from swampdragon.route_handler import BaseRouter, ModelRouter
from models import Chat
from serializer import ChatSerializer
from extuser.models import User

class ChatRouter(BaseRouter):
    route_name = 'chat-route'
    valid_verbs = ['chat', 'subscribe']

    def get_subscription_channels(self, **kwargs):
        return ['chatroom']

    def chat(self, *args, **kwargs):
        errors = {}
        if 'message' not in kwargs or len(kwargs['message']) is 0:
            errors['message'] = 'Enter a chat message'
        if errors:
            self.send_error(errors)
        else:
            self.send({'status': 'ok'})
            chat = Chat()
            chat.text = kwargs['message']
            chat.user_receive_id = kwargs['user']
            chat.user_sent = User.objects.get(id=kwargs['user_sent'])
            chat.save()
            self.publish(self.get_subscription_channels(), kwargs)

    # юзера отсюда достать не получилось None, поэтому через шаблон
    def get_subscription_contexts(self, **kwargs):
        return {'user': self.connection.user}


route_handler.register(ChatRouter)


class NotificationRouter(ModelRouter):
    
    valid_verbs = ['subscribe']
    route_name = 'notification'
    model = Chat
    serializer_class = ChatSerializer

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


route_handler.register(NotificationRouter)
