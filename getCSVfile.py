import pandas as pd
#將xxxxxx改為主機名稱  yyyy改為檔案名稱
csv_file ="http://xxxxxx.asuscomm.com/~tony/stockData/data/yyyy.csv"
st2454 = pd.read_csv(csv_file)
#print(type(st2454))
dt=type(st2454)
hd=st2454.head()
