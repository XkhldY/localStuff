from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, redirect
import requests
import pandas as pd
from bs4 import BeautifulSoup
import io
import json
import logging
import datetime
from django.conf import settings
from sqlalchemy import create_engine
from .models import Stock, Company
from .utils.BulkManager import BulkContextManager, tst
from django.forms import modelform_factory


# Create your views here.
def _db():
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    host = settings.DATABASES['default']['HOST']
    url = f"postgresql+psycopg2://{user}:{password}@{host}:5432/postgres"
    engine = create_engine(url=url)

    return engine


def date(request):
    # companies = pd.read_excel('/Users/khaled/Downloads/SODWeightings_20210316_COMP.xlsx', header=4, usecols='A,B')
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0"
    }
    companies_request = requests.get('https://api.nasdaq.com/api/quote/list-type/nasdaq100', headers=headers)
    companies = companies_request.json()
    companies = pd.DataFrame(companies['data']['data']['rows'], columns=companies['data']['data']['headers'])

    with BulkContextManager() as bcm:
        for index, company in companies[['symbol', 'companyName']].iterrows():
            com = Company(**company)
            bcm.add(com)
    i = 0
    for index, company in companies[['symbol', 'companyName']].iterrows():
        try:
            r = requests.get('https://www.webull.com/quote/nasdaq-' + company[0].lower())
            soup = BeautifulSoup(r.text, 'html.parser')
            y = json.loads(soup.find('script', {'id': "server-side-script"}).contents[0].replace(
                'window.__initState__ = ', ''))
            tickerId = list(y['tickerMap'].keys())[0]
            print('tickerId: ', company[0])

            r = requests.get('https://quotes-gw.webullfintech.com/api/quote/charts/query?period=y1&tickerIds=' +
                             tickerId)
            data = io.StringIO('\n'.join(r.json()[0]['data']))
            df = pd.read_csv(data, names=['Date', 'open', 'close', 'high', 'low', 'prev close', 'volume'],
                             index_col=False)


            df.Date = df.Date.apply(lambda x: datetime.datetime.fromtimestamp(x))
            # save to django model
            # stock = Stocks(**df.iloc[0, :])
            # stock.save()
            t = tst('ali', 90, True)
            com = Company.objects.filter(companyName=company[1]).first()
            with BulkContextManager() as bm:
                for index, row in df.iterrows():

                    row['company'] = com
                    stock = Stock(**row)
                    bm.add(stock)

            # Stocks.objects.bulk_create([stock])
            # database save
            # df.to_sql('stocks', if_exists='append', con=_db(), index=True)

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




def welwel(request):
    companies = Company.objects.filter(symbol__contains= 'AD')
    return render(request, 'justmodels/welcome.html', {'companies': companies})


def show_stock(request, symbol):
    stocks = get_list_or_404(Stock, company__symbol=symbol.upper())
    return render(request, 'justmodels/stock.html', {'stocks': stocks})


ModelCompany = modelform_factory(Company, exclude=[])


def add_company(request):
    if request.method == 'POST':
        form = ModelCompany(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('welwel')
    else:
        form = ModelCompany()
    return render(request, 'justmodels/addcompany.html',  {'form': form})


ModelStock = modelform_factory(Stock, exclude=[])


def add_stock_day(request):
    form = ModelStock()
    return render(request, 'justmodels/addstockday.html', {'form': form})