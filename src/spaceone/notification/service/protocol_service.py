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
            'data_type': 'PLAIN_TEXT',
            'data': {
                'schema': {
                    'properties': {
                        'phone_number': {
                            'minLength': 8,
                            'title': 'Phone Number',
                            'type': 'string',
                            'pattern': '^[0-9]{8,15}$'
                        },
                        'country_code': {
                            'minLength': 1,
                            'title': 'Country Code',
                            'type': 'string',
                            'pattern': '^[0-9\-]{1,5}$'
                        }
                    },
                    'required': [
                        'phone_number'
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
