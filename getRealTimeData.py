import twstock
#single stock
stock = twstock.realtime.get('2454')
#multiple stocks
stocks = twstock.realtime.get(['2330', '2454', '8464'])
