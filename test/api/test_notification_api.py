import os
import logging

from spaceone.core import utils, config
from spaceone.tester import TestCase, print_json, to_json
from google.protobuf.json_format import MessageToDict

_LOGGER = logging.getLogger(__name__)

ACCESS_KEY = os.environ.get('ACCESS_KEY', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)
PHONE = os.environ.get('PHONE', None)
COUNTRY_CODE = os.environ.get('COUNTRY_CODE', None)


if ACCESS_KEY == None or SECRET_KEY == None:
    print("""
##################################################
# ERROR
#
# Configure your Slack Token first for test
##################################################
example)

export ACCESS_KEY=<MEGAZONE_MESSAGE_ACCESS_KEY>
export SECRET_KEY=<MEGAZONE_MESSAGE_SECRET_KEY>
""")
    exit


class TestVoiceCallNotification(TestCase):
    config = utils.load_yaml_from_file(
        os.environ.get('SPACEONE_TEST_CONFIG_FILE', './config.yml'))
    endpoints = config.get('ENDPOINTS', {})
    secret_data = {
        'access_key': ACCESS_KEY,
        'secret_key': SECRET_KEY,
        'phone': PHONE,
        'country_code': COUNTRY_CODE
    }

    def test_init(self):
        v_info = self.notification.Protocol.init({'options': {}})
        print_json(v_info)

    def test_verify(self):
        options = {}
        self.notification.Protocol.verify({'options': options, 'secret_data': self.secret_data})

    def test_dispatch(self):
        options = {}

        self.notification.Notification.dispatch({
            'options': options,
            'message': {
                'message': 'Test..',
                'closing': 'Complete..'
            },
            'notification_type': 'INFO',
            'secret_data': self.secret_data
        })
