import time

import requests
r = requests.post('http://192.168.5.1/goform/set', json={"login": {"pwd": 'dfdc213123188d70c359ce254f3a7af6'}}, timeout=5)
print(f"Status Code: {r.status_code}, Response: {r.json()}")
r = requests.get('http://192.168.5.1/goform/telnet', timeout=10)
print(r.text)




### Habilitar telnet #####

#r = requests.post('http://192.168.6.1/login.html', auth=('', '12345678'))
#print(r.status_code)
#r = requests.get('http://192.168.6.1/goform/get?module_id=guest_pass')
#print(r.status_code)
#r = requests.get('http://192.168.6.1/goform/telnet')
#print(r.status_code)