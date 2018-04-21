from iFinDPy import *
def ths():
    THS_iFinDLogin('yrzc001','666888')
    thsData=THS_HistoryQuotes('000001.SH','open;close;low;high;volume;amount;changeper','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','2018-02-21','2018-03-20')
    thsData=THS_Trans2DataFrame(thsData)
    open=list(thsData['open'])
    close=list(thsData['close'])
    low = list(thsData['low'])
    high = list(thsData['high'])
    volume = list(thsData['volume'])
    amount = list(thsData['amount'])
    changeper = list(thsData['changeper'])
    onetestx=[]
    for i in range(len(open)):
        each=[]
        each.append(open[i])
        each.append(close[i])
        each.append(low[i])
        each.append(high[i])
        each.append(volume[i])
        each.append(amount[i])
        each.append(changeper[i])
        onetestx.append(each)
    #history=list(thsData['close'])
    #print(len(realtest))
    #print(alldata)
    realy = THS_HistoryQuotes('000001.SH', 'high',
                                'period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB', '2018-02-12',
                                '2018-03-15')
    realy = THS_Trans2DataFrame(realy)
    realy=list(realy['high'])
    return onetestx,realy