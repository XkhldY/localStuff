from django.http import HttpResponse
import requests
import pandas as pd
from bs4 import BeautifulSoup
import io
import json
import logging
import datetime
from django.conf import settings
from sqlalchemy import create_engine
from .models import Stks

def _db():
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    host = settings.DATABASES['default']['HOST']
    url = f"postgresql+psycopg2://{user}:{password}@{host}:5432/postgres"
    engine = create_engine(url=url)

    return engine


def welcome(request):
    # r = requests.get('https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1?api_key=yKCbY_r4TFmFJxkSeXv1')
    # print(r.json()['dataset'])
    # dataset = pd.DataFrame(r.json()['dataset']['data'], columns=r.json()['dataset']['column_names'])
    # print(dataset.head())
    return HttpResponse("welcome motherfuckers")


def date(request):
    # companies = pd.read_excel('/Users/khaled/Downloads/SODWeightings_20210316_COMP.xlsx', header=4, usecols='A,B')
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0"
    }
    companies_request = requests.get('https://api.nasdaq.com/api/quote/list-type/nasdaq100', headers=headers)
    companies = companies_request.json()
    companies = pd.DataFrame(companies['data']['data']['rows'], columns=companies['data']['data']['headers'])

    i = 0
    for company in companies.loc[:, 'symbol']:
        try:
            r = requests.get('https://www.webull.com/quote/nasdaq-' + company.lower())
            soup = BeautifulSoup(r.text, 'html.parser')
            y = json.loads(soup.find('script', {'id': "server-side-script"}).contents[0].replace( 'window.__initState__ = ', ''))
            tickerId = list(y['tickerMap'].keys())[0]
            print('tickerId: ', company)

            r = requests.get('https://quotes-gw.webullfintech.com/api/quote/charts/query?period=y1&tickerIds=' + tickerId)
            data = io.StringIO('\n'.join(r.json()[0]['data']))
            df = pd.read_csv(data, names=['Date', 'Open', 'close', 'high', 'low', 'prev close', 'Volume'], index_col=False)
            df.Date = df.Date.apply(lambda x: datetime.datetime.fromtimestamp(x))
            # database save
            df.to_sql('stocks', if_exists='append', con=_db(), index=True)

            df['positive'] = df.close - df['prev close']
            df['positive2'] = (df.close - df['prev close']) > 0
            print('max change\n', df.iloc[df.positive.idxmax()])
            print('min change\n', df.iloc[df.positive.idxmin()])
            print(df)
            print('number', i)
            i += 1
        except Exception as e:
            logging.warning(e)

    return HttpResponse(r.json()[0]['data'])


def webull(request):
    i = 0
    while i < 1:
        r = requests.get('https://www.webull.com/quote/nasdaq-tsla')

        soup = BeautifulSoup(r.text, 'html.parser')
        x = soup.find('div', {'class': "jss9bfy31"}).find('div', {'class': "jssbj9t66"}).text
        print('price = ', x)
        try:
            x = soup.find('div', {'class': "jss9bfy31"}).find('span').text

            print('price after hours = ', x)
        except:
            print('not yet')
        i += 1
    return HttpResponse("motherfuckers")


def yahoo_finance(request):
    r = requests.get('https://finance.yahoo.com/quote/tsla')
    soup = BeautifulSoup(r.text, 'html.parser')
    x = soup.find('div', {'class': "My(6px) Pos(r) smartphone_Mt(6px)"}).find('span').text

    print('price = ', x)
    return HttpResponse('i think this might work asshole')