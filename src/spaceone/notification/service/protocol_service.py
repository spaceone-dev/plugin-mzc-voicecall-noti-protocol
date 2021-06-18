import logging
from spaceone.core.service import *

_LOGGER = logging.getLogger(__name__)


@authentication_handler
class ProtocolService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)

    @check_required(['options'])
    def init(self, params):
        """ init plugin by options
        """
        return {'metadata': {
            'data_type': 'SECRET',
            'data': {
                'schema': {
                    'properties': {
                        'phone': {
                            'minLength': 4,
                            'title': 'Phone number to send the alarm to',
                            'type': 'string'
                        },
                        'country_code': {
                            'minLength': 4,
                            'title': 'Phone country code',
                            'type': 'string'
                        }
                    },
                    'required': [
                        'phone'
                    ],
                    'type': 'object'
                }
            }
        }}

    @transaction
    @check_required(['options'])
    def verify(self, params):
        """
        Args:
              params:
                - options
                - secret_data
        """
        options = params['options']
        secret_data = params.get('secret_data', {})

        return {}
