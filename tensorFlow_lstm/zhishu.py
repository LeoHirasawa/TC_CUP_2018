from iFinDPy import *
def ths():
    THS_iFinDLogin('yrzc001','666888')
    thsData=THS_HistoryQuotes('000001.SH','open;close;low;high;volume;amount;changeper','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','1990-12-20','2015-12-10')
    thsData=THS_Trans2DataFrame(thsData)
    print(thsData)
    labeldata=THS_HistoryQuotes('000001.SH','high','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','1990-12-21','2015-12-11')
    labeldata=THS_Trans2DataFrame(labeldata)
    date=list(thsData['time'])
    open=list(thsData['open'])
    close=list(thsData['close'])
    low = list(thsData['low'])
    high = list(thsData['high'])
    volume = list(thsData['volume'])
    amount = list(thsData['amount'])
    changeper = list(thsData['changeper'])
    label=list(labeldata['high'])
    alldata=[]
    for i in range(len(open)):
        each=[]
        # each.append(date[i])
        each.append(open[i])
        each.append(close[i])
        each.append(low[i])
        each.append(high[i])
        each.append(volume[i])
        each.append(amount[i])
        each.append(changeper[i])
        each.append(label[i])
        alldata.append(each)
    #history=list(thsData['close'])
    #print(len(realtest))
    print(alldata)
    return alldata

ths()