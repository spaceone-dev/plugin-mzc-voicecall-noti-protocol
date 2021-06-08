import logging

from spaceone.core.service import *
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
                    - message
                    - closing
                    - subscriptions
                - notification_type
                - secret_data:
                    - access_key
                    - secret_key
                    - phone
                    - country_code (otpional)
        """
        secret_data = params.get('secret_data', {})
        notification_type = params['notification_type']
        message = params['message']

        access_key = secret_data.get('access_key')
        secret_key = secret_data.get('secret_key')
        phone = secret_data.get('phone')
        country_code = secret_data.get('country_code', MEGAZONE_VOICE_CONF['default']['country_code'])

        noti_mgr: NotificationManager = self.locator.get_manager('NotificationManager')
        noti_mgr.dispatch(access_key, secret_key, country_code, phone, f'[{notification_type}] {message["message"]}', closing=message['closing'])

