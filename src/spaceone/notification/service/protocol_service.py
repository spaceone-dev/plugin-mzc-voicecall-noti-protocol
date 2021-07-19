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
                            'description': 'The phone number to receive alerts. Must insert the cell phone number format, and only numbers without special characters.',
                            'minLength': 8,
                            'title': 'Phone Number',
                            'type': 'string',
                            'pattern': '^[0-9]{8,11}$',
                            'examples': ['0104445566']
                        },
                        'country_code': {
                            'description': 'Country code to call. Only numbers without special characters. Not mandatory, 82(Korea country code) is default.',
                            'minLength': 1,
                            'title': 'Country Code',
                            'type': 'string',
                            'pattern': '^[0-9\-]{1,5}$',
                            'examples': ['82']
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
