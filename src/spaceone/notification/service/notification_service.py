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
                    - callbacks
                        - url
                        - options
                - notification_type
                - secret_data:
                    - access_key
                    - secret_key
                    - phone
                    - country_code (otpional)
        """

        secret_data = params.get('secret_data', {})
        notification_type = params['notification_type']
        params_message = params['message']
        send_message = params_message.get('title', MEGAZONE_VOICE_CONF['default']['message'])

        access_key = secret_data.get('access_key')
        secret_key = secret_data.get('secret_key')
        phone = secret_data.get('phone')
        country_code = secret_data.get('country_code', MEGAZONE_VOICE_CONF['default']['country_code'])
        kwargs = {}

        if 'callbacks' in params_message:
            subscriptions = []

            send_message = f'{send_message}. 스페이스원에 응답 메시지를 보내시려면 1번을 눌러주세요.'
            for _cb in params_message['callbacks']:
                url = _cb.get('url')
                endpoint = parse_endpoint(url)
                subscriptions.append({
                    'type': endpoint['scheme'].upper(),
                    'uri': url
                })

            kwargs['subscriptions'] = subscriptions

        noti_mgr: NotificationManager = self.locator.get_manager('NotificationManager')
        noti_mgr.dispatch(access_key, secret_key, country_code, phone, send_message, **kwargs)

