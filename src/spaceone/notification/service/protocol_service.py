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
                'properties': {
                    'access_key': {
                        'minLength': 4,
                        'title': 'Megazone Voice Access Key',
                        'type': 'string'
                    },
                    'secret_key': {
                        'minLength': 4,
                        'title': 'Megazone Voice Secret Key',
                        'type': 'string'
                    }
                },
                'required': [
                    'access_key',
                    'secret_key'
                ],
                'type': 'object'
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
