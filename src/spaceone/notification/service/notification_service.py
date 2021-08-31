import logging

from spaceone.core.service import *
from spaceone.core.utils import parse_endpoint
from spaceone.notification.manager.notification_manager import NotificationManager
from spaceone.notification.conf.megazone_voice_conf import MEGAZONE_VOICE_CONF

_LOGGER = logging.getLogger(__name__)


@authentication_handler
class NotificationService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)

    @transaction
    @check_required(['options', 'message', 'notification_type'])
    def dispatch(self, params):
        """
        Args:
            params:
                - options
                - message
                    - title
                    - shot_message
                    - callbacks
                        - url
                        - options
                - notification_type
                - secret_data:
                    - access_key
                    - secret_key
                - channel_data
                    - phone
                    - country_code (otpional)
        """

        secret_data = params.get('secret_data', {})
        channel_data = params.get('channel_data', {})
        notification_type = params['notification_type']
        access_key = secret_data.get('access_key')
        secret_key = secret_data.get('secret_key')
        phone_number = channel_data.get('phone_number')
        country_code = channel_data.get('country_code', MEGAZONE_VOICE_CONF['default']['country_code'])

        params_message = params['message']
        send_message = params_message.get('short_message')

        if send_message:
            kwargs = {}

            if 'callbacks' in params_message:
                subscriptions = []

                send_message = f'{send_message}. {MEGAZONE_VOICE_CONF["default"]["tail_message"]}'
                for _cb in params_message['callbacks']:
                    url = _cb.get('url')
                    endpoint = parse_endpoint(url)
                    subscriptions.append({
                        'type': endpoint['scheme'].upper(),
                        'uri': url
                    })

                kwargs['subscriptions'] = subscriptions

            noti_mgr: NotificationManager = self.locator.get_manager('NotificationManager')
            noti_mgr.dispatch(access_key, secret_key, country_code, phone_number, send_message, **kwargs)
        else:
            _LOGGER.debug("[dispatch] Skip Send message. no short_message value")
