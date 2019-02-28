import pandas as pd
from datetime import date, timedelta
import datetime
import requests

def uploadYm(counterId, token, file):
    url = 'https://api-metrika.yandex.net/management/v1/counter/' + str(counterId) + '/offline_conversions/upload?client_id_type=USER_ID'

    headers = {
        'Authorization': 'OAuth ' + token
    }
    r = requests.post(url, files={'file':open(file, 'r')}, headers=headers)


def main():
    counterId = '****'
    token = '****'
    file = 'data.csv'
    dateStart = date.today() - timedelta(1)
    dateStart = dateStart.strftime('%Y%m%d')
    uploadYm(counterId,token,file)


if __name__ == '__main__':
    try:
        main()
