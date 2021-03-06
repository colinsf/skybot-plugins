import json
import requests

from util import hook


def getTickerData():
    """ get the latest litecoin information from btc-e.com """

    url = 'http://btc-e.com/api/2/ltc_usd/ticker'

    session = requests.Session()

    r = json.loads(
        session.get(url, headers={'Content-type': 'application/json'}).text
    )

    tickerData = r.get('ticker', None)

    if not tickerData:
        return 'Error retrieving ticker data from bte.com/api/2/ltc_usd/ticker'

    return tickerData


@hook.command('ltc', autohelp=False)
@hook.command(autohelp=False)
def litecoin(inp, say=None):
    "litecoin -- gets current exchange rate for litecoins from btc-e.com"
    ticker = getTickerData()

    return 'Current: \x0312$%.2f\x0f - High: \x0312$%.2f\x0f - Low: ' \
        '\x0312$%.2f\x0f - Volume: \x0312%.2f\x0f LTC' % (

        ticker.get('last', None),
        ticker.get('high', None),
        ticker.get('low', None),
        ticker.get('vol', None)
    )

if __name__ == '__main__':
    print litecoin("")
