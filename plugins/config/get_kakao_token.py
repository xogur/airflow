import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = 'f44782b809fb4708ce75f56bec05be9c'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'SH0Hlc2wSIv20KzvHkW2FvCrBgYEPghcFIueq7-oIfPlEB3vcNcqwwAAAAQKFxZiAAABletP3Ayvm_uHqQwxKA'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)