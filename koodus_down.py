# -*- coding: utf-8 -*-
from urllib import response
import requests

token = 'INSERT YOUR TOKEN HERE.'
sha256 = 'INSERT YOU WANT DOWNLOAD APK SHA256'

download_url = 'https://developer.koodus.com/apks/{sha256}/download'
headers = {'Authorization': f'Token {token}'}
response = requests.get(url=download_url.format(sha256=sha256), headers=headers)
response.raise_for_status()

with open(f'{sha256}.apk', 'wb') as f:
    f.write(response.content)
print('Download Successful.')
