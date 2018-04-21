from iFinDPy import *
THS_iFinDLogin('yrzc001','666888')
labeldata=THS_HistoryQuotes('000001.SH','close','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','2017-01-01','2017-12-11')
labeldata=THS_Trans2DataFrame(labeldata)
print(labeldata)