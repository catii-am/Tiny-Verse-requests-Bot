import requests
import time
import json

with open('headers.json', 'r', encoding='utf-8') as file:
    headers = json.load(file)


def make_list_from_file(file):
    with open(file, 'r') as f:
        return [x for x in f.read().split('\n') if x]


def collect():
    while True:
        sessions = make_list_from_file('sessions.txt')
        for session in sessions:
            print(session)
            try:
                data = {'session': session}
                response = requests.post('https://api.tonverse.app/galaxy/collect', headers=headers, data=data)
                print(response.text)
                time.sleep(3540)

            except Exception as e:
                print(e)


def scan():
    while True:
        scan_data = make_list_from_file('scan_data.txt')
        for data in scan_data:
            try:
                split_data = data.split(':')
                session = split_data[0]
                galaxy_id = split_data[1]

                result_data = {
                    'session': session,
                    'galaxy_id': galaxy_id
                }

                request_data = {
                    'session': session,
                    'galaxy_id': galaxy_id,
                    'power': '1',
                }

                response = requests.post('https://api.tonverse.app/scan/result', headers=headers, data=result_data)

                print(response.text)

                time.sleep(3)

                response = requests.post('https://api.tonverse.app/scan/start', headers=headers, data=request_data)
                print(response.text)
                time.sleep(1260)

            except Exception as e:
                print(e)


def crete_stars():
    while True:
        create_data = make_list_from_file('scan_data.txt')
        for data in create_data:
            try:
                split_data = data.split(':')
                session = split_data[0]
                galaxy_id = split_data[1]

                data = {
                    'session': session,
                    'galaxy_id': galaxy_id,
                    'stars': '100',
                }

                response = requests.post('https://api.tonverse.app/stars/create', headers=headers, data=data)
                print(response.text)
            except Exception as e:
                print(e)

        time.sleep(90*60)


if __name__ == '__main__':
    crete_stars()
    scan()
    collect()
