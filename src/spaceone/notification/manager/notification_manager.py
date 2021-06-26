from spaceone.core.manager import BaseManager
from spaceone.notification.manager.megazone_voice_manager import MegazoneVoiceCallManager


class NotificationManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch(self, access_key, secret_key, country_code, phone_number, message, **kwargs):
        mz_voice_mgr: MegazoneVoiceCallManager = self.locator.get_manager('MegazoneVoiceCallManager')
        mz_voice_mgr.set_connector(access_key, secret_key)
        mz_voice_mgr.request_voice_call(country_code, phone_number, message, **kwargs)