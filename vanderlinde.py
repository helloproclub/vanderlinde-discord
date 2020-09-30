import requests

def url_get(path):
    headers = {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjkxZjRiNTFhLTQxNTctNDQwMi1iM2E2LWYyMDU1YzliYzllOSJ9.rxir6oY-vzfS_yvz9RSoJr2pwXqe2FEMT6Hpdzvy0-U'}
    url = 'https://aqueous-reaches-39441.herokuapp.com' + path
    return requests.get(url, headers = headers)

def url_post(path,data):
    headers = {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjkxZjRiNTFhLTQxNTctNDQwMi1iM2E2LWYyMDU1YzliYzllOSJ9.rxir6oY-vzfS_yvz9RSoJr2pwXqe2FEMT6Hpdzvy0-U'}
    url = 'https://aqueous-reaches-39441.herokuapp.com' + path
    return requests.post(url, headers = headers, json=data)

def count_registration_list():
    resp = url_get('/status?status=0')
    text = f'Ada {resp.json()["data"]["count"]} data registrasi yang belum direview'
    return text

def get_user_by_status(status):
    resp_status = url_get(f'/status?status={status}')
    text = ''
    for item in resp_status.json()["data"]["items"]:
        resp_user = url_get(f'/user/{item["user_id"]}')
        text += f'{resp_user.json()["data"]["nim"]} | {resp_user.json()["data"]["name"]}\n'
    return text

def get_user_by_nim(nim):
    resp_status = url_get(f'/status/')
    if resp_status.status_code != 200:
        print('Cannot fetch all tasks: {}'.format(resp.status_code))
    for item in resp_status.json()["data"]["items"]:
        resp_user = url_get(f'/user/{item["user_id"]}')
        text = f'NIM : {resp_user.json()["data"]["nim"]} \nNama : {resp_user.json()["data"]["name"]} \nEmail : {resp_user.json()["data"]["email"]} \nURL KTM : {resp_user.json()["data"]["ktmurl_get"]} \nURL LETTER : {resp_user.json()["data"]["letterurl_get"]} \nURL LINKEDIN : {resp_user.json()["data"]["linkedinurl_get"]}'
        return text
    return f'Data dengan {nim} Tidak ditemukan'

def accept_user_by_nim(nim,invite_link):
    resp_status = url_get(f'/status?status=0')
    for item in resp_status.json()["data"]["items"]:
        resp_user = url_get(f'/user/{item["user_id"]}')
        if(resp_user.json()["data"]["nim"] == nim):
            data = {"discord_invite": f"{invite_link}","secret": "secret"}
            resp = url_post(f'/status/{resp_user.json()["data"]["id"]}/accept',data)
            if resp.status_code != 200:
                return f'Kesalahan teknis'
            else:
                return f'data registrasi dengan {nim} berhasil diterima'
    return f'data registrasi dengan {nim} tidak ada'

def decline_user_by_nim(nim,message):
    resp_status = url_get(f'/status?status=0')
    for item in resp_status.json()["data"]["items"]:
        resp_user = url_get(f'/user/{item["user_id"]}')
        if(resp_user.json()["data"]["nim"] == nim):
            data = {"message": f"{message}","secret": "secret"}
            resp = url_post(f'/status/{resp_user.json()["data"]["id"]}/decline',data)
            print('1231321231')
            if resp.status_code != 201:
                return f'Ada kesalahan teknis'
            else:
                return f'data registrasi dengan {nim} tidak diterima'
    return f'data registrasi dengan {nim} tidak ada'