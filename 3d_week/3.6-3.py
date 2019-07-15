import requests

raw_url = 'http://numbersapi.com/{}/math'
params = {
    'json': True,
}

with open('dataset_24476_3.txt') as in_f, open('3.6-3_output.txt', 'a') as out_f:
    for line in in_f:
        line = line.strip()

        api_url = raw_url.format(line)
        res = requests.get(api_url, params=params)

        result_list = []

        if res.json()['found']:
            result = 'Interesting'
        else:
            result = 'Boring'

        out_f.write(result + '\n')
