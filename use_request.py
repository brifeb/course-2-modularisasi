import requests

url = 'https://detik.com'
try:
    respon = requests.get(url)
    if respon.status_code == 200:
        print(f'Success! {respon.status_code}')
        print(f'Content: {respon.text}')
    else:
        print('Gagal')
except Exception as e:
    print('Ada error ', e)
