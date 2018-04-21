from iFinDPy import *
def ths():
    THS_iFinDLogin('yrzc001','666888')
    thsData=THS_HistoryQuotes('603757.SH','close','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','2017-01-01','2017-10-23')
    thsData=THS_Trans2DataFrame(thsData)
    history=list(thsData['close'])
    realtest=THS_HistoryQuotes('603757.SH','close','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','2017-10-24','2017-11-20')
    realtest=THS_Trans2DataFrame(realtest)
    realtest=list(realtest['close'])
    #print(len(realtest))
    return history,realtest
# print(history)
# print(len(history))


