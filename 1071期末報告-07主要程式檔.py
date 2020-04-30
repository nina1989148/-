
#############
##抓出關鍵詞##
#############
import pandas as pd
#try:
#    data = pd.read_csv('muscle_content.csv',encoding = 'cp950')
#except:
#    data = pd.read_csv('muscle_content.csv', encoding = 'utf-8')
    
import jieba
# 
ret = open("爬蟲＿fitness.txt", "r", encoding = 'utf-8').read()

# 切詞
seglist = jieba.cut(ret, cut_all=False)

# 讀入停止詞
stopw = [line.strip() for line in open('stop_words.txt','r',encoding = 'utf-8').readlines()]

# 轉成list 讓切詞結果不會用一次就不見
seglist = list(seglist)

# 過濾掉不必要的詞
tmp = set(seglist)-set(stopw)



import json
hash = {}
for item in tmp: 
  if item in hash:
    hash[item] += 1
  else:
    hash[item] = 1
    

a = list(hash.keys())
a.sort()

new = set(seglist)-set(stopw)-set(a[0:4802])



import json
newhash = {}
for item in seglist: 
  if item in newhash and item in new:
    newhash[item] += 1
  elif item in new:
    newhash[item] = 1


nn = pd.DataFrame(list(newhash.keys()), list(newhash.values())).reset_index()
columns = ['value', 'name']
nn.columns=columns

nn.to_excel('關鍵詞_fitness.xls')

##############
##   畫圖   ##
#############
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'msj.ttf')#輸入中文字體
import seaborn as sns



# 以new_nnn作為new_nn重新設定 index的指標，並為欄重新命名
new_nn = nn[nn['value']>150]['name']
new_nnn = new_nn.reset_index()
col = ['value', 'name']
new_nnn.columns = col
new_nnn.to_excel('new_nnn.xls')

#sns.relplot(x="value", y="name", sizes=(15, 3000), data = new_nn[])
final_nnn = pd.read_excel('new_nnn.xls')
from matplotlib.font_manager import FontProperties
import matplotlib as mpl
myfont=FontProperties(fname='msj.ttf',size=14)

from pylab import * 
mpl.rcParams['font.sans-serif'] = ['SimHei'] 

x = final_nnn['name']
y = final_nnn['value']
plt.xlabel('key words',fontproperties= myfont)
plt.ylabel('frequency')
plt.title('瘦身版',fontproperties = myfont)
plt.plot(x,y)
#plt.show(fontproperties= myfont)
fig = plt.gcf()
fig.set_size_inches(16.5, 10.5)
fig.savefig('fitness.png', dpi=300) # 存檔且設定解析度
plt.show()


#plt.legend(prop=myfont)  # 圖例中文設定


import seaborn as sns
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import FontProperties
myfont=FontProperties(fname='msj.ttf',size=14)
import seaborn as sns
sns.set(font=['sans-serif'])
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})
sns.set(font=myfont.get_family())

sns.set(style="ticks", color_codes=True)

sns.catplot(x = new_nnn['name'], y = new_nnn['value'], kind="box", data = new_nnn)



names = ['北', '中', '南', '東']
values = [10, 15 ,5 ,20]
# 執行
ax = sns.barplot(x=names, y=values)

names = new_nnn['name']
values = new_nnn['value']
# 執行
ax = sns.barplot(x=names, y=values)







json.dump(hash,open("count.json","w"))

fd = open("count.csv","w")
fd.write("word,count\n")
for k in hash:
  fd.write("%s,%d\n"%(k.encode("utf8"),hash[k]))
