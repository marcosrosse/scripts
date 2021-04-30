import requests
import yaml
import string
import random

def generate_password(length):
  return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(length))

def generate_username(length):
  return ''.join(random.choice(string.digits + string.ascii_lowercase) for i in range(length))

with open('secret.yml') as file:
     doc = yaml.load(file, Loader=yaml.FullLoader)

new_username = generate_username(12)
new_password = generate_password(12)

new_user = {'username': new_username, 'password': new_password}

with open('secret.yml', 'w') as file:
    data = yaml.dump(new_user, file)
raw_data = {'password':f'{new_password}', 'roles': 'superuser', 'full_name': 'automated user'}
r = requests.post('http://my-url/_security/user/{new_username}?pretty', data=raw_data, headers={'Content-Type': 'application/json'}, auth=('elastic', 'my_pass'))
print(r.text)