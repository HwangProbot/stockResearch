import twstock
import pandas as pd
st = twstock.Stock('2454')
# 獲取 2018 年 01 月至今日之股票資料
st1= st.fetch_from(2018,1)     
st2454 = pd.DataFrame(st1)
st2454 = st2454.set_index('date')
c=st2454.close
o=st2454.open
h=st2454.high
l=st2454.low
v=st2454.capacity  #成交量
ch=st2454.change  #漲跌
to=st2454.turnover  #成交值
trs=st2454.transaction #成交筆
