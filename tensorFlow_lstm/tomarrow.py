from iFinDPy import *
import time
import numpy as np
def ths():
    endday=time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(endday)
    THS_iFinDLogin('yrzc001','qwer1234')
    thsData=THS_HistoryQuotes('000001.SH','open;close;low;high;volume;amount;changeper','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','2018-02-26',endday)
    THS_iFinDLogout()
    thsData=THS_Trans2DataFrame(thsData)
    thsData=np.array(thsData).tolist()
    for i in range(len(thsData)):
	thsData[i]=thsData[i][2:]
    onetestx=thsData[len(thsData)-20:]
   # thsData=thsData[len(thsData)-20:]
    #print(thsData)
   # open=list(thsData['open'])
   # close=list(thsData['close'])
    #low = list(thsData['low'])
    #high = list(thsData['high'])
    #volume = list(thsData['volume'])
    #amount = list(thsData['amount'])
    #changeper = list(thsData['changeper'])
    #onetestx=[]
    #for i in range(len(open)):
    #    each=[]
    #    each.append(open[i])
    #   each.append(close[i])
    #   each.append(low[i])
    #   each.append(high[i])
    #    each.append(volume[i])
    #    each.append(amount[i])
    #    each.append(changeper[i])
    #    onetestx.append(each)
    #history=list(thsData['close'])
    #print(alldata)
    return onetestx,endday

#ths()
