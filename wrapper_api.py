import requests

def _url(path):
    return 'http://jsonplaceholder.typicode.com' + path

def get_users():
    text = ""
    resp = requests.get(_url('/users'))
    if resp.status_code != 200:
        raise ApiError('Cannot fetch all tasks: {}'.format(resp.status_code))
    for item in resp.json():
        text += '{} |\t {} \n'.format(item['id'], item['name'])
    
    return text
def get_user_detail(id):
    resp = requests.get(_url(f'/users/{id}'))
    if resp.status_code != 200:
        raise ApiError('Cannot fetch all tasks: {}'.format(resp.status_code))
    item = resp.json()
    text = 'Nama : {} \nEmail : {} \nAlamat : {} \nNomor Telepon : {} \n'.format(item['name'],item['email'],item['address']['street'],item['phone'])
    
    return text

def count_registration():
    counter = 0
    resp = requests.get(_url('/users'))
    if resp.status_code != 200:
        raise ApiError('Cannot fetch all tasks: {}'.format(resp.status_code))
    for item in resp.json():
        counter+=1
    text = f'Ada {counter} data yang belum direview'
    return text

