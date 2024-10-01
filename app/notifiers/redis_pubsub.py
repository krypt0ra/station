import json
import redis
import structlog
from notifiers.utils import NotifierUtils


class RedisPublisher(NotifierUtils):
    """Class for handling Redis pubsub notifications with a specified channel.
    """

    # Class-level dictionary to store connections
    _redis_connections = {}

    def __init__(self, host, port, password, channel):
        self._logger = structlog.get_logger()
        self._host = host
        self._port = port
        self._password = password
        self._channel = channel
        self._connection_key = f"{self._host}:{self._port}:{self._channel}"

        # Create a connection if it doesn't exist
        self._get_or_create_connection()

    def _get_or_create_connection(self):
        """Get an existing connection or create a new one."""
        if self._connection_key in self._redis_connections:
            return self._redis_connections[self._connection_key]
        else:
            try:
                redis_conn = redis.Redis(
                    host=self._host,
                    port=self._port,
                    password=self._password,
                    socket_timeout=5,  # Add timeout to handle reconnects better
                    retry_on_timeout=True
                )
                # Test the connection
                redis_conn.ping()
                self._redis_connections[self._connection_key] = redis_conn
                return redis_conn
            except redis.exceptions.ConnectionError as e:
                self._logger.error(f"Failed to connect to Redis: {e}")
                raise

    def notify(self, messages, retrying = False):
        """Sends a message to the Redis pubsub channel defined in the constructor.

        Args:
            messages (list): The message to send.
            retrying (bool): The indicator of message sending retrying. Useful for unexpected connection loss cases
                             and for getting out from recursion
        """

        try:
            redis_conn = self._get_or_create_connection()

            for message in messages:
                # Publish message to the preset channel
                redis_conn.publish(self._channel, json.dumps(message))
        except redis.exceptions.ConnectionError:
            if retrying:
                return  # Do not repeat itself endless
            self._logger.error(f"Connection lost to Redis server {self._connection_key}, attempting reconnect.")
            # Clear the connection and retry
            del self._redis_connections[self._connection_key]
            self.notify(messages, True)  # Retry with a new connection
