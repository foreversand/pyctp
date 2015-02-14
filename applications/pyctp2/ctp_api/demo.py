#-*- coding=utf-8 -*-
"This is the main demo file"
from .MdApi import MdApi, MdSpi
from . import UserApiStruct
import time
import traceback

class myMdSpi(MdSpi):
    def __init__(self, instruments, broker_id,
                 investor_id, passwd, *args,**kwargs):
        self.requestid=0
        self.instruments = instruments
        self.broker_id =broker_id
        self.investor_id = investor_id
        self.passwd = passwd

    def OnRspError(self, info, RequestId, IsLast):
        print(" Error")
        self.isErrorRspInfo(info)

    def isErrorRspInfo(self, info):
        if info.ErrorID !=0:
            print("ErrorID=", info.ErrorID, ", ErrorMsg=", info.ErrorMsg)
        return info.ErrorID !=0

    def OnFrontDisConnected(self, reason):
        print("onFrontDisConnected:", reason)

    def OnHeartBeatWarning(self, time):
        print("onHeartBeatWarning", time)

    def OnFrontConnected(self):
        print("OnFrontConnected:")
        self.user_login(self.broker_id, self.investor_id, self.passwd)

    def user_login(self, broker_id, investor_id, passwd):
        req = UserApiStruct.ReqUserLogin(BrokerID=broker_id, UserID=investor_id, Password=passwd)

        self.requestid+=1
        r=self.api.ReqUserLogin(req, self.requestid)
        

    def OnRspUserLogin(self, userlogin, info, rid, is_last):
        print("OnRspUserLogin", is_last, info)
        if is_last and not self.isErrorRspInfo(info):
            print("get today's trading day:", repr(self.api.GetTradingDay()))
            self.subscribe_market_data(self.instruments)

    def subscribe_market_data(self, instruments):
        self.api.SubscribeMarketData(instruments)

    #def OnRspSubMarketData(self, spec_instrument, info, requestid, islast):
    #    print "OnRspSubMarketData"

    #def OnRspUnSubMarketData(self, spec_instrument, info, requestid, islast):
    #    print "OnRspUnSubMarketData"

    def OnRtnDepthMarketData(self, depth_market_data):
        print ("OnRtnDepthMarketData")
        print(depth_market_data.BidPrice1,depth_market_data.BidVolume1,depth_market_data.AskPrice1,depth_market_data.AskVolume1,depth_market_data.LastPrice,depth_market_data.Volume,depth_market_data.UpdateTime,depth_market_data.UpdateMillisec,depth_market_data.InstrumentID)

inst = [u'cu1407']
def main():
    user = MdApi.CreateMdApi("data")
    user.RegisterSpi(myMdSpi(instruments=inst, 
                             broker_id="2030",
                             investor_id="00092",
                             passwd="888888"))
    user.RegisterFront("tcp://asp-sim2-md1.financial-trading-platform.com:26213")
    user.Init()

    while True:
        time.sleep(1)

if __name__=="__main__": main()
