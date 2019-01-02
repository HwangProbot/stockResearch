import twstock
import matplotlib.pyplot as plt
import pandas as pd
st = twstock.Stock('2454')
# 獲取 2018 年 01 月至今日之股票資料
st1= st.fetch_from(2018,1)    
st2454 = pd.DataFrame(st1)
st2454 = st2454.set_index('date')
fig = plt.figure(figsize=(10, 6))
plt.plot(st2454.close, '-' , label="close")
plt.plot(st2454.open, '-' , label="open")
plt.title('MediaTech 2018 open/close',loc='right')
# loc->title的位置
plt.xlabel('date')
plt.ylabel('close')
plt.grid(True, axis='y')
plt.legend()
fig.savefig('day20_01.png')
