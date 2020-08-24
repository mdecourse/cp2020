import requests

s = requests.Session()

headers = {'X-Requested-With': 'XMLHttpRequest'}

semester = '1082'
courseno = '0744'

url = 'https://osa.nfu.edu.tw/query/studlist_ajax.php'
post_var = {'pselyr': semester, 'pseqno': courseno}

result = s.post(url=url, data = post_var, headers=headers)
print(result.text)



