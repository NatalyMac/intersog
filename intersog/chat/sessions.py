from swampdragon.pubsub_providers.redis_publisher import get_redis_cli
from swampdragon.sessions.session_store import BaseSessionStore


class UserOnlyCustomSession(BaseSessionStore):
    key_expires = 30  # seconds

    def __init__(self, connection):
        super(UserOnlyCustomSession, self).__init__(connection)
        self.keys = []
        self.redis_client = get_redis_cli()

    def compose_key(self, key):
        if not self.connection.user:
            return None
        return 'uid:{}|key:{}'.format(self.connection.user.pk, key)

    def get(self, key):
        complete_key = self.compose_key(key)
        if not complete_key:
            return None
        return self.redis_client.get(complete_key)

    def set(self, key, val):
        complete_key = self.compose_key(key)
        if not complete_key:
            return
        self.redis_client.set(complete_key, val)
        self.redis_client.expire(complete_key, self.key_expires)

    def refresh_key_timeout(self, key):
        complete_key = self.compose_key(key)
        self.redis_client.expire(complete_key, self.key_expires)