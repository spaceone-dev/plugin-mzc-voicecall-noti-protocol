from spaceone.core.manager import BaseManager
from spaceone.notification.connector.megazone_voice_message import MegazoneVoiceMessageConnector


class MegazoneVoiceCallManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mz_voice_connector = None

    def set_connector(self, access_key, secret_key):
        self.mz_voice_connector: MegazoneVoiceMessageConnector = self.locator.get_connector('MegazoneVoiceMessageConnector')
        self.mz_voice_connector.set_connector(access_key, secret_key)

    def request_voice_call(self, country_code, to, message, **kwargs):
        self.mz_voice_connector.request_voice_call(country_code, to, message, **kwargs)
