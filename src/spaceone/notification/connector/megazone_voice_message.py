import base64
import json
import requests
import logging
from spaceone.notification.conf.megazone_voice_conf import MEGAZONE_VOICE_CONF

from spaceone.core.connector import BaseConnector

__all__ = ['MegazoneVoiceMessageConnector']
_LOGGER = logging.getLogger(__name__)


class MegazoneVoiceMessageConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.encode_key = None

    def set_connector(self, access_key, secret_key):
        # Encode Key to base64 encoding
        self.encode_key = self.string_to_base64(f'{access_key}:{secret_key}')

    def request_voice_call(self, country_code, to, message, **kwargs):
        request_url = f'{MEGAZONE_VOICE_CONF["endpoint"]}/voice/v1/messages'

        body = {
            'flowId': kwargs.get('flowId', MEGAZONE_VOICE_CONF['default']['flow_id']),
            'countryCode': country_code,
            'to': to,
            'body': message,
            'language': kwargs.get('language', MEGAZONE_VOICE_CONF['default']['language']),
            'closing': kwargs.get('closing', MEGAZONE_VOICE_CONF['default']['closing']),
        }

        if 'subscriptions' in kwargs:
            body.update({
                'subscriptions': kwargs.get('subscriptions'),
            })

        _LOGGER.debug(f'[VoiceCall Params] {body}')

        res = requests.post(request_url, data=json.dumps(body), headers=make_header(self.encode_key))

        _LOGGER.debug(f'[VoiceCall Response] Status Code: {res.status_code}')

    @staticmethod
    def string_to_base64(string):
        base64_bytes = base64.b64encode(string.encode('utf-8'))
        return base64_bytes.decode("UTF-8")


def make_header(auth_key):
    return {
        'Authorization': f'Basic {auth_key}',
        'Content-Type': 'application/json'
    }
