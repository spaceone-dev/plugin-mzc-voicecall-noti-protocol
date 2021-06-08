MEGAZONE_VOICE_CONF = {
    'endpoint': 'https://message.megazoneapis.com',
    'default': {
        'flow_id': 'one-two-interaction-flow',
        'language': 'ko',
        'country_code': '82',    # KOREA
        'subscriptions': [{
            "type": "HTTPS",
            "uri": "https://u5ygfuanvb.execute-api.ap-northeast-2.amazonaws.com/test/notify-test"
        }],
        'closing': '완료되었습니다'
    }
}
