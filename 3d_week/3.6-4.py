import requests
import json

client_id = 'id'
client_secret = 'secret'

r = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                  data={
                      'client_id': client_id,
                      'client_secret': client_secret
                  })

headers = {'X-Xapp-Token': json.loads(r.text)['token']}

artists = []
with open('dataset_24476_4.txt') as file:
    for line in file:
        artists.append(
            json.loads(requests.get('https://api.artsy.net/api/artists/' + line.rstrip(), headers=headers).text))

artists = [{'date': artist['birthday'], 'name': artist['sortable_name']} for artist in artists]

artists.sort(key=lambda x: (x['date'], x['name']))

print('\n'.join([artist['name'] for artist in artists]))
