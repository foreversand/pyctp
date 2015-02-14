#-*- coding=utf-8 -*-
"""

A wrapper for CTP's Api library
author: Lvsoft@gmail.com
date: 2010-07-20

This file is part of python-ctp library

python-ctp is free software; you can redistribute it and/or modify it
under the terms of the GUL Lesser General Public License as published
by the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

python-ctp is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY of FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along the python-ctp; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301 USA
"""

#This file is auto generated! Please don't edit directly.

def tou(x, enc='gbk', err='ignore'):
    return str(x, enc, err) if isinstance(x, bytes) else str(x)
    

class CThostFtdcCurrTransferIdentityField:
    def __init__(self, IdentityID=0):
        self.IdentityID=IdentityID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IdentityID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('IdentityID', u'交易中心代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInstrumentCommissionRateField:
    def __init__(self, CloseTodayRatioByMoney=0, InstrumentID="", OpenRatioByVolume=0, CloseTodayRatioByVolume=0, OpenRatioByMoney=0, CloseRatioByVolume=0, BrokerID="", InvestorID="", InvestorRange='1', CloseRatioByMoney=0):
        self.CloseTodayRatioByMoney=CloseTodayRatioByMoney
        self.InstrumentID=tou(InstrumentID)
        self.OpenRatioByVolume=OpenRatioByVolume
        self.CloseTodayRatioByVolume=CloseTodayRatioByVolume
        self.OpenRatioByMoney=OpenRatioByMoney
        self.CloseRatioByVolume=CloseRatioByVolume
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.CloseRatioByMoney=CloseRatioByMoney
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CloseTodayRatioByMoney', 'InstrumentID', 'OpenRatioByVolume', 'CloseTodayRatioByVolume', 'OpenRatioByMoney', 'CloseRatioByVolume', 'BrokerID', 'InvestorID', 'InvestorRange', 'CloseRatioByMoney']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CloseTodayRatioByMoney', u'平今手续费率'),('InstrumentID', u'合约代码'),('OpenRatioByVolume', u'开仓手续费'),('CloseTodayRatioByVolume', u'平今手续费'),('OpenRatioByMoney', u'开仓手续费率'),('CloseRatioByVolume', u'平仓手续费'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('CloseRatioByMoney', u'平仓手续费率')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingInstrumentTradingRightField:
    def __init__(self, InstrumentID="", InvestorID="", InvestorRange='1', BrokerID="", TradingRight='0'):
        self.InstrumentID=tou(InstrumentID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.BrokerID=tou(BrokerID)
        self.TradingRight=tou(TradingRight)
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}, 'TradingRight': {"'1'": '只能平仓', "'0'": '可以交易', "'2'": '不能交易'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'InvestorRange', 'BrokerID', 'TradingRight']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('BrokerID', u'经纪公司代码'),('TradingRight', u'交易权限')]])
    def getval(self, n):
        if n in ['InvestorRange', 'TradingRight']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferFutureToBankRspField:
    def __init__(self, FutureAccount="", RetCode="", RetInfo="", TradeAmt=0, CustFee=0, CurrencyCode=""):
        self.FutureAccount=tou(FutureAccount)
        self.RetCode=tou(RetCode)
        self.RetInfo=tou(RetInfo)
        self.TradeAmt=TradeAmt
        self.CustFee=CustFee
        self.CurrencyCode=tou(CurrencyCode)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'RetCode', 'RetInfo', 'TradeAmt', 'CustFee', 'CurrencyCode']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FutureAccount', u'资金账户'),('RetCode', u'响应代码'),('RetInfo', u'响应信息'),('TradeAmt', u'转帐金额'),('CustFee', u'应收客户手续费'),('CurrencyCode', u'币种')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarginModelField:
    def __init__(self, BrokerID="", MarginModelID="", MarginModelName=""):
        self.BrokerID=tou(BrokerID)
        self.MarginModelID=tou(MarginModelID)
        self.MarginModelName=tou(MarginModelName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'MarginModelID', 'MarginModelName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('MarginModelID', u'保证金率模板代码'),('MarginModelName', u'模板名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryDepthMarketDataField:
    def __init__(self, InstrumentID=""):
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspQueryAccountField:
    def __init__(self, BankPwdFlag='0', TradingDay="", TradeTime="", FutureSerial=0, DeviceID="", InstallID=0, BrokerID="", SessionID=0, IdentifiedCardNo="", AccountID="", SecuPwdFlag='0', BankFetchAmount=0, VerifyCertNoFlag='0', BankUseAmount=0, BankID="", CurrencyID="", BankSecuAccType='1', OperNo="", BankAccount="", Digest="", BankSecuAcc="", Password="", LastFragment='0', RequestID=0, BankAccType='1', TradeDate="", UserID="", CustType='0', IdCardType='0', BankSerial="", BrokerIDByBank="", TradeCode="", CustomerName="", BankPassWord="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.BankPwdFlag=tou(BankPwdFlag)
        self.TradingDay=tou(TradingDay)
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.DeviceID=tou(DeviceID)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.AccountID=tou(AccountID)
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.BankFetchAmount=BankFetchAmount
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.BankUseAmount=BankUseAmount
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.Digest=tou(Digest)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.BankAccType=tou(BankAccType)
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.IdCardType=tou(IdCardType)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankPwdFlag', 'TradingDay', 'TradeTime', 'FutureSerial', 'DeviceID', 'InstallID', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'AccountID', 'SecuPwdFlag', 'BankFetchAmount', 'VerifyCertNoFlag', 'BankUseAmount', 'BankID', 'CurrencyID', 'BankSecuAccType', 'OperNo', 'BankAccount', 'Digest', 'BankSecuAcc', 'Password', 'LastFragment', 'RequestID', 'BankAccType', 'TradeDate', 'UserID', 'CustType', 'IdCardType', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'CustomerName', 'BankPassWord', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankPwdFlag', u'银行密码标志'),('TradingDay', u'交易系统日期'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('DeviceID', u'渠道标志'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('AccountID', u'投资者帐号'),('SecuPwdFlag', u'期货资金密码核对标志'),('BankFetchAmount', u'银行可取金额'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('BankUseAmount', u'银行可用金额'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('BankSecuAccType', u'期货单位帐号类型'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('Digest', u'摘要'),('BankSecuAcc', u'期货单位帐号'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BankAccType', u'银行帐号类型'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('CustType', u'客户类型'),('IdCardType', u'证件类型'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['BankPwdFlag', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'LastFragment', 'BankAccType', 'CustType', 'IdCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryEWarrantOffsetField:
    def __init__(self, BrokerID="", InvestorID="", ExchangeID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'ExchangeID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcFrontStatusField:
    def __init__(self, LastReportDate="", FrontID=0, IsActive=0, LastReportTime=""):
        self.LastReportDate=tou(LastReportDate)
        self.FrontID=FrontID
        self.IsActive=IsActive
        self.LastReportTime=tou(LastReportTime)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LastReportDate', 'FrontID', 'IsActive', 'LastReportTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LastReportDate', u'上次报告日期'),('FrontID', u'前置编号'),('IsActive', u'是否活跃'),('LastReportTime', u'上次报告时间')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcDisseminationField:
    def __init__(self, SequenceSeries=0, SequenceNo=0):
        self.SequenceSeries=SequenceSeries
        self.SequenceNo=SequenceNo
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SequenceSeries', 'SequenceNo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('SequenceSeries', u'序列系列号'),('SequenceNo', u'序列号')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingInvestorField:
    def __init__(self, CommModelID="", InvestorName="", IsActive=0, Address="", BrokerID="", InvestorID="", IdentifiedCardType='0', OpenDate="", IdentifiedCardNo="", Mobile="", Telephone="", InvestorGroupID="", MarginModelID=""):
        self.CommModelID=tou(CommModelID)
        self.InvestorName=tou(InvestorName)
        self.IsActive=IsActive
        self.Address=tou(Address)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.IdentifiedCardType=tou(IdentifiedCardType)
        self.OpenDate=tou(OpenDate)
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.Mobile=tou(Mobile)
        self.Telephone=tou(Telephone)
        self.InvestorGroupID=tou(InvestorGroupID)
        self.MarginModelID=tou(MarginModelID)
        self.vcmap={'IdentifiedCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CommModelID', 'InvestorName', 'IsActive', 'Address', 'BrokerID', 'InvestorID', 'IdentifiedCardType', 'OpenDate', 'IdentifiedCardNo', 'Mobile', 'Telephone', 'InvestorGroupID', 'MarginModelID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CommModelID', u'手续费率模板代码'),('InvestorName', u'投资者名称'),('IsActive', u'是否活跃'),('Address', u'通讯地址'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('IdentifiedCardType', u'证件类型'),('OpenDate', u'开户日期'),('IdentifiedCardNo', u'证件号码'),('Mobile', u'手机'),('Telephone', u'联系电话'),('InvestorGroupID', u'投资者分组代码'),('MarginModelID', u'保证金率模板代码')]])
    def getval(self, n):
        if n in ['IdentifiedCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferBankField:
    def __init__(self, IsActive=0, BankID="", BankBrchID="", BankName=""):
        self.IsActive=IsActive
        self.BankID=tou(BankID)
        self.BankBrchID=tou(BankBrchID)
        self.BankName=tou(BankName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IsActive', 'BankID', 'BankBrchID', 'BankName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('IsActive', u'是否活跃'),('BankID', u'银行代码'),('BankBrchID', u'银行分中心代码'),('BankName', u'银行名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcCommPhaseField:
    def __init__(self, TradingDay="", CommPhaseNo=0, SystemID=""):
        self.TradingDay=tou(TradingDay)
        self.CommPhaseNo=CommPhaseNo
        self.SystemID=tou(SystemID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'CommPhaseNo', 'SystemID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易日'),('CommPhaseNo', u'通讯时段编号'),('SystemID', u'系统编号')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryProductField:
    def __init__(self, ProductID=""):
        self.ProductID=tou(ProductID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ProductID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ProductID', u'产品代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataExchangeField:
    def __init__(self, ExchangeID=""):
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorGroupField:
    def __init__(self, BrokerID="", InvestorGroupID="", InvestorGroupName=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorGroupID=tou(InvestorGroupID)
        self.InvestorGroupName=tou(InvestorGroupName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorGroupID', 'InvestorGroupName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorGroupID', u'投资者分组代码'),('InvestorGroupName', u'投资者分组名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcDiscountField:
    def __init__(self, Discount=0, BrokerID="", InvestorID="", InvestorRange='1'):
        self.Discount=Discount
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Discount', 'BrokerID', 'InvestorID', 'InvestorRange']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Discount', u'资金折扣比例'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInstrumentMarginRateField:
    def __init__(self, BrokerID="", InvestorID="", InstrumentID="", HedgeFlag='1'):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InstrumentID=tou(InstrumentID)
        self.HedgeFlag=tou(HedgeFlag)
        self.vcmap={'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'InstrumentID', 'HedgeFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InstrumentID', u'合约代码'),('HedgeFlag', u'投机套保标志')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcCommRateModelField:
    def __init__(self, CommModelID="", BrokerID="", CommModelName=""):
        self.CommModelID=tou(CommModelID)
        self.BrokerID=tou(BrokerID)
        self.CommModelName=tou(CommModelName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CommModelID', 'BrokerID', 'CommModelName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CommModelID', u'手续费率模板代码'),('BrokerID', u'经纪公司代码'),('CommModelName', u'模板名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSettlementInfoConfirmField:
    def __init__(self, BrokerID="", InvestorID="", ConfirmDate="", ConfirmTime=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ConfirmDate=tou(ConfirmDate)
        self.ConfirmTime=tou(ConfirmTime)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'ConfirmDate', 'ConfirmTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ConfirmDate', u'确认日期'),('ConfirmTime', u'确认时间')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcForceUserLogoutField:
    def __init__(self, BrokerID="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerUserRightAssignField:
    def __init__(self, BrokerID="", DRIdentityID=0, Tradeable=0):
        self.BrokerID=tou(BrokerID)
        self.DRIdentityID=DRIdentityID
        self.Tradeable=Tradeable
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'DRIdentityID', 'Tradeable']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'应用单元代码'),('DRIdentityID', u'交易中心代码'),('Tradeable', u'能否交易')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcUserRightsAssignField:
    def __init__(self, BrokerID="", UserID="", DRIdentityID=0):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.DRIdentityID=DRIdentityID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID', 'DRIdentityID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'应用单元代码'),('UserID', u'用户代码'),('DRIdentityID', u'交易中心代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSuperUserField:
    def __init__(self, Password="", UserID="", IsActive=0, UserName=""):
        self.Password=tou(Password)
        self.UserID=tou(UserID)
        self.IsActive=IsActive
        self.UserName=tou(UserName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'UserID', 'IsActive', 'UserName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('UserID', u'用户代码'),('IsActive', u'是否活跃'),('UserName', u'用户名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryErrOrderField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorField:
    def __init__(self, CommModelID="", InvestorName="", IsActive=0, Address="", BrokerID="", InvestorID="", IdentifiedCardType='0', OpenDate="", IdentifiedCardNo="", Mobile="", Telephone="", InvestorGroupID="", MarginModelID=""):
        self.CommModelID=tou(CommModelID)
        self.InvestorName=tou(InvestorName)
        self.IsActive=IsActive
        self.Address=tou(Address)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.IdentifiedCardType=tou(IdentifiedCardType)
        self.OpenDate=tou(OpenDate)
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.Mobile=tou(Mobile)
        self.Telephone=tou(Telephone)
        self.InvestorGroupID=tou(InvestorGroupID)
        self.MarginModelID=tou(MarginModelID)
        self.vcmap={'IdentifiedCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CommModelID', 'InvestorName', 'IsActive', 'Address', 'BrokerID', 'InvestorID', 'IdentifiedCardType', 'OpenDate', 'IdentifiedCardNo', 'Mobile', 'Telephone', 'InvestorGroupID', 'MarginModelID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CommModelID', u'手续费率模板代码'),('InvestorName', u'投资者名称'),('IsActive', u'是否活跃'),('Address', u'通讯地址'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('IdentifiedCardType', u'证件类型'),('OpenDate', u'开户日期'),('IdentifiedCardNo', u'证件号码'),('Mobile', u'手机'),('Telephone', u'联系电话'),('InvestorGroupID', u'投资者分组代码'),('MarginModelID', u'保证金率模板代码')]])
    def getval(self, n):
        if n in ['IdentifiedCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTraderField:
    def __init__(self, ExchangeID="", TraderID="", ParticipantID=""):
        self.ExchangeID=tou(ExchangeID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTransferBankField:
    def __init__(self, BankID="", BankBrchID=""):
        self.BankID=tou(BankID)
        self.BankBrchID=tou(BankBrchID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankID', 'BankBrchID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankID', u'银行代码'),('BankBrchID', u'银行分中心代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryOrderActionField:
    def __init__(self, BrokerID="", InvestorID="", ExchangeID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcVerifyInvestorPasswordField:
    def __init__(self, Password="", BrokerID="", InvestorID=""):
        self.Password=tou(Password)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInputOrderActionField:
    def __init__(self, OrderSysID="", RequestID=0, SessionID=0, BrokerID="", FrontID=0, InvestorID="", ActionFlag='0', InstrumentID="", LimitPrice=0, OrderActionRef=0, VolumeChange=0, ExchangeID="", UserID="", OrderRef=""):
        self.OrderSysID=tou(OrderSysID)
        self.RequestID=RequestID
        self.SessionID=SessionID
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.InvestorID=tou(InvestorID)
        self.ActionFlag=tou(ActionFlag)
        self.InstrumentID=tou(InstrumentID)
        self.LimitPrice=LimitPrice
        self.OrderActionRef=OrderActionRef
        self.VolumeChange=VolumeChange
        self.ExchangeID=tou(ExchangeID)
        self.UserID=tou(UserID)
        self.OrderRef=tou(OrderRef)
        self.vcmap={'ActionFlag': {"'3'": '修改', "'0'": '删除'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderSysID', 'RequestID', 'SessionID', 'BrokerID', 'FrontID', 'InvestorID', 'ActionFlag', 'InstrumentID', 'LimitPrice', 'OrderActionRef', 'VolumeChange', 'ExchangeID', 'UserID', 'OrderRef']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderSysID', u'报单编号'),('RequestID', u'请求编号'),('SessionID', u'会话编号'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('InvestorID', u'投资者代码'),('ActionFlag', u'操作标志'),('InstrumentID', u'合约代码'),('LimitPrice', u'价格'),('OrderActionRef', u'报单操作引用'),('VolumeChange', u'数量变化'),('ExchangeID', u'交易所代码'),('UserID', u'用户代码'),('OrderRef', u'报单引用')]])
    def getval(self, n):
        if n in ['ActionFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcErrOrderActionField:
    def __init__(self, InvestorID="", ClientID="", InstallID=0, BrokerID="", FrontID=0, SessionID=0, TraderID="", StatusMsg="", ActionLocalID="", VolumeChange=0, ActionDate="", ErrorMsg="", ExchangeID="", OrderSysID="", RequestID=0, UserID="", InstrumentID="", ParticipantID="", ActionFlag='0', ErrorID=0, BusinessUnit="", OrderActionStatus='a', LimitPrice=0, OrderActionRef=0, OrderRef="", OrderLocalID="", ActionTime=""):
        self.InvestorID=tou(InvestorID)
        self.ClientID=tou(ClientID)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.TraderID=tou(TraderID)
        self.StatusMsg=tou(StatusMsg)
        self.ActionLocalID=tou(ActionLocalID)
        self.VolumeChange=VolumeChange
        self.ActionDate=tou(ActionDate)
        self.ErrorMsg=tou(ErrorMsg)
        self.ExchangeID=tou(ExchangeID)
        self.OrderSysID=tou(OrderSysID)
        self.RequestID=RequestID
        self.UserID=tou(UserID)
        self.InstrumentID=tou(InstrumentID)
        self.ParticipantID=tou(ParticipantID)
        self.ActionFlag=tou(ActionFlag)
        self.ErrorID=ErrorID
        self.BusinessUnit=tou(BusinessUnit)
        self.OrderActionStatus=tou(OrderActionStatus)
        self.LimitPrice=LimitPrice
        self.OrderActionRef=OrderActionRef
        self.OrderRef=tou(OrderRef)
        self.OrderLocalID=tou(OrderLocalID)
        self.ActionTime=tou(ActionTime)
        self.vcmap={'ActionFlag': {"'3'": '修改', "'0'": '删除'}, 'OrderActionStatus': {"'a'": '已经提交', "'c'": '已经被拒绝', "'b'": '已经接受'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'ClientID', 'InstallID', 'BrokerID', 'FrontID', 'SessionID', 'TraderID', 'StatusMsg', 'ActionLocalID', 'VolumeChange', 'ActionDate', 'ErrorMsg', 'ExchangeID', 'OrderSysID', 'RequestID', 'UserID', 'InstrumentID', 'ParticipantID', 'ActionFlag', 'ErrorID', 'BusinessUnit', 'OrderActionStatus', 'LimitPrice', 'OrderActionRef', 'OrderRef', 'OrderLocalID', 'ActionTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('ClientID', u'客户代码'),('InstallID', u'安装编号'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('SessionID', u'会话编号'),('TraderID', u'交易所交易员代码'),('StatusMsg', u'状态信息'),('ActionLocalID', u'操作本地编号'),('VolumeChange', u'数量变化'),('ActionDate', u'操作日期'),('ErrorMsg', u'错误信息'),('ExchangeID', u'交易所代码'),('OrderSysID', u'报单编号'),('RequestID', u'请求编号'),('UserID', u'用户代码'),('InstrumentID', u'合约代码'),('ParticipantID', u'会员代码'),('ActionFlag', u'操作标志'),('ErrorID', u'错误代码'),('BusinessUnit', u'业务单元'),('OrderActionStatus', u'报单操作状态'),('LimitPrice', u'价格'),('OrderActionRef', u'报单操作引用'),('OrderRef', u'报单引用'),('OrderLocalID', u'本地报单编号'),('ActionTime', u'操作时间')]])
    def getval(self, n):
        if n in ['ActionFlag', 'OrderActionStatus']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTradingCodeField:
    def __init__(self, ClientID="", ClientIDType='1', BrokerID="", InvestorID="", ExchangeID=""):
        self.ClientID=tou(ClientID)
        self.ClientIDType=tou(ClientIDType)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={'ClientIDType': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ClientID', 'ClientIDType', 'BrokerID', 'InvestorID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ClientID', u'客户代码'),('ClientIDType', u'交易编码类型'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in ['ClientIDType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeMarginRateAdjustField:
    def __init__(self, LongMarginRatioByMoney=0, NoShortMarginRatioByVolume=0, ShortMarginRatioByVolume=0, ExchLongMarginRatioByVolume=0, LongMarginRatioByVolume=0, ShortMarginRatioByMoney=0, ExchShortMarginRatioByVolume=0, NoLongMarginRatioByVolume=0, InstrumentID="", BrokerID="", HedgeFlag='1', ExchLongMarginRatioByMoney=0, NoLongMarginRatioByMoney=0, NoShortMarginRatioByMoney=0, ExchShortMarginRatioByMoney=0):
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.NoShortMarginRatioByVolume=NoShortMarginRatioByVolume
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.ExchLongMarginRatioByVolume=ExchLongMarginRatioByVolume
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.ExchShortMarginRatioByVolume=ExchShortMarginRatioByVolume
        self.NoLongMarginRatioByVolume=NoLongMarginRatioByVolume
        self.InstrumentID=tou(InstrumentID)
        self.BrokerID=tou(BrokerID)
        self.HedgeFlag=tou(HedgeFlag)
        self.ExchLongMarginRatioByMoney=ExchLongMarginRatioByMoney
        self.NoLongMarginRatioByMoney=NoLongMarginRatioByMoney
        self.NoShortMarginRatioByMoney=NoShortMarginRatioByMoney
        self.ExchShortMarginRatioByMoney=ExchShortMarginRatioByMoney
        self.vcmap={'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LongMarginRatioByMoney', 'NoShortMarginRatioByVolume', 'ShortMarginRatioByVolume', 'ExchLongMarginRatioByVolume', 'LongMarginRatioByVolume', 'ShortMarginRatioByMoney', 'ExchShortMarginRatioByVolume', 'NoLongMarginRatioByVolume', 'InstrumentID', 'BrokerID', 'HedgeFlag', 'ExchLongMarginRatioByMoney', 'NoLongMarginRatioByMoney', 'NoShortMarginRatioByMoney', 'ExchShortMarginRatioByMoney']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LongMarginRatioByMoney', u'跟随交易所投资者多头保证金率'),('NoShortMarginRatioByVolume', u'不跟随交易所投资者空头保证金费'),('ShortMarginRatioByVolume', u'跟随交易所投资者空头保证金费'),('ExchLongMarginRatioByVolume', u'交易所多头保证金费'),('LongMarginRatioByVolume', u'跟随交易所投资者多头保证金费'),('ShortMarginRatioByMoney', u'跟随交易所投资者空头保证金率'),('ExchShortMarginRatioByVolume', u'交易所空头保证金费'),('NoLongMarginRatioByVolume', u'不跟随交易所投资者多头保证金费'),('InstrumentID', u'合约代码'),('BrokerID', u'经纪公司代码'),('HedgeFlag', u'投机套保标志'),('ExchLongMarginRatioByMoney', u'交易所多头保证金率'),('NoLongMarginRatioByMoney', u'不跟随交易所投资者多头保证金率'),('NoShortMarginRatioByMoney', u'不跟随交易所投资者空头保证金率'),('ExchShortMarginRatioByMoney', u'交易所空头保证金率')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcFensUserInfoField:
    def __init__(self, BrokerID="", UserID="", LoginMode='0'):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.LoginMode=tou(LoginMode)
        self.vcmap={'LoginMode': {"'1'": '转账', "'0'": '交易'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID', 'LoginMode']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserID', u'用户代码'),('LoginMode', u'登录模式')]])
    def getval(self, n):
        if n in ['LoginMode']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryBrokerTradingAlgosField:
    def __init__(self, BrokerID="", ExchangeID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'ExchangeID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcPartBrokerField:
    def __init__(self, IsActive=0, BrokerID="", ExchangeID="", ParticipantID=""):
        self.IsActive=IsActive
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IsActive', 'BrokerID', 'ExchangeID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('IsActive', u'是否活跃'),('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQueryMaxOrderVolumeField:
    def __init__(self, InstrumentID="", OffsetFlag='0', HedgeFlag='1', MaxVolume=0, Direction='0', BrokerID="", InvestorID=""):
        self.InstrumentID=tou(InstrumentID)
        self.OffsetFlag=tou(OffsetFlag)
        self.HedgeFlag=tou(HedgeFlag)
        self.MaxVolume=MaxVolume
        self.Direction=tou(Direction)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={'Direction': {"'1'": '卖', "'0'": '买'}, 'OffsetFlag': {"'1'": '平仓', "'6'": '本地强平', "'0'": '开仓', "'5'": '强减', "'4'": '平昨', "'3'": '平今', "'2'": '强平'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'OffsetFlag', 'HedgeFlag', 'MaxVolume', 'Direction', 'BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('OffsetFlag', u'开平标志'),('HedgeFlag', u'投机套保标志'),('MaxVolume', u'最大允许报单数量'),('Direction', u'买卖方向'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in ['OffsetFlag', 'HedgeFlag', 'Direction']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTraderOfferField:
    def __init__(self, ExchangeID="", TraderID="", ParticipantID=""):
        self.ExchangeID=tou(ExchangeID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcUserSessionField:
    def __init__(self, MacAddress="", UserProductInfo="", LoginDate="", ProtocolInfo="", LoginTime="", InterfaceProductInfo="", BrokerID="", FrontID=0, SessionID=0, UserID="", IPAddress=""):
        self.MacAddress=tou(MacAddress)
        self.UserProductInfo=tou(UserProductInfo)
        self.LoginDate=tou(LoginDate)
        self.ProtocolInfo=tou(ProtocolInfo)
        self.LoginTime=tou(LoginTime)
        self.InterfaceProductInfo=tou(InterfaceProductInfo)
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.UserID=tou(UserID)
        self.IPAddress=tou(IPAddress)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MacAddress', 'UserProductInfo', 'LoginDate', 'ProtocolInfo', 'LoginTime', 'InterfaceProductInfo', 'BrokerID', 'FrontID', 'SessionID', 'UserID', 'IPAddress']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('MacAddress', u'Mac地址'),('UserProductInfo', u'用户端产品信息'),('LoginDate', u'登录日期'),('ProtocolInfo', u'协议信息'),('LoginTime', u'登录时间'),('InterfaceProductInfo', u'接口端产品信息'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('SessionID', u'会话编号'),('UserID', u'用户代码'),('IPAddress', u'IP地址')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcOrderField:
    def __init__(self, InsertDate="", ZCETotalTradedVolume=0, Direction='0', OrderSubmitStatus='0', BrokerID="", SessionID=0, MinVolume=0, VolumeTotalOriginal=0, CancelTime="", StopPrice=0, InsertTime="", BrokerOrderSeq=0, VolumeTraded=0, ExchangeInstID="", ParticipantID="", SettlementID=0, ActiveTime="", GTDDate="", OrderRef="", ContingentCondition='1', VolumeCondition='1', OrderType='0', OrderLocalID="", ActiveUserID="", NotifySequence=0, RelativeOrderSysID="", OrderPriceType='1', SuspendTime="", VolumeTotal=0, ClientID="", StatusMsg="", InstallID=0, InvestorID="", ForceCloseReason='0', TraderID="", InstrumentID="", FrontID=0, UserForceClose=0, OrderStatus='0', ExchangeID="", OrderSysID="", RequestID=0, IsAutoSuspend=0, IsSwapOrder=0, SequenceNo=0, CombOffsetFlag="", OrderSource='0', TradingDay="", ClearingPartID="", TimeCondition='1', UpdateTime="", BusinessUnit="", UserProductInfo="", LimitPrice=0, CombHedgeFlag="", ActiveTraderID="", UserID=""):
        self.InsertDate=tou(InsertDate)
        self.ZCETotalTradedVolume=ZCETotalTradedVolume
        self.Direction=tou(Direction)
        self.OrderSubmitStatus=tou(OrderSubmitStatus)
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.MinVolume=MinVolume
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.CancelTime=tou(CancelTime)
        self.StopPrice=StopPrice
        self.InsertTime=tou(InsertTime)
        self.BrokerOrderSeq=BrokerOrderSeq
        self.VolumeTraded=VolumeTraded
        self.ExchangeInstID=tou(ExchangeInstID)
        self.ParticipantID=tou(ParticipantID)
        self.SettlementID=SettlementID
        self.ActiveTime=tou(ActiveTime)
        self.GTDDate=tou(GTDDate)
        self.OrderRef=tou(OrderRef)
        self.ContingentCondition=tou(ContingentCondition)
        self.VolumeCondition=tou(VolumeCondition)
        self.OrderType=tou(OrderType)
        self.OrderLocalID=tou(OrderLocalID)
        self.ActiveUserID=tou(ActiveUserID)
        self.NotifySequence=NotifySequence
        self.RelativeOrderSysID=tou(RelativeOrderSysID)
        self.OrderPriceType=tou(OrderPriceType)
        self.SuspendTime=tou(SuspendTime)
        self.VolumeTotal=VolumeTotal
        self.ClientID=tou(ClientID)
        self.StatusMsg=tou(StatusMsg)
        self.InstallID=InstallID
        self.InvestorID=tou(InvestorID)
        self.ForceCloseReason=tou(ForceCloseReason)
        self.TraderID=tou(TraderID)
        self.InstrumentID=tou(InstrumentID)
        self.FrontID=FrontID
        self.UserForceClose=UserForceClose
        self.OrderStatus=tou(OrderStatus)
        self.ExchangeID=tou(ExchangeID)
        self.OrderSysID=tou(OrderSysID)
        self.RequestID=RequestID
        self.IsAutoSuspend=IsAutoSuspend
        self.IsSwapOrder=IsSwapOrder
        self.SequenceNo=SequenceNo
        self.CombOffsetFlag=tou(CombOffsetFlag)
        self.OrderSource=tou(OrderSource)
        self.TradingDay=tou(TradingDay)
        self.ClearingPartID=tou(ClearingPartID)
        self.TimeCondition=tou(TimeCondition)
        self.UpdateTime=tou(UpdateTime)
        self.BusinessUnit=tou(BusinessUnit)
        self.UserProductInfo=tou(UserProductInfo)
        self.LimitPrice=LimitPrice
        self.CombHedgeFlag=tou(CombHedgeFlag)
        self.ActiveTraderID=tou(ActiveTraderID)
        self.UserID=tou(UserID)
        self.vcmap={'VolumeCondition': {"'1'": '任何数量', "'3'": '全部数量', "'2'": '最小数量'}, 'OrderPriceType': {"'1'": '任意价', "'F'": '买一价浮动上浮3个ticks', "'E'": '买一价浮动上浮2个ticks', "'4'": '最新价', "'3'": '最优价', "'2'": '限价', "'7'": '最新价浮动上浮3个ticks', "'A'": '卖一价浮动上浮2个ticks', "'6'": '最新价浮动上浮2个ticks', "'5'": '最新价浮动上浮1个ticks', "'D'": '买一价浮动上浮1个ticks', "'9'": '卖一价浮动上浮1个ticks', "'C'": '买一价', "'8'": '卖一价', "'B'": '卖一价浮动上浮3个ticks'}, 'OrderSource': {"'1'": '来自管理员', "'0'": '来自参与者'}, 'ContingentCondition': {"'1'": '立即', "'F'": '买一价小于条件价', "'E'": '买一价大于等于条件价', "'4'": '预埋单', "'3'": '止赢', "'H'": '买一价小于等于条件价', "'2'": '止损', "'7'": '最新价小于条件价', "'A'": '卖一价大于等于条件价', "'6'": '最新价大于等于条件价', "'5'": '最新价大于条件价', "'D'": '买一价大于条件价', "'9'": '卖一价大于条件价', "'C'": '卖一价小于等于条件价', "'8'": '最新价小于等于条件价', "'B'": '卖一价小于条件价'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'OrderSubmitStatus': {"'1'": '撤单已经提交', "'6'": '改单已经被拒绝', "'0'": '已经提交', "'5'": '撤单已经被拒绝', "'4'": '报单已经被拒绝', "'3'": '已经接受', "'2'": '修改已经提交'}, 'OrderStatus': {"'1'": '部分成交还在队列中', "'0'": '全部成交', "'5'": '撤单', "'4'": '未成交不在队列中', "'3'": '未成交还在队列中', "'2'": '部分成交不在队列中', "'c'": '已触发', "'a'": '未知', "'b'": '尚未触发'}, 'OrderType': {"'1'": '报价衍生', "'0'": '正常', "'5'": '互换单', "'4'": '条件单', "'3'": '组合报单', "'2'": '组合衍生'}, 'ForceCloseReason': {"'7'": '自然人临近交割', "'1'": '资金不足', "'6'": '其它', "'0'": '非强平', "'5'": '违规', "'4'": '持仓非整数倍', "'3'": '会员超仓', "'2'": '客户超仓'}, 'TimeCondition': {"'1'": '立即完成，否则撤销', "'6'": '集合竞价有效', "'5'": '撤销前有效', "'4'": '指定日期前有效', "'3'": '当日有效', "'2'": '本节有效'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InsertDate', 'ZCETotalTradedVolume', 'Direction', 'OrderSubmitStatus', 'BrokerID', 'SessionID', 'MinVolume', 'VolumeTotalOriginal', 'CancelTime', 'StopPrice', 'InsertTime', 'BrokerOrderSeq', 'VolumeTraded', 'ExchangeInstID', 'ParticipantID', 'SettlementID', 'ActiveTime', 'GTDDate', 'OrderRef', 'ContingentCondition', 'VolumeCondition', 'OrderType', 'OrderLocalID', 'ActiveUserID', 'NotifySequence', 'RelativeOrderSysID', 'OrderPriceType', 'SuspendTime', 'VolumeTotal', 'ClientID', 'StatusMsg', 'InstallID', 'InvestorID', 'ForceCloseReason', 'TraderID', 'InstrumentID', 'FrontID', 'UserForceClose', 'OrderStatus', 'ExchangeID', 'OrderSysID', 'RequestID', 'IsAutoSuspend', 'IsSwapOrder', 'SequenceNo', 'CombOffsetFlag', 'OrderSource', 'TradingDay', 'ClearingPartID', 'TimeCondition', 'UpdateTime', 'BusinessUnit', 'UserProductInfo', 'LimitPrice', 'CombHedgeFlag', 'ActiveTraderID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InsertDate', u'报单日期'),('ZCETotalTradedVolume', u'郑商所成交数量'),('Direction', u'买卖方向'),('OrderSubmitStatus', u'报单提交状态'),('BrokerID', u'经纪公司代码'),('SessionID', u'会话编号'),('MinVolume', u'最小成交量'),('VolumeTotalOriginal', u'数量'),('CancelTime', u'撤销时间'),('StopPrice', u'止损价'),('InsertTime', u'委托时间'),('BrokerOrderSeq', u'经纪公司报单编号'),('VolumeTraded', u'今成交数量'),('ExchangeInstID', u'合约在交易所的代码'),('ParticipantID', u'会员代码'),('SettlementID', u'结算编号'),('ActiveTime', u'激活时间'),('GTDDate', u'GTD日期'),('OrderRef', u'报单引用'),('ContingentCondition', u'触发条件'),('VolumeCondition', u'成交量类型'),('OrderType', u'报单类型'),('OrderLocalID', u'本地报单编号'),('ActiveUserID', u'操作用户代码'),('NotifySequence', u'报单提示序号'),('RelativeOrderSysID', u'相关报单'),('OrderPriceType', u'报单价格条件'),('SuspendTime', u'挂起时间'),('VolumeTotal', u'剩余数量'),('ClientID', u'客户代码'),('StatusMsg', u'状态信息'),('InstallID', u'安装编号'),('InvestorID', u'投资者代码'),('ForceCloseReason', u'强平原因'),('TraderID', u'交易所交易员代码'),('InstrumentID', u'合约代码'),('FrontID', u'前置编号'),('UserForceClose', u'用户强评标志'),('OrderStatus', u'报单状态'),('ExchangeID', u'交易所代码'),('OrderSysID', u'报单编号'),('RequestID', u'请求编号'),('IsAutoSuspend', u'自动挂起标志'),('IsSwapOrder', u'互换单标志'),('SequenceNo', u'序号'),('CombOffsetFlag', u'组合开平标志'),('OrderSource', u'报单来源'),('TradingDay', u'交易日'),('ClearingPartID', u'结算会员编号'),('TimeCondition', u'有效期类型'),('UpdateTime', u'最后修改时间'),('BusinessUnit', u'业务单元'),('UserProductInfo', u'用户端产品信息'),('LimitPrice', u'价格'),('CombHedgeFlag', u'组合投机套保标志'),('ActiveTraderID', u'最后修改交易所交易员代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in ['Direction', 'OrderSubmitStatus', 'ContingentCondition', 'VolumeCondition', 'OrderType', 'OrderPriceType', 'ForceCloseReason', 'OrderStatus', 'OrderSource', 'TimeCondition']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryPartBrokerField:
    def __init__(self, BrokerID="", ExchangeID="", ParticipantID=""):
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'ExchangeID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQrySettlementInfoConfirmField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQrySuperUserFunctionField:
    def __init__(self, UserID=""):
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryExchangeMarginRateAdjustField:
    def __init__(self, BrokerID="", InstrumentID="", HedgeFlag='1'):
        self.BrokerID=tou(BrokerID)
        self.InstrumentID=tou(InstrumentID)
        self.HedgeFlag=tou(HedgeFlag)
        self.vcmap={'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InstrumentID', 'HedgeFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InstrumentID', u'合约代码'),('HedgeFlag', u'投机套保标志')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqQueryTradeResultBySerialField:
    def __init__(self, TradingDay="", TradeTime="", BrokerID="", SessionID=0, IdentifiedCardNo="", AccountID="", RefrenceIssureType='0', TradeAmount=0, Reference=0, BankID="", CurrencyID="", BankAccount="", Digest="", Password="", LastFragment='0', TradeDate="", CustType='0', IdCardType='0', BankSerial="", TradeCode="", CustomerName="", RefrenceIssure="", BankPassWord="", BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.TradingDay=tou(TradingDay)
        self.TradeTime=tou(TradeTime)
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.AccountID=tou(AccountID)
        self.RefrenceIssureType=tou(RefrenceIssureType)
        self.TradeAmount=TradeAmount
        self.Reference=Reference
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.BankAccount=tou(BankAccount)
        self.Digest=tou(Digest)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.TradeDate=tou(TradeDate)
        self.CustType=tou(CustType)
        self.IdCardType=tou(IdCardType)
        self.BankSerial=tou(BankSerial)
        self.TradeCode=tou(TradeCode)
        self.CustomerName=tou(CustomerName)
        self.RefrenceIssure=tou(RefrenceIssure)
        self.BankPassWord=tou(BankPassWord)
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'RefrenceIssureType': {"'1'": '期商', "'0'": '银行', "'2'": '券商'}, 'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'TradeTime', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'AccountID', 'RefrenceIssureType', 'TradeAmount', 'Reference', 'BankID', 'CurrencyID', 'BankAccount', 'Digest', 'Password', 'LastFragment', 'TradeDate', 'CustType', 'IdCardType', 'BankSerial', 'TradeCode', 'CustomerName', 'RefrenceIssure', 'BankPassWord', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易系统日期'),('TradeTime', u'交易时间'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('AccountID', u'投资者帐号'),('RefrenceIssureType', u'本流水号发布者的机构类型'),('TradeAmount', u'转帐金额'),('Reference', u'流水号'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('BankAccount', u'银行帐号'),('Digest', u'摘要'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('TradeDate', u'交易日期'),('CustType', u'客户类型'),('IdCardType', u'证件类型'),('BankSerial', u'银行流水号'),('TradeCode', u'业务功能码'),('CustomerName', u'客户姓名'),('RefrenceIssure', u'本流水号发布者机构编码'),('BankPassWord', u'银行密码'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['RefrenceIssureType', 'LastFragment', 'CustType', 'IdCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryExchangeOrderActionField:
    def __init__(self, ClientID="", ExchangeID="", TraderID="", ParticipantID=""):
        self.ClientID=tou(ClientID)
        self.ExchangeID=tou(ExchangeID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ClientID', 'ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ClientID', u'客户代码'),('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcNotifyFutureSignInField:
    def __init__(self, TradeTime="", DeviceID="", ErrorID=0, InstallID=0, BrokerID="", SessionID=0, BankID="", CurrencyID="", ErrorMsg="", PinKey="", OperNo="", MacKey="", Digest="", LastFragment='0', RequestID=0, TradeDate="", UserID="", TradingDay="", BankSerial="", BrokerIDByBank="", TradeCode="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.PinKey=tou(PinKey)
        self.OperNo=tou(OperNo)
        self.MacKey=tou(MacKey)
        self.Digest=tou(Digest)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeTime', 'DeviceID', 'ErrorID', 'InstallID', 'BrokerID', 'SessionID', 'BankID', 'CurrencyID', 'ErrorMsg', 'PinKey', 'OperNo', 'MacKey', 'Digest', 'LastFragment', 'RequestID', 'TradeDate', 'UserID', 'TradingDay', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('PinKey', u'PIN密钥'),('OperNo', u'交易柜员'),('MacKey', u'MAC密钥'),('Digest', u'摘要'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('TradingDay', u'交易系统日期'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryParkedOrderActionField:
    def __init__(self, BrokerID="", InvestorID="", ExchangeID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'ExchangeID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMulticastGroupInfoField:
    def __init__(self, GroupPort=0, SourceIP="", GroupIP=""):
        self.GroupPort=GroupPort
        self.SourceIP=tou(SourceIP)
        self.GroupIP=tou(GroupIP)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['GroupPort', 'SourceIP', 'GroupIP']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('GroupPort', u'组播组IP端口'),('SourceIP', u'源地址'),('GroupIP', u'组播组IP地址')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorPositionCombineDetailField:
    def __init__(self, ExchMargin=0, ComTradeID="", TradingDay="", TradeID="", CombInstrumentID="", Margin=0, Direction='0', LegMultiple=0, BrokerID="", InvestorID="", MarginRateByVolume=0, OpenDate="", SettlementID=0, InstrumentID="", TradeGroupID=0, HedgeFlag='1', LegID=0, ExchangeID="", MarginRateByMoney=0, TotalAmt=0):
        self.ExchMargin=ExchMargin
        self.ComTradeID=tou(ComTradeID)
        self.TradingDay=tou(TradingDay)
        self.TradeID=tou(TradeID)
        self.CombInstrumentID=tou(CombInstrumentID)
        self.Margin=Margin
        self.Direction=tou(Direction)
        self.LegMultiple=LegMultiple
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.MarginRateByVolume=MarginRateByVolume
        self.OpenDate=tou(OpenDate)
        self.SettlementID=SettlementID
        self.InstrumentID=tou(InstrumentID)
        self.TradeGroupID=TradeGroupID
        self.HedgeFlag=tou(HedgeFlag)
        self.LegID=LegID
        self.ExchangeID=tou(ExchangeID)
        self.MarginRateByMoney=MarginRateByMoney
        self.TotalAmt=TotalAmt
        self.vcmap={'Direction': {"'1'": '卖', "'0'": '买'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchMargin', 'ComTradeID', 'TradingDay', 'TradeID', 'CombInstrumentID', 'Margin', 'Direction', 'LegMultiple', 'BrokerID', 'InvestorID', 'MarginRateByVolume', 'OpenDate', 'SettlementID', 'InstrumentID', 'TradeGroupID', 'HedgeFlag', 'LegID', 'ExchangeID', 'MarginRateByMoney', 'TotalAmt']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchMargin', u'交易所保证金'),('ComTradeID', u'组合编号'),('TradingDay', u'交易日'),('TradeID', u'撮合编号'),('CombInstrumentID', u'组合持仓合约编码'),('Margin', u'投资者保证金'),('Direction', u'买卖'),('LegMultiple', u'单腿乘数'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('MarginRateByVolume', u'保证金率(按手数)'),('OpenDate', u'开仓日期'),('SettlementID', u'结算编号'),('InstrumentID', u'合约代码'),('TradeGroupID', u'成交组号'),('HedgeFlag', u'投机套保标志'),('LegID', u'单腿编号'),('ExchangeID', u'交易所代码'),('MarginRateByMoney', u'保证金率'),('TotalAmt', u'持仓量')]])
    def getval(self, n):
        if n in ['Direction', 'HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQrySettlementInfoField:
    def __init__(self, BrokerID="", InvestorID="", TradingDay=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.TradingDay=tou(TradingDay)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'TradingDay']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('TradingDay', u'交易日')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRemoveParkedOrderField:
    def __init__(self, ParkedOrderID="", BrokerID="", InvestorID=""):
        self.ParkedOrderID=tou(ParkedOrderID)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ParkedOrderID', 'BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ParkedOrderID', u'预埋报单编号'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingAccountReserveField:
    def __init__(self, Reserve=0, BrokerID="", InvestorID=""):
        self.Reserve=Reserve
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Reserve', 'BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Reserve', u'基本准备金'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingInstrumentMarginRateField:
    def __init__(self, InstrumentID="", ShortMarginRatioByVolume=0, LongMarginRatioByMoney=0, HedgeFlag='1', IsRelative=0, BrokerID="", InvestorID="", InvestorRange='1', LongMarginRatioByVolume=0, ShortMarginRatioByMoney=0):
        self.InstrumentID=tou(InstrumentID)
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.HedgeFlag=tou(HedgeFlag)
        self.IsRelative=IsRelative
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByVolume', 'LongMarginRatioByMoney', 'HedgeFlag', 'IsRelative', 'BrokerID', 'InvestorID', 'InvestorRange', 'LongMarginRatioByVolume', 'ShortMarginRatioByMoney']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByVolume', u'空头保证金费'),('LongMarginRatioByMoney', u'多头保证金率'),('HedgeFlag', u'投机套保标志'),('IsRelative', u'是否相对交易所收取'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('LongMarginRatioByVolume', u'多头保证金费'),('ShortMarginRatioByMoney', u'空头保证金率')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqCancelAccountField:
    def __init__(self, TradingDay="", DeviceID="", BrokerID="", ZipCode="", SessionID=0, IdentifiedCardNo="", IdCardType='0', MobilePhone="", BankID="", BankPwdFlag='0', OperNo="", BankAccount="", BankSecuAcc="", LastFragment='0', Gender='0', Address="", TradeDate="", MoneyAccountStatus='0', AccountID="", BankSerial="", CustomerName="", BankPassWord="", CashExchangeCode='1', Digest="", PlateSerial=0, Fax="", EMail="", TradeTime="", InstallID=0, SecuPwdFlag='0', VerifyCertNoFlag='0', CurrencyID="", BankSecuAccType='1', Password="", BankBranchID="", CountryCode="", BrokerBranchID="", UserID="", CustType='0', BrokerIDByBank="", TradeCode="", BankAccType='1', TID=0, Telephone=""):
        self.TradingDay=tou(TradingDay)
        self.DeviceID=tou(DeviceID)
        self.BrokerID=tou(BrokerID)
        self.ZipCode=tou(ZipCode)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.MobilePhone=tou(MobilePhone)
        self.BankID=tou(BankID)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.LastFragment=tou(LastFragment)
        self.Gender=tou(Gender)
        self.Address=tou(Address)
        self.TradeDate=tou(TradeDate)
        self.MoneyAccountStatus=tou(MoneyAccountStatus)
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.CashExchangeCode=tou(CashExchangeCode)
        self.Digest=tou(Digest)
        self.PlateSerial=PlateSerial
        self.Fax=tou(Fax)
        self.EMail=tou(EMail)
        self.TradeTime=tou(TradeTime)
        self.InstallID=InstallID
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.CurrencyID=tou(CurrencyID)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.Password=tou(Password)
        self.BankBranchID=tou(BankBranchID)
        self.CountryCode=tou(CountryCode)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.BankAccType=tou(BankAccType)
        self.TID=TID
        self.Telephone=tou(Telephone)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'Gender': {"'1'": '男', "'0'": '未知状态', "'2'": '女'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'CashExchangeCode': {"'1'": '汇', "'2'": '钞'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'MoneyAccountStatus': {"'1'": '销户', "'0'": '正常'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DeviceID', 'BrokerID', 'ZipCode', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'MobilePhone', 'BankID', 'BankPwdFlag', 'OperNo', 'BankAccount', 'BankSecuAcc', 'LastFragment', 'Gender', 'Address', 'TradeDate', 'MoneyAccountStatus', 'AccountID', 'BankSerial', 'CustomerName', 'BankPassWord', 'CashExchangeCode', 'Digest', 'PlateSerial', 'Fax', 'EMail', 'TradeTime', 'InstallID', 'SecuPwdFlag', 'VerifyCertNoFlag', 'CurrencyID', 'BankSecuAccType', 'Password', 'BankBranchID', 'CountryCode', 'BrokerBranchID', 'UserID', 'CustType', 'BrokerIDByBank', 'TradeCode', 'BankAccType', 'TID', 'Telephone']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易系统日期'),('DeviceID', u'渠道标志'),('BrokerID', u'期商代码'),('ZipCode', u'邮编'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('MobilePhone', u'手机'),('BankID', u'银行代码'),('BankPwdFlag', u'银行密码标志'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('BankSecuAcc', u'期货单位帐号'),('LastFragment', u'最后分片标志'),('Gender', u'性别'),('Address', u'地址'),('TradeDate', u'交易日期'),('MoneyAccountStatus', u'资金账户状态'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('CashExchangeCode', u'汇钞标志'),('Digest', u'摘要'),('PlateSerial', u'银期平台消息流水号'),('Fax', u'传真'),('EMail', u'电子邮件'),('TradeTime', u'交易时间'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('CurrencyID', u'币种代码'),('BankSecuAccType', u'期货单位帐号类型'),('Password', u'期货密码'),('BankBranchID', u'银行分支机构代码'),('CountryCode', u'国家代码'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('CustType', u'客户类型'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('BankAccType', u'银行帐号类型'),('TID', u'交易ID'),('Telephone', u'电话号码')]])
    def getval(self, n):
        if n in ['IdCardType', 'BankPwdFlag', 'LastFragment', 'Gender', 'MoneyAccountStatus', 'CashExchangeCode', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'CustType', 'BankAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcCFMMCBrokerKeyField:
    def __init__(self, CreateDate="", CreateTime="", KeyKind='R', CurrentKey="", BrokerID="", KeyID=0, ParticipantID=""):
        self.CreateDate=tou(CreateDate)
        self.CreateTime=tou(CreateTime)
        self.KeyKind=tou(KeyKind)
        self.CurrentKey=tou(CurrentKey)
        self.BrokerID=tou(BrokerID)
        self.KeyID=KeyID
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={'KeyKind': {"'A'": 'CFMMC自动更新', "'M'": 'CFMMC手动更新', "'R'": '主动请求更新'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CreateDate', 'CreateTime', 'KeyKind', 'CurrentKey', 'BrokerID', 'KeyID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CreateDate', u'密钥生成日期'),('CreateTime', u'密钥生成时间'),('KeyKind', u'动态密钥类型'),('CurrentKey', u'动态密钥'),('BrokerID', u'经纪公司代码'),('KeyID', u'密钥编号'),('ParticipantID', u'经纪公司统一编码')]])
    def getval(self, n):
        if n in ['KeyKind']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcAuthenticationInfoField:
    def __init__(self, AuthInfo="", IsResult=0, BrokerID="", UserProductInfo="", UserID=""):
        self.AuthInfo=tou(AuthInfo)
        self.IsResult=IsResult
        self.BrokerID=tou(BrokerID)
        self.UserProductInfo=tou(UserProductInfo)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AuthInfo', 'IsResult', 'BrokerID', 'UserProductInfo', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('AuthInfo', u'认证信息'),('IsResult', u'是否为认证结果'),('BrokerID', u'经纪公司代码'),('UserProductInfo', u'用户端产品信息'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQrySuperUserField:
    def __init__(self, UserID=""):
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataLastMatchField:
    def __init__(self, LastPrice=0, OpenInterest=0, Turnover=0, Volume=0):
        self.LastPrice=LastPrice
        self.OpenInterest=OpenInterest
        self.Turnover=Turnover
        self.Volume=Volume
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LastPrice', 'OpenInterest', 'Turnover', 'Volume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LastPrice', u'最新价'),('OpenInterest', u'持仓量'),('Turnover', u'成交金额'),('Volume', u'数量')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryExchangeOrderField:
    def __init__(self, ClientID="", ExchangeID="", ExchangeInstID="", TraderID="", ParticipantID=""):
        self.ClientID=tou(ClientID)
        self.ExchangeID=tou(ExchangeID)
        self.ExchangeInstID=tou(ExchangeInstID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ClientID', 'ExchangeID', 'ExchangeInstID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ClientID', u'客户代码'),('ExchangeID', u'交易所代码'),('ExchangeInstID', u'合约在交易所的代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInstrumentStatusField:
    def __init__(self, InstrumentID="", InstrumentStatus='0', SettlementGroupID="", TradingSegmentSN=0, ExchangeID="", ExchangeInstID="", EnterTime="", EnterReason='1'):
        self.InstrumentID=tou(InstrumentID)
        self.InstrumentStatus=tou(InstrumentStatus)
        self.SettlementGroupID=tou(SettlementGroupID)
        self.TradingSegmentSN=TradingSegmentSN
        self.ExchangeID=tou(ExchangeID)
        self.ExchangeInstID=tou(ExchangeInstID)
        self.EnterTime=tou(EnterTime)
        self.EnterReason=tou(EnterReason)
        self.vcmap={'InstrumentStatus': {"'1'": '非交易', "'6'": '收盘', "'0'": '开盘前', "'5'": '集合竞价撮合', "'4'": '集合竞价价格平衡', "'3'": '集合竞价报单', "'2'": '连续交易'}, 'EnterReason': {"'1'": '自动切换', "'3'": '熔断', "'2'": '手动切换'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InstrumentStatus', 'SettlementGroupID', 'TradingSegmentSN', 'ExchangeID', 'ExchangeInstID', 'EnterTime', 'EnterReason']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InstrumentStatus', u'合约交易状态'),('SettlementGroupID', u'结算组代码'),('TradingSegmentSN', u'交易阶段编号'),('ExchangeID', u'交易所代码'),('ExchangeInstID', u'合约在交易所的代码'),('EnterTime', u'进入本状态时间'),('EnterReason', u'进入本状态原因')]])
    def getval(self, n):
        if n in ['InstrumentStatus', 'EnterReason']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqAuthenticateField:
    def __init__(self, BrokerID="", UserProductInfo="", AuthCode="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserProductInfo=tou(UserProductInfo)
        self.AuthCode=tou(AuthCode)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserProductInfo', 'AuthCode', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserProductInfo', u'用户端产品信息'),('AuthCode', u'认证码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataField:
    def __init__(self, LowestPrice=0, ClosePrice=0, CurrDelta=0, HighestPrice=0, OpenPrice=0, OpenInterest=0, InstrumentID="", Turnover=0, ExchangeInstID="", UpdateMillisec=0, UpdateTime="", PreClosePrice=0, Volume=0, LastPrice=0, ExchangeID="", LowerLimitPrice=0, TradingDay="", SettlementPrice=0, PreOpenInterest=0, PreSettlementPrice=0, ActionDay="", PreDelta=0, UpperLimitPrice=0):
        self.LowestPrice=LowestPrice
        self.ClosePrice=ClosePrice
        self.CurrDelta=CurrDelta
        self.HighestPrice=HighestPrice
        self.OpenPrice=OpenPrice
        self.OpenInterest=OpenInterest
        self.InstrumentID=tou(InstrumentID)
        self.Turnover=Turnover
        self.ExchangeInstID=tou(ExchangeInstID)
        self.UpdateMillisec=UpdateMillisec
        self.UpdateTime=tou(UpdateTime)
        self.PreClosePrice=PreClosePrice
        self.Volume=Volume
        self.LastPrice=LastPrice
        self.ExchangeID=tou(ExchangeID)
        self.LowerLimitPrice=LowerLimitPrice
        self.TradingDay=tou(TradingDay)
        self.SettlementPrice=SettlementPrice
        self.PreOpenInterest=PreOpenInterest
        self.PreSettlementPrice=PreSettlementPrice
        self.ActionDay=tou(ActionDay)
        self.PreDelta=PreDelta
        self.UpperLimitPrice=UpperLimitPrice
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LowestPrice', 'ClosePrice', 'CurrDelta', 'HighestPrice', 'OpenPrice', 'OpenInterest', 'InstrumentID', 'Turnover', 'ExchangeInstID', 'UpdateMillisec', 'UpdateTime', 'PreClosePrice', 'Volume', 'LastPrice', 'ExchangeID', 'LowerLimitPrice', 'TradingDay', 'SettlementPrice', 'PreOpenInterest', 'PreSettlementPrice', 'ActionDay', 'PreDelta', 'UpperLimitPrice']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LowestPrice', u'最低价'),('ClosePrice', u'今收盘'),('CurrDelta', u'今虚实度'),('HighestPrice', u'最高价'),('OpenPrice', u'今开盘'),('OpenInterest', u'持仓量'),('InstrumentID', u'合约代码'),('Turnover', u'成交金额'),('ExchangeInstID', u'合约在交易所的代码'),('UpdateMillisec', u'最后修改毫秒'),('UpdateTime', u'最后修改时间'),('PreClosePrice', u'昨收盘'),('Volume', u'数量'),('LastPrice', u'最新价'),('ExchangeID', u'交易所代码'),('LowerLimitPrice', u'跌停板价'),('TradingDay', u'交易日'),('SettlementPrice', u'本次结算价'),('PreOpenInterest', u'昨持仓量'),('PreSettlementPrice', u'上次结算价'),('ActionDay', u'业务日期'),('PreDelta', u'昨虚实度'),('UpperLimitPrice', u'涨停板价')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInstrumentCommissionRateField:
    def __init__(self, BrokerID="", InvestorID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcCFMMCTradingAccountKeyField:
    def __init__(self, CurrentKey="", BrokerID="", AccountID="", KeyID=0, ParticipantID=""):
        self.CurrentKey=tou(CurrentKey)
        self.BrokerID=tou(BrokerID)
        self.AccountID=tou(AccountID)
        self.KeyID=KeyID
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CurrentKey', 'BrokerID', 'AccountID', 'KeyID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CurrentKey', u'动态密钥'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号'),('KeyID', u'密钥编号'),('ParticipantID', u'经纪公司统一编码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryExchangeSequenceField:
    def __init__(self, ExchangeID=""):
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInstrumentTradingRightField:
    def __init__(self, BrokerID="", InvestorID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspUserLoginField:
    def __init__(self, TradingDay="", SystemName="", SHFETime="", BrokerID="", FrontID=0, SessionID=0, FFEXTime="", CZCETime="", LoginTime="", DCETime="", MaxOrderRef="", UserID=""):
        self.TradingDay=tou(TradingDay)
        self.SystemName=tou(SystemName)
        self.SHFETime=tou(SHFETime)
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.FFEXTime=tou(FFEXTime)
        self.CZCETime=tou(CZCETime)
        self.LoginTime=tou(LoginTime)
        self.DCETime=tou(DCETime)
        self.MaxOrderRef=tou(MaxOrderRef)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'SystemName', 'SHFETime', 'BrokerID', 'FrontID', 'SessionID', 'FFEXTime', 'CZCETime', 'LoginTime', 'DCETime', 'MaxOrderRef', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易日'),('SystemName', u'交易系统名称'),('SHFETime', u'上期所时间'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('SessionID', u'会话编号'),('FFEXTime', u'中金所时间'),('CZCETime', u'郑商所时间'),('LoginTime', u'登录成功时间'),('DCETime', u'大商所时间'),('MaxOrderRef', u'最大报单引用'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingNoticeField:
    def __init__(self, SequenceSeries=0, SequenceNo=0, SendTime="", BrokerID="", InvestorID="", InvestorRange='1', UserID="", FieldContent=""):
        self.SequenceSeries=SequenceSeries
        self.SequenceNo=SequenceNo
        self.SendTime=tou(SendTime)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.UserID=tou(UserID)
        self.FieldContent=tou(FieldContent)
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SequenceSeries', 'SequenceNo', 'SendTime', 'BrokerID', 'InvestorID', 'InvestorRange', 'UserID', 'FieldContent']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('SequenceSeries', u'序列系列号'),('SequenceNo', u'序列号'),('SendTime', u'发送时间'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('UserID', u'用户代码'),('FieldContent', u'消息正文')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQueryBrokerDepositField:
    def __init__(self, BrokerID="", ExchangeID=""):
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInstrumentMarginRateField:
    def __init__(self, InstrumentID="", ShortMarginRatioByVolume=0, LongMarginRatioByMoney=0, HedgeFlag='1', IsRelative=0, BrokerID="", InvestorID="", InvestorRange='1', LongMarginRatioByVolume=0, ShortMarginRatioByMoney=0):
        self.InstrumentID=tou(InstrumentID)
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.HedgeFlag=tou(HedgeFlag)
        self.IsRelative=IsRelative
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByVolume', 'LongMarginRatioByMoney', 'HedgeFlag', 'IsRelative', 'BrokerID', 'InvestorID', 'InvestorRange', 'LongMarginRatioByVolume', 'ShortMarginRatioByMoney']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByVolume', u'空头保证金费'),('LongMarginRatioByMoney', u'多头保证金率'),('HedgeFlag', u'投机套保标志'),('IsRelative', u'是否相对交易所收取'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('LongMarginRatioByVolume', u'多头保证金费'),('ShortMarginRatioByMoney', u'空头保证金率')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcVerifyCustInfoField:
    def __init__(self, CustomerName="", IdCardType='0', IdentifiedCardNo="", CustType='0'):
        self.CustomerName=tou(CustomerName)
        self.IdCardType=tou(IdCardType)
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.CustType=tou(CustType)
        self.vcmap={'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CustomerName', 'IdCardType', 'IdentifiedCardNo', 'CustType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CustomerName', u'客户姓名'),('IdCardType', u'证件类型'),('IdentifiedCardNo', u'证件号码'),('CustType', u'客户类型')]])
    def getval(self, n):
        if n in ['IdCardType', 'CustType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcPositionProfitAlgorithmField:
    def __init__(self, Algorithm='1', Memo="", BrokerID="", AccountID=""):
        self.Algorithm=tou(Algorithm)
        self.Memo=tou(Memo)
        self.BrokerID=tou(BrokerID)
        self.AccountID=tou(AccountID)
        self.vcmap={'Algorithm': {"'4'": '浮盈浮亏都不计算', "'1'": '浮盈浮亏都计算', "'3'": '浮盈计，浮亏不计', "'2'": '浮盈不计，浮亏计'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Algorithm', 'Memo', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Algorithm', u'盈亏算法'),('Memo', u'备注'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in ['Algorithm']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcUserPasswordUpdateField:
    def __init__(self, NewPassword="", BrokerID="", UserID="", OldPassword=""):
        self.NewPassword=tou(NewPassword)
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.OldPassword=tou(OldPassword)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['NewPassword', 'BrokerID', 'UserID', 'OldPassword']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('NewPassword', u'新的口令'),('BrokerID', u'经纪公司代码'),('UserID', u'用户代码'),('OldPassword', u'原来的口令')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTradeField:
    def __init__(self, InstrumentID="", TradeTimeStart="", TradeID="", BrokerID="", InvestorID="", ExchangeID="", TradeTimeEnd=""):
        self.InstrumentID=tou(InstrumentID)
        self.TradeTimeStart=tou(TradeTimeStart)
        self.TradeID=tou(TradeID)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.TradeTimeEnd=tou(TradeTimeEnd)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'TradeTimeStart', 'TradeID', 'BrokerID', 'InvestorID', 'ExchangeID', 'TradeTimeEnd']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('TradeTimeStart', u'开始时间'),('TradeID', u'成交编号'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('TradeTimeEnd', u'结束时间')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcDepositResultInformField:
    def __init__(self, DepositSeqNo="", RequestID=0, ReturnCode="", DescrInfoForReturnCode="", BrokerID="", InvestorID="", Deposit=0):
        self.DepositSeqNo=tou(DepositSeqNo)
        self.RequestID=RequestID
        self.ReturnCode=tou(ReturnCode)
        self.DescrInfoForReturnCode=tou(DescrInfoForReturnCode)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.Deposit=Deposit
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['DepositSeqNo', 'RequestID', 'ReturnCode', 'DescrInfoForReturnCode', 'BrokerID', 'InvestorID', 'Deposit']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('DepositSeqNo', u'出入金流水号，该流水号为银期报盘返回的流水号'),('RequestID', u'请求编号'),('ReturnCode', u'返回代码'),('DescrInfoForReturnCode', u'返回码描述'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('Deposit', u'入金金额')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingAccountField:
    def __init__(self, WithdrawQuota=0, DeliveryMargin=0, PreMortgage=0, Balance=0, BrokerID="", Deposit=0, CashIn=0, Reserve=0, ExchangeMargin=0, CurrMargin=0, PositionProfit=0, FrozenMargin=0, Commission=0, Interest=0, Available=0, Credit=0, CloseProfit=0, ReserveBalance=0, ExchangeDeliveryMargin=0, FrozenCommission=0, InterestBase=0, TradingDay="", AccountID="", FrozenCash=0, SettlementID=0, Mortgage=0, PreCredit=0, PreDeposit=0, PreMargin=0, Withdraw=0, PreBalance=0):
        self.WithdrawQuota=WithdrawQuota
        self.DeliveryMargin=DeliveryMargin
        self.PreMortgage=PreMortgage
        self.Balance=Balance
        self.BrokerID=tou(BrokerID)
        self.Deposit=Deposit
        self.CashIn=CashIn
        self.Reserve=Reserve
        self.ExchangeMargin=ExchangeMargin
        self.CurrMargin=CurrMargin
        self.PositionProfit=PositionProfit
        self.FrozenMargin=FrozenMargin
        self.Commission=Commission
        self.Interest=Interest
        self.Available=Available
        self.Credit=Credit
        self.CloseProfit=CloseProfit
        self.ReserveBalance=ReserveBalance
        self.ExchangeDeliveryMargin=ExchangeDeliveryMargin
        self.FrozenCommission=FrozenCommission
        self.InterestBase=InterestBase
        self.TradingDay=tou(TradingDay)
        self.AccountID=tou(AccountID)
        self.FrozenCash=FrozenCash
        self.SettlementID=SettlementID
        self.Mortgage=Mortgage
        self.PreCredit=PreCredit
        self.PreDeposit=PreDeposit
        self.PreMargin=PreMargin
        self.Withdraw=Withdraw
        self.PreBalance=PreBalance
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['WithdrawQuota', 'DeliveryMargin', 'PreMortgage', 'Balance', 'BrokerID', 'Deposit', 'CashIn', 'Reserve', 'ExchangeMargin', 'CurrMargin', 'PositionProfit', 'FrozenMargin', 'Commission', 'Interest', 'Available', 'Credit', 'CloseProfit', 'ReserveBalance', 'ExchangeDeliveryMargin', 'FrozenCommission', 'InterestBase', 'TradingDay', 'AccountID', 'FrozenCash', 'SettlementID', 'Mortgage', 'PreCredit', 'PreDeposit', 'PreMargin', 'Withdraw', 'PreBalance']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('WithdrawQuota', u'可取资金'),('DeliveryMargin', u'投资者交割保证金'),('PreMortgage', u'上次质押金额'),('Balance', u'期货结算准备金'),('BrokerID', u'经纪公司代码'),('Deposit', u'入金金额'),('CashIn', u'资金差额'),('Reserve', u'基本准备金'),('ExchangeMargin', u'交易所保证金'),('CurrMargin', u'当前保证金总额'),('PositionProfit', u'持仓盈亏'),('FrozenMargin', u'冻结的保证金'),('Commission', u'手续费'),('Interest', u'利息收入'),('Available', u'可用资金'),('Credit', u'信用额度'),('CloseProfit', u'平仓盈亏'),('ReserveBalance', u'保底期货结算准备金'),('ExchangeDeliveryMargin', u'交易所交割保证金'),('FrozenCommission', u'冻结的手续费'),('InterestBase', u'利息基数'),('TradingDay', u'交易日'),('AccountID', u'投资者帐号'),('FrozenCash', u'冻结的资金'),('SettlementID', u'结算编号'),('Mortgage', u'质押金额'),('PreCredit', u'上次信用额度'),('PreDeposit', u'上次存款额'),('PreMargin', u'上次占用的保证金'),('Withdraw', u'出金金额'),('PreBalance', u'上次结算准备金')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerUserFunctionField:
    def __init__(self, BrokerID="", BrokerFunctionCode='1', UserID=""):
        self.BrokerID=tou(BrokerID)
        self.BrokerFunctionCode=tou(BrokerFunctionCode)
        self.UserID=tou(UserID)
        self.vcmap={'BrokerFunctionCode': {"'G'": '风险级别标准设置', "'F'": '发送业务通知', "'5'": '报单插入', "'E'": '同步动态令牌', "'z'": '数据导出', "'s'": '投资者信息查询', "'j'": '察看经纪公司资金权限', "'H'": '交易终端应急功能', "'a'": '系统功能：登入/登出/修改密码等', "'q'": '风险通知查询', "'d'": '交易功能：报单，撤单', "'2'": '变更用户口令', "'c'": '交易查询：如查成交，委托', "'b'": '基本查询：查询基础数据，如合约，交易所等常量', "'g'": '查询/管理：查询会话，踢人等', "'7'": '全部查询', "'1'": '强制用户登出', "'f'": '风险监控', "'p'": '用户事件查询', "'e'": '银期转账', "'l'": '报单查询', "'t'": '交易编码查询', "'i'": '风控通知发送', "'3'": '同步经纪公司数据', "'h'": '风控通知控制', "'r'": '出入金查询', "'w'": '权益反算', "'6'": '报单操作', "'A'": '风控指标设置', "'v'": '压力测试', "'k'": '资金查询', "'u'": '强平', "'4'": '批量同步经纪公司数据', "'o'": '行情查询', "'D'": '业务通知模板设置', "'y'": '风险预算', "'n'": '持仓查询', "'C'": '业务通知查询', "'x'": '净持仓保证金指标', "'m'": '成交查询', "'B'": '行情预警'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'BrokerFunctionCode', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('BrokerFunctionCode', u'经纪公司功能代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in ['BrokerFunctionCode']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingCodeField:
    def __init__(self, IsActive=0, ClientID="", ClientIDType='1', BrokerID="", InvestorID="", ExchangeID=""):
        self.IsActive=IsActive
        self.ClientID=tou(ClientID)
        self.ClientIDType=tou(ClientIDType)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={'ClientIDType': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IsActive', 'ClientID', 'ClientIDType', 'BrokerID', 'InvestorID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('IsActive', u'是否活跃'),('ClientID', u'客户代码'),('ClientIDType', u'交易编码类型'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in ['ClientIDType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingAccountPasswordUpdateField:
    def __init__(self, NewPassword="", BrokerID="", AccountID="", OldPassword=""):
        self.NewPassword=tou(NewPassword)
        self.BrokerID=tou(BrokerID)
        self.AccountID=tou(AccountID)
        self.OldPassword=tou(OldPassword)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['NewPassword', 'BrokerID', 'AccountID', 'OldPassword']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('NewPassword', u'新的口令'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号'),('OldPassword', u'原来的口令')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcVerifyFuturePasswordAndCustInfoField:
    def __init__(self, Password="", CustomerName="", CustType='0', AccountID="", IdentifiedCardNo="", IdCardType='0'):
        self.Password=tou(Password)
        self.CustomerName=tou(CustomerName)
        self.CustType=tou(CustType)
        self.AccountID=tou(AccountID)
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.vcmap={'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'CustomerName', 'CustType', 'AccountID', 'IdentifiedCardNo', 'IdCardType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'期货密码'),('CustomerName', u'客户姓名'),('CustType', u'客户类型'),('AccountID', u'投资者帐号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型')]])
    def getval(self, n):
        if n in ['CustType', 'IdCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTransferSerialField:
    def __init__(self, BankID="", BrokerID="", AccountID=""):
        self.BankID=tou(BankID)
        self.BrokerID=tou(BrokerID)
        self.AccountID=tou(AccountID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankID', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankID', u'银行编码'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcErrorConditionalOrderField:
    def __init__(self, InsertDate="", ZCETotalTradedVolume=0, Direction='0', OrderSubmitStatus='0', BrokerID="", SessionID=0, MinVolume=0, VolumeTotalOriginal=0, CancelTime="", StopPrice=0, InsertTime="", BrokerOrderSeq=0, ErrorMsg="", VolumeTraded=0, ExchangeInstID="", ParticipantID="", SettlementID=0, ActiveTime="", GTDDate="", OrderRef="", ContingentCondition='1', VolumeCondition='1', OrderType='0', OrderLocalID="", ActiveUserID="", NotifySequence=0, RelativeOrderSysID="", OrderPriceType='1', SuspendTime="", VolumeTotal=0, ClientID="", StatusMsg="", InstallID=0, ErrorID=0, InvestorID="", ForceCloseReason='0', TraderID="", InstrumentID="", FrontID=0, UserForceClose=0, OrderStatus='0', ExchangeID="", OrderSysID="", RequestID=0, IsAutoSuspend=0, IsSwapOrder=0, SequenceNo=0, CombOffsetFlag="", OrderSource='0', TradingDay="", ClearingPartID="", TimeCondition='1', UpdateTime="", BusinessUnit="", UserProductInfo="", LimitPrice=0, CombHedgeFlag="", ActiveTraderID="", UserID=""):
        self.InsertDate=tou(InsertDate)
        self.ZCETotalTradedVolume=ZCETotalTradedVolume
        self.Direction=tou(Direction)
        self.OrderSubmitStatus=tou(OrderSubmitStatus)
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.MinVolume=MinVolume
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.CancelTime=tou(CancelTime)
        self.StopPrice=StopPrice
        self.InsertTime=tou(InsertTime)
        self.BrokerOrderSeq=BrokerOrderSeq
        self.ErrorMsg=tou(ErrorMsg)
        self.VolumeTraded=VolumeTraded
        self.ExchangeInstID=tou(ExchangeInstID)
        self.ParticipantID=tou(ParticipantID)
        self.SettlementID=SettlementID
        self.ActiveTime=tou(ActiveTime)
        self.GTDDate=tou(GTDDate)
        self.OrderRef=tou(OrderRef)
        self.ContingentCondition=tou(ContingentCondition)
        self.VolumeCondition=tou(VolumeCondition)
        self.OrderType=tou(OrderType)
        self.OrderLocalID=tou(OrderLocalID)
        self.ActiveUserID=tou(ActiveUserID)
        self.NotifySequence=NotifySequence
        self.RelativeOrderSysID=tou(RelativeOrderSysID)
        self.OrderPriceType=tou(OrderPriceType)
        self.SuspendTime=tou(SuspendTime)
        self.VolumeTotal=VolumeTotal
        self.ClientID=tou(ClientID)
        self.StatusMsg=tou(StatusMsg)
        self.InstallID=InstallID
        self.ErrorID=ErrorID
        self.InvestorID=tou(InvestorID)
        self.ForceCloseReason=tou(ForceCloseReason)
        self.TraderID=tou(TraderID)
        self.InstrumentID=tou(InstrumentID)
        self.FrontID=FrontID
        self.UserForceClose=UserForceClose
        self.OrderStatus=tou(OrderStatus)
        self.ExchangeID=tou(ExchangeID)
        self.OrderSysID=tou(OrderSysID)
        self.RequestID=RequestID
        self.IsAutoSuspend=IsAutoSuspend
        self.IsSwapOrder=IsSwapOrder
        self.SequenceNo=SequenceNo
        self.CombOffsetFlag=tou(CombOffsetFlag)
        self.OrderSource=tou(OrderSource)
        self.TradingDay=tou(TradingDay)
        self.ClearingPartID=tou(ClearingPartID)
        self.TimeCondition=tou(TimeCondition)
        self.UpdateTime=tou(UpdateTime)
        self.BusinessUnit=tou(BusinessUnit)
        self.UserProductInfo=tou(UserProductInfo)
        self.LimitPrice=LimitPrice
        self.CombHedgeFlag=tou(CombHedgeFlag)
        self.ActiveTraderID=tou(ActiveTraderID)
        self.UserID=tou(UserID)
        self.vcmap={'VolumeCondition': {"'1'": '任何数量', "'3'": '全部数量', "'2'": '最小数量'}, 'OrderPriceType': {"'1'": '任意价', "'F'": '买一价浮动上浮3个ticks', "'E'": '买一价浮动上浮2个ticks', "'4'": '最新价', "'3'": '最优价', "'2'": '限价', "'7'": '最新价浮动上浮3个ticks', "'A'": '卖一价浮动上浮2个ticks', "'6'": '最新价浮动上浮2个ticks', "'5'": '最新价浮动上浮1个ticks', "'D'": '买一价浮动上浮1个ticks', "'9'": '卖一价浮动上浮1个ticks', "'C'": '买一价', "'8'": '卖一价', "'B'": '卖一价浮动上浮3个ticks'}, 'OrderSource': {"'1'": '来自管理员', "'0'": '来自参与者'}, 'ContingentCondition': {"'1'": '立即', "'F'": '买一价小于条件价', "'E'": '买一价大于等于条件价', "'4'": '预埋单', "'3'": '止赢', "'H'": '买一价小于等于条件价', "'2'": '止损', "'7'": '最新价小于条件价', "'A'": '卖一价大于等于条件价', "'6'": '最新价大于等于条件价', "'5'": '最新价大于条件价', "'D'": '买一价大于条件价', "'9'": '卖一价大于条件价', "'C'": '卖一价小于等于条件价', "'8'": '最新价小于等于条件价', "'B'": '卖一价小于条件价'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'OrderSubmitStatus': {"'1'": '撤单已经提交', "'6'": '改单已经被拒绝', "'0'": '已经提交', "'5'": '撤单已经被拒绝', "'4'": '报单已经被拒绝', "'3'": '已经接受', "'2'": '修改已经提交'}, 'OrderStatus': {"'1'": '部分成交还在队列中', "'0'": '全部成交', "'5'": '撤单', "'4'": '未成交不在队列中', "'3'": '未成交还在队列中', "'2'": '部分成交不在队列中', "'c'": '已触发', "'a'": '未知', "'b'": '尚未触发'}, 'OrderType': {"'1'": '报价衍生', "'0'": '正常', "'5'": '互换单', "'4'": '条件单', "'3'": '组合报单', "'2'": '组合衍生'}, 'ForceCloseReason': {"'7'": '自然人临近交割', "'1'": '资金不足', "'6'": '其它', "'0'": '非强平', "'5'": '违规', "'4'": '持仓非整数倍', "'3'": '会员超仓', "'2'": '客户超仓'}, 'TimeCondition': {"'1'": '立即完成，否则撤销', "'6'": '集合竞价有效', "'5'": '撤销前有效', "'4'": '指定日期前有效', "'3'": '当日有效', "'2'": '本节有效'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InsertDate', 'ZCETotalTradedVolume', 'Direction', 'OrderSubmitStatus', 'BrokerID', 'SessionID', 'MinVolume', 'VolumeTotalOriginal', 'CancelTime', 'StopPrice', 'InsertTime', 'BrokerOrderSeq', 'ErrorMsg', 'VolumeTraded', 'ExchangeInstID', 'ParticipantID', 'SettlementID', 'ActiveTime', 'GTDDate', 'OrderRef', 'ContingentCondition', 'VolumeCondition', 'OrderType', 'OrderLocalID', 'ActiveUserID', 'NotifySequence', 'RelativeOrderSysID', 'OrderPriceType', 'SuspendTime', 'VolumeTotal', 'ClientID', 'StatusMsg', 'InstallID', 'ErrorID', 'InvestorID', 'ForceCloseReason', 'TraderID', 'InstrumentID', 'FrontID', 'UserForceClose', 'OrderStatus', 'ExchangeID', 'OrderSysID', 'RequestID', 'IsAutoSuspend', 'IsSwapOrder', 'SequenceNo', 'CombOffsetFlag', 'OrderSource', 'TradingDay', 'ClearingPartID', 'TimeCondition', 'UpdateTime', 'BusinessUnit', 'UserProductInfo', 'LimitPrice', 'CombHedgeFlag', 'ActiveTraderID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InsertDate', u'报单日期'),('ZCETotalTradedVolume', u'郑商所成交数量'),('Direction', u'买卖方向'),('OrderSubmitStatus', u'报单提交状态'),('BrokerID', u'经纪公司代码'),('SessionID', u'会话编号'),('MinVolume', u'最小成交量'),('VolumeTotalOriginal', u'数量'),('CancelTime', u'撤销时间'),('StopPrice', u'止损价'),('InsertTime', u'委托时间'),('BrokerOrderSeq', u'经纪公司报单编号'),('ErrorMsg', u'错误信息'),('VolumeTraded', u'今成交数量'),('ExchangeInstID', u'合约在交易所的代码'),('ParticipantID', u'会员代码'),('SettlementID', u'结算编号'),('ActiveTime', u'激活时间'),('GTDDate', u'GTD日期'),('OrderRef', u'报单引用'),('ContingentCondition', u'触发条件'),('VolumeCondition', u'成交量类型'),('OrderType', u'报单类型'),('OrderLocalID', u'本地报单编号'),('ActiveUserID', u'操作用户代码'),('NotifySequence', u'报单提示序号'),('RelativeOrderSysID', u'相关报单'),('OrderPriceType', u'报单价格条件'),('SuspendTime', u'挂起时间'),('VolumeTotal', u'剩余数量'),('ClientID', u'客户代码'),('StatusMsg', u'状态信息'),('InstallID', u'安装编号'),('ErrorID', u'错误代码'),('InvestorID', u'投资者代码'),('ForceCloseReason', u'强平原因'),('TraderID', u'交易所交易员代码'),('InstrumentID', u'合约代码'),('FrontID', u'前置编号'),('UserForceClose', u'用户强评标志'),('OrderStatus', u'报单状态'),('ExchangeID', u'交易所代码'),('OrderSysID', u'报单编号'),('RequestID', u'请求编号'),('IsAutoSuspend', u'自动挂起标志'),('IsSwapOrder', u'互换单标志'),('SequenceNo', u'序号'),('CombOffsetFlag', u'组合开平标志'),('OrderSource', u'报单来源'),('TradingDay', u'交易日'),('ClearingPartID', u'结算会员编号'),('TimeCondition', u'有效期类型'),('UpdateTime', u'最后修改时间'),('BusinessUnit', u'业务单元'),('UserProductInfo', u'用户端产品信息'),('LimitPrice', u'价格'),('CombHedgeFlag', u'组合投机套保标志'),('ActiveTraderID', u'最后修改交易所交易员代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in ['Direction', 'OrderSubmitStatus', 'ContingentCondition', 'VolumeCondition', 'OrderType', 'OrderPriceType', 'ForceCloseReason', 'OrderStatus', 'OrderSource', 'TimeCondition']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQrySyncStatusField:
    def __init__(self, TradingDay=""):
        self.TradingDay=tou(TradingDay)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易日')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryNoticeField:
    def __init__(self, BrokerID=""):
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingInstrumentCommissionRateField:
    def __init__(self, CloseTodayRatioByMoney=0, InstrumentID="", OpenRatioByVolume=0, CloseTodayRatioByVolume=0, OpenRatioByMoney=0, CloseRatioByVolume=0, BrokerID="", InvestorID="", InvestorRange='1', CloseRatioByMoney=0):
        self.CloseTodayRatioByMoney=CloseTodayRatioByMoney
        self.InstrumentID=tou(InstrumentID)
        self.OpenRatioByVolume=OpenRatioByVolume
        self.CloseTodayRatioByVolume=CloseTodayRatioByVolume
        self.OpenRatioByMoney=OpenRatioByMoney
        self.CloseRatioByVolume=CloseRatioByVolume
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.CloseRatioByMoney=CloseRatioByMoney
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CloseTodayRatioByMoney', 'InstrumentID', 'OpenRatioByVolume', 'CloseTodayRatioByVolume', 'OpenRatioByMoney', 'CloseRatioByVolume', 'BrokerID', 'InvestorID', 'InvestorRange', 'CloseRatioByMoney']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CloseTodayRatioByMoney', u'平今手续费率'),('InstrumentID', u'合约代码'),('OpenRatioByVolume', u'开仓手续费'),('CloseTodayRatioByVolume', u'平今手续费'),('OpenRatioByMoney', u'开仓手续费率'),('CloseRatioByVolume', u'平仓手续费'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('CloseRatioByMoney', u'平仓手续费率')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferQryDetailReqField:
    def __init__(self, FutureAccount=""):
        self.FutureAccount=tou(FutureAccount)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FutureAccount', u'期货资金账户')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerUserField:
    def __init__(self, IsActive=0, UserName="", BrokerID="", UserType='0', UserID="", IsUsingOTP=0):
        self.IsActive=IsActive
        self.UserName=tou(UserName)
        self.BrokerID=tou(BrokerID)
        self.UserType=tou(UserType)
        self.UserID=tou(UserID)
        self.IsUsingOTP=IsUsingOTP
        self.vcmap={'UserType': {"'1'": '操作员', "'0'": '投资者', "'2'": '管理员'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IsActive', 'UserName', 'BrokerID', 'UserType', 'UserID', 'IsUsingOTP']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('IsActive', u'是否活跃'),('UserName', u'用户名称'),('BrokerID', u'经纪公司代码'),('UserType', u'用户类型'),('UserID', u'用户代码'),('IsUsingOTP', u'是否使用令牌')]])
    def getval(self, n):
        if n in ['UserType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspFutureSignOutField:
    def __init__(self, TradeTime="", DeviceID="", ErrorID=0, InstallID=0, BrokerID="", SessionID=0, BankID="", CurrencyID="", ErrorMsg="", OperNo="", Digest="", LastFragment='0', RequestID=0, TradeDate="", UserID="", TradingDay="", BankSerial="", BrokerIDByBank="", TradeCode="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.OperNo=tou(OperNo)
        self.Digest=tou(Digest)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeTime', 'DeviceID', 'ErrorID', 'InstallID', 'BrokerID', 'SessionID', 'BankID', 'CurrencyID', 'ErrorMsg', 'OperNo', 'Digest', 'LastFragment', 'RequestID', 'TradeDate', 'UserID', 'TradingDay', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('OperNo', u'交易柜员'),('Digest', u'摘要'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('TradingDay', u'交易系统日期'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcCancelAccountField:
    def __init__(self, TradingDay="", DeviceID="", ErrorID=0, BrokerID="", ZipCode="", SessionID=0, IdentifiedCardNo="", IdCardType='0', MobilePhone="", BankID="", BankPwdFlag='0', OperNo="", BankAccount="", BankSecuAcc="", LastFragment='0', Gender='0', Address="", TradeDate="", MoneyAccountStatus='0', AccountID="", BankSerial="", CustomerName="", BankPassWord="", CashExchangeCode='1', Digest="", PlateSerial=0, Fax="", EMail="", TradeTime="", InstallID=0, SecuPwdFlag='0', VerifyCertNoFlag='0', CurrencyID="", ErrorMsg="", BankSecuAccType='1', Password="", BankBranchID="", CountryCode="", BrokerBranchID="", UserID="", CustType='0', BrokerIDByBank="", TradeCode="", BankAccType='1', TID=0, Telephone=""):
        self.TradingDay=tou(TradingDay)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.BrokerID=tou(BrokerID)
        self.ZipCode=tou(ZipCode)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.MobilePhone=tou(MobilePhone)
        self.BankID=tou(BankID)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.LastFragment=tou(LastFragment)
        self.Gender=tou(Gender)
        self.Address=tou(Address)
        self.TradeDate=tou(TradeDate)
        self.MoneyAccountStatus=tou(MoneyAccountStatus)
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.CashExchangeCode=tou(CashExchangeCode)
        self.Digest=tou(Digest)
        self.PlateSerial=PlateSerial
        self.Fax=tou(Fax)
        self.EMail=tou(EMail)
        self.TradeTime=tou(TradeTime)
        self.InstallID=InstallID
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.Password=tou(Password)
        self.BankBranchID=tou(BankBranchID)
        self.CountryCode=tou(CountryCode)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.BankAccType=tou(BankAccType)
        self.TID=TID
        self.Telephone=tou(Telephone)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'Gender': {"'1'": '男', "'0'": '未知状态', "'2'": '女'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'CashExchangeCode': {"'1'": '汇', "'2'": '钞'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'MoneyAccountStatus': {"'1'": '销户', "'0'": '正常'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DeviceID', 'ErrorID', 'BrokerID', 'ZipCode', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'MobilePhone', 'BankID', 'BankPwdFlag', 'OperNo', 'BankAccount', 'BankSecuAcc', 'LastFragment', 'Gender', 'Address', 'TradeDate', 'MoneyAccountStatus', 'AccountID', 'BankSerial', 'CustomerName', 'BankPassWord', 'CashExchangeCode', 'Digest', 'PlateSerial', 'Fax', 'EMail', 'TradeTime', 'InstallID', 'SecuPwdFlag', 'VerifyCertNoFlag', 'CurrencyID', 'ErrorMsg', 'BankSecuAccType', 'Password', 'BankBranchID', 'CountryCode', 'BrokerBranchID', 'UserID', 'CustType', 'BrokerIDByBank', 'TradeCode', 'BankAccType', 'TID', 'Telephone']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易系统日期'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('BrokerID', u'期商代码'),('ZipCode', u'邮编'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('MobilePhone', u'手机'),('BankID', u'银行代码'),('BankPwdFlag', u'银行密码标志'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('BankSecuAcc', u'期货单位帐号'),('LastFragment', u'最后分片标志'),('Gender', u'性别'),('Address', u'地址'),('TradeDate', u'交易日期'),('MoneyAccountStatus', u'资金账户状态'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('CashExchangeCode', u'汇钞标志'),('Digest', u'摘要'),('PlateSerial', u'银期平台消息流水号'),('Fax', u'传真'),('EMail', u'电子邮件'),('TradeTime', u'交易时间'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankSecuAccType', u'期货单位帐号类型'),('Password', u'期货密码'),('BankBranchID', u'银行分支机构代码'),('CountryCode', u'国家代码'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('CustType', u'客户类型'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('BankAccType', u'银行帐号类型'),('TID', u'交易ID'),('Telephone', u'电话号码')]])
    def getval(self, n):
        if n in ['IdCardType', 'BankPwdFlag', 'LastFragment', 'Gender', 'MoneyAccountStatus', 'CashExchangeCode', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'CustType', 'BankAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInvestorPositionCombineDetailField:
    def __init__(self, BrokerID="", InvestorID="", CombInstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.CombInstrumentID=tou(CombInstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'CombInstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('CombInstrumentID', u'组合持仓合约编码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerWithdrawAlgorithmField:
    def __init__(self, UsingRatio=0, AllWithoutTrade='0', AvailIncludeCloseProfit='0', IncludeCloseProfit='0', BrokerID="", WithdrawAlgorithm='1', IsBrokerUserEvent=0):
        self.UsingRatio=UsingRatio
        self.AllWithoutTrade=tou(AllWithoutTrade)
        self.AvailIncludeCloseProfit=tou(AvailIncludeCloseProfit)
        self.IncludeCloseProfit=tou(IncludeCloseProfit)
        self.BrokerID=tou(BrokerID)
        self.WithdrawAlgorithm=tou(WithdrawAlgorithm)
        self.IsBrokerUserEvent=IsBrokerUserEvent
        self.vcmap={'IncludeCloseProfit': {"'0'": '包含平仓盈利', "'2'": '不包含平仓盈利'}, 'AllWithoutTrade': {"'3'": '无仓不受可提比例限制', "'0'": '无仓无成交不受可提比例限制', "'2'": '受可提比例限制'}, 'AvailIncludeCloseProfit': {"'0'": '包含平仓盈利', "'2'": '不包含平仓盈利'}, 'WithdrawAlgorithm': {"'4'": '浮盈浮亏都不计算', "'1'": '浮盈浮亏都计算', "'3'": '浮盈计，浮亏不计', "'2'": '浮盈不计，浮亏计'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UsingRatio', 'AllWithoutTrade', 'AvailIncludeCloseProfit', 'IncludeCloseProfit', 'BrokerID', 'WithdrawAlgorithm', 'IsBrokerUserEvent']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('UsingRatio', u'资金使用率'),('AllWithoutTrade', u'本日无仓且无成交客户是否受可提比例限制'),('AvailIncludeCloseProfit', u'可用是否包含平仓盈利'),('IncludeCloseProfit', u'可提是否包含平仓盈利'),('BrokerID', u'经纪公司代码'),('WithdrawAlgorithm', u'可提资金算法'),('IsBrokerUserEvent', u'是否启用用户事件')]])
    def getval(self, n):
        if n in ['AllWithoutTrade', 'AvailIncludeCloseProfit', 'IncludeCloseProfit', 'WithdrawAlgorithm']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcEWarrantOffsetField:
    def __init__(self, InstrumentID="", InvestorID="", Volume=0, HedgeFlag='1', Direction='0', BrokerID="", TradingDay="", ExchangeID=""):
        self.InstrumentID=tou(InstrumentID)
        self.InvestorID=tou(InvestorID)
        self.Volume=Volume
        self.HedgeFlag=tou(HedgeFlag)
        self.Direction=tou(Direction)
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={'Direction': {"'1'": '卖', "'0'": '买'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'Volume', 'HedgeFlag', 'Direction', 'BrokerID', 'TradingDay', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('Volume', u'数量'),('HedgeFlag', u'投机套保标志'),('Direction', u'买卖方向'),('BrokerID', u'经纪公司代码'),('TradingDay', u'交易日期'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'Direction']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcNotifyQueryAccountField:
    def __init__(self, BankPwdFlag='0', TradingDay="", TradeTime="", FutureSerial=0, DeviceID="", InstallID=0, BrokerID="", SessionID=0, IdentifiedCardNo="", AccountID="", SecuPwdFlag='0', BankFetchAmount=0, VerifyCertNoFlag='0', BankUseAmount=0, BankID="", CurrencyID="", ErrorMsg="", BankSecuAccType='1', OperNo="", BankAccount="", Digest="", BankSecuAcc="", Password="", LastFragment='0', RequestID=0, ErrorID=0, BankAccType='1', TradeDate="", UserID="", CustType='0', IdCardType='0', BankSerial="", BrokerIDByBank="", TradeCode="", CustomerName="", BankPassWord="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.BankPwdFlag=tou(BankPwdFlag)
        self.TradingDay=tou(TradingDay)
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.DeviceID=tou(DeviceID)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.AccountID=tou(AccountID)
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.BankFetchAmount=BankFetchAmount
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.BankUseAmount=BankUseAmount
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.Digest=tou(Digest)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.ErrorID=ErrorID
        self.BankAccType=tou(BankAccType)
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.IdCardType=tou(IdCardType)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankPwdFlag', 'TradingDay', 'TradeTime', 'FutureSerial', 'DeviceID', 'InstallID', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'AccountID', 'SecuPwdFlag', 'BankFetchAmount', 'VerifyCertNoFlag', 'BankUseAmount', 'BankID', 'CurrencyID', 'ErrorMsg', 'BankSecuAccType', 'OperNo', 'BankAccount', 'Digest', 'BankSecuAcc', 'Password', 'LastFragment', 'RequestID', 'ErrorID', 'BankAccType', 'TradeDate', 'UserID', 'CustType', 'IdCardType', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'CustomerName', 'BankPassWord', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankPwdFlag', u'银行密码标志'),('TradingDay', u'交易系统日期'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('DeviceID', u'渠道标志'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('AccountID', u'投资者帐号'),('SecuPwdFlag', u'期货资金密码核对标志'),('BankFetchAmount', u'银行可取金额'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('BankUseAmount', u'银行可用金额'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankSecuAccType', u'期货单位帐号类型'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('Digest', u'摘要'),('BankSecuAcc', u'期货单位帐号'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('ErrorID', u'错误代码'),('BankAccType', u'银行帐号类型'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('CustType', u'客户类型'),('IdCardType', u'证件类型'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['BankPwdFlag', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'LastFragment', 'BankAccType', 'CustType', 'IdCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerTradingAlgosField:
    def __init__(self, HandleTradingAccountAlgoID='1', InstrumentID="", HandlePositionAlgoID='1', BrokerID="", ExchangeID="", FindMarginRateAlgoID='1'):
        self.HandleTradingAccountAlgoID=tou(HandleTradingAccountAlgoID)
        self.InstrumentID=tou(InstrumentID)
        self.HandlePositionAlgoID=tou(HandlePositionAlgoID)
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.FindMarginRateAlgoID=tou(FindMarginRateAlgoID)
        self.vcmap={'HandleTradingAccountAlgoID': {"'1'": '基本', "'3'": '郑州商品交易所', "'2'": '大连商品交易所'}, 'FindMarginRateAlgoID': {"'1'": '基本', "'3'": '郑州商品交易所', "'2'": '大连商品交易所'}, 'HandlePositionAlgoID': {"'1'": '基本', "'3'": '郑州商品交易所', "'2'": '大连商品交易所'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['HandleTradingAccountAlgoID', 'InstrumentID', 'HandlePositionAlgoID', 'BrokerID', 'ExchangeID', 'FindMarginRateAlgoID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('HandleTradingAccountAlgoID', u'资金处理算法编号'),('InstrumentID', u'合约代码'),('HandlePositionAlgoID', u'持仓处理算法编号'),('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码'),('FindMarginRateAlgoID', u'寻找保证金率算法编号')]])
    def getval(self, n):
        if n in ['HandleTradingAccountAlgoID', 'HandlePositionAlgoID', 'FindMarginRateAlgoID']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqQueryAccountField:
    def __init__(self, BankPwdFlag='0', TradingDay="", TradeTime="", FutureSerial=0, DeviceID="", InstallID=0, BrokerID="", SessionID=0, IdentifiedCardNo="", AccountID="", SecuPwdFlag='0', VerifyCertNoFlag='0', BankID="", CurrencyID="", BankSecuAccType='1', OperNo="", BankAccount="", Digest="", BankSecuAcc="", Password="", LastFragment='0', RequestID=0, BankAccType='1', TradeDate="", UserID="", CustType='0', IdCardType='0', BankSerial="", BrokerIDByBank="", TradeCode="", CustomerName="", BankPassWord="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.BankPwdFlag=tou(BankPwdFlag)
        self.TradingDay=tou(TradingDay)
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.DeviceID=tou(DeviceID)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.AccountID=tou(AccountID)
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.Digest=tou(Digest)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.BankAccType=tou(BankAccType)
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.IdCardType=tou(IdCardType)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankPwdFlag', 'TradingDay', 'TradeTime', 'FutureSerial', 'DeviceID', 'InstallID', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'AccountID', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankID', 'CurrencyID', 'BankSecuAccType', 'OperNo', 'BankAccount', 'Digest', 'BankSecuAcc', 'Password', 'LastFragment', 'RequestID', 'BankAccType', 'TradeDate', 'UserID', 'CustType', 'IdCardType', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'CustomerName', 'BankPassWord', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankPwdFlag', u'银行密码标志'),('TradingDay', u'交易系统日期'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('DeviceID', u'渠道标志'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('AccountID', u'投资者帐号'),('SecuPwdFlag', u'期货资金密码核对标志'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('BankSecuAccType', u'期货单位帐号类型'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('Digest', u'摘要'),('BankSecuAcc', u'期货单位帐号'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BankAccType', u'银行帐号类型'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('CustType', u'客户类型'),('IdCardType', u'证件类型'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['BankPwdFlag', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'LastFragment', 'BankAccType', 'CustType', 'IdCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspFutureSignInField:
    def __init__(self, TradeTime="", DeviceID="", ErrorID=0, InstallID=0, BrokerID="", SessionID=0, BankID="", CurrencyID="", ErrorMsg="", PinKey="", OperNo="", MacKey="", Digest="", LastFragment='0', RequestID=0, TradeDate="", UserID="", TradingDay="", BankSerial="", BrokerIDByBank="", TradeCode="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.PinKey=tou(PinKey)
        self.OperNo=tou(OperNo)
        self.MacKey=tou(MacKey)
        self.Digest=tou(Digest)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeTime', 'DeviceID', 'ErrorID', 'InstallID', 'BrokerID', 'SessionID', 'BankID', 'CurrencyID', 'ErrorMsg', 'PinKey', 'OperNo', 'MacKey', 'Digest', 'LastFragment', 'RequestID', 'TradeDate', 'UserID', 'TradingDay', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('PinKey', u'PIN密钥'),('OperNo', u'交易柜员'),('MacKey', u'MAC密钥'),('Digest', u'摘要'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('TradingDay', u'交易系统日期'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryLinkManField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTradingNoticeField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryBrokerUserEventField:
    def __init__(self, BrokerID="", UserEventType='1', UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserEventType=tou(UserEventType)
        self.UserID=tou(UserID)
        self.vcmap={'UserEventType': {"'1'": '登录', "'6'": '客户端认证', "'5'": '修改密码', "'4'": '交易失败', "'9'": '其他', "'3'": '交易成功', "'2'": '登出'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserEventType', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserEventType', u'用户事件类型'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in ['UserEventType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcLoadSettlementInfoField:
    def __init__(self, BrokerID=""):
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataUpdateTimeField:
    def __init__(self, UpdateTime="", InstrumentID="", ActionDay="", UpdateMillisec=0):
        self.UpdateTime=tou(UpdateTime)
        self.InstrumentID=tou(InstrumentID)
        self.ActionDay=tou(ActionDay)
        self.UpdateMillisec=UpdateMillisec
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UpdateTime', 'InstrumentID', 'ActionDay', 'UpdateMillisec']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('UpdateTime', u'最后修改时间'),('InstrumentID', u'合约代码'),('ActionDay', u'业务日期'),('UpdateMillisec', u'最后修改毫秒')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataStaticField:
    def __init__(self, LowestPrice=0, ClosePrice=0, UpperLimitPrice=0, HighestPrice=0, LowerLimitPrice=0, OpenPrice=0, SettlementPrice=0, CurrDelta=0):
        self.LowestPrice=LowestPrice
        self.ClosePrice=ClosePrice
        self.UpperLimitPrice=UpperLimitPrice
        self.HighestPrice=HighestPrice
        self.LowerLimitPrice=LowerLimitPrice
        self.OpenPrice=OpenPrice
        self.SettlementPrice=SettlementPrice
        self.CurrDelta=CurrDelta
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LowestPrice', 'ClosePrice', 'UpperLimitPrice', 'HighestPrice', 'LowerLimitPrice', 'OpenPrice', 'SettlementPrice', 'CurrDelta']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LowestPrice', u'最低价'),('ClosePrice', u'今收盘'),('UpperLimitPrice', u'涨停板价'),('HighestPrice', u'最高价'),('LowerLimitPrice', u'跌停板价'),('OpenPrice', u'今开盘'),('SettlementPrice', u'本次结算价'),('CurrDelta', u'今虚实度')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcUserLogoutField:
    def __init__(self, BrokerID="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcDepthMarketDataField:
    def __init__(self, ClosePrice=0, CurrDelta=0, HighestPrice=0, UpperLimitPrice=0, Turnover=0, ExchangeInstID="", BidVolume1=0, BidVolume3=0, BidVolume2=0, BidVolume5=0, BidVolume4=0, LastPrice=0, LowerLimitPrice=0, SettlementPrice=0, PreOpenInterest=0, PreSettlementPrice=0, AveragePrice=0, AskVolume5=0, AskVolume4=0, AskVolume3=0, AskVolume2=0, AskVolume1=0, LowestPrice=0, OpenPrice=0, OpenInterest=0, InstrumentID="", PreClosePrice=0, ExchangeID="", UpdateMillisec=0, ActionDay="", Volume=0, TradingDay="", PreDelta=0, UpdateTime="", BidPrice5=0, BidPrice4=0, BidPrice3=0, BidPrice2=0, BidPrice1=0, AskPrice5=0, AskPrice4=0, AskPrice1=0, AskPrice3=0, AskPrice2=0):
        self.ClosePrice=ClosePrice
        self.CurrDelta=CurrDelta
        self.HighestPrice=HighestPrice
        self.UpperLimitPrice=UpperLimitPrice
        self.Turnover=Turnover
        self.ExchangeInstID=tou(ExchangeInstID)
        self.BidVolume1=BidVolume1
        self.BidVolume3=BidVolume3
        self.BidVolume2=BidVolume2
        self.BidVolume5=BidVolume5
        self.BidVolume4=BidVolume4
        self.LastPrice=LastPrice
        self.LowerLimitPrice=LowerLimitPrice
        self.SettlementPrice=SettlementPrice
        self.PreOpenInterest=PreOpenInterest
        self.PreSettlementPrice=PreSettlementPrice
        self.AveragePrice=AveragePrice
        self.AskVolume5=AskVolume5
        self.AskVolume4=AskVolume4
        self.AskVolume3=AskVolume3
        self.AskVolume2=AskVolume2
        self.AskVolume1=AskVolume1
        self.LowestPrice=LowestPrice
        self.OpenPrice=OpenPrice
        self.OpenInterest=OpenInterest
        self.InstrumentID=tou(InstrumentID)
        self.PreClosePrice=PreClosePrice
        self.ExchangeID=tou(ExchangeID)
        self.UpdateMillisec=UpdateMillisec
        self.ActionDay=tou(ActionDay)
        self.Volume=Volume
        self.TradingDay=tou(TradingDay)
        self.PreDelta=PreDelta
        self.UpdateTime=tou(UpdateTime)
        self.BidPrice5=BidPrice5
        self.BidPrice4=BidPrice4
        self.BidPrice3=BidPrice3
        self.BidPrice2=BidPrice2
        self.BidPrice1=BidPrice1
        self.AskPrice5=AskPrice5
        self.AskPrice4=AskPrice4
        self.AskPrice1=AskPrice1
        self.AskPrice3=AskPrice3
        self.AskPrice2=AskPrice2
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ClosePrice', 'CurrDelta', 'HighestPrice', 'UpperLimitPrice', 'Turnover', 'ExchangeInstID', 'BidVolume1', 'BidVolume3', 'BidVolume2', 'BidVolume5', 'BidVolume4', 'LastPrice', 'LowerLimitPrice', 'SettlementPrice', 'PreOpenInterest', 'PreSettlementPrice', 'AveragePrice', 'AskVolume5', 'AskVolume4', 'AskVolume3', 'AskVolume2', 'AskVolume1', 'LowestPrice', 'OpenPrice', 'OpenInterest', 'InstrumentID', 'PreClosePrice', 'ExchangeID', 'UpdateMillisec', 'ActionDay', 'Volume', 'TradingDay', 'PreDelta', 'UpdateTime', 'BidPrice5', 'BidPrice4', 'BidPrice3', 'BidPrice2', 'BidPrice1', 'AskPrice5', 'AskPrice4', 'AskPrice1', 'AskPrice3', 'AskPrice2']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ClosePrice', u'今收盘'),('CurrDelta', u'今虚实度'),('HighestPrice', u'最高价'),('UpperLimitPrice', u'涨停板价'),('Turnover', u'成交金额'),('ExchangeInstID', u'合约在交易所的代码'),('BidVolume1', u'申买量一'),('BidVolume3', u'申买量三'),('BidVolume2', u'申买量二'),('BidVolume5', u'申买量五'),('BidVolume4', u'申买量四'),('LastPrice', u'最新价'),('LowerLimitPrice', u'跌停板价'),('SettlementPrice', u'本次结算价'),('PreOpenInterest', u'昨持仓量'),('PreSettlementPrice', u'上次结算价'),('AveragePrice', u'当日均价'),('AskVolume5', u'申卖量五'),('AskVolume4', u'申卖量四'),('AskVolume3', u'申卖量三'),('AskVolume2', u'申卖量二'),('AskVolume1', u'申卖量一'),('LowestPrice', u'最低价'),('OpenPrice', u'今开盘'),('OpenInterest', u'持仓量'),('InstrumentID', u'合约代码'),('PreClosePrice', u'昨收盘'),('ExchangeID', u'交易所代码'),('UpdateMillisec', u'最后修改毫秒'),('ActionDay', u'业务日期'),('Volume', u'数量'),('TradingDay', u'交易日'),('PreDelta', u'昨虚实度'),('UpdateTime', u'最后修改时间'),('BidPrice5', u'申买价五'),('BidPrice4', u'申买价四'),('BidPrice3', u'申买价三'),('BidPrice2', u'申买价二'),('BidPrice1', u'申买价一'),('AskPrice5', u'申卖价五'),('AskPrice4', u'申卖价四'),('AskPrice1', u'申卖价一'),('AskPrice3', u'申卖价三'),('AskPrice2', u'申卖价二')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQueryMaxOrderVolumeWithPriceField:
    def __init__(self, Price=0, InstrumentID="", OffsetFlag='0', HedgeFlag='1', MaxVolume=0, Direction='0', BrokerID="", InvestorID=""):
        self.Price=Price
        self.InstrumentID=tou(InstrumentID)
        self.OffsetFlag=tou(OffsetFlag)
        self.HedgeFlag=tou(HedgeFlag)
        self.MaxVolume=MaxVolume
        self.Direction=tou(Direction)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={'Direction': {"'1'": '卖', "'0'": '买'}, 'OffsetFlag': {"'1'": '平仓', "'6'": '本地强平', "'0'": '开仓', "'5'": '强减', "'4'": '平昨', "'3'": '平今', "'2'": '强平'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Price', 'InstrumentID', 'OffsetFlag', 'HedgeFlag', 'MaxVolume', 'Direction', 'BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Price', u'报单价格'),('InstrumentID', u'合约代码'),('OffsetFlag', u'开平标志'),('HedgeFlag', u'投机套保标志'),('MaxVolume', u'最大允许报单数量'),('Direction', u'买卖方向'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in ['OffsetFlag', 'HedgeFlag', 'Direction']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryExchangeMarginRateField:
    def __init__(self, BrokerID="", InstrumentID="", HedgeFlag='1'):
        self.BrokerID=tou(BrokerID)
        self.InstrumentID=tou(InstrumentID)
        self.HedgeFlag=tou(HedgeFlag)
        self.vcmap={'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InstrumentID', 'HedgeFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InstrumentID', u'合约代码'),('HedgeFlag', u'投机套保标志')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncStatusField:
    def __init__(self, TradingDay="", DataSyncStatus='1'):
        self.TradingDay=tou(TradingDay)
        self.DataSyncStatus=tou(DataSyncStatus)
        self.vcmap={'DataSyncStatus': {"'1'": '未同步', "'3'": '已同步', "'2'": '同步中'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DataSyncStatus']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易日'),('DataSyncStatus', u'数据同步状态')]])
    def getval(self, n):
        if n in ['DataSyncStatus']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSpecificInstrumentField:
    def __init__(self, InstrumentID=""):
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferSerialField:
    def __init__(self, AvailabilityFlag='0', TradingDay="", TradeTime="", FutureSerial=0, ErrorID=0, BrokerID="", InvestorID="", SessionID=0, IdentifiedCardNo="", IdCardType='0', TradeAmount=0, BankID="", CurrencyID="", ErrorMsg="", BankNewAccount="", BankAccount="", OperatorCode="", BankAccType='1', TradeDate="", CustFee=0, FutureAccType='1', AccountID="", BankSerial="", TradeCode="", BrokerFee=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.AvailabilityFlag=tou(AvailabilityFlag)
        self.TradingDay=tou(TradingDay)
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.ErrorID=ErrorID
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.TradeAmount=TradeAmount
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.BankNewAccount=tou(BankNewAccount)
        self.BankAccount=tou(BankAccount)
        self.OperatorCode=tou(OperatorCode)
        self.BankAccType=tou(BankAccType)
        self.TradeDate=tou(TradeDate)
        self.CustFee=CustFee
        self.FutureAccType=tou(FutureAccType)
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.TradeCode=tou(TradeCode)
        self.BrokerFee=BrokerFee
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'AvailabilityFlag': {"'1'": '有效', "'0'": '未确认', "'2'": '冲正'}, 'FutureAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AvailabilityFlag', 'TradingDay', 'TradeTime', 'FutureSerial', 'ErrorID', 'BrokerID', 'InvestorID', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'TradeAmount', 'BankID', 'CurrencyID', 'ErrorMsg', 'BankNewAccount', 'BankAccount', 'OperatorCode', 'BankAccType', 'TradeDate', 'CustFee', 'FutureAccType', 'AccountID', 'BankSerial', 'TradeCode', 'BrokerFee', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('AvailabilityFlag', u'有效标志'),('TradingDay', u'交易日期'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('ErrorID', u'错误代码'),('BrokerID', u'期货公司编码'),('InvestorID', u'投资者代码'),('SessionID', u'会话编号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('TradeAmount', u'交易金额'),('BankID', u'银行编码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankNewAccount', u'新银行帐号'),('BankAccount', u'银行帐号'),('OperatorCode', u'操作员'),('BankAccType', u'银行帐号类型'),('TradeDate', u'交易发起方日期'),('CustFee', u'应收客户费用'),('FutureAccType', u'期货公司帐号类型'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('TradeCode', u'交易代码'),('BrokerFee', u'应收期货公司费用'),('BankBranchID', u'银行分支机构编码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'平台流水号')]])
    def getval(self, n):
        if n in ['AvailabilityFlag', 'IdCardType', 'BankAccType', 'FutureAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerUserOTPParamField:
    def __init__(self, OTPVendorsID="", OTPType='0', LastDrift=0, AuthKey="", SerialNumber="", BrokerID="", LastSuccess=0, UserID=""):
        self.OTPVendorsID=tou(OTPVendorsID)
        self.OTPType=tou(OTPType)
        self.LastDrift=LastDrift
        self.AuthKey=tou(AuthKey)
        self.SerialNumber=tou(SerialNumber)
        self.BrokerID=tou(BrokerID)
        self.LastSuccess=LastSuccess
        self.UserID=tou(UserID)
        self.vcmap={'OTPType': {"'1'": '时间令牌', "'0'": '无动态令牌'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OTPVendorsID', 'OTPType', 'LastDrift', 'AuthKey', 'SerialNumber', 'BrokerID', 'LastSuccess', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OTPVendorsID', u'动态令牌提供商'),('OTPType', u'动态令牌类型'),('LastDrift', u'漂移值'),('AuthKey', u'令牌密钥'),('SerialNumber', u'动态令牌序列号'),('BrokerID', u'经纪公司代码'),('LastSuccess', u'成功值'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in ['OTPType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingTradingCodeField:
    def __init__(self, IsActive=0, ClientID="", ClientIDType='1', BrokerID="", InvestorID="", ExchangeID=""):
        self.IsActive=IsActive
        self.ClientID=tou(ClientID)
        self.ClientIDType=tou(ClientIDType)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={'ClientIDType': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IsActive', 'ClientID', 'ClientIDType', 'BrokerID', 'InvestorID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('IsActive', u'是否活跃'),('ClientID', u'客户代码'),('ClientIDType', u'交易编码类型'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in ['ClientIDType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryBrokerField:
    def __init__(self, BrokerID=""):
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInstrumentField:
    def __init__(self, CreateDate="", InstrumentName="", DeliveryMonth=0, StartDelivDate="", MinMarketOrderVolume=0, ProductClass='1', VolumeMultiple=0, PriceTick=0, InstLifePhase='0', MaxMarginSideAlgorithm='0', InstrumentID="", ExpireDate="", ExchangeInstID="", DeliveryYear=0, ShortMarginRatio=0, EndDelivDate="", MaxMarketOrderVolume=0, MinLimitOrderVolume=0, PositionType='1', ProductID="", OpenDate="", PositionDateType='1', IsTrading=0, LongMarginRatio=0, ExchangeID="", MaxLimitOrderVolume=0):
        self.CreateDate=tou(CreateDate)
        self.InstrumentName=tou(InstrumentName)
        self.DeliveryMonth=DeliveryMonth
        self.StartDelivDate=tou(StartDelivDate)
        self.MinMarketOrderVolume=MinMarketOrderVolume
        self.ProductClass=tou(ProductClass)
        self.VolumeMultiple=VolumeMultiple
        self.PriceTick=PriceTick
        self.InstLifePhase=tou(InstLifePhase)
        self.MaxMarginSideAlgorithm=tou(MaxMarginSideAlgorithm)
        self.InstrumentID=tou(InstrumentID)
        self.ExpireDate=tou(ExpireDate)
        self.ExchangeInstID=tou(ExchangeInstID)
        self.DeliveryYear=DeliveryYear
        self.ShortMarginRatio=ShortMarginRatio
        self.EndDelivDate=tou(EndDelivDate)
        self.MaxMarketOrderVolume=MaxMarketOrderVolume
        self.MinLimitOrderVolume=MinLimitOrderVolume
        self.PositionType=tou(PositionType)
        self.ProductID=tou(ProductID)
        self.OpenDate=tou(OpenDate)
        self.PositionDateType=tou(PositionDateType)
        self.IsTrading=IsTrading
        self.LongMarginRatio=LongMarginRatio
        self.ExchangeID=tou(ExchangeID)
        self.MaxLimitOrderVolume=MaxLimitOrderVolume
        self.vcmap={'MaxMarginSideAlgorithm': {"'1'": '使用大额单边保证金算法', "'0'": '不使用大额单边保证金算法'}, 'ProductClass': {"'4'": '即期', "'1'": '期货', "'3'": '组合', "'5'": '期转现', "'2'": '期权'}, 'PositionDateType': {"'1'": '使用历史持仓', "'2'": '不使用历史持仓'}, 'InstLifePhase': {"'1'": '上市', "'3'": '到期', "'0'": '未上市', "'2'": '停牌'}, 'PositionType': {"'1'": '净持仓', "'2'": '综合持仓'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CreateDate', 'InstrumentName', 'DeliveryMonth', 'StartDelivDate', 'MinMarketOrderVolume', 'ProductClass', 'VolumeMultiple', 'PriceTick', 'InstLifePhase', 'MaxMarginSideAlgorithm', 'InstrumentID', 'ExpireDate', 'ExchangeInstID', 'DeliveryYear', 'ShortMarginRatio', 'EndDelivDate', 'MaxMarketOrderVolume', 'MinLimitOrderVolume', 'PositionType', 'ProductID', 'OpenDate', 'PositionDateType', 'IsTrading', 'LongMarginRatio', 'ExchangeID', 'MaxLimitOrderVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CreateDate', u'创建日'),('InstrumentName', u'合约名称'),('DeliveryMonth', u'交割月'),('StartDelivDate', u'开始交割日'),('MinMarketOrderVolume', u'市价单最小下单量'),('ProductClass', u'产品类型'),('VolumeMultiple', u'合约数量乘数'),('PriceTick', u'最小变动价位'),('InstLifePhase', u'合约生命周期状态'),('MaxMarginSideAlgorithm', u'是否使用大额单边保证金算法'),('InstrumentID', u'合约代码'),('ExpireDate', u'到期日'),('ExchangeInstID', u'合约在交易所的代码'),('DeliveryYear', u'交割年份'),('ShortMarginRatio', u'空头保证金率'),('EndDelivDate', u'结束交割日'),('MaxMarketOrderVolume', u'市价单最大下单量'),('MinLimitOrderVolume', u'限价单最小下单量'),('PositionType', u'持仓类型'),('ProductID', u'产品代码'),('OpenDate', u'上市日'),('PositionDateType', u'持仓日期类型'),('IsTrading', u'当前是否交易'),('LongMarginRatio', u'多头保证金率'),('ExchangeID', u'交易所代码'),('MaxLimitOrderVolume', u'限价单最大下单量')]])
    def getval(self, n):
        if n in ['ProductClass', 'InstLifePhase', 'MaxMarginSideAlgorithm', 'PositionType', 'PositionDateType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncDepositField:
    def __init__(self, DepositSeqNo="", BrokerID="", InvestorID="", IsForce=0, Deposit=0):
        self.DepositSeqNo=tou(DepositSeqNo)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.IsForce=IsForce
        self.Deposit=Deposit
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['DepositSeqNo', 'BrokerID', 'InvestorID', 'IsForce', 'Deposit']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('DepositSeqNo', u'出入金流水号'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('IsForce', u'是否强制进行'),('Deposit', u'入金金额')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspSyncKeyField:
    def __init__(self, TradeTime="", DeviceID="", ErrorID=0, InstallID=0, BrokerID="", SessionID=0, BankID="", ErrorMsg="", OperNo="", LastFragment='0', RequestID=0, TradeDate="", UserID="", TradingDay="", BankSerial="", BrokerIDByBank="", TradeCode="", Message="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.BankID=tou(BankID)
        self.ErrorMsg=tou(ErrorMsg)
        self.OperNo=tou(OperNo)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.Message=tou(Message)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeTime', 'DeviceID', 'ErrorID', 'InstallID', 'BrokerID', 'SessionID', 'BankID', 'ErrorMsg', 'OperNo', 'LastFragment', 'RequestID', 'TradeDate', 'UserID', 'TradingDay', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'Message', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('ErrorMsg', u'错误信息'),('OperNo', u'交易柜员'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('TradingDay', u'交易系统日期'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('Message', u'交易核心给银期报盘的消息'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataBestPriceField:
    def __init__(self, BidVolume1=0, AskPrice1=0, AskVolume1=0, BidPrice1=0):
        self.BidVolume1=BidVolume1
        self.AskPrice1=AskPrice1
        self.AskVolume1=AskVolume1
        self.BidPrice1=BidPrice1
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BidVolume1', 'AskPrice1', 'AskVolume1', 'BidPrice1']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BidVolume1', u'申买量一'),('AskPrice1', u'申卖价一'),('AskVolume1', u'申卖量一'),('BidPrice1', u'申买价一')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorPositionField:
    def __init__(self, LongFrozen=0, PosiDirection='1', CloseProfitByTrade=0, SettlementPrice=0, BrokerID="", InvestorID="", OpenCost=0, Commission=0, CashIn=0, TodayPosition=0, InstrumentID="", CloseProfit=0, ExchangeMargin=0, CombLongFrozen=0, PositionProfit=0, PreSettlementPrice=0, FrozenMargin=0, Position=0, ShortFrozen=0, SettlementID=0, LongFrozenAmount=0, ShortFrozenAmount=0, CloseProfitByDate=0, FrozenCommission=0, MarginRateByVolume=0, MarginRateByMoney=0, TradingDay="", UseMargin=0, OpenVolume=0, FrozenCash=0, PositionCost=0, CloseAmount=0, YdPosition=0, OpenAmount=0, HedgeFlag='1', CloseVolume=0, CombPosition=0, PreMargin=0, CombShortFrozen=0, PositionDate='1'):
        self.LongFrozen=LongFrozen
        self.PosiDirection=tou(PosiDirection)
        self.CloseProfitByTrade=CloseProfitByTrade
        self.SettlementPrice=SettlementPrice
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.OpenCost=OpenCost
        self.Commission=Commission
        self.CashIn=CashIn
        self.TodayPosition=TodayPosition
        self.InstrumentID=tou(InstrumentID)
        self.CloseProfit=CloseProfit
        self.ExchangeMargin=ExchangeMargin
        self.CombLongFrozen=CombLongFrozen
        self.PositionProfit=PositionProfit
        self.PreSettlementPrice=PreSettlementPrice
        self.FrozenMargin=FrozenMargin
        self.Position=Position
        self.ShortFrozen=ShortFrozen
        self.SettlementID=SettlementID
        self.LongFrozenAmount=LongFrozenAmount
        self.ShortFrozenAmount=ShortFrozenAmount
        self.CloseProfitByDate=CloseProfitByDate
        self.FrozenCommission=FrozenCommission
        self.MarginRateByVolume=MarginRateByVolume
        self.MarginRateByMoney=MarginRateByMoney
        self.TradingDay=tou(TradingDay)
        self.UseMargin=UseMargin
        self.OpenVolume=OpenVolume
        self.FrozenCash=FrozenCash
        self.PositionCost=PositionCost
        self.CloseAmount=CloseAmount
        self.YdPosition=YdPosition
        self.OpenAmount=OpenAmount
        self.HedgeFlag=tou(HedgeFlag)
        self.CloseVolume=CloseVolume
        self.CombPosition=CombPosition
        self.PreMargin=PreMargin
        self.CombShortFrozen=CombShortFrozen
        self.PositionDate=tou(PositionDate)
        self.vcmap={'PositionDate': {"'1'": '今日持仓', "'2'": '历史持仓'}, 'PosiDirection': {"'1'": '净', "'3'": '空头', "'2'": '多头'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LongFrozen', 'PosiDirection', 'CloseProfitByTrade', 'SettlementPrice', 'BrokerID', 'InvestorID', 'OpenCost', 'Commission', 'CashIn', 'TodayPosition', 'InstrumentID', 'CloseProfit', 'ExchangeMargin', 'CombLongFrozen', 'PositionProfit', 'PreSettlementPrice', 'FrozenMargin', 'Position', 'ShortFrozen', 'SettlementID', 'LongFrozenAmount', 'ShortFrozenAmount', 'CloseProfitByDate', 'FrozenCommission', 'MarginRateByVolume', 'MarginRateByMoney', 'TradingDay', 'UseMargin', 'OpenVolume', 'FrozenCash', 'PositionCost', 'CloseAmount', 'YdPosition', 'OpenAmount', 'HedgeFlag', 'CloseVolume', 'CombPosition', 'PreMargin', 'CombShortFrozen', 'PositionDate']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LongFrozen', u'多头冻结'),('PosiDirection', u'持仓多空方向'),('CloseProfitByTrade', u'逐笔对冲平仓盈亏'),('SettlementPrice', u'本次结算价'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('OpenCost', u'开仓成本'),('Commission', u'手续费'),('CashIn', u'资金差额'),('TodayPosition', u'今日持仓'),('InstrumentID', u'合约代码'),('CloseProfit', u'平仓盈亏'),('ExchangeMargin', u'交易所保证金'),('CombLongFrozen', u'组合多头冻结'),('PositionProfit', u'持仓盈亏'),('PreSettlementPrice', u'上次结算价'),('FrozenMargin', u'冻结的保证金'),('Position', u'今日持仓'),('ShortFrozen', u'空头冻结'),('SettlementID', u'结算编号'),('LongFrozenAmount', u'开仓冻结金额'),('ShortFrozenAmount', u'开仓冻结金额'),('CloseProfitByDate', u'逐日盯市平仓盈亏'),('FrozenCommission', u'冻结的手续费'),('MarginRateByVolume', u'保证金率(按手数)'),('MarginRateByMoney', u'保证金率'),('TradingDay', u'交易日'),('UseMargin', u'占用的保证金'),('OpenVolume', u'开仓量'),('FrozenCash', u'冻结的资金'),('PositionCost', u'持仓成本'),('CloseAmount', u'平仓金额'),('YdPosition', u'上日持仓'),('OpenAmount', u'开仓金额'),('HedgeFlag', u'投机套保标志'),('CloseVolume', u'平仓量'),('CombPosition', u'组合成交形成的持仓'),('PreMargin', u'上次占用的保证金'),('CombShortFrozen', u'组合空头冻结'),('PositionDate', u'持仓日期')]])
    def getval(self, n):
        if n in ['PosiDirection', 'HedgeFlag', 'PositionDate']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryContractBankField:
    def __init__(self, BankID="", BrokerID="", BankBrchID=""):
        self.BankID=tou(BankID)
        self.BrokerID=tou(BrokerID)
        self.BankBrchID=tou(BankBrchID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankID', 'BrokerID', 'BankBrchID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankID', u'银行代码'),('BrokerID', u'经纪公司代码'),('BankBrchID', u'银行分中心代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryCommRateModelField:
    def __init__(self, CommModelID="", BrokerID=""):
        self.CommModelID=tou(CommModelID)
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CommModelID', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CommModelID', u'手续费率模板代码'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeOrderField:
    def __init__(self, CombOffsetFlag="", OrderPriceType='1', OrderSubmitStatus='0', OrderSysID="", InsertTime="", ClientID="", InstallID=0, CombHedgeFlag="", MinVolume=0, ForceCloseReason='0', VolumeTotalOriginal=0, InsertDate="", CancelTime="", TradingDay="", OrderStatus='0', ExchangeInstID="", VolumeTotal=0, NotifySequence=0, UpdateTime="", SuspendTime="", RequestID=0, IsAutoSuspend=0, SequenceNo=0, VolumeTraded=0, ActiveTime="", StopPrice=0, OrderSource='0', ExchangeID="", GTDDate="", TraderID="", ParticipantID="", SettlementID=0, Direction='0', BusinessUnit="", LimitPrice=0, ClearingPartID="", ContingentCondition='1', VolumeCondition='1', ActiveTraderID="", OrderType='0', OrderLocalID="", TimeCondition='1'):
        self.CombOffsetFlag=tou(CombOffsetFlag)
        self.OrderPriceType=tou(OrderPriceType)
        self.OrderSubmitStatus=tou(OrderSubmitStatus)
        self.OrderSysID=tou(OrderSysID)
        self.InsertTime=tou(InsertTime)
        self.ClientID=tou(ClientID)
        self.InstallID=InstallID
        self.CombHedgeFlag=tou(CombHedgeFlag)
        self.MinVolume=MinVolume
        self.ForceCloseReason=tou(ForceCloseReason)
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.InsertDate=tou(InsertDate)
        self.CancelTime=tou(CancelTime)
        self.TradingDay=tou(TradingDay)
        self.OrderStatus=tou(OrderStatus)
        self.ExchangeInstID=tou(ExchangeInstID)
        self.VolumeTotal=VolumeTotal
        self.NotifySequence=NotifySequence
        self.UpdateTime=tou(UpdateTime)
        self.SuspendTime=tou(SuspendTime)
        self.RequestID=RequestID
        self.IsAutoSuspend=IsAutoSuspend
        self.SequenceNo=SequenceNo
        self.VolumeTraded=VolumeTraded
        self.ActiveTime=tou(ActiveTime)
        self.StopPrice=StopPrice
        self.OrderSource=tou(OrderSource)
        self.ExchangeID=tou(ExchangeID)
        self.GTDDate=tou(GTDDate)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.SettlementID=SettlementID
        self.Direction=tou(Direction)
        self.BusinessUnit=tou(BusinessUnit)
        self.LimitPrice=LimitPrice
        self.ClearingPartID=tou(ClearingPartID)
        self.ContingentCondition=tou(ContingentCondition)
        self.VolumeCondition=tou(VolumeCondition)
        self.ActiveTraderID=tou(ActiveTraderID)
        self.OrderType=tou(OrderType)
        self.OrderLocalID=tou(OrderLocalID)
        self.TimeCondition=tou(TimeCondition)
        self.vcmap={'TimeCondition': {"'1'": '立即完成，否则撤销', "'6'": '集合竞价有效', "'5'": '撤销前有效', "'4'": '指定日期前有效', "'3'": '当日有效', "'2'": '本节有效'}, 'VolumeCondition': {"'1'": '任何数量', "'3'": '全部数量', "'2'": '最小数量'}, 'OrderPriceType': {"'1'": '任意价', "'F'": '买一价浮动上浮3个ticks', "'E'": '买一价浮动上浮2个ticks', "'4'": '最新价', "'3'": '最优价', "'2'": '限价', "'7'": '最新价浮动上浮3个ticks', "'A'": '卖一价浮动上浮2个ticks', "'6'": '最新价浮动上浮2个ticks', "'5'": '最新价浮动上浮1个ticks', "'D'": '买一价浮动上浮1个ticks', "'9'": '卖一价浮动上浮1个ticks', "'C'": '买一价', "'8'": '卖一价', "'B'": '卖一价浮动上浮3个ticks'}, 'ContingentCondition': {"'1'": '立即', "'F'": '买一价小于条件价', "'E'": '买一价大于等于条件价', "'4'": '预埋单', "'3'": '止赢', "'H'": '买一价小于等于条件价', "'2'": '止损', "'7'": '最新价小于条件价', "'A'": '卖一价大于等于条件价', "'6'": '最新价大于等于条件价', "'5'": '最新价大于条件价', "'D'": '买一价大于条件价', "'9'": '卖一价大于条件价', "'C'": '卖一价小于等于条件价', "'8'": '最新价小于等于条件价', "'B'": '卖一价小于条件价'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'OrderSubmitStatus': {"'1'": '撤单已经提交', "'6'": '改单已经被拒绝', "'0'": '已经提交', "'5'": '撤单已经被拒绝', "'4'": '报单已经被拒绝', "'3'": '已经接受', "'2'": '修改已经提交'}, 'OrderSource': {"'1'": '来自管理员', "'0'": '来自参与者'}, 'OrderStatus': {"'1'": '部分成交还在队列中', "'0'": '全部成交', "'5'": '撤单', "'4'": '未成交不在队列中', "'3'": '未成交还在队列中', "'2'": '部分成交不在队列中', "'c'": '已触发', "'a'": '未知', "'b'": '尚未触发'}, 'ForceCloseReason': {"'7'": '自然人临近交割', "'1'": '资金不足', "'6'": '其它', "'0'": '非强平', "'5'": '违规', "'4'": '持仓非整数倍', "'3'": '会员超仓', "'2'": '客户超仓'}, 'OrderType': {"'1'": '报价衍生', "'0'": '正常', "'5'": '互换单', "'4'": '条件单', "'3'": '组合报单', "'2'": '组合衍生'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CombOffsetFlag', 'OrderPriceType', 'OrderSubmitStatus', 'OrderSysID', 'InsertTime', 'ClientID', 'InstallID', 'CombHedgeFlag', 'MinVolume', 'ForceCloseReason', 'VolumeTotalOriginal', 'InsertDate', 'CancelTime', 'TradingDay', 'OrderStatus', 'ExchangeInstID', 'VolumeTotal', 'NotifySequence', 'UpdateTime', 'SuspendTime', 'RequestID', 'IsAutoSuspend', 'SequenceNo', 'VolumeTraded', 'ActiveTime', 'StopPrice', 'OrderSource', 'ExchangeID', 'GTDDate', 'TraderID', 'ParticipantID', 'SettlementID', 'Direction', 'BusinessUnit', 'LimitPrice', 'ClearingPartID', 'ContingentCondition', 'VolumeCondition', 'ActiveTraderID', 'OrderType', 'OrderLocalID', 'TimeCondition']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CombOffsetFlag', u'组合开平标志'),('OrderPriceType', u'报单价格条件'),('OrderSubmitStatus', u'报单提交状态'),('OrderSysID', u'报单编号'),('InsertTime', u'委托时间'),('ClientID', u'客户代码'),('InstallID', u'安装编号'),('CombHedgeFlag', u'组合投机套保标志'),('MinVolume', u'最小成交量'),('ForceCloseReason', u'强平原因'),('VolumeTotalOriginal', u'数量'),('InsertDate', u'报单日期'),('CancelTime', u'撤销时间'),('TradingDay', u'交易日'),('OrderStatus', u'报单状态'),('ExchangeInstID', u'合约在交易所的代码'),('VolumeTotal', u'剩余数量'),('NotifySequence', u'报单提示序号'),('UpdateTime', u'最后修改时间'),('SuspendTime', u'挂起时间'),('RequestID', u'请求编号'),('IsAutoSuspend', u'自动挂起标志'),('SequenceNo', u'序号'),('VolumeTraded', u'今成交数量'),('ActiveTime', u'激活时间'),('StopPrice', u'止损价'),('OrderSource', u'报单来源'),('ExchangeID', u'交易所代码'),('GTDDate', u'GTD日期'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码'),('SettlementID', u'结算编号'),('Direction', u'买卖方向'),('BusinessUnit', u'业务单元'),('LimitPrice', u'价格'),('ClearingPartID', u'结算会员编号'),('ContingentCondition', u'触发条件'),('VolumeCondition', u'成交量类型'),('ActiveTraderID', u'最后修改交易所交易员代码'),('OrderType', u'报单类型'),('OrderLocalID', u'本地报单编号'),('TimeCondition', u'有效期类型')]])
    def getval(self, n):
        if n in ['OrderPriceType', 'OrderSubmitStatus', 'ForceCloseReason', 'OrderStatus', 'OrderSource', 'Direction', 'ContingentCondition', 'VolumeCondition', 'OrderType', 'TimeCondition']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcCurrentTimeField:
    def __init__(self, CurrTime="", CurrDate="", ActionDay="", CurrMillisec=0):
        self.CurrTime=tou(CurrTime)
        self.CurrDate=tou(CurrDate)
        self.ActionDay=tou(ActionDay)
        self.CurrMillisec=CurrMillisec
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CurrTime', 'CurrDate', 'ActionDay', 'CurrMillisec']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CurrTime', u'当前时间'),('CurrDate', u'当前日期'),('ActionDay', u'业务日期'),('CurrMillisec', u'当前时间（毫秒）')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerField:
    def __init__(self, IsActive=0, BrokerID="", BrokerName="", BrokerAbbr=""):
        self.IsActive=IsActive
        self.BrokerID=tou(BrokerID)
        self.BrokerName=tou(BrokerName)
        self.BrokerAbbr=tou(BrokerAbbr)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['IsActive', 'BrokerID', 'BrokerName', 'BrokerAbbr']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('IsActive', u'是否活跃'),('BrokerID', u'经纪公司代码'),('BrokerName', u'经纪公司名称'),('BrokerAbbr', u'经纪公司简称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeOrderActionErrorField:
    def __init__(self, OrderSysID="", ExchangeID="", ActionLocalID="", ErrorID=0, InstallID=0, ErrorMsg="", OrderLocalID="", TraderID=""):
        self.OrderSysID=tou(OrderSysID)
        self.ExchangeID=tou(ExchangeID)
        self.ActionLocalID=tou(ActionLocalID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.ErrorMsg=tou(ErrorMsg)
        self.OrderLocalID=tou(OrderLocalID)
        self.TraderID=tou(TraderID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderSysID', 'ExchangeID', 'ActionLocalID', 'ErrorID', 'InstallID', 'ErrorMsg', 'OrderLocalID', 'TraderID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderSysID', u'报单编号'),('ExchangeID', u'交易所代码'),('ActionLocalID', u'操作本地编号'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('ErrorMsg', u'错误信息'),('OrderLocalID', u'本地报单编号'),('TraderID', u'交易所交易员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorProductGroupMarginField:
    def __init__(self, FrozenCommission=0, CashIn=0, BrokerID="", InvestorID="", LongOffsetAmount=0, LongExchMargin=0, Commission=0, ExchMargin=0, CloseProfit=0, ProductGroupID="", PositionProfit=0, ExchOffsetAmount=0, FrozenMargin=0, LongExchOffsetAmount=0, ShortUseMargin=0, OffsetAmount=0, ShortOffsetAmount=0, ShortExchMargin=0, TradingDay="", UseMargin=0, FrozenCash=0, SettlementID=0, ShortExchOffsetAmount=0, ShortFrozenMargin=0, LongUseMargin=0, LongFrozenMargin=0):
        self.FrozenCommission=FrozenCommission
        self.CashIn=CashIn
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.LongOffsetAmount=LongOffsetAmount
        self.LongExchMargin=LongExchMargin
        self.Commission=Commission
        self.ExchMargin=ExchMargin
        self.CloseProfit=CloseProfit
        self.ProductGroupID=tou(ProductGroupID)
        self.PositionProfit=PositionProfit
        self.ExchOffsetAmount=ExchOffsetAmount
        self.FrozenMargin=FrozenMargin
        self.LongExchOffsetAmount=LongExchOffsetAmount
        self.ShortUseMargin=ShortUseMargin
        self.OffsetAmount=OffsetAmount
        self.ShortOffsetAmount=ShortOffsetAmount
        self.ShortExchMargin=ShortExchMargin
        self.TradingDay=tou(TradingDay)
        self.UseMargin=UseMargin
        self.FrozenCash=FrozenCash
        self.SettlementID=SettlementID
        self.ShortExchOffsetAmount=ShortExchOffsetAmount
        self.ShortFrozenMargin=ShortFrozenMargin
        self.LongUseMargin=LongUseMargin
        self.LongFrozenMargin=LongFrozenMargin
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrozenCommission', 'CashIn', 'BrokerID', 'InvestorID', 'LongOffsetAmount', 'LongExchMargin', 'Commission', 'ExchMargin', 'CloseProfit', 'ProductGroupID', 'PositionProfit', 'ExchOffsetAmount', 'FrozenMargin', 'LongExchOffsetAmount', 'ShortUseMargin', 'OffsetAmount', 'ShortOffsetAmount', 'ShortExchMargin', 'TradingDay', 'UseMargin', 'FrozenCash', 'SettlementID', 'ShortExchOffsetAmount', 'ShortFrozenMargin', 'LongUseMargin', 'LongFrozenMargin']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FrozenCommission', u'冻结的手续费'),('CashIn', u'资金差额'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('LongOffsetAmount', u'多头折抵总金额'),('LongExchMargin', u'交易所多头保证金'),('Commission', u'手续费'),('ExchMargin', u'交易所保证金'),('CloseProfit', u'平仓盈亏'),('ProductGroupID', u'品种/跨品种标示'),('PositionProfit', u'持仓盈亏'),('ExchOffsetAmount', u'交易所折抵总金额'),('FrozenMargin', u'冻结的保证金'),('LongExchOffsetAmount', u'交易所多头折抵总金额'),('ShortUseMargin', u'空头保证金'),('OffsetAmount', u'折抵总金额'),('ShortOffsetAmount', u'空头折抵总金额'),('ShortExchMargin', u'交易所空头保证金'),('TradingDay', u'交易日'),('UseMargin', u'占用的保证金'),('FrozenCash', u'冻结的资金'),('SettlementID', u'结算编号'),('ShortExchOffsetAmount', u'交易所空头折抵总金额'),('ShortFrozenMargin', u'空头冻结的保证金'),('LongUseMargin', u'多头保证金'),('LongFrozenMargin', u'多头冻结的保证金')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerUserEventField:
    def __init__(self, UserEventInfo="", InstrumentID="", InvestorID="", EventTime="", BrokerID="", EventDate="", UserEventType='1', UserID="", EventSequenceNo=0):
        self.UserEventInfo=tou(UserEventInfo)
        self.InstrumentID=tou(InstrumentID)
        self.InvestorID=tou(InvestorID)
        self.EventTime=tou(EventTime)
        self.BrokerID=tou(BrokerID)
        self.EventDate=tou(EventDate)
        self.UserEventType=tou(UserEventType)
        self.UserID=tou(UserID)
        self.EventSequenceNo=EventSequenceNo
        self.vcmap={'UserEventType': {"'1'": '登录', "'6'": '客户端认证', "'5'": '修改密码', "'4'": '交易失败', "'9'": '其他', "'3'": '交易成功', "'2'": '登出'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UserEventInfo', 'InstrumentID', 'InvestorID', 'EventTime', 'BrokerID', 'EventDate', 'UserEventType', 'UserID', 'EventSequenceNo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('UserEventInfo', u'用户事件信息'),('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('EventTime', u'事件发生时间'),('BrokerID', u'经纪公司代码'),('EventDate', u'事件发生日期'),('UserEventType', u'用户事件类型'),('UserID', u'用户代码'),('EventSequenceNo', u'用户事件序号')]])
    def getval(self, n):
        if n in ['UserEventType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInvestorGroupField:
    def __init__(self, BrokerID=""):
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryUserSessionField:
    def __init__(self, BrokerID="", FrontID=0, SessionID=0, UserID=""):
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'FrontID', 'SessionID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('SessionID', u'会话编号'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryCFMMCTradingAccountKeyField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingAccountPasswordField:
    def __init__(self, Password="", BrokerID="", AccountID=""):
        self.Password=tou(Password)
        self.BrokerID=tou(BrokerID)
        self.AccountID=tou(AccountID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcNotifyFutureSignOutField:
    def __init__(self, TradeTime="", DeviceID="", ErrorID=0, InstallID=0, BrokerID="", SessionID=0, BankID="", CurrencyID="", ErrorMsg="", OperNo="", Digest="", LastFragment='0', RequestID=0, TradeDate="", UserID="", TradingDay="", BankSerial="", BrokerIDByBank="", TradeCode="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.OperNo=tou(OperNo)
        self.Digest=tou(Digest)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeTime', 'DeviceID', 'ErrorID', 'InstallID', 'BrokerID', 'SessionID', 'BankID', 'CurrencyID', 'ErrorMsg', 'OperNo', 'Digest', 'LastFragment', 'RequestID', 'TradeDate', 'UserID', 'TradingDay', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('OperNo', u'交易柜员'),('Digest', u'摘要'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('TradingDay', u'交易系统日期'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInvestorField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqOpenAccountField:
    def __init__(self, TradingDay="", DeviceID="", BrokerID="", ZipCode="", SessionID=0, IdentifiedCardNo="", IdCardType='0', MobilePhone="", BankID="", BankPwdFlag='0', OperNo="", BankAccount="", BankSecuAcc="", LastFragment='0', Gender='0', Address="", TradeDate="", MoneyAccountStatus='0', AccountID="", BankSerial="", CustomerName="", BankPassWord="", CashExchangeCode='1', Digest="", PlateSerial=0, Fax="", EMail="", TradeTime="", InstallID=0, SecuPwdFlag='0', VerifyCertNoFlag='0', CurrencyID="", BankSecuAccType='1', Password="", BankBranchID="", CountryCode="", BrokerBranchID="", UserID="", CustType='0', BrokerIDByBank="", TradeCode="", BankAccType='1', TID=0, Telephone=""):
        self.TradingDay=tou(TradingDay)
        self.DeviceID=tou(DeviceID)
        self.BrokerID=tou(BrokerID)
        self.ZipCode=tou(ZipCode)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.MobilePhone=tou(MobilePhone)
        self.BankID=tou(BankID)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.LastFragment=tou(LastFragment)
        self.Gender=tou(Gender)
        self.Address=tou(Address)
        self.TradeDate=tou(TradeDate)
        self.MoneyAccountStatus=tou(MoneyAccountStatus)
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.CashExchangeCode=tou(CashExchangeCode)
        self.Digest=tou(Digest)
        self.PlateSerial=PlateSerial
        self.Fax=tou(Fax)
        self.EMail=tou(EMail)
        self.TradeTime=tou(TradeTime)
        self.InstallID=InstallID
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.CurrencyID=tou(CurrencyID)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.Password=tou(Password)
        self.BankBranchID=tou(BankBranchID)
        self.CountryCode=tou(CountryCode)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.BankAccType=tou(BankAccType)
        self.TID=TID
        self.Telephone=tou(Telephone)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'Gender': {"'1'": '男', "'0'": '未知状态', "'2'": '女'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'CashExchangeCode': {"'1'": '汇', "'2'": '钞'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'MoneyAccountStatus': {"'1'": '销户', "'0'": '正常'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DeviceID', 'BrokerID', 'ZipCode', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'MobilePhone', 'BankID', 'BankPwdFlag', 'OperNo', 'BankAccount', 'BankSecuAcc', 'LastFragment', 'Gender', 'Address', 'TradeDate', 'MoneyAccountStatus', 'AccountID', 'BankSerial', 'CustomerName', 'BankPassWord', 'CashExchangeCode', 'Digest', 'PlateSerial', 'Fax', 'EMail', 'TradeTime', 'InstallID', 'SecuPwdFlag', 'VerifyCertNoFlag', 'CurrencyID', 'BankSecuAccType', 'Password', 'BankBranchID', 'CountryCode', 'BrokerBranchID', 'UserID', 'CustType', 'BrokerIDByBank', 'TradeCode', 'BankAccType', 'TID', 'Telephone']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易系统日期'),('DeviceID', u'渠道标志'),('BrokerID', u'期商代码'),('ZipCode', u'邮编'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('MobilePhone', u'手机'),('BankID', u'银行代码'),('BankPwdFlag', u'银行密码标志'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('BankSecuAcc', u'期货单位帐号'),('LastFragment', u'最后分片标志'),('Gender', u'性别'),('Address', u'地址'),('TradeDate', u'交易日期'),('MoneyAccountStatus', u'资金账户状态'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('CashExchangeCode', u'汇钞标志'),('Digest', u'摘要'),('PlateSerial', u'银期平台消息流水号'),('Fax', u'传真'),('EMail', u'电子邮件'),('TradeTime', u'交易时间'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('CurrencyID', u'币种代码'),('BankSecuAccType', u'期货单位帐号类型'),('Password', u'期货密码'),('BankBranchID', u'银行分支机构代码'),('CountryCode', u'国家代码'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('CustType', u'客户类型'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('BankAccType', u'银行帐号类型'),('TID', u'交易ID'),('Telephone', u'电话号码')]])
    def getval(self, n):
        if n in ['IdCardType', 'BankPwdFlag', 'LastFragment', 'Gender', 'MoneyAccountStatus', 'CashExchangeCode', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'CustType', 'BankAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataAsk23Field:
    def __init__(self, AskVolume3=0, AskVolume2=0, AskPrice3=0, AskPrice2=0):
        self.AskVolume3=AskVolume3
        self.AskVolume2=AskVolume2
        self.AskPrice3=AskPrice3
        self.AskPrice2=AskPrice2
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AskVolume3', 'AskVolume2', 'AskPrice3', 'AskPrice2']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('AskVolume3', u'申卖量三'),('AskVolume2', u'申卖量二'),('AskPrice3', u'申卖价三'),('AskPrice2', u'申卖价二')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataBid23Field:
    def __init__(self, BidVolume3=0, BidVolume2=0, BidPrice3=0, BidPrice2=0):
        self.BidVolume3=BidVolume3
        self.BidVolume2=BidVolume2
        self.BidPrice3=BidPrice3
        self.BidPrice2=BidPrice2
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BidVolume3', 'BidVolume2', 'BidPrice3', 'BidPrice2']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BidVolume3', u'申买量三'),('BidVolume2', u'申买量二'),('BidPrice3', u'申买价三'),('BidPrice2', u'申买价二')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspInfoField:
    def __init__(self, ErrorID=0, ErrorMsg=""):
        self.ErrorID=ErrorID
        self.ErrorMsg=tou(ErrorMsg)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ErrorID', 'ErrorMsg']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ErrorID', u'错误代码'),('ErrorMsg', u'错误信息')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcLoginInfoField:
    def __init__(self, Password="", LoginDate="", SystemName="", SHFETime="", MacAddress="", BrokerID="", FrontID=0, SessionID=0, ProtocolInfo="", OneTimePassword="", FFEXTime="", UserProductInfo="", CZCETime="", LoginTime="", InterfaceProductInfo="", DCETime="", MaxOrderRef="", UserID="", IPAddress=""):
        self.Password=tou(Password)
        self.LoginDate=tou(LoginDate)
        self.SystemName=tou(SystemName)
        self.SHFETime=tou(SHFETime)
        self.MacAddress=tou(MacAddress)
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.ProtocolInfo=tou(ProtocolInfo)
        self.OneTimePassword=tou(OneTimePassword)
        self.FFEXTime=tou(FFEXTime)
        self.UserProductInfo=tou(UserProductInfo)
        self.CZCETime=tou(CZCETime)
        self.LoginTime=tou(LoginTime)
        self.InterfaceProductInfo=tou(InterfaceProductInfo)
        self.DCETime=tou(DCETime)
        self.MaxOrderRef=tou(MaxOrderRef)
        self.UserID=tou(UserID)
        self.IPAddress=tou(IPAddress)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'LoginDate', 'SystemName', 'SHFETime', 'MacAddress', 'BrokerID', 'FrontID', 'SessionID', 'ProtocolInfo', 'OneTimePassword', 'FFEXTime', 'UserProductInfo', 'CZCETime', 'LoginTime', 'InterfaceProductInfo', 'DCETime', 'MaxOrderRef', 'UserID', 'IPAddress']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('LoginDate', u'登录日期'),('SystemName', u'系统名称'),('SHFETime', u'上期所时间'),('MacAddress', u'Mac地址'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('SessionID', u'会话编号'),('ProtocolInfo', u'协议信息'),('OneTimePassword', u'动态密码'),('FFEXTime', u'中金所时间'),('UserProductInfo', u'用户端产品信息'),('CZCETime', u'郑商所时间'),('LoginTime', u'登录时间'),('InterfaceProductInfo', u'接口端产品信息'),('DCETime', u'大商所时间'),('MaxOrderRef', u'最大报单引用'),('UserID', u'用户代码'),('IPAddress', u'IP地址')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeOrderActionField:
    def __init__(self, OrderSysID="", ActionLocalID="", BusinessUnit="", ClientID="", InstallID=0, UserID="", VolumeChange=0, TraderID="", ParticipantID="", ActionFlag='0', ExchangeID="", OrderActionStatus='a', LimitPrice=0, ActionTime="", ActionDate="", OrderLocalID=""):
        self.OrderSysID=tou(OrderSysID)
        self.ActionLocalID=tou(ActionLocalID)
        self.BusinessUnit=tou(BusinessUnit)
        self.ClientID=tou(ClientID)
        self.InstallID=InstallID
        self.UserID=tou(UserID)
        self.VolumeChange=VolumeChange
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.ActionFlag=tou(ActionFlag)
        self.ExchangeID=tou(ExchangeID)
        self.OrderActionStatus=tou(OrderActionStatus)
        self.LimitPrice=LimitPrice
        self.ActionTime=tou(ActionTime)
        self.ActionDate=tou(ActionDate)
        self.OrderLocalID=tou(OrderLocalID)
        self.vcmap={'ActionFlag': {"'3'": '修改', "'0'": '删除'}, 'OrderActionStatus': {"'a'": '已经提交', "'c'": '已经被拒绝', "'b'": '已经接受'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderSysID', 'ActionLocalID', 'BusinessUnit', 'ClientID', 'InstallID', 'UserID', 'VolumeChange', 'TraderID', 'ParticipantID', 'ActionFlag', 'ExchangeID', 'OrderActionStatus', 'LimitPrice', 'ActionTime', 'ActionDate', 'OrderLocalID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderSysID', u'报单编号'),('ActionLocalID', u'操作本地编号'),('BusinessUnit', u'业务单元'),('ClientID', u'客户代码'),('InstallID', u'安装编号'),('UserID', u'用户代码'),('VolumeChange', u'数量变化'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码'),('ActionFlag', u'操作标志'),('ExchangeID', u'交易所代码'),('OrderActionStatus', u'报单操作状态'),('LimitPrice', u'价格'),('ActionTime', u'操作时间'),('ActionDate', u'操作日期'),('OrderLocalID', u'本地报单编号')]])
    def getval(self, n):
        if n in ['ActionFlag', 'OrderActionStatus']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcFutureSignIOField:
    def __init__(self, LastFragment='0', RequestID=0, UserID="", TradeTime="", DeviceID="", TradeDate="", BrokerID="", TradingDay="", SessionID=0, BankSerial="", OperNo="", BrokerIDByBank="", TradeCode="", InstallID=0, TID=0, BankID="", CurrencyID="", BankBranchID="", BrokerBranchID="", PlateSerial=0, Digest=""):
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.UserID=tou(UserID)
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.TradeDate=tou(TradeDate)
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.SessionID=SessionID
        self.BankSerial=tou(BankSerial)
        self.OperNo=tou(OperNo)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.InstallID=InstallID
        self.TID=TID
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.Digest=tou(Digest)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LastFragment', 'RequestID', 'UserID', 'TradeTime', 'DeviceID', 'TradeDate', 'BrokerID', 'TradingDay', 'SessionID', 'BankSerial', 'OperNo', 'BrokerIDByBank', 'TradeCode', 'InstallID', 'TID', 'BankID', 'CurrencyID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('BrokerID', u'期商代码'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('InstallID', u'安装编号'),('TID', u'交易ID'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorPositionDetailField:
    def __init__(self, TradeID="", CombInstrumentID="", Direction='0', BrokerID="", InvestorID="", OpenPrice=0, TradeType='0', SettlementPrice=0, ExchMargin=0, InstrumentID="", ExchangeID="", CloseProfitByTrade=0, PositionProfitByDate=0, Margin=0, Volume=0, CloseAmount=0, MarginRateByMoney=0, TradingDay="", MarginRateByVolume=0, OpenDate="", SettlementID=0, PositionProfitByTrade=0, HedgeFlag='1', CloseVolume=0, CloseProfitByDate=0, LastSettlementPrice=0):
        self.TradeID=tou(TradeID)
        self.CombInstrumentID=tou(CombInstrumentID)
        self.Direction=tou(Direction)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.OpenPrice=OpenPrice
        self.TradeType=tou(TradeType)
        self.SettlementPrice=SettlementPrice
        self.ExchMargin=ExchMargin
        self.InstrumentID=tou(InstrumentID)
        self.ExchangeID=tou(ExchangeID)
        self.CloseProfitByTrade=CloseProfitByTrade
        self.PositionProfitByDate=PositionProfitByDate
        self.Margin=Margin
        self.Volume=Volume
        self.CloseAmount=CloseAmount
        self.MarginRateByMoney=MarginRateByMoney
        self.TradingDay=tou(TradingDay)
        self.MarginRateByVolume=MarginRateByVolume
        self.OpenDate=tou(OpenDate)
        self.SettlementID=SettlementID
        self.PositionProfitByTrade=PositionProfitByTrade
        self.HedgeFlag=tou(HedgeFlag)
        self.CloseVolume=CloseVolume
        self.CloseProfitByDate=CloseProfitByDate
        self.LastSettlementPrice=LastSettlementPrice
        self.vcmap={'Direction': {"'1'": '卖', "'0'": '买'}, 'TradeType': {"'4'": '组合衍生成交', "'1'": '期权执行', "'3'": '期转现衍生成交', "'0'": '普通成交', "'2'": 'OTC成交'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeID', 'CombInstrumentID', 'Direction', 'BrokerID', 'InvestorID', 'OpenPrice', 'TradeType', 'SettlementPrice', 'ExchMargin', 'InstrumentID', 'ExchangeID', 'CloseProfitByTrade', 'PositionProfitByDate', 'Margin', 'Volume', 'CloseAmount', 'MarginRateByMoney', 'TradingDay', 'MarginRateByVolume', 'OpenDate', 'SettlementID', 'PositionProfitByTrade', 'HedgeFlag', 'CloseVolume', 'CloseProfitByDate', 'LastSettlementPrice']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeID', u'成交编号'),('CombInstrumentID', u'组合合约代码'),('Direction', u'买卖'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('OpenPrice', u'开仓价'),('TradeType', u'成交类型'),('SettlementPrice', u'结算价'),('ExchMargin', u'交易所保证金'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('CloseProfitByTrade', u'逐笔对冲平仓盈亏'),('PositionProfitByDate', u'逐日盯市持仓盈亏'),('Margin', u'投资者保证金'),('Volume', u'数量'),('CloseAmount', u'平仓金额'),('MarginRateByMoney', u'保证金率'),('TradingDay', u'交易日'),('MarginRateByVolume', u'保证金率(按手数)'),('OpenDate', u'开仓日期'),('SettlementID', u'结算编号'),('PositionProfitByTrade', u'逐笔对冲持仓盈亏'),('HedgeFlag', u'投机套保标志'),('CloseVolume', u'平仓量'),('CloseProfitByDate', u'逐日盯市平仓盈亏'),('LastSettlementPrice', u'昨结算价')]])
    def getval(self, n):
        if n in ['Direction', 'TradeType', 'HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspAuthenticateField:
    def __init__(self, BrokerID="", UserProductInfo="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserProductInfo=tou(UserProductInfo)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserProductInfo', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserProductInfo', u'用户端产品信息'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorWithdrawAlgorithmField:
    def __init__(self, UsingRatio=0, BrokerID="", InvestorID="", InvestorRange='1'):
        self.UsingRatio=UsingRatio
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['UsingRatio', 'BrokerID', 'InvestorID', 'InvestorRange']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('UsingRatio', u'可提资金比例'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围')]])
    def getval(self, n):
        if n in ['InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryMarginModelField:
    def __init__(self, BrokerID="", MarginModelID=""):
        self.BrokerID=tou(BrokerID)
        self.MarginModelID=tou(MarginModelID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'MarginModelID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('MarginModelID', u'保证金率模板代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeField:
    def __init__(self, ExchangeName="", ExchangeProperty='0', ExchangeID=""):
        self.ExchangeName=tou(ExchangeName)
        self.ExchangeProperty=tou(ExchangeProperty)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={'ExchangeProperty': {"'1'": '根据成交生成报单', "'0'": '正常'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeName', 'ExchangeProperty', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeName', u'交易所名称'),('ExchangeProperty', u'交易所属性'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in ['ExchangeProperty']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcCombinationLegField:
    def __init__(self, Direction='0', CombInstrumentID="", LegID=0, LegMultiple=0, ImplyLevel=0, LegInstrumentID=""):
        self.Direction=tou(Direction)
        self.CombInstrumentID=tou(CombInstrumentID)
        self.LegID=LegID
        self.LegMultiple=LegMultiple
        self.ImplyLevel=ImplyLevel
        self.LegInstrumentID=tou(LegInstrumentID)
        self.vcmap={'Direction': {"'1'": '卖', "'0'": '买'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Direction', 'CombInstrumentID', 'LegID', 'LegMultiple', 'ImplyLevel', 'LegInstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Direction', u'买卖方向'),('CombInstrumentID', u'组合合约代码'),('LegID', u'单腿编号'),('LegMultiple', u'单腿乘数'),('ImplyLevel', u'派生层数'),('LegInstrumentID', u'单腿合约代码')]])
    def getval(self, n):
        if n in ['Direction']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSettlementRefField:
    def __init__(self, SettlementID=0, TradingDay=""):
        self.SettlementID=SettlementID
        self.TradingDay=tou(TradingDay)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SettlementID', 'TradingDay']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('SettlementID', u'结算编号'),('TradingDay', u'交易日')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryTradingAccountField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSuperUserFunctionField:
    def __init__(self, FunctionCode='1', UserID=""):
        self.FunctionCode=tou(FunctionCode)
        self.UserID=tou(UserID)
        self.vcmap={'FunctionCode': {"'1'": '数据异步化', "'E'": '同步动态令牌', "'4'": '变更经纪公司口令', "'3'": '变更管理用户口令', "'2'": '强制用户登出', "'7'": '报单操作', "'A'": '批量同步经纪公司数据', "'6'": '报单插入', "'5'": '变更投资者口令', "'D'": '报单操作', "'9'": '同步经纪公司数据', "'C'": '报单插入', "'8'": '同步系统数据', "'B'": '超级查询'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FunctionCode', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FunctionCode', u'功能代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in ['FunctionCode']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataBaseField:
    def __init__(self, PreOpenInterest=0, PreSettlementPrice=0, TradingDay="", PreClosePrice=0, PreDelta=0):
        self.PreOpenInterest=PreOpenInterest
        self.PreSettlementPrice=PreSettlementPrice
        self.TradingDay=tou(TradingDay)
        self.PreClosePrice=PreClosePrice
        self.PreDelta=PreDelta
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['PreOpenInterest', 'PreSettlementPrice', 'TradingDay', 'PreClosePrice', 'PreDelta']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('PreOpenInterest', u'昨持仓量'),('PreSettlementPrice', u'上次结算价'),('TradingDay', u'交易日'),('PreClosePrice', u'昨收盘'),('PreDelta', u'昨虚实度')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingTradingAccountField:
    def __init__(self, WithdrawQuota=0, DeliveryMargin=0, PreMortgage=0, Balance=0, BrokerID="", Deposit=0, CashIn=0, Reserve=0, ExchangeMargin=0, CurrMargin=0, PositionProfit=0, FrozenMargin=0, Commission=0, Interest=0, Available=0, Credit=0, CloseProfit=0, ReserveBalance=0, ExchangeDeliveryMargin=0, FrozenCommission=0, InterestBase=0, TradingDay="", AccountID="", FrozenCash=0, SettlementID=0, Mortgage=0, PreCredit=0, PreDeposit=0, PreMargin=0, Withdraw=0, PreBalance=0):
        self.WithdrawQuota=WithdrawQuota
        self.DeliveryMargin=DeliveryMargin
        self.PreMortgage=PreMortgage
        self.Balance=Balance
        self.BrokerID=tou(BrokerID)
        self.Deposit=Deposit
        self.CashIn=CashIn
        self.Reserve=Reserve
        self.ExchangeMargin=ExchangeMargin
        self.CurrMargin=CurrMargin
        self.PositionProfit=PositionProfit
        self.FrozenMargin=FrozenMargin
        self.Commission=Commission
        self.Interest=Interest
        self.Available=Available
        self.Credit=Credit
        self.CloseProfit=CloseProfit
        self.ReserveBalance=ReserveBalance
        self.ExchangeDeliveryMargin=ExchangeDeliveryMargin
        self.FrozenCommission=FrozenCommission
        self.InterestBase=InterestBase
        self.TradingDay=tou(TradingDay)
        self.AccountID=tou(AccountID)
        self.FrozenCash=FrozenCash
        self.SettlementID=SettlementID
        self.Mortgage=Mortgage
        self.PreCredit=PreCredit
        self.PreDeposit=PreDeposit
        self.PreMargin=PreMargin
        self.Withdraw=Withdraw
        self.PreBalance=PreBalance
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['WithdrawQuota', 'DeliveryMargin', 'PreMortgage', 'Balance', 'BrokerID', 'Deposit', 'CashIn', 'Reserve', 'ExchangeMargin', 'CurrMargin', 'PositionProfit', 'FrozenMargin', 'Commission', 'Interest', 'Available', 'Credit', 'CloseProfit', 'ReserveBalance', 'ExchangeDeliveryMargin', 'FrozenCommission', 'InterestBase', 'TradingDay', 'AccountID', 'FrozenCash', 'SettlementID', 'Mortgage', 'PreCredit', 'PreDeposit', 'PreMargin', 'Withdraw', 'PreBalance']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('WithdrawQuota', u'可取资金'),('DeliveryMargin', u'投资者交割保证金'),('PreMortgage', u'上次质押金额'),('Balance', u'期货结算准备金'),('BrokerID', u'经纪公司代码'),('Deposit', u'入金金额'),('CashIn', u'资金差额'),('Reserve', u'基本准备金'),('ExchangeMargin', u'交易所保证金'),('CurrMargin', u'当前保证金总额'),('PositionProfit', u'持仓盈亏'),('FrozenMargin', u'冻结的保证金'),('Commission', u'手续费'),('Interest', u'利息收入'),('Available', u'可用资金'),('Credit', u'信用额度'),('CloseProfit', u'平仓盈亏'),('ReserveBalance', u'保底期货结算准备金'),('ExchangeDeliveryMargin', u'交易所交割保证金'),('FrozenCommission', u'冻结的手续费'),('InterestBase', u'利息基数'),('TradingDay', u'交易日'),('AccountID', u'投资者帐号'),('FrozenCash', u'冻结的资金'),('SettlementID', u'结算编号'),('Mortgage', u'质押金额'),('PreCredit', u'上次信用额度'),('PreDeposit', u'上次存款额'),('PreMargin', u'上次占用的保证金'),('Withdraw', u'出金金额'),('PreBalance', u'上次结算准备金')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInstrumentTradingRightField:
    def __init__(self, InstrumentID="", InvestorID="", InvestorRange='1', BrokerID="", TradingRight='0'):
        self.InstrumentID=tou(InstrumentID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.BrokerID=tou(BrokerID)
        self.TradingRight=tou(TradingRight)
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}, 'TradingRight': {"'1'": '只能平仓', "'0'": '可以交易', "'2'": '不能交易'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'InvestorID', 'InvestorRange', 'BrokerID', 'TradingRight']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('BrokerID', u'经纪公司代码'),('TradingRight', u'交易权限')]])
    def getval(self, n):
        if n in ['InvestorRange', 'TradingRight']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingAccountPasswordUpdateV1Field:
    def __init__(self, NewPassword="", BrokerID="", InvestorID="", OldPassword=""):
        self.NewPassword=tou(NewPassword)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.OldPassword=tou(OldPassword)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['NewPassword', 'BrokerID', 'InvestorID', 'OldPassword']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('NewPassword', u'新的口令'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('OldPassword', u'原来的口令')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferQryDetailRspField:
    def __init__(self, FutureAccount="", TradeTime="", FutureSerial=0, TradeDate="", CertCode="", BankBrchID="", TxAmount=0, BankSerial=0, CurrencyCode="", TradeCode="", FutureID="", BankID="", Flag='0', BankAccount=""):
        self.FutureAccount=tou(FutureAccount)
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.TradeDate=tou(TradeDate)
        self.CertCode=tou(CertCode)
        self.BankBrchID=tou(BankBrchID)
        self.TxAmount=TxAmount
        self.BankSerial=BankSerial
        self.CurrencyCode=tou(CurrencyCode)
        self.TradeCode=tou(TradeCode)
        self.FutureID=tou(FutureID)
        self.BankID=tou(BankID)
        self.Flag=tou(Flag)
        self.BankAccount=tou(BankAccount)
        self.vcmap={'Flag': {"'1'": '有效', "'0'": '无效或失败', "'2'": '冲正'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'TradeTime', 'FutureSerial', 'TradeDate', 'CertCode', 'BankBrchID', 'TxAmount', 'BankSerial', 'CurrencyCode', 'TradeCode', 'FutureID', 'BankID', 'Flag', 'BankAccount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FutureAccount', u'资金帐号'),('TradeTime', u'交易时间'),('FutureSerial', u'期货流水号'),('TradeDate', u'交易日期'),('CertCode', u'证件号码'),('BankBrchID', u'银行分中心代码'),('TxAmount', u'发生金额'),('BankSerial', u'银行流水号'),('CurrencyCode', u'货币代码'),('TradeCode', u'交易代码'),('FutureID', u'期货公司代码'),('BankID', u'银行代码'),('Flag', u'有效标志'),('BankAccount', u'银行账号')]])
    def getval(self, n):
        if n in ['Flag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcNotifySyncKeyField:
    def __init__(self, TradeTime="", DeviceID="", ErrorID=0, InstallID=0, BrokerID="", SessionID=0, BankID="", ErrorMsg="", OperNo="", LastFragment='0', RequestID=0, TradeDate="", UserID="", TradingDay="", BankSerial="", BrokerIDByBank="", TradeCode="", Message="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.BankID=tou(BankID)
        self.ErrorMsg=tou(ErrorMsg)
        self.OperNo=tou(OperNo)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.Message=tou(Message)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeTime', 'DeviceID', 'ErrorID', 'InstallID', 'BrokerID', 'SessionID', 'BankID', 'ErrorMsg', 'OperNo', 'LastFragment', 'RequestID', 'TradeDate', 'UserID', 'TradingDay', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'Message', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('BankID', u'银行代码'),('ErrorMsg', u'错误信息'),('OperNo', u'交易柜员'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('TradingDay', u'交易系统日期'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('Message', u'交易核心给银期报盘的消息'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeSequenceField:
    def __init__(self, MarketStatus='0', ExchangeID="", SequenceNo=0):
        self.MarketStatus=tou(MarketStatus)
        self.ExchangeID=tou(ExchangeID)
        self.SequenceNo=SequenceNo
        self.vcmap={'MarketStatus': {"'1'": '非交易', "'6'": '收盘', "'0'": '开盘前', "'5'": '集合竞价撮合', "'4'": '集合竞价价格平衡', "'3'": '集合竞价报单', "'2'": '连续交易'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MarketStatus', 'ExchangeID', 'SequenceNo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('MarketStatus', u'合约交易状态'),('ExchangeID', u'交易所代码'),('SequenceNo', u'序号')]])
    def getval(self, n):
        if n in ['MarketStatus']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspTransferField:
    def __init__(self, CustType='0', DeviceID="", ErrorID=0, BrokerID="", SessionID=0, IdentifiedCardNo="", IdCardType='0', FutureFetchAmount=0, BankID="", BankPwdFlag='0', OperNo="", BankAccount="", BankSecuAcc="", LastFragment='0', TradeDate="", CustFee=0, AccountID="", BankSerial="", BrokerFee=0, CustomerName="", BankPassWord="", Message="", TransferStatus='0', Digest="", PlateSerial=0, TradeAmount=0, TradeTime="", FutureSerial=0, InstallID=0, SecuPwdFlag='0', VerifyCertNoFlag='0', CurrencyID="", ErrorMsg="", BankSecuAccType='1', Password="", RequestID=0, BankAccType='1', BrokerBranchID="", UserID="", TradingDay="", BrokerIDByBank="", TradeCode="", BankBranchID="", FeePayFlag='0', TID=0):
        self.CustType=tou(CustType)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.FutureFetchAmount=FutureFetchAmount
        self.BankID=tou(BankID)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.LastFragment=tou(LastFragment)
        self.TradeDate=tou(TradeDate)
        self.CustFee=CustFee
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.BrokerFee=BrokerFee
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.Message=tou(Message)
        self.TransferStatus=tou(TransferStatus)
        self.Digest=tou(Digest)
        self.PlateSerial=PlateSerial
        self.TradeAmount=TradeAmount
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.InstallID=InstallID
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.Password=tou(Password)
        self.RequestID=RequestID
        self.BankAccType=tou(BankAccType)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.BankBranchID=tou(BankBranchID)
        self.FeePayFlag=tou(FeePayFlag)
        self.TID=TID
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'FeePayFlag': {"'1'": '由发送方支付费用', "'0'": '由受益方支付费用', "'2'": '由发送方支付发起的费用，受益方支付接受的费用'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'TransferStatus': {"'1'": '被冲正', "'0'": '正常'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CustType', 'DeviceID', 'ErrorID', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'FutureFetchAmount', 'BankID', 'BankPwdFlag', 'OperNo', 'BankAccount', 'BankSecuAcc', 'LastFragment', 'TradeDate', 'CustFee', 'AccountID', 'BankSerial', 'BrokerFee', 'CustomerName', 'BankPassWord', 'Message', 'TransferStatus', 'Digest', 'PlateSerial', 'TradeAmount', 'TradeTime', 'FutureSerial', 'InstallID', 'SecuPwdFlag', 'VerifyCertNoFlag', 'CurrencyID', 'ErrorMsg', 'BankSecuAccType', 'Password', 'RequestID', 'BankAccType', 'BrokerBranchID', 'UserID', 'TradingDay', 'BrokerIDByBank', 'TradeCode', 'BankBranchID', 'FeePayFlag', 'TID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CustType', u'客户类型'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('FutureFetchAmount', u'期货可取金额'),('BankID', u'银行代码'),('BankPwdFlag', u'银行密码标志'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('BankSecuAcc', u'期货单位帐号'),('LastFragment', u'最后分片标志'),('TradeDate', u'交易日期'),('CustFee', u'应收客户费用'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('BrokerFee', u'应收期货公司费用'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('Message', u'发送方给接收方的消息'),('TransferStatus', u'转账交易状态'),('Digest', u'摘要'),('PlateSerial', u'银期平台消息流水号'),('TradeAmount', u'转帐金额'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankSecuAccType', u'期货单位帐号类型'),('Password', u'期货密码'),('RequestID', u'请求编号'),('BankAccType', u'银行帐号类型'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('TradingDay', u'交易系统日期'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('BankBranchID', u'银行分支机构代码'),('FeePayFlag', u'费用支付标志'),('TID', u'交易ID')]])
    def getval(self, n):
        if n in ['CustType', 'IdCardType', 'BankPwdFlag', 'LastFragment', 'TransferStatus', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'BankAccType', 'FeePayFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcLogoutAllField:
    def __init__(self, FrontID=0, SessionID=0, SystemName=""):
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.SystemName=tou(SystemName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrontID', 'SessionID', 'SystemName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FrontID', u'前置编号'),('SessionID', u'会话编号'),('SystemName', u'系统名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqSyncKeyField:
    def __init__(self, LastFragment='0', RequestID=0, UserID="", TradeTime="", DeviceID="", TradeDate="", BrokerID="", TradingDay="", SessionID=0, BankSerial="", OperNo="", BrokerIDByBank="", TradeCode="", InstallID=0, Message="", BankID="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.UserID=tou(UserID)
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.TradeDate=tou(TradeDate)
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.SessionID=SessionID
        self.BankSerial=tou(BankSerial)
        self.OperNo=tou(OperNo)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.InstallID=InstallID
        self.Message=tou(Message)
        self.BankID=tou(BankID)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LastFragment', 'RequestID', 'UserID', 'TradeTime', 'DeviceID', 'TradeDate', 'BrokerID', 'TradingDay', 'SessionID', 'BankSerial', 'OperNo', 'BrokerIDByBank', 'TradeCode', 'InstallID', 'Message', 'BankID', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('BrokerID', u'期商代码'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('InstallID', u'安装编号'),('Message', u'交易核心给银期报盘的消息'),('BankID', u'银行代码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInstrumentField:
    def __init__(self, ExchangeInstID="", InstrumentID="", ExchangeID="", ProductID=""):
        self.ExchangeInstID=tou(ExchangeInstID)
        self.InstrumentID=tou(InstrumentID)
        self.ExchangeID=tou(ExchangeID)
        self.ProductID=tou(ProductID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeInstID', 'InstrumentID', 'ExchangeID', 'ProductID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeInstID', u'合约在交易所的代码'),('InstrumentID', u'合约代码'),('ExchangeID', u'交易所代码'),('ProductID', u'产品代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataAveragePriceField:
    def __init__(self, AveragePrice=0):
        self.AveragePrice=AveragePrice
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AveragePrice']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('AveragePrice', u'当日均价')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcContractBankField:
    def __init__(self, BankID="", BrokerID="", BankBrchID="", BankName=""):
        self.BankID=tou(BankID)
        self.BrokerID=tou(BrokerID)
        self.BankBrchID=tou(BankBrchID)
        self.BankName=tou(BankName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankID', 'BrokerID', 'BankBrchID', 'BankName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankID', u'银行代码'),('BrokerID', u'经纪公司代码'),('BankBrchID', u'银行分中心代码'),('BankName', u'银行名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqDayEndFileReadyField:
    def __init__(self, LastFragment='0', FileBusinessCode='0', TradeTime="", TradeDate="", BrokerID="", TradingDay="", SessionID=0, BankSerial="", TradeCode="", BankID="", BankBranchID="", BrokerBranchID="", PlateSerial=0, Digest=""):
        self.LastFragment=tou(LastFragment)
        self.FileBusinessCode=tou(FileBusinessCode)
        self.TradeTime=tou(TradeTime)
        self.TradeDate=tou(TradeDate)
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.SessionID=SessionID
        self.BankSerial=tou(BankSerial)
        self.TradeCode=tou(TradeCode)
        self.BankID=tou(BankID)
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.Digest=tou(Digest)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'FileBusinessCode': {"'1'": '转账交易明细对账', "'f'": '协办存管银行资金监管数据', "'0'": '其他', "'e'": '存管银行备付金余额', "'4'": '期货账户信息变更明细对账', "'3'": '账户类交易明细对账', "'2'": '客户账户状态对账', "'7'": '客户资金余额对账结果', "'a'": '客户资金交收明细', "'6'": '客户销户结息明细对账', "'5'": '客户资金台账余额明细对账', "'d'": '总分平衡监管数据', "'9'": '客户结息净额明细', "'c'": '主体间资金交收汇总', "'8'": '其它对账异常结果文件', "'b'": '法人存管银行资金交收汇总'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LastFragment', 'FileBusinessCode', 'TradeTime', 'TradeDate', 'BrokerID', 'TradingDay', 'SessionID', 'BankSerial', 'TradeCode', 'BankID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LastFragment', u'最后分片标志'),('FileBusinessCode', u'文件业务功能'),('TradeTime', u'交易时间'),('TradeDate', u'交易日期'),('BrokerID', u'期商代码'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BankSerial', u'银行流水号'),('TradeCode', u'业务功能码'),('BankID', u'银行代码'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['LastFragment', 'FileBusinessCode']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferHeaderField:
    def __init__(self, RequestID=0, TradeTime="", DeviceID="", TradeDate="", SessionID=0, TradeSerial="", BankBrchID="", RecordNum="", Version="", TradeCode="", FutureID="", BankID="", OperNo=""):
        self.RequestID=RequestID
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.TradeDate=tou(TradeDate)
        self.SessionID=SessionID
        self.TradeSerial=tou(TradeSerial)
        self.BankBrchID=tou(BankBrchID)
        self.RecordNum=tou(RecordNum)
        self.Version=tou(Version)
        self.TradeCode=tou(TradeCode)
        self.FutureID=tou(FutureID)
        self.BankID=tou(BankID)
        self.OperNo=tou(OperNo)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['RequestID', 'TradeTime', 'DeviceID', 'TradeDate', 'SessionID', 'TradeSerial', 'BankBrchID', 'RecordNum', 'Version', 'TradeCode', 'FutureID', 'BankID', 'OperNo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('RequestID', u'请求编号，N/A'),('TradeTime', u'交易时间，必填，格式：hhmmss'),('DeviceID', u'交易设备类型，N/A'),('TradeDate', u'交易日期，必填，格式：yyyymmdd'),('SessionID', u'会话编号，N/A'),('TradeSerial', u'发起方流水号，N/A'),('BankBrchID', u'银行分中心代码，根据查询银行得到，必填'),('RecordNum', u'记录数，N/A'),('Version', u'版本号，常量，1.0'),('TradeCode', u'交易代码，必填'),('FutureID', u'期货公司代码，必填'),('BankID', u'银行代码，根据查询银行得到，必填'),('OperNo', u'操作员，N/A')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcParkedOrderActionField:
    def __init__(self, OrderSysID="", ParkedOrderActionID="", RequestID=0, UserType='0', SessionID=0, BrokerID="", FrontID=0, InvestorID="", Status='1', ActionFlag='0', ErrorID=0, InstrumentID="", LimitPrice=0, OrderActionRef=0, VolumeChange=0, ErrorMsg="", ExchangeID="", UserID="", OrderRef=""):
        self.OrderSysID=tou(OrderSysID)
        self.ParkedOrderActionID=tou(ParkedOrderActionID)
        self.RequestID=RequestID
        self.UserType=tou(UserType)
        self.SessionID=SessionID
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.InvestorID=tou(InvestorID)
        self.Status=tou(Status)
        self.ActionFlag=tou(ActionFlag)
        self.ErrorID=ErrorID
        self.InstrumentID=tou(InstrumentID)
        self.LimitPrice=LimitPrice
        self.OrderActionRef=OrderActionRef
        self.VolumeChange=VolumeChange
        self.ErrorMsg=tou(ErrorMsg)
        self.ExchangeID=tou(ExchangeID)
        self.UserID=tou(UserID)
        self.OrderRef=tou(OrderRef)
        self.vcmap={'ActionFlag': {"'3'": '修改', "'0'": '删除'}, 'UserType': {"'1'": '操作员', "'0'": '投资者', "'2'": '管理员'}, 'Status': {"'1'": '未发送', "'3'": '已删除', "'2'": '已发送'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderSysID', 'ParkedOrderActionID', 'RequestID', 'UserType', 'SessionID', 'BrokerID', 'FrontID', 'InvestorID', 'Status', 'ActionFlag', 'ErrorID', 'InstrumentID', 'LimitPrice', 'OrderActionRef', 'VolumeChange', 'ErrorMsg', 'ExchangeID', 'UserID', 'OrderRef']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderSysID', u'报单编号'),('ParkedOrderActionID', u'预埋撤单单编号'),('RequestID', u'请求编号'),('UserType', u'用户类型'),('SessionID', u'会话编号'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('InvestorID', u'投资者代码'),('Status', u'预埋撤单状态'),('ActionFlag', u'操作标志'),('ErrorID', u'错误代码'),('InstrumentID', u'合约代码'),('LimitPrice', u'价格'),('OrderActionRef', u'报单操作引用'),('VolumeChange', u'数量变化'),('ErrorMsg', u'错误信息'),('ExchangeID', u'交易所代码'),('UserID', u'用户代码'),('OrderRef', u'报单引用')]])
    def getval(self, n):
        if n in ['UserType', 'Status', 'ActionFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerSyncField:
    def __init__(self, BrokerID=""):
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInvestorPositionField:
    def __init__(self, BrokerID="", InvestorID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcVerifyFuturePasswordField:
    def __init__(self, Password="", LastFragment='0', TradeTime="", InstallID=0, TradeDate="", BrokerID="", TradingDay="", SessionID=0, AccountID="", BankSerial="", TradeCode="", BankPassWord="", BankID="", TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0, BankAccount=""):
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.TradeTime=tou(TradeTime)
        self.InstallID=InstallID
        self.TradeDate=tou(TradeDate)
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.SessionID=SessionID
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.TradeCode=tou(TradeCode)
        self.BankPassWord=tou(BankPassWord)
        self.BankID=tou(BankID)
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.BankAccount=tou(BankAccount)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'LastFragment', 'TradeTime', 'InstallID', 'TradeDate', 'BrokerID', 'TradingDay', 'SessionID', 'AccountID', 'BankSerial', 'TradeCode', 'BankPassWord', 'BankID', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial', 'BankAccount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('TradeTime', u'交易时间'),('InstallID', u'安装编号'),('TradeDate', u'交易日期'),('BrokerID', u'期商代码'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('TradeCode', u'业务功能码'),('BankPassWord', u'银行密码'),('BankID', u'银行代码'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号'),('BankAccount', u'银行帐号')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcManualSyncBrokerUserOTPField:
    def __init__(self, SecondOTP="", BrokerID="", OTPType='0', UserID="", FirstOTP=""):
        self.SecondOTP=tou(SecondOTP)
        self.BrokerID=tou(BrokerID)
        self.OTPType=tou(OTPType)
        self.UserID=tou(UserID)
        self.FirstOTP=tou(FirstOTP)
        self.vcmap={'OTPType': {"'1'": '时间令牌', "'0'": '无动态令牌'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SecondOTP', 'BrokerID', 'OTPType', 'UserID', 'FirstOTP']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('SecondOTP', u'第二个动态密码'),('BrokerID', u'经纪公司代码'),('OTPType', u'动态令牌类型'),('UserID', u'用户代码'),('FirstOTP', u'第一个动态密码')]])
    def getval(self, n):
        if n in ['OTPType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryBrokerUserFunctionField:
    def __init__(self, BrokerID="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInputOrderField:
    def __init__(self, OrderPriceType='1', Direction='0', BrokerID="", InvestorID="", MinVolume=0, ForceCloseReason='0', VolumeTotalOriginal=0, InstrumentID="", ContingentCondition='1', UserForceClose=0, StopPrice=0, RequestID=0, IsAutoSuspend=0, IsSwapOrder=0, UserID="", GTDDate="", BusinessUnit="", LimitPrice=0, OrderRef="", CombHedgeFlag="", VolumeCondition='1', CombOffsetFlag="", TimeCondition='1'):
        self.OrderPriceType=tou(OrderPriceType)
        self.Direction=tou(Direction)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.MinVolume=MinVolume
        self.ForceCloseReason=tou(ForceCloseReason)
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.InstrumentID=tou(InstrumentID)
        self.ContingentCondition=tou(ContingentCondition)
        self.UserForceClose=UserForceClose
        self.StopPrice=StopPrice
        self.RequestID=RequestID
        self.IsAutoSuspend=IsAutoSuspend
        self.IsSwapOrder=IsSwapOrder
        self.UserID=tou(UserID)
        self.GTDDate=tou(GTDDate)
        self.BusinessUnit=tou(BusinessUnit)
        self.LimitPrice=LimitPrice
        self.OrderRef=tou(OrderRef)
        self.CombHedgeFlag=tou(CombHedgeFlag)
        self.VolumeCondition=tou(VolumeCondition)
        self.CombOffsetFlag=tou(CombOffsetFlag)
        self.TimeCondition=tou(TimeCondition)
        self.vcmap={'VolumeCondition': {"'1'": '任何数量', "'3'": '全部数量', "'2'": '最小数量'}, 'OrderPriceType': {"'1'": '任意价', "'F'": '买一价浮动上浮3个ticks', "'E'": '买一价浮动上浮2个ticks', "'4'": '最新价', "'3'": '最优价', "'2'": '限价', "'7'": '最新价浮动上浮3个ticks', "'A'": '卖一价浮动上浮2个ticks', "'6'": '最新价浮动上浮2个ticks', "'5'": '最新价浮动上浮1个ticks', "'D'": '买一价浮动上浮1个ticks', "'9'": '卖一价浮动上浮1个ticks', "'C'": '买一价', "'8'": '卖一价', "'B'": '卖一价浮动上浮3个ticks'}, 'ContingentCondition': {"'1'": '立即', "'F'": '买一价小于条件价', "'E'": '买一价大于等于条件价', "'4'": '预埋单', "'3'": '止赢', "'H'": '买一价小于等于条件价', "'2'": '止损', "'7'": '最新价小于条件价', "'A'": '卖一价大于等于条件价', "'6'": '最新价大于等于条件价', "'5'": '最新价大于条件价', "'D'": '买一价大于条件价', "'9'": '卖一价大于条件价', "'C'": '卖一价小于等于条件价', "'8'": '最新价小于等于条件价', "'B'": '卖一价小于条件价'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'ForceCloseReason': {"'7'": '自然人临近交割', "'1'": '资金不足', "'6'": '其它', "'0'": '非强平', "'5'": '违规', "'4'": '持仓非整数倍', "'3'": '会员超仓', "'2'": '客户超仓'}, 'TimeCondition': {"'1'": '立即完成，否则撤销', "'6'": '集合竞价有效', "'5'": '撤销前有效', "'4'": '指定日期前有效', "'3'": '当日有效', "'2'": '本节有效'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderPriceType', 'Direction', 'BrokerID', 'InvestorID', 'MinVolume', 'ForceCloseReason', 'VolumeTotalOriginal', 'InstrumentID', 'ContingentCondition', 'UserForceClose', 'StopPrice', 'RequestID', 'IsAutoSuspend', 'IsSwapOrder', 'UserID', 'GTDDate', 'BusinessUnit', 'LimitPrice', 'OrderRef', 'CombHedgeFlag', 'VolumeCondition', 'CombOffsetFlag', 'TimeCondition']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderPriceType', u'报单价格条件'),('Direction', u'买卖方向'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('MinVolume', u'最小成交量'),('ForceCloseReason', u'强平原因'),('VolumeTotalOriginal', u'数量'),('InstrumentID', u'合约代码'),('ContingentCondition', u'触发条件'),('UserForceClose', u'用户强评标志'),('StopPrice', u'止损价'),('RequestID', u'请求编号'),('IsAutoSuspend', u'自动挂起标志'),('IsSwapOrder', u'互换单标志'),('UserID', u'用户代码'),('GTDDate', u'GTD日期'),('BusinessUnit', u'业务单元'),('LimitPrice', u'价格'),('OrderRef', u'报单引用'),('CombHedgeFlag', u'组合投机套保标志'),('VolumeCondition', u'成交量类型'),('CombOffsetFlag', u'组合开平标志'),('TimeCondition', u'有效期类型')]])
    def getval(self, n):
        if n in ['OrderPriceType', 'Direction', 'ForceCloseReason', 'ContingentCondition', 'VolumeCondition', 'TimeCondition']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferQryBankReqField:
    def __init__(self, CurrencyCode="", FutureAccount="", FutureAccPwd="", FuturePwdFlag='0'):
        self.CurrencyCode=tou(CurrencyCode)
        self.FutureAccount=tou(FutureAccount)
        self.FutureAccPwd=tou(FutureAccPwd)
        self.FuturePwdFlag=tou(FuturePwdFlag)
        self.vcmap={'FuturePwdFlag': {"'1'": '核对', "'0'": '不核对'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CurrencyCode', 'FutureAccount', 'FutureAccPwd', 'FuturePwdFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CurrencyCode', u'币种：RMB-人民币 USD-美圆 HKD-港元'),('FutureAccount', u'期货资金账户'),('FutureAccPwd', u'密码'),('FuturePwdFlag', u'密码标志')]])
    def getval(self, n):
        if n in ['FuturePwdFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryOrderField:
    def __init__(self, OrderSysID="", InstrumentID="", InsertTimeEnd="", BrokerID="", InvestorID="", ExchangeID="", InsertTimeStart=""):
        self.OrderSysID=tou(OrderSysID)
        self.InstrumentID=tou(InstrumentID)
        self.InsertTimeEnd=tou(InsertTimeEnd)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.InsertTimeStart=tou(InsertTimeStart)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderSysID', 'InstrumentID', 'InsertTimeEnd', 'BrokerID', 'InvestorID', 'ExchangeID', 'InsertTimeStart']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderSysID', u'报单编号'),('InstrumentID', u'合约代码'),('InsertTimeEnd', u'结束时间'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('InsertTimeStart', u'开始时间')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataBid45Field:
    def __init__(self, BidPrice5=0, BidPrice4=0, BidVolume5=0, BidVolume4=0):
        self.BidPrice5=BidPrice5
        self.BidPrice4=BidPrice4
        self.BidVolume5=BidVolume5
        self.BidVolume4=BidVolume4
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BidPrice5', 'BidPrice4', 'BidVolume5', 'BidVolume4']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BidPrice5', u'申买价五'),('BidPrice4', u'申买价四'),('BidVolume5', u'申买量五'),('BidVolume4', u'申买量四')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqRepealField:
    def __init__(self, TradingDay="", DeviceID="", BrokerID="", SessionID=0, IdentifiedCardNo="", IdCardType='0', FutureRepealSerial=0, FutureFetchAmount=0, BankID="", BankPwdFlag='0', BankRepealFlag='0', BankAccount="", BankSecuAcc="", LastFragment='0', PlateRepealSerial=0, TradeDate="", CustFee=0, AccountID="", BankSerial="", OperNo="", BrokerFee=0, CustomerName="", BankPassWord="", Message="", BankBranchID="", Digest="", PlateSerial=0, RepealedTimes=0, TransferStatus='0', TradeAmount=0, TradeTime="", FutureSerial=0, InstallID=0, SecuPwdFlag='0', BrokerRepealFlag='0', BankRepealSerial="", VerifyCertNoFlag='0', RepealTimeInterval=0, CurrencyID="", BankSecuAccType='1', Password="", RequestID=0, BankAccType='1', BrokerBranchID="", UserID="", CustType='0', BrokerIDByBank="", TradeCode="", FeePayFlag='0', TID=0):
        self.TradingDay=tou(TradingDay)
        self.DeviceID=tou(DeviceID)
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.FutureRepealSerial=FutureRepealSerial
        self.FutureFetchAmount=FutureFetchAmount
        self.BankID=tou(BankID)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.BankRepealFlag=tou(BankRepealFlag)
        self.BankAccount=tou(BankAccount)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.LastFragment=tou(LastFragment)
        self.PlateRepealSerial=PlateRepealSerial
        self.TradeDate=tou(TradeDate)
        self.CustFee=CustFee
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.OperNo=tou(OperNo)
        self.BrokerFee=BrokerFee
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.Message=tou(Message)
        self.BankBranchID=tou(BankBranchID)
        self.Digest=tou(Digest)
        self.PlateSerial=PlateSerial
        self.RepealedTimes=RepealedTimes
        self.TransferStatus=tou(TransferStatus)
        self.TradeAmount=TradeAmount
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.InstallID=InstallID
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.BrokerRepealFlag=tou(BrokerRepealFlag)
        self.BankRepealSerial=tou(BankRepealSerial)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.RepealTimeInterval=RepealTimeInterval
        self.CurrencyID=tou(CurrencyID)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.Password=tou(Password)
        self.RequestID=RequestID
        self.BankAccType=tou(BankAccType)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.FeePayFlag=tou(FeePayFlag)
        self.TID=TID
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'BrokerRepealFlag': {"'1'": '期商待自动冲正', "'0'": '期商无需自动冲正', "'2'": '期商已自动冲正'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'FeePayFlag': {"'1'": '由发送方支付费用', "'0'": '由受益方支付费用', "'2'": '由发送方支付发起的费用，受益方支付接受的费用'}, 'TransferStatus': {"'1'": '被冲正', "'0'": '正常'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankRepealFlag': {"'1'": '银行待自动冲正', "'0'": '银行无需自动冲正', "'2'": '银行已自动冲正'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DeviceID', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'FutureRepealSerial', 'FutureFetchAmount', 'BankID', 'BankPwdFlag', 'BankRepealFlag', 'BankAccount', 'BankSecuAcc', 'LastFragment', 'PlateRepealSerial', 'TradeDate', 'CustFee', 'AccountID', 'BankSerial', 'OperNo', 'BrokerFee', 'CustomerName', 'BankPassWord', 'Message', 'BankBranchID', 'Digest', 'PlateSerial', 'RepealedTimes', 'TransferStatus', 'TradeAmount', 'TradeTime', 'FutureSerial', 'InstallID', 'SecuPwdFlag', 'BrokerRepealFlag', 'BankRepealSerial', 'VerifyCertNoFlag', 'RepealTimeInterval', 'CurrencyID', 'BankSecuAccType', 'Password', 'RequestID', 'BankAccType', 'BrokerBranchID', 'UserID', 'CustType', 'BrokerIDByBank', 'TradeCode', 'FeePayFlag', 'TID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易系统日期'),('DeviceID', u'渠道标志'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('FutureRepealSerial', u'被冲正期货流水号'),('FutureFetchAmount', u'期货可取金额'),('BankID', u'银行代码'),('BankPwdFlag', u'银行密码标志'),('BankRepealFlag', u'银行冲正标志'),('BankAccount', u'银行帐号'),('BankSecuAcc', u'期货单位帐号'),('LastFragment', u'最后分片标志'),('PlateRepealSerial', u'被冲正平台流水号'),('TradeDate', u'交易日期'),('CustFee', u'应收客户费用'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('BrokerFee', u'应收期货公司费用'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('Message', u'发送方给接收方的消息'),('BankBranchID', u'银行分支机构代码'),('Digest', u'摘要'),('PlateSerial', u'银期平台消息流水号'),('RepealedTimes', u'已经冲正次数'),('TransferStatus', u'转账交易状态'),('TradeAmount', u'转帐金额'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('BrokerRepealFlag', u'期商冲正标志'),('BankRepealSerial', u'被冲正银行流水号'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('RepealTimeInterval', u'冲正时间间隔'),('CurrencyID', u'币种代码'),('BankSecuAccType', u'期货单位帐号类型'),('Password', u'期货密码'),('RequestID', u'请求编号'),('BankAccType', u'银行帐号类型'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('CustType', u'客户类型'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('FeePayFlag', u'费用支付标志'),('TID', u'交易ID')]])
    def getval(self, n):
        if n in ['IdCardType', 'BankPwdFlag', 'BankRepealFlag', 'LastFragment', 'TransferStatus', 'SecuPwdFlag', 'BrokerRepealFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'BankAccType', 'CustType', 'FeePayFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcAccountregisterField:
    def __init__(self, RegDate="", OpenOrDestroy='1', TradeDay="", CustType='0', IdCardType='0', IdentifiedCardNo="", AccountID="", TID=0, CustomerName="", BankAccType='1', OutDate="", BankID="", CurrencyID="", BankBranchID="", BrokerBranchID="", BrokerID="", BankAccount=""):
        self.RegDate=tou(RegDate)
        self.OpenOrDestroy=tou(OpenOrDestroy)
        self.TradeDay=tou(TradeDay)
        self.CustType=tou(CustType)
        self.IdCardType=tou(IdCardType)
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.AccountID=tou(AccountID)
        self.TID=TID
        self.CustomerName=tou(CustomerName)
        self.BankAccType=tou(BankAccType)
        self.OutDate=tou(OutDate)
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.BrokerID=tou(BrokerID)
        self.BankAccount=tou(BankAccount)
        self.vcmap={'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'OpenOrDestroy': {"'1'": '开户', "'0'": '销户'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['RegDate', 'OpenOrDestroy', 'TradeDay', 'CustType', 'IdCardType', 'IdentifiedCardNo', 'AccountID', 'TID', 'CustomerName', 'BankAccType', 'OutDate', 'BankID', 'CurrencyID', 'BankBranchID', 'BrokerBranchID', 'BrokerID', 'BankAccount']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('RegDate', u'签约日期'),('OpenOrDestroy', u'开销户类别'),('TradeDay', u'交易日期'),('CustType', u'客户类型'),('IdCardType', u'证件类型'),('IdentifiedCardNo', u'证件号码'),('AccountID', u'投资者帐号'),('TID', u'交易ID'),('CustomerName', u'客户姓名'),('BankAccType', u'银行帐号类型'),('OutDate', u'解约日期'),('BankID', u'银行编码'),('CurrencyID', u'币种代码'),('BankBranchID', u'银行分支机构编码'),('BrokerBranchID', u'期货公司分支机构编码'),('BrokerID', u'期货公司编码'),('BankAccount', u'银行帐号')]])
    def getval(self, n):
        if n in ['OpenOrDestroy', 'CustType', 'IdCardType', 'BankAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcParkedOrderField:
    def __init__(self, OrderPriceType='1', Direction='0', BrokerID="", InvestorID="", MinVolume=0, Status='1', ForceCloseReason='0', VolumeTotalOriginal=0, InstrumentID="", ContingentCondition='1', UserForceClose=0, ErrorMsg="", StopPrice=0, RequestID=0, IsAutoSuspend=0, IsSwapOrder=0, UserType='0', ExchangeID="", UserID="", GTDDate="", ErrorID=0, BusinessUnit="", ParkedOrderID="", LimitPrice=0, OrderRef="", CombHedgeFlag="", VolumeCondition='1', CombOffsetFlag="", TimeCondition='1'):
        self.OrderPriceType=tou(OrderPriceType)
        self.Direction=tou(Direction)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.MinVolume=MinVolume
        self.Status=tou(Status)
        self.ForceCloseReason=tou(ForceCloseReason)
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.InstrumentID=tou(InstrumentID)
        self.ContingentCondition=tou(ContingentCondition)
        self.UserForceClose=UserForceClose
        self.ErrorMsg=tou(ErrorMsg)
        self.StopPrice=StopPrice
        self.RequestID=RequestID
        self.IsAutoSuspend=IsAutoSuspend
        self.IsSwapOrder=IsSwapOrder
        self.UserType=tou(UserType)
        self.ExchangeID=tou(ExchangeID)
        self.UserID=tou(UserID)
        self.GTDDate=tou(GTDDate)
        self.ErrorID=ErrorID
        self.BusinessUnit=tou(BusinessUnit)
        self.ParkedOrderID=tou(ParkedOrderID)
        self.LimitPrice=LimitPrice
        self.OrderRef=tou(OrderRef)
        self.CombHedgeFlag=tou(CombHedgeFlag)
        self.VolumeCondition=tou(VolumeCondition)
        self.CombOffsetFlag=tou(CombOffsetFlag)
        self.TimeCondition=tou(TimeCondition)
        self.vcmap={'VolumeCondition': {"'1'": '任何数量', "'3'": '全部数量', "'2'": '最小数量'}, 'OrderPriceType': {"'1'": '任意价', "'F'": '买一价浮动上浮3个ticks', "'E'": '买一价浮动上浮2个ticks', "'4'": '最新价', "'3'": '最优价', "'2'": '限价', "'7'": '最新价浮动上浮3个ticks', "'A'": '卖一价浮动上浮2个ticks', "'6'": '最新价浮动上浮2个ticks', "'5'": '最新价浮动上浮1个ticks', "'D'": '买一价浮动上浮1个ticks', "'9'": '卖一价浮动上浮1个ticks', "'C'": '买一价', "'8'": '卖一价', "'B'": '卖一价浮动上浮3个ticks'}, 'ContingentCondition': {"'1'": '立即', "'F'": '买一价小于条件价', "'E'": '买一价大于等于条件价', "'4'": '预埋单', "'3'": '止赢', "'H'": '买一价小于等于条件价', "'2'": '止损', "'7'": '最新价小于条件价', "'A'": '卖一价大于等于条件价', "'6'": '最新价大于等于条件价', "'5'": '最新价大于条件价', "'D'": '买一价大于条件价', "'9'": '卖一价大于条件价', "'C'": '卖一价小于等于条件价', "'8'": '最新价小于等于条件价', "'B'": '卖一价小于条件价'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'UserType': {"'1'": '操作员', "'0'": '投资者', "'2'": '管理员'}, 'ForceCloseReason': {"'7'": '自然人临近交割', "'1'": '资金不足', "'6'": '其它', "'0'": '非强平', "'5'": '违规', "'4'": '持仓非整数倍', "'3'": '会员超仓', "'2'": '客户超仓'}, 'Status': {"'1'": '未发送', "'3'": '已删除', "'2'": '已发送'}, 'TimeCondition': {"'1'": '立即完成，否则撤销', "'6'": '集合竞价有效', "'5'": '撤销前有效', "'4'": '指定日期前有效', "'3'": '当日有效', "'2'": '本节有效'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderPriceType', 'Direction', 'BrokerID', 'InvestorID', 'MinVolume', 'Status', 'ForceCloseReason', 'VolumeTotalOriginal', 'InstrumentID', 'ContingentCondition', 'UserForceClose', 'ErrorMsg', 'StopPrice', 'RequestID', 'IsAutoSuspend', 'IsSwapOrder', 'UserType', 'ExchangeID', 'UserID', 'GTDDate', 'ErrorID', 'BusinessUnit', 'ParkedOrderID', 'LimitPrice', 'OrderRef', 'CombHedgeFlag', 'VolumeCondition', 'CombOffsetFlag', 'TimeCondition']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderPriceType', u'报单价格条件'),('Direction', u'买卖方向'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('MinVolume', u'最小成交量'),('Status', u'预埋单状态'),('ForceCloseReason', u'强平原因'),('VolumeTotalOriginal', u'数量'),('InstrumentID', u'合约代码'),('ContingentCondition', u'触发条件'),('UserForceClose', u'用户强评标志'),('ErrorMsg', u'错误信息'),('StopPrice', u'止损价'),('RequestID', u'请求编号'),('IsAutoSuspend', u'自动挂起标志'),('IsSwapOrder', u'互换单标志'),('UserType', u'用户类型'),('ExchangeID', u'交易所代码'),('UserID', u'用户代码'),('GTDDate', u'GTD日期'),('ErrorID', u'错误代码'),('BusinessUnit', u'业务单元'),('ParkedOrderID', u'预埋报单编号'),('LimitPrice', u'价格'),('OrderRef', u'报单引用'),('CombHedgeFlag', u'组合投机套保标志'),('VolumeCondition', u'成交量类型'),('CombOffsetFlag', u'组合开平标志'),('TimeCondition', u'有效期类型')]])
    def getval(self, n):
        if n in ['OrderPriceType', 'Direction', 'Status', 'ForceCloseReason', 'ContingentCondition', 'UserType', 'VolumeCondition', 'TimeCondition']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcLinkManField:
    def __init__(self, PersonName="", InvestorID="", Address="", Priority=0, Telephone="", BrokerID="", PersonType='1', ZipCode="", IdentifiedCardType='0', IdentifiedCardNo=""):
        self.PersonName=tou(PersonName)
        self.InvestorID=tou(InvestorID)
        self.Address=tou(Address)
        self.Priority=Priority
        self.Telephone=tou(Telephone)
        self.BrokerID=tou(BrokerID)
        self.PersonType=tou(PersonType)
        self.ZipCode=tou(ZipCode)
        self.IdentifiedCardType=tou(IdentifiedCardType)
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.vcmap={'PersonType': {"'1'": '指定下单人', "'4'": '结算单确认人', "'3'": '资金调拨人', "'2'": '开户授权人', "'7'": '投资者联系人', "'A'": '托（保）管机构法人代表', "'6'": '法人代表', "'5'": '法人', "'9'": '托（保）管人', "'C'": '托（保）管机构联系人', "'8'": '分户管理资产负责人', "'B'": '托（保）管机构开户授权人'}, 'IdentifiedCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['PersonName', 'InvestorID', 'Address', 'Priority', 'Telephone', 'BrokerID', 'PersonType', 'ZipCode', 'IdentifiedCardType', 'IdentifiedCardNo']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('PersonName', u'名称'),('InvestorID', u'投资者代码'),('Address', u'通讯地址'),('Priority', u'优先级'),('Telephone', u'联系电话'),('BrokerID', u'经纪公司代码'),('PersonType', u'联系人类型'),('ZipCode', u'邮政编码'),('IdentifiedCardType', u'证件类型'),('IdentifiedCardNo', u'证件号码')]])
    def getval(self, n):
        if n in ['PersonType', 'IdentifiedCardType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRemoveParkedOrderActionField:
    def __init__(self, ParkedOrderActionID="", BrokerID="", InvestorID=""):
        self.ParkedOrderActionID=tou(ParkedOrderActionID)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ParkedOrderActionID', 'BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ParkedOrderActionID', u'预埋撤单编号'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradeField:
    def __init__(self, TradeSource='0', InvestorID="", TradeID="", PriceSource='0', TradeTime="", ClientID="", ClearingPartID="", BrokerID="", OffsetFlag='0', TradeType='0', TraderID="", TradingRole='1', Price=0, OrderLocalID="", ExchangeInstID="", OrderSysID="", BrokerOrderSeq=0, SequenceNo=0, Volume=0, TradeDate="", UserID="", TradingDay="", InstrumentID="", ParticipantID="", SettlementID=0, Direction='0', BusinessUnit="", OrderRef="", HedgeFlag='1', ExchangeID=""):
        self.TradeSource=tou(TradeSource)
        self.InvestorID=tou(InvestorID)
        self.TradeID=tou(TradeID)
        self.PriceSource=tou(PriceSource)
        self.TradeTime=tou(TradeTime)
        self.ClientID=tou(ClientID)
        self.ClearingPartID=tou(ClearingPartID)
        self.BrokerID=tou(BrokerID)
        self.OffsetFlag=tou(OffsetFlag)
        self.TradeType=tou(TradeType)
        self.TraderID=tou(TraderID)
        self.TradingRole=tou(TradingRole)
        self.Price=Price
        self.OrderLocalID=tou(OrderLocalID)
        self.ExchangeInstID=tou(ExchangeInstID)
        self.OrderSysID=tou(OrderSysID)
        self.BrokerOrderSeq=BrokerOrderSeq
        self.SequenceNo=SequenceNo
        self.Volume=Volume
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.TradingDay=tou(TradingDay)
        self.InstrumentID=tou(InstrumentID)
        self.ParticipantID=tou(ParticipantID)
        self.SettlementID=SettlementID
        self.Direction=tou(Direction)
        self.BusinessUnit=tou(BusinessUnit)
        self.OrderRef=tou(OrderRef)
        self.HedgeFlag=tou(HedgeFlag)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={'TradeSource': {"'1'": '来自查询', "'0'": '来自交易所普通回报'}, 'TradingRole': {"'1'": '代理', "'3'": '做市商', "'2'": '自营'}, 'PriceSource': {"'1'": '买委托价', "'0'": '前成交价', "'2'": '卖委托价'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'OffsetFlag': {"'1'": '平仓', "'6'": '本地强平', "'0'": '开仓', "'5'": '强减', "'4'": '平昨', "'3'": '平今', "'2'": '强平'}, 'TradeType': {"'4'": '组合衍生成交', "'1'": '期权执行', "'3'": '期转现衍生成交', "'0'": '普通成交', "'2'": 'OTC成交'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeSource', 'InvestorID', 'TradeID', 'PriceSource', 'TradeTime', 'ClientID', 'ClearingPartID', 'BrokerID', 'OffsetFlag', 'TradeType', 'TraderID', 'TradingRole', 'Price', 'OrderLocalID', 'ExchangeInstID', 'OrderSysID', 'BrokerOrderSeq', 'SequenceNo', 'Volume', 'TradeDate', 'UserID', 'TradingDay', 'InstrumentID', 'ParticipantID', 'SettlementID', 'Direction', 'BusinessUnit', 'OrderRef', 'HedgeFlag', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeSource', u'成交来源'),('InvestorID', u'投资者代码'),('TradeID', u'成交编号'),('PriceSource', u'成交价来源'),('TradeTime', u'成交时间'),('ClientID', u'客户代码'),('ClearingPartID', u'结算会员编号'),('BrokerID', u'经纪公司代码'),('OffsetFlag', u'开平标志'),('TradeType', u'成交类型'),('TraderID', u'交易所交易员代码'),('TradingRole', u'交易角色'),('Price', u'价格'),('OrderLocalID', u'本地报单编号'),('ExchangeInstID', u'合约在交易所的代码'),('OrderSysID', u'报单编号'),('BrokerOrderSeq', u'经纪公司报单编号'),('SequenceNo', u'序号'),('Volume', u'数量'),('TradeDate', u'成交时期'),('UserID', u'用户代码'),('TradingDay', u'交易日'),('InstrumentID', u'合约代码'),('ParticipantID', u'会员代码'),('SettlementID', u'结算编号'),('Direction', u'买卖方向'),('BusinessUnit', u'业务单元'),('OrderRef', u'报单引用'),('HedgeFlag', u'投机套保标志'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in ['TradeSource', 'PriceSource', 'OffsetFlag', 'TradeType', 'TradingRole', 'Direction', 'HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqFutureSignOutField:
    def __init__(self, LastFragment='0', RequestID=0, UserID="", TradeTime="", DeviceID="", TradeDate="", BrokerID="", TradingDay="", SessionID=0, BankSerial="", OperNo="", BrokerIDByBank="", TradeCode="", InstallID=0, TID=0, BankID="", CurrencyID="", BankBranchID="", BrokerBranchID="", PlateSerial=0, Digest=""):
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.UserID=tou(UserID)
        self.TradeTime=tou(TradeTime)
        self.DeviceID=tou(DeviceID)
        self.TradeDate=tou(TradeDate)
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.SessionID=SessionID
        self.BankSerial=tou(BankSerial)
        self.OperNo=tou(OperNo)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.InstallID=InstallID
        self.TID=TID
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.Digest=tou(Digest)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LastFragment', 'RequestID', 'UserID', 'TradeTime', 'DeviceID', 'TradeDate', 'BrokerID', 'TradingDay', 'SessionID', 'BankSerial', 'OperNo', 'BrokerIDByBank', 'TradeCode', 'InstallID', 'TID', 'BankID', 'CurrencyID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial', 'Digest']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('UserID', u'用户标识'),('TradeTime', u'交易时间'),('DeviceID', u'渠道标志'),('TradeDate', u'交易日期'),('BrokerID', u'期商代码'),('TradingDay', u'交易系统日期'),('SessionID', u'会话号'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('InstallID', u'安装编号'),('TID', u'交易ID'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号'),('Digest', u'摘要')]])
    def getval(self, n):
        if n in ['LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcLoginForbiddenUserField:
    def __init__(self, BrokerID="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferBankToFutureRspField:
    def __init__(self, FutureAccount="", RetCode="", RetInfo="", TradeAmt=0, CustFee=0, CurrencyCode=""):
        self.FutureAccount=tou(FutureAccount)
        self.RetCode=tou(RetCode)
        self.RetInfo=tou(RetInfo)
        self.TradeAmt=TradeAmt
        self.CustFee=CustFee
        self.CurrencyCode=tou(CurrencyCode)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'RetCode', 'RetInfo', 'TradeAmt', 'CustFee', 'CurrencyCode']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FutureAccount', u'资金账户'),('RetCode', u'响应代码'),('RetInfo', u'响应信息'),('TradeAmt', u'转帐金额'),('CustFee', u'应收客户手续费'),('CurrencyCode', u'币种')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqUserLoginField:
    def __init__(self, Password="", UserProductInfo="", InterfaceProductInfo="", ClientIPAddress="", MacAddress="", BrokerID="", TradingDay="", UserID="", ProtocolInfo="", OneTimePassword=""):
        self.Password=tou(Password)
        self.UserProductInfo=tou(UserProductInfo)
        self.InterfaceProductInfo=tou(InterfaceProductInfo)
        self.ClientIPAddress=tou(ClientIPAddress)
        self.MacAddress=tou(MacAddress)
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.UserID=tou(UserID)
        self.ProtocolInfo=tou(ProtocolInfo)
        self.OneTimePassword=tou(OneTimePassword)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'UserProductInfo', 'InterfaceProductInfo', 'ClientIPAddress', 'MacAddress', 'BrokerID', 'TradingDay', 'UserID', 'ProtocolInfo', 'OneTimePassword']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('UserProductInfo', u'用户端产品信息'),('InterfaceProductInfo', u'接口端产品信息'),('ClientIPAddress', u'终端IP地址'),('MacAddress', u'Mac地址'),('BrokerID', u'经纪公司代码'),('TradingDay', u'交易日'),('UserID', u'用户代码'),('ProtocolInfo', u'协议信息'),('OneTimePassword', u'动态密码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReturnResultField:
    def __init__(self, DescrInfoForReturnCode="", ReturnCode=""):
        self.DescrInfoForReturnCode=tou(DescrInfoForReturnCode)
        self.ReturnCode=tou(ReturnCode)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['DescrInfoForReturnCode', 'ReturnCode']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('DescrInfoForReturnCode', u'返回码描述'),('ReturnCode', u'返回代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerTradingParamsField:
    def __init__(self, MarginPriceType='1', Algorithm='1', BrokerID="", InvestorID="", AvailIncludeCloseProfit='0'):
        self.MarginPriceType=tou(MarginPriceType)
        self.Algorithm=tou(Algorithm)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.AvailIncludeCloseProfit=tou(AvailIncludeCloseProfit)
        self.vcmap={'MarginPriceType': {"'4'": '开仓价', "'1'": '昨结算价', "'3'": '成交均价', "'2'": '最新价'}, 'Algorithm': {"'4'": '浮盈浮亏都不计算', "'1'": '浮盈浮亏都计算', "'3'": '浮盈计，浮亏不计', "'2'": '浮盈不计，浮亏计'}, 'AvailIncludeCloseProfit': {"'0'": '包含平仓盈利', "'2'": '不包含平仓盈利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MarginPriceType', 'Algorithm', 'BrokerID', 'InvestorID', 'AvailIncludeCloseProfit']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('MarginPriceType', u'保证金价格类型'),('Algorithm', u'盈亏算法'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('AvailIncludeCloseProfit', u'可用是否包含平仓盈利')]])
    def getval(self, n):
        if n in ['MarginPriceType', 'Algorithm', 'AvailIncludeCloseProfit']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcProductField:
    def __init__(self, MaxMarketOrderVolume=0, MinLimitOrderVolume=0, CloseDealType='0', PositionType='1', MinMarketOrderVolume=0, ProductName="", VolumeMultiple=0, PriceTick=0, PositionDateType='1', ProductClass='1', ProductID="", ExchangeID="", MaxLimitOrderVolume=0):
        self.MaxMarketOrderVolume=MaxMarketOrderVolume
        self.MinLimitOrderVolume=MinLimitOrderVolume
        self.CloseDealType=tou(CloseDealType)
        self.PositionType=tou(PositionType)
        self.MinMarketOrderVolume=MinMarketOrderVolume
        self.ProductName=tou(ProductName)
        self.VolumeMultiple=VolumeMultiple
        self.PriceTick=PriceTick
        self.PositionDateType=tou(PositionDateType)
        self.ProductClass=tou(ProductClass)
        self.ProductID=tou(ProductID)
        self.ExchangeID=tou(ExchangeID)
        self.MaxLimitOrderVolume=MaxLimitOrderVolume
        self.vcmap={'ProductClass': {"'4'": '即期', "'1'": '期货', "'3'": '组合', "'5'": '期转现', "'2'": '期权'}, 'PositionDateType': {"'1'": '使用历史持仓', "'2'": '不使用历史持仓'}, 'CloseDealType': {"'1'": '投机平仓优先', "'0'": '正常'}, 'PositionType': {"'1'": '净持仓', "'2'": '综合持仓'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MaxMarketOrderVolume', 'MinLimitOrderVolume', 'CloseDealType', 'PositionType', 'MinMarketOrderVolume', 'ProductName', 'VolumeMultiple', 'PriceTick', 'PositionDateType', 'ProductClass', 'ProductID', 'ExchangeID', 'MaxLimitOrderVolume']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('MaxMarketOrderVolume', u'市价单最大下单量'),('MinLimitOrderVolume', u'限价单最小下单量'),('CloseDealType', u'平仓处理类型'),('PositionType', u'持仓类型'),('MinMarketOrderVolume', u'市价单最小下单量'),('ProductName', u'产品名称'),('VolumeMultiple', u'合约数量乘数'),('PriceTick', u'最小变动价位'),('PositionDateType', u'持仓日期类型'),('ProductClass', u'产品类型'),('ProductID', u'产品代码'),('ExchangeID', u'交易所代码'),('MaxLimitOrderVolume', u'限价单最大下单量')]])
    def getval(self, n):
        if n in ['CloseDealType', 'PositionType', 'PositionDateType', 'ProductClass']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcUserIPField:
    def __init__(self, BrokerID="", MacAddress="", UserID="", IPAddress="", IPMask=""):
        self.BrokerID=tou(BrokerID)
        self.MacAddress=tou(MacAddress)
        self.UserID=tou(UserID)
        self.IPAddress=tou(IPAddress)
        self.IPMask=tou(IPMask)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'MacAddress', 'UserID', 'IPAddress', 'IPMask']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('MacAddress', u'Mac地址'),('UserID', u'用户代码'),('IPAddress', u'IP地址'),('IPMask', u'IP地址掩码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryFrontStatusField:
    def __init__(self, FrontID=0):
        self.FrontID=FrontID
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FrontID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FrontID', u'前置编号')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMDTraderOfferField:
    def __init__(self, Password="", ConnectDate="", ConnectTime="", TraderConnectStatus='1', ConnectRequestTime="", InstallID=0, BrokerID="", ExchangeID="", TraderID="", ParticipantID="", ConnectRequestDate="", LastReportDate="", MaxTradeID="", StartTime="", TradingDay="", MaxOrderMessageReference="", StartDate="", OrderLocalID="", LastReportTime=""):
        self.Password=tou(Password)
        self.ConnectDate=tou(ConnectDate)
        self.ConnectTime=tou(ConnectTime)
        self.TraderConnectStatus=tou(TraderConnectStatus)
        self.ConnectRequestTime=tou(ConnectRequestTime)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.ConnectRequestDate=tou(ConnectRequestDate)
        self.LastReportDate=tou(LastReportDate)
        self.MaxTradeID=tou(MaxTradeID)
        self.StartTime=tou(StartTime)
        self.TradingDay=tou(TradingDay)
        self.MaxOrderMessageReference=tou(MaxOrderMessageReference)
        self.StartDate=tou(StartDate)
        self.OrderLocalID=tou(OrderLocalID)
        self.LastReportTime=tou(LastReportTime)
        self.vcmap={'TraderConnectStatus': {"'4'": '订阅私有流', "'1'": '没有任何连接', "'3'": '已经发出合约查询请求', "'2'": '已经连接'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'ConnectDate', 'ConnectTime', 'TraderConnectStatus', 'ConnectRequestTime', 'InstallID', 'BrokerID', 'ExchangeID', 'TraderID', 'ParticipantID', 'ConnectRequestDate', 'LastReportDate', 'MaxTradeID', 'StartTime', 'TradingDay', 'MaxOrderMessageReference', 'StartDate', 'OrderLocalID', 'LastReportTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('ConnectDate', u'完成连接日期'),('ConnectTime', u'完成连接时间'),('TraderConnectStatus', u'交易所交易员连接状态'),('ConnectRequestTime', u'发出连接请求的时间'),('InstallID', u'安装编号'),('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码'),('ConnectRequestDate', u'发出连接请求的日期'),('LastReportDate', u'上次报告日期'),('MaxTradeID', u'本席位最大成交编号'),('StartTime', u'启动时间'),('TradingDay', u'交易日'),('MaxOrderMessageReference', u'本席位最大报单备拷'),('StartDate', u'启动日期'),('OrderLocalID', u'本地报单编号'),('LastReportTime', u'上次报告时间')]])
    def getval(self, n):
        if n in ['TraderConnectStatus']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryMDTraderOfferField:
    def __init__(self, ExchangeID="", TraderID="", ParticipantID=""):
        self.ExchangeID=tou(ExchangeID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqChangeAccountField:
    def __init__(self, MoneyAccountStatus='0', BankPwdFlag='0', CustType='0', TradeTime="", InstallID=0, BrokerID="", ZipCode="", SessionID=0, IdentifiedCardNo="", NewBankAccount="", SecuPwdFlag='0', EMail="", VerifyCertNoFlag='0', MobilePhone="", BankID="", CurrencyID="", AccountID="", BankAccount="", Digest="", Fax="", Password="", LastFragment='0', Gender='0', Address="", NewBankPassWord="", BrokerIDByBank="", CountryCode="", TradeDate="", TradingDay="", IdCardType='0', BankSerial="", BankAccType='1', TradeCode="", CustomerName="", BankBranchID="", BankPassWord="", TID=0, Telephone="", BrokerBranchID="", PlateSerial=0):
        self.MoneyAccountStatus=tou(MoneyAccountStatus)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.CustType=tou(CustType)
        self.TradeTime=tou(TradeTime)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.ZipCode=tou(ZipCode)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.NewBankAccount=tou(NewBankAccount)
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.EMail=tou(EMail)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.MobilePhone=tou(MobilePhone)
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.AccountID=tou(AccountID)
        self.BankAccount=tou(BankAccount)
        self.Digest=tou(Digest)
        self.Fax=tou(Fax)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.Gender=tou(Gender)
        self.Address=tou(Address)
        self.NewBankPassWord=tou(NewBankPassWord)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.CountryCode=tou(CountryCode)
        self.TradeDate=tou(TradeDate)
        self.TradingDay=tou(TradingDay)
        self.IdCardType=tou(IdCardType)
        self.BankSerial=tou(BankSerial)
        self.BankAccType=tou(BankAccType)
        self.TradeCode=tou(TradeCode)
        self.CustomerName=tou(CustomerName)
        self.BankBranchID=tou(BankBranchID)
        self.BankPassWord=tou(BankPassWord)
        self.TID=TID
        self.Telephone=tou(Telephone)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'Gender': {"'1'": '男', "'0'": '未知状态', "'2'": '女'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'MoneyAccountStatus': {"'1'": '销户', "'0'": '正常'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MoneyAccountStatus', 'BankPwdFlag', 'CustType', 'TradeTime', 'InstallID', 'BrokerID', 'ZipCode', 'SessionID', 'IdentifiedCardNo', 'NewBankAccount', 'SecuPwdFlag', 'EMail', 'VerifyCertNoFlag', 'MobilePhone', 'BankID', 'CurrencyID', 'AccountID', 'BankAccount', 'Digest', 'Fax', 'Password', 'LastFragment', 'Gender', 'Address', 'NewBankPassWord', 'BrokerIDByBank', 'CountryCode', 'TradeDate', 'TradingDay', 'IdCardType', 'BankSerial', 'BankAccType', 'TradeCode', 'CustomerName', 'BankBranchID', 'BankPassWord', 'TID', 'Telephone', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('MoneyAccountStatus', u'资金账户状态'),('BankPwdFlag', u'银行密码标志'),('CustType', u'客户类型'),('TradeTime', u'交易时间'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('ZipCode', u'邮编'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('NewBankAccount', u'新银行帐号'),('SecuPwdFlag', u'期货资金密码核对标志'),('EMail', u'电子邮件'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('MobilePhone', u'手机'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('Digest', u'摘要'),('Fax', u'传真'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('Gender', u'性别'),('Address', u'地址'),('NewBankPassWord', u'新银行密码'),('BrokerIDByBank', u'期货公司银行编码'),('CountryCode', u'国家代码'),('TradeDate', u'交易日期'),('TradingDay', u'交易系统日期'),('IdCardType', u'证件类型'),('BankSerial', u'银行流水号'),('BankAccType', u'银行帐号类型'),('TradeCode', u'业务功能码'),('CustomerName', u'客户姓名'),('BankBranchID', u'银行分支机构代码'),('BankPassWord', u'银行密码'),('TID', u'交易ID'),('Telephone', u'电话号码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['MoneyAccountStatus', 'BankPwdFlag', 'CustType', 'SecuPwdFlag', 'VerifyCertNoFlag', 'LastFragment', 'Gender', 'IdCardType', 'BankAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryLoginForbiddenUserField:
    def __init__(self, BrokerID="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerUserPasswordField:
    def __init__(self, Password="", BrokerID="", UserID=""):
        self.Password=tou(Password)
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferBankToFutureReqField:
    def __init__(self, FutureAccount="", FutureAccPwd="", CurrencyCode="", TradeAmt=0, CustFee=0, FuturePwdFlag='0'):
        self.FutureAccount=tou(FutureAccount)
        self.FutureAccPwd=tou(FutureAccPwd)
        self.CurrencyCode=tou(CurrencyCode)
        self.TradeAmt=TradeAmt
        self.CustFee=CustFee
        self.FuturePwdFlag=tou(FuturePwdFlag)
        self.vcmap={'FuturePwdFlag': {"'1'": '核对', "'0'": '不核对'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'FutureAccPwd', 'CurrencyCode', 'TradeAmt', 'CustFee', 'FuturePwdFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FutureAccount', u'期货资金账户'),('FutureAccPwd', u'密码'),('CurrencyCode', u'币种：RMB-人民币 USD-美圆 HKD-港元'),('TradeAmt', u'转账金额'),('CustFee', u'客户手续费'),('FuturePwdFlag', u'密码标志')]])
    def getval(self, n):
        if n in ['FuturePwdFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryBrokerUserField:
    def __init__(self, BrokerID="", UserID=""):
        self.BrokerID=tou(BrokerID)
        self.UserID=tou(UserID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'UserID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('UserID', u'用户代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcUserRightField:
    def __init__(self, BrokerID="", IsForbidden=0, UserID="", UserRightType='1'):
        self.BrokerID=tou(BrokerID)
        self.IsForbidden=IsForbidden
        self.UserID=tou(UserID)
        self.UserRightType=tou(UserRightType)
        self.vcmap={'UserRightType': {"'4'": '传真结算单', "'1'": '登录', "'3'": '邮寄结算单', "'5'": '条件单', "'2'": '银期转帐'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'IsForbidden', 'UserID', 'UserRightType']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('IsForbidden', u'是否禁止'),('UserID', u'用户代码'),('UserRightType', u'客户权限类型')]])
    def getval(self, n):
        if n in ['UserRightType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryHisOrderField:
    def __init__(self, OrderSysID="", SettlementID=0, InstrumentID="", TradingDay="", InsertTimeEnd="", BrokerID="", InvestorID="", ExchangeID="", InsertTimeStart=""):
        self.OrderSysID=tou(OrderSysID)
        self.SettlementID=SettlementID
        self.InstrumentID=tou(InstrumentID)
        self.TradingDay=tou(TradingDay)
        self.InsertTimeEnd=tou(InsertTimeEnd)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.InsertTimeStart=tou(InsertTimeStart)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderSysID', 'SettlementID', 'InstrumentID', 'TradingDay', 'InsertTimeEnd', 'BrokerID', 'InvestorID', 'ExchangeID', 'InsertTimeStart']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderSysID', u'报单编号'),('SettlementID', u'结算编号'),('InstrumentID', u'合约代码'),('TradingDay', u'交易日'),('InsertTimeEnd', u'结束时间'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('InsertTimeStart', u'开始时间')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcMarketDataAsk45Field:
    def __init__(self, AskPrice5=0, AskPrice4=0, AskVolume5=0, AskVolume4=0):
        self.AskPrice5=AskPrice5
        self.AskPrice4=AskPrice4
        self.AskVolume5=AskVolume5
        self.AskVolume4=AskVolume4
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['AskPrice5', 'AskPrice4', 'AskVolume5', 'AskVolume4']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('AskPrice5', u'申卖价五'),('AskPrice4', u'申卖价四'),('AskVolume5', u'申卖量五'),('AskVolume4', u'申卖量四')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryExchangeField:
    def __init__(self, ExchangeID=""):
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspRepealField:
    def __init__(self, TradingDay="", DeviceID="", ErrorID=0, BrokerID="", SessionID=0, IdentifiedCardNo="", IdCardType='0', FutureRepealSerial=0, FutureFetchAmount=0, BankID="", BankPwdFlag='0', BankRepealFlag='0', BankAccount="", BankSecuAcc="", LastFragment='0', PlateRepealSerial=0, TradeDate="", CustFee=0, AccountID="", BankSerial="", OperNo="", BrokerFee=0, CustomerName="", BankPassWord="", Message="", BankBranchID="", Digest="", PlateSerial=0, RepealedTimes=0, TransferStatus='0', TradeAmount=0, TradeTime="", FutureSerial=0, InstallID=0, SecuPwdFlag='0', BrokerRepealFlag='0', BankRepealSerial="", VerifyCertNoFlag='0', RepealTimeInterval=0, CurrencyID="", ErrorMsg="", BankSecuAccType='1', Password="", RequestID=0, BankAccType='1', BrokerBranchID="", UserID="", CustType='0', BrokerIDByBank="", TradeCode="", FeePayFlag='0', TID=0):
        self.TradingDay=tou(TradingDay)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.FutureRepealSerial=FutureRepealSerial
        self.FutureFetchAmount=FutureFetchAmount
        self.BankID=tou(BankID)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.BankRepealFlag=tou(BankRepealFlag)
        self.BankAccount=tou(BankAccount)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.LastFragment=tou(LastFragment)
        self.PlateRepealSerial=PlateRepealSerial
        self.TradeDate=tou(TradeDate)
        self.CustFee=CustFee
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.OperNo=tou(OperNo)
        self.BrokerFee=BrokerFee
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.Message=tou(Message)
        self.BankBranchID=tou(BankBranchID)
        self.Digest=tou(Digest)
        self.PlateSerial=PlateSerial
        self.RepealedTimes=RepealedTimes
        self.TransferStatus=tou(TransferStatus)
        self.TradeAmount=TradeAmount
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.InstallID=InstallID
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.BrokerRepealFlag=tou(BrokerRepealFlag)
        self.BankRepealSerial=tou(BankRepealSerial)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.RepealTimeInterval=RepealTimeInterval
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.Password=tou(Password)
        self.RequestID=RequestID
        self.BankAccType=tou(BankAccType)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.FeePayFlag=tou(FeePayFlag)
        self.TID=TID
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'BrokerRepealFlag': {"'1'": '期商待自动冲正', "'0'": '期商无需自动冲正', "'2'": '期商已自动冲正'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'FeePayFlag': {"'1'": '由发送方支付费用', "'0'": '由受益方支付费用', "'2'": '由发送方支付发起的费用，受益方支付接受的费用'}, 'TransferStatus': {"'1'": '被冲正', "'0'": '正常'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankRepealFlag': {"'1'": '银行待自动冲正', "'0'": '银行无需自动冲正', "'2'": '银行已自动冲正'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DeviceID', 'ErrorID', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'FutureRepealSerial', 'FutureFetchAmount', 'BankID', 'BankPwdFlag', 'BankRepealFlag', 'BankAccount', 'BankSecuAcc', 'LastFragment', 'PlateRepealSerial', 'TradeDate', 'CustFee', 'AccountID', 'BankSerial', 'OperNo', 'BrokerFee', 'CustomerName', 'BankPassWord', 'Message', 'BankBranchID', 'Digest', 'PlateSerial', 'RepealedTimes', 'TransferStatus', 'TradeAmount', 'TradeTime', 'FutureSerial', 'InstallID', 'SecuPwdFlag', 'BrokerRepealFlag', 'BankRepealSerial', 'VerifyCertNoFlag', 'RepealTimeInterval', 'CurrencyID', 'ErrorMsg', 'BankSecuAccType', 'Password', 'RequestID', 'BankAccType', 'BrokerBranchID', 'UserID', 'CustType', 'BrokerIDByBank', 'TradeCode', 'FeePayFlag', 'TID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易系统日期'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('FutureRepealSerial', u'被冲正期货流水号'),('FutureFetchAmount', u'期货可取金额'),('BankID', u'银行代码'),('BankPwdFlag', u'银行密码标志'),('BankRepealFlag', u'银行冲正标志'),('BankAccount', u'银行帐号'),('BankSecuAcc', u'期货单位帐号'),('LastFragment', u'最后分片标志'),('PlateRepealSerial', u'被冲正平台流水号'),('TradeDate', u'交易日期'),('CustFee', u'应收客户费用'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('OperNo', u'交易柜员'),('BrokerFee', u'应收期货公司费用'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('Message', u'发送方给接收方的消息'),('BankBranchID', u'银行分支机构代码'),('Digest', u'摘要'),('PlateSerial', u'银期平台消息流水号'),('RepealedTimes', u'已经冲正次数'),('TransferStatus', u'转账交易状态'),('TradeAmount', u'转帐金额'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('BrokerRepealFlag', u'期商冲正标志'),('BankRepealSerial', u'被冲正银行流水号'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('RepealTimeInterval', u'冲正时间间隔'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankSecuAccType', u'期货单位帐号类型'),('Password', u'期货密码'),('RequestID', u'请求编号'),('BankAccType', u'银行帐号类型'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('CustType', u'客户类型'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('FeePayFlag', u'费用支付标志'),('TID', u'交易ID')]])
    def getval(self, n):
        if n in ['IdCardType', 'BankPwdFlag', 'BankRepealFlag', 'LastFragment', 'TransferStatus', 'SecuPwdFlag', 'BrokerRepealFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'BankAccType', 'CustType', 'FeePayFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInstrumentStatusField:
    def __init__(self, ExchangeInstID="", ExchangeID=""):
        self.ExchangeInstID=tou(ExchangeInstID)
        self.ExchangeID=tou(ExchangeID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeInstID', 'ExchangeID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeInstID', u'合约在交易所的代码'),('ExchangeID', u'交易所代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryParkedOrderField:
    def __init__(self, BrokerID="", InvestorID="", ExchangeID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ExchangeID=tou(ExchangeID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'ExchangeID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ExchangeID', u'交易所代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTraderField:
    def __init__(self, Password="", InstallCount=0, BrokerID="", ExchangeID="", TraderID="", ParticipantID=""):
        self.Password=tou(Password)
        self.InstallCount=InstallCount
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'InstallCount', 'BrokerID', 'ExchangeID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('InstallCount', u'安装数量'),('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSettlementInfoField:
    def __init__(self, SettlementID=0, Content="", InvestorID="", SequenceNo=0, BrokerID="", TradingDay=""):
        self.SettlementID=SettlementID
        self.Content=tou(Content)
        self.InvestorID=tou(InvestorID)
        self.SequenceNo=SequenceNo
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SettlementID', 'Content', 'InvestorID', 'SequenceNo', 'BrokerID', 'TradingDay']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('SettlementID', u'结算编号'),('Content', u'消息正文'),('InvestorID', u'投资者代码'),('SequenceNo', u'序号'),('BrokerID', u'经纪公司代码'),('TradingDay', u'交易日')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferQryBankRspField:
    def __init__(self, FutureAccount="", RetCode="", RetInfo="", TradeAmt=0, UseAmt=0, FetchAmt=0, CurrencyCode=""):
        self.FutureAccount=tou(FutureAccount)
        self.RetCode=tou(RetCode)
        self.RetInfo=tou(RetInfo)
        self.TradeAmt=TradeAmt
        self.UseAmt=UseAmt
        self.FetchAmt=FetchAmt
        self.CurrencyCode=tou(CurrencyCode)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'RetCode', 'RetInfo', 'TradeAmt', 'UseAmt', 'FetchAmt', 'CurrencyCode']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FutureAccount', u'资金账户'),('RetCode', u'响应代码'),('RetInfo', u'响应信息'),('TradeAmt', u'银行余额'),('UseAmt', u'银行可用余额'),('FetchAmt', u'银行可取余额'),('CurrencyCode', u'币种')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQrySyncDepositField:
    def __init__(self, DepositSeqNo="", BrokerID=""):
        self.DepositSeqNo=tou(DepositSeqNo)
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['DepositSeqNo', 'BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('DepositSeqNo', u'出入金流水号'),('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcOpenAccountField:
    def __init__(self, TradingDay="", DeviceID="", ErrorID=0, BrokerID="", ZipCode="", SessionID=0, IdentifiedCardNo="", IdCardType='0', MobilePhone="", BankID="", BankPwdFlag='0', OperNo="", BankAccount="", BankSecuAcc="", LastFragment='0', Gender='0', Address="", TradeDate="", MoneyAccountStatus='0', AccountID="", BankSerial="", CustomerName="", BankPassWord="", CashExchangeCode='1', Digest="", PlateSerial=0, Fax="", EMail="", TradeTime="", InstallID=0, SecuPwdFlag='0', VerifyCertNoFlag='0', CurrencyID="", ErrorMsg="", BankSecuAccType='1', Password="", BankBranchID="", CountryCode="", BrokerBranchID="", UserID="", CustType='0', BrokerIDByBank="", TradeCode="", BankAccType='1', TID=0, Telephone=""):
        self.TradingDay=tou(TradingDay)
        self.DeviceID=tou(DeviceID)
        self.ErrorID=ErrorID
        self.BrokerID=tou(BrokerID)
        self.ZipCode=tou(ZipCode)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.IdCardType=tou(IdCardType)
        self.MobilePhone=tou(MobilePhone)
        self.BankID=tou(BankID)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.BankSecuAcc=tou(BankSecuAcc)
        self.LastFragment=tou(LastFragment)
        self.Gender=tou(Gender)
        self.Address=tou(Address)
        self.TradeDate=tou(TradeDate)
        self.MoneyAccountStatus=tou(MoneyAccountStatus)
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.CashExchangeCode=tou(CashExchangeCode)
        self.Digest=tou(Digest)
        self.PlateSerial=PlateSerial
        self.Fax=tou(Fax)
        self.EMail=tou(EMail)
        self.TradeTime=tou(TradeTime)
        self.InstallID=InstallID
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.Password=tou(Password)
        self.BankBranchID=tou(BankBranchID)
        self.CountryCode=tou(CountryCode)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.BankAccType=tou(BankAccType)
        self.TID=TID
        self.Telephone=tou(Telephone)
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'Gender': {"'1'": '男', "'0'": '未知状态', "'2'": '女'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'CashExchangeCode': {"'1'": '汇', "'2'": '钞'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'MoneyAccountStatus': {"'1'": '销户', "'0'": '正常'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradingDay', 'DeviceID', 'ErrorID', 'BrokerID', 'ZipCode', 'SessionID', 'IdentifiedCardNo', 'IdCardType', 'MobilePhone', 'BankID', 'BankPwdFlag', 'OperNo', 'BankAccount', 'BankSecuAcc', 'LastFragment', 'Gender', 'Address', 'TradeDate', 'MoneyAccountStatus', 'AccountID', 'BankSerial', 'CustomerName', 'BankPassWord', 'CashExchangeCode', 'Digest', 'PlateSerial', 'Fax', 'EMail', 'TradeTime', 'InstallID', 'SecuPwdFlag', 'VerifyCertNoFlag', 'CurrencyID', 'ErrorMsg', 'BankSecuAccType', 'Password', 'BankBranchID', 'CountryCode', 'BrokerBranchID', 'UserID', 'CustType', 'BrokerIDByBank', 'TradeCode', 'BankAccType', 'TID', 'Telephone']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradingDay', u'交易系统日期'),('DeviceID', u'渠道标志'),('ErrorID', u'错误代码'),('BrokerID', u'期商代码'),('ZipCode', u'邮编'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('IdCardType', u'证件类型'),('MobilePhone', u'手机'),('BankID', u'银行代码'),('BankPwdFlag', u'银行密码标志'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('BankSecuAcc', u'期货单位帐号'),('LastFragment', u'最后分片标志'),('Gender', u'性别'),('Address', u'地址'),('TradeDate', u'交易日期'),('MoneyAccountStatus', u'资金账户状态'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('CashExchangeCode', u'汇钞标志'),('Digest', u'摘要'),('PlateSerial', u'银期平台消息流水号'),('Fax', u'传真'),('EMail', u'电子邮件'),('TradeTime', u'交易时间'),('InstallID', u'安装编号'),('SecuPwdFlag', u'期货资金密码核对标志'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankSecuAccType', u'期货单位帐号类型'),('Password', u'期货密码'),('BankBranchID', u'银行分支机构代码'),('CountryCode', u'国家代码'),('BrokerBranchID', u'期商分支机构代码'),('UserID', u'用户标识'),('CustType', u'客户类型'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('BankAccType', u'银行帐号类型'),('TID', u'交易ID'),('Telephone', u'电话号码')]])
    def getval(self, n):
        if n in ['IdCardType', 'BankPwdFlag', 'LastFragment', 'Gender', 'MoneyAccountStatus', 'CashExchangeCode', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'CustType', 'BankAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTransferFutureToBankReqField:
    def __init__(self, FutureAccount="", FutureAccPwd="", CurrencyCode="", TradeAmt=0, CustFee=0, FuturePwdFlag='0'):
        self.FutureAccount=tou(FutureAccount)
        self.FutureAccPwd=tou(FutureAccPwd)
        self.CurrencyCode=tou(CurrencyCode)
        self.TradeAmt=TradeAmt
        self.CustFee=CustFee
        self.FuturePwdFlag=tou(FuturePwdFlag)
        self.vcmap={'FuturePwdFlag': {"'1'": '核对', "'0'": '不核对'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['FutureAccount', 'FutureAccPwd', 'CurrencyCode', 'TradeAmt', 'CustFee', 'FuturePwdFlag']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('FutureAccount', u'期货资金账户'),('FutureAccPwd', u'密码'),('CurrencyCode', u'币种：RMB-人民币 USD-美圆 HKD-港元'),('TradeAmt', u'转账金额'),('CustFee', u'客户手续费'),('FuturePwdFlag', u'密码标志')]])
    def getval(self, n):
        if n in ['FuturePwdFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInvestorPositionDetailField:
    def __init__(self, BrokerID="", InvestorID="", InstrumentID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InstrumentID=tou(InstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'InstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InstrumentID', u'合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcNoticeField:
    def __init__(self, SequenceLabel="", BrokerID="", Content=""):
        self.SequenceLabel=tou(SequenceLabel)
        self.BrokerID=tou(BrokerID)
        self.Content=tou(Content)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SequenceLabel', 'BrokerID', 'Content']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('SequenceLabel', u'经纪公司通知内容序列号'),('BrokerID', u'经纪公司代码'),('Content', u'消息正文')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryCombinationLegField:
    def __init__(self, LegID=0, CombInstrumentID="", LegInstrumentID=""):
        self.LegID=LegID
        self.CombInstrumentID=tou(CombInstrumentID)
        self.LegInstrumentID=tou(LegInstrumentID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LegID', 'CombInstrumentID', 'LegInstrumentID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LegID', u'单腿编号'),('CombInstrumentID', u'组合合约代码'),('LegInstrumentID', u'单腿合约代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcBrokerDepositField:
    def __init__(self, CloseProfit=0, Balance=0, BrokerID="", TradingDay="", Deposit=0, Reserve=0, ExchangeID="", PreBalance=0, CurrMargin=0, FrozenMargin=0, ParticipantID="", Withdraw=0, Available=0):
        self.CloseProfit=CloseProfit
        self.Balance=Balance
        self.BrokerID=tou(BrokerID)
        self.TradingDay=tou(TradingDay)
        self.Deposit=Deposit
        self.Reserve=Reserve
        self.ExchangeID=tou(ExchangeID)
        self.PreBalance=PreBalance
        self.CurrMargin=CurrMargin
        self.FrozenMargin=FrozenMargin
        self.ParticipantID=tou(ParticipantID)
        self.Withdraw=Withdraw
        self.Available=Available
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['CloseProfit', 'Balance', 'BrokerID', 'TradingDay', 'Deposit', 'Reserve', 'ExchangeID', 'PreBalance', 'CurrMargin', 'FrozenMargin', 'ParticipantID', 'Withdraw', 'Available']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('CloseProfit', u'平仓盈亏'),('Balance', u'期货结算准备金'),('BrokerID', u'经纪公司代码'),('TradingDay', u'交易日期'),('Deposit', u'入金金额'),('Reserve', u'基本准备金'),('ExchangeID', u'交易所代码'),('PreBalance', u'上次结算准备金'),('CurrMargin', u'当前保证金总额'),('FrozenMargin', u'冻结的保证金'),('ParticipantID', u'会员代码'),('Withdraw', u'出金金额'),('Available', u'可提资金')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryAccountregisterField:
    def __init__(self, BankID="", BrokerID="", AccountID=""):
        self.BankID=tou(BankID)
        self.BrokerID=tou(BrokerID)
        self.AccountID=tou(AccountID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BankID', 'BrokerID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BankID', u'银行编码'),('BrokerID', u'经纪公司代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryCFMMCBrokerKeyField:
    def __init__(self, BrokerID=""):
        self.BrokerID=tou(BrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeTradeField:
    def __init__(self, TradeSource='0', TradeID="", PriceSource='0', TradeTime="", ClientID="", ClearingPartID="", OffsetFlag='0', TradeType='0', TraderID="", TradingRole='1', Price=0, ExchangeID="", OrderSysID="", ExchangeInstID="", SequenceNo=0, Volume=0, TradeDate="", ParticipantID="", Direction='0', BusinessUnit="", HedgeFlag='1', OrderLocalID=""):
        self.TradeSource=tou(TradeSource)
        self.TradeID=tou(TradeID)
        self.PriceSource=tou(PriceSource)
        self.TradeTime=tou(TradeTime)
        self.ClientID=tou(ClientID)
        self.ClearingPartID=tou(ClearingPartID)
        self.OffsetFlag=tou(OffsetFlag)
        self.TradeType=tou(TradeType)
        self.TraderID=tou(TraderID)
        self.TradingRole=tou(TradingRole)
        self.Price=Price
        self.ExchangeID=tou(ExchangeID)
        self.OrderSysID=tou(OrderSysID)
        self.ExchangeInstID=tou(ExchangeInstID)
        self.SequenceNo=SequenceNo
        self.Volume=Volume
        self.TradeDate=tou(TradeDate)
        self.ParticipantID=tou(ParticipantID)
        self.Direction=tou(Direction)
        self.BusinessUnit=tou(BusinessUnit)
        self.HedgeFlag=tou(HedgeFlag)
        self.OrderLocalID=tou(OrderLocalID)
        self.vcmap={'TradeSource': {"'1'": '来自查询', "'0'": '来自交易所普通回报'}, 'TradingRole': {"'1'": '代理', "'3'": '做市商', "'2'": '自营'}, 'PriceSource': {"'1'": '买委托价', "'0'": '前成交价', "'2'": '卖委托价'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'OffsetFlag': {"'1'": '平仓', "'6'": '本地强平', "'0'": '开仓', "'5'": '强减', "'4'": '平昨', "'3'": '平今', "'2'": '强平'}, 'TradeType': {"'4'": '组合衍生成交', "'1'": '期权执行', "'3'": '期转现衍生成交', "'0'": '普通成交', "'2'": 'OTC成交'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['TradeSource', 'TradeID', 'PriceSource', 'TradeTime', 'ClientID', 'ClearingPartID', 'OffsetFlag', 'TradeType', 'TraderID', 'TradingRole', 'Price', 'ExchangeID', 'OrderSysID', 'ExchangeInstID', 'SequenceNo', 'Volume', 'TradeDate', 'ParticipantID', 'Direction', 'BusinessUnit', 'HedgeFlag', 'OrderLocalID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('TradeSource', u'成交来源'),('TradeID', u'成交编号'),('PriceSource', u'成交价来源'),('TradeTime', u'成交时间'),('ClientID', u'客户代码'),('ClearingPartID', u'结算会员编号'),('OffsetFlag', u'开平标志'),('TradeType', u'成交类型'),('TraderID', u'交易所交易员代码'),('TradingRole', u'交易角色'),('Price', u'价格'),('ExchangeID', u'交易所代码'),('OrderSysID', u'报单编号'),('ExchangeInstID', u'合约在交易所的代码'),('SequenceNo', u'序号'),('Volume', u'数量'),('TradeDate', u'成交时期'),('ParticipantID', u'会员代码'),('Direction', u'买卖方向'),('BusinessUnit', u'业务单元'),('HedgeFlag', u'投机套保标志'),('OrderLocalID', u'本地报单编号')]])
    def getval(self, n):
        if n in ['TradeSource', 'PriceSource', 'OffsetFlag', 'TradeType', 'TradingRole', 'Direction', 'HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInstrumentMarginRateAdjustField:
    def __init__(self, InstrumentID="", ShortMarginRatioByVolume=0, LongMarginRatioByMoney=0, HedgeFlag='1', IsRelative=0, BrokerID="", InvestorID="", InvestorRange='1', LongMarginRatioByVolume=0, ShortMarginRatioByMoney=0):
        self.InstrumentID=tou(InstrumentID)
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.HedgeFlag=tou(HedgeFlag)
        self.IsRelative=IsRelative
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.InvestorRange=tou(InvestorRange)
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.vcmap={'InvestorRange': {"'1'": '所有', "'3'": '单一投资者', "'2'": '投资者组'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByVolume', 'LongMarginRatioByMoney', 'HedgeFlag', 'IsRelative', 'BrokerID', 'InvestorID', 'InvestorRange', 'LongMarginRatioByVolume', 'ShortMarginRatioByMoney']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByVolume', u'空头保证金费'),('LongMarginRatioByMoney', u'多头保证金率'),('HedgeFlag', u'投机套保标志'),('IsRelative', u'是否相对交易所收取'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('InvestorRange', u'投资者范围'),('LongMarginRatioByVolume', u'多头保证金费'),('ShortMarginRatioByMoney', u'空头保证金率')]])
    def getval(self, n):
        if n in ['HedgeFlag', 'InvestorRange']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeMarginRateField:
    def __init__(self, InstrumentID="", ShortMarginRatioByVolume=0, HedgeFlag='1', LongMarginRatioByMoney=0, BrokerID="", LongMarginRatioByVolume=0, ShortMarginRatioByMoney=0):
        self.InstrumentID=tou(InstrumentID)
        self.ShortMarginRatioByVolume=ShortMarginRatioByVolume
        self.HedgeFlag=tou(HedgeFlag)
        self.LongMarginRatioByMoney=LongMarginRatioByMoney
        self.BrokerID=tou(BrokerID)
        self.LongMarginRatioByVolume=LongMarginRatioByVolume
        self.ShortMarginRatioByMoney=ShortMarginRatioByMoney
        self.vcmap={'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InstrumentID', 'ShortMarginRatioByVolume', 'HedgeFlag', 'LongMarginRatioByMoney', 'BrokerID', 'LongMarginRatioByVolume', 'ShortMarginRatioByMoney']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InstrumentID', u'合约代码'),('ShortMarginRatioByVolume', u'空头保证金费'),('HedgeFlag', u'投机套保标志'),('LongMarginRatioByMoney', u'多头保证金率'),('BrokerID', u'经纪公司代码'),('LongMarginRatioByVolume', u'多头保证金费'),('ShortMarginRatioByMoney', u'空头保证金率')]])
    def getval(self, n):
        if n in ['HedgeFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTradingNoticeInfoField:
    def __init__(self, SequenceSeries=0, SequenceNo=0, SendTime="", BrokerID="", InvestorID="", FieldContent=""):
        self.SequenceSeries=SequenceSeries
        self.SequenceNo=SequenceNo
        self.SendTime=tou(SendTime)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.FieldContent=tou(FieldContent)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['SequenceSeries', 'SequenceNo', 'SendTime', 'BrokerID', 'InvestorID', 'FieldContent']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('SequenceSeries', u'序列系列号'),('SequenceNo', u'序列号'),('SendTime', u'发送时间'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('FieldContent', u'消息正文')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryBrokerTradingParamsField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcReqTransferField:
    def __init__(self, Digest="", TransferStatus='0', BankPwdFlag='0', TradingDay="", TradeTime="", FutureSerial=0, DeviceID="", InstallID=0, BrokerID="", SessionID=0, IdentifiedCardNo="", AccountID="", SecuPwdFlag='0', Message="", TradeAmount=0, VerifyCertNoFlag='0', BankID="", CurrencyID="", BankSecuAccType='1', OperNo="", BankAccount="", CustFee=0, BankSecuAcc="", Password="", LastFragment='0', RequestID=0, BankAccType='1', TradeDate="", UserID="", CustType='0', IdCardType='0', BankSerial="", BrokerIDByBank="", TradeCode="", CustomerName="", BankPassWord="", FeePayFlag='0', FutureFetchAmount=0, TID=0, BankBranchID="", BrokerBranchID="", PlateSerial=0, BrokerFee=0):
        self.Digest=tou(Digest)
        self.TransferStatus=tou(TransferStatus)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.TradingDay=tou(TradingDay)
        self.TradeTime=tou(TradeTime)
        self.FutureSerial=FutureSerial
        self.DeviceID=tou(DeviceID)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.AccountID=tou(AccountID)
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.Message=tou(Message)
        self.TradeAmount=TradeAmount
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.BankSecuAccType=tou(BankSecuAccType)
        self.OperNo=tou(OperNo)
        self.BankAccount=tou(BankAccount)
        self.CustFee=CustFee
        self.BankSecuAcc=tou(BankSecuAcc)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.RequestID=RequestID
        self.BankAccType=tou(BankAccType)
        self.TradeDate=tou(TradeDate)
        self.UserID=tou(UserID)
        self.CustType=tou(CustType)
        self.IdCardType=tou(IdCardType)
        self.BankSerial=tou(BankSerial)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.TradeCode=tou(TradeCode)
        self.CustomerName=tou(CustomerName)
        self.BankPassWord=tou(BankPassWord)
        self.FeePayFlag=tou(FeePayFlag)
        self.FutureFetchAmount=FutureFetchAmount
        self.TID=TID
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.BrokerFee=BrokerFee
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'FeePayFlag': {"'1'": '由发送方支付费用', "'0'": '由受益方支付费用', "'2'": '由发送方支付发起的费用，受益方支付接受的费用'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'TransferStatus': {"'1'": '被冲正', "'0'": '正常'}, 'BankSecuAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Digest', 'TransferStatus', 'BankPwdFlag', 'TradingDay', 'TradeTime', 'FutureSerial', 'DeviceID', 'InstallID', 'BrokerID', 'SessionID', 'IdentifiedCardNo', 'AccountID', 'SecuPwdFlag', 'Message', 'TradeAmount', 'VerifyCertNoFlag', 'BankID', 'CurrencyID', 'BankSecuAccType', 'OperNo', 'BankAccount', 'CustFee', 'BankSecuAcc', 'Password', 'LastFragment', 'RequestID', 'BankAccType', 'TradeDate', 'UserID', 'CustType', 'IdCardType', 'BankSerial', 'BrokerIDByBank', 'TradeCode', 'CustomerName', 'BankPassWord', 'FeePayFlag', 'FutureFetchAmount', 'TID', 'BankBranchID', 'BrokerBranchID', 'PlateSerial', 'BrokerFee']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Digest', u'摘要'),('TransferStatus', u'转账交易状态'),('BankPwdFlag', u'银行密码标志'),('TradingDay', u'交易系统日期'),('TradeTime', u'交易时间'),('FutureSerial', u'期货公司流水号'),('DeviceID', u'渠道标志'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('AccountID', u'投资者帐号'),('SecuPwdFlag', u'期货资金密码核对标志'),('Message', u'发送方给接收方的消息'),('TradeAmount', u'转帐金额'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('BankSecuAccType', u'期货单位帐号类型'),('OperNo', u'交易柜员'),('BankAccount', u'银行帐号'),('CustFee', u'应收客户费用'),('BankSecuAcc', u'期货单位帐号'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('RequestID', u'请求编号'),('BankAccType', u'银行帐号类型'),('TradeDate', u'交易日期'),('UserID', u'用户标识'),('CustType', u'客户类型'),('IdCardType', u'证件类型'),('BankSerial', u'银行流水号'),('BrokerIDByBank', u'期货公司银行编码'),('TradeCode', u'业务功能码'),('CustomerName', u'客户姓名'),('BankPassWord', u'银行密码'),('FeePayFlag', u'费用支付标志'),('FutureFetchAmount', u'期货可取金额'),('TID', u'交易ID'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号'),('BrokerFee', u'应收期货公司费用')]])
    def getval(self, n):
        if n in ['TransferStatus', 'BankPwdFlag', 'SecuPwdFlag', 'VerifyCertNoFlag', 'BankSecuAccType', 'LastFragment', 'BankAccType', 'CustType', 'IdCardType', 'FeePayFlag']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcRspQueryTradeResultBySerialField:
    def __init__(self, OriginReturnCode="", TradeAmount=0, TradeTime="", ErrorID=0, BrokerID="", SessionID=0, RefrenceIssureType='0', OriginDescrInfoForReturnCode="", Reference=0, BankID="", CurrencyID="", ErrorMsg="", BankAccount="", Digest="", Password="", LastFragment='0', TradeDate="", TradingDay="", AccountID="", BankSerial="", TradeCode="", RefrenceIssure="", BankPassWord="", BankBranchID="", BrokerBranchID="", PlateSerial=0):
        self.OriginReturnCode=tou(OriginReturnCode)
        self.TradeAmount=TradeAmount
        self.TradeTime=tou(TradeTime)
        self.ErrorID=ErrorID
        self.BrokerID=tou(BrokerID)
        self.SessionID=SessionID
        self.RefrenceIssureType=tou(RefrenceIssureType)
        self.OriginDescrInfoForReturnCode=tou(OriginDescrInfoForReturnCode)
        self.Reference=Reference
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.BankAccount=tou(BankAccount)
        self.Digest=tou(Digest)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.TradeDate=tou(TradeDate)
        self.TradingDay=tou(TradingDay)
        self.AccountID=tou(AccountID)
        self.BankSerial=tou(BankSerial)
        self.TradeCode=tou(TradeCode)
        self.RefrenceIssure=tou(RefrenceIssure)
        self.BankPassWord=tou(BankPassWord)
        self.BankBranchID=tou(BankBranchID)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'RefrenceIssureType': {"'1'": '期商', "'0'": '银行', "'2'": '券商'}, 'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OriginReturnCode', 'TradeAmount', 'TradeTime', 'ErrorID', 'BrokerID', 'SessionID', 'RefrenceIssureType', 'OriginDescrInfoForReturnCode', 'Reference', 'BankID', 'CurrencyID', 'ErrorMsg', 'BankAccount', 'Digest', 'Password', 'LastFragment', 'TradeDate', 'TradingDay', 'AccountID', 'BankSerial', 'TradeCode', 'RefrenceIssure', 'BankPassWord', 'BankBranchID', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OriginReturnCode', u'原始返回代码'),('TradeAmount', u'转帐金额'),('TradeTime', u'交易时间'),('ErrorID', u'错误代码'),('BrokerID', u'期商代码'),('SessionID', u'会话号'),('RefrenceIssureType', u'本流水号发布者的机构类型'),('OriginDescrInfoForReturnCode', u'原始返回码描述'),('Reference', u'流水号'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('BankAccount', u'银行帐号'),('Digest', u'摘要'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('TradeDate', u'交易日期'),('TradingDay', u'交易系统日期'),('AccountID', u'投资者帐号'),('BankSerial', u'银行流水号'),('TradeCode', u'业务功能码'),('RefrenceIssure', u'本流水号发布者机构编码'),('BankPassWord', u'银行密码'),('BankBranchID', u'银行分支机构代码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['RefrenceIssureType', 'LastFragment']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcChangeAccountField:
    def __init__(self, MoneyAccountStatus='0', BankPwdFlag='0', CustType='0', TradeTime="", ErrorID=0, InstallID=0, BrokerID="", ZipCode="", SessionID=0, IdentifiedCardNo="", NewBankAccount="", SecuPwdFlag='0', EMail="", VerifyCertNoFlag='0', MobilePhone="", BankID="", CurrencyID="", ErrorMsg="", AccountID="", BankAccount="", Digest="", Fax="", Password="", LastFragment='0', Gender='0', Address="", NewBankPassWord="", BrokerIDByBank="", CountryCode="", TradeDate="", TradingDay="", IdCardType='0', BankSerial="", BankAccType='1', TradeCode="", CustomerName="", BankBranchID="", BankPassWord="", TID=0, Telephone="", BrokerBranchID="", PlateSerial=0):
        self.MoneyAccountStatus=tou(MoneyAccountStatus)
        self.BankPwdFlag=tou(BankPwdFlag)
        self.CustType=tou(CustType)
        self.TradeTime=tou(TradeTime)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.ZipCode=tou(ZipCode)
        self.SessionID=SessionID
        self.IdentifiedCardNo=tou(IdentifiedCardNo)
        self.NewBankAccount=tou(NewBankAccount)
        self.SecuPwdFlag=tou(SecuPwdFlag)
        self.EMail=tou(EMail)
        self.VerifyCertNoFlag=tou(VerifyCertNoFlag)
        self.MobilePhone=tou(MobilePhone)
        self.BankID=tou(BankID)
        self.CurrencyID=tou(CurrencyID)
        self.ErrorMsg=tou(ErrorMsg)
        self.AccountID=tou(AccountID)
        self.BankAccount=tou(BankAccount)
        self.Digest=tou(Digest)
        self.Fax=tou(Fax)
        self.Password=tou(Password)
        self.LastFragment=tou(LastFragment)
        self.Gender=tou(Gender)
        self.Address=tou(Address)
        self.NewBankPassWord=tou(NewBankPassWord)
        self.BrokerIDByBank=tou(BrokerIDByBank)
        self.CountryCode=tou(CountryCode)
        self.TradeDate=tou(TradeDate)
        self.TradingDay=tou(TradingDay)
        self.IdCardType=tou(IdCardType)
        self.BankSerial=tou(BankSerial)
        self.BankAccType=tou(BankAccType)
        self.TradeCode=tou(TradeCode)
        self.CustomerName=tou(CustomerName)
        self.BankBranchID=tou(BankBranchID)
        self.BankPassWord=tou(BankPassWord)
        self.TID=TID
        self.Telephone=tou(Telephone)
        self.BrokerBranchID=tou(BrokerBranchID)
        self.PlateSerial=PlateSerial
        self.vcmap={'LastFragment': {"'1'": '不是最后分片', "'0'": '是最后分片'}, 'CustType': {"'1'": '机构户', "'0'": '自然人'}, 'VerifyCertNoFlag': {"'1'": '否', "'0'": '是'}, 'BankAccType': {"'1'": '银行存折', "'3'": '信用卡', "'2'": '储蓄卡'}, 'Gender': {"'1'": '男', "'0'": '未知状态', "'2'": '女'}, 'SecuPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'MoneyAccountStatus': {"'1'": '销户', "'0'": '正常'}, 'BankPwdFlag': {"'1'": '明文核对', "'0'": '不核对', "'2'": '密文核对'}, 'IdCardType': {"'8'": '回乡证', "'1'": '身份证', "'0'": '组织机构代码', "'4'": '士兵证', "'3'": '警官证', "'2'": '军官证', "'7'": '台胞证', "'A'": '税务登记号', "'6'": '护照', "'5'": '户口簿', "'9'": '营业执照号', "'x'": '其他证件'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['MoneyAccountStatus', 'BankPwdFlag', 'CustType', 'TradeTime', 'ErrorID', 'InstallID', 'BrokerID', 'ZipCode', 'SessionID', 'IdentifiedCardNo', 'NewBankAccount', 'SecuPwdFlag', 'EMail', 'VerifyCertNoFlag', 'MobilePhone', 'BankID', 'CurrencyID', 'ErrorMsg', 'AccountID', 'BankAccount', 'Digest', 'Fax', 'Password', 'LastFragment', 'Gender', 'Address', 'NewBankPassWord', 'BrokerIDByBank', 'CountryCode', 'TradeDate', 'TradingDay', 'IdCardType', 'BankSerial', 'BankAccType', 'TradeCode', 'CustomerName', 'BankBranchID', 'BankPassWord', 'TID', 'Telephone', 'BrokerBranchID', 'PlateSerial']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('MoneyAccountStatus', u'资金账户状态'),('BankPwdFlag', u'银行密码标志'),('CustType', u'客户类型'),('TradeTime', u'交易时间'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('BrokerID', u'期商代码'),('ZipCode', u'邮编'),('SessionID', u'会话号'),('IdentifiedCardNo', u'证件号码'),('NewBankAccount', u'新银行帐号'),('SecuPwdFlag', u'期货资金密码核对标志'),('EMail', u'电子邮件'),('VerifyCertNoFlag', u'验证客户证件号码标志'),('MobilePhone', u'手机'),('BankID', u'银行代码'),('CurrencyID', u'币种代码'),('ErrorMsg', u'错误信息'),('AccountID', u'投资者帐号'),('BankAccount', u'银行帐号'),('Digest', u'摘要'),('Fax', u'传真'),('Password', u'期货密码'),('LastFragment', u'最后分片标志'),('Gender', u'性别'),('Address', u'地址'),('NewBankPassWord', u'新银行密码'),('BrokerIDByBank', u'期货公司银行编码'),('CountryCode', u'国家代码'),('TradeDate', u'交易日期'),('TradingDay', u'交易系统日期'),('IdCardType', u'证件类型'),('BankSerial', u'银行流水号'),('BankAccType', u'银行帐号类型'),('TradeCode', u'业务功能码'),('CustomerName', u'客户姓名'),('BankBranchID', u'银行分支机构代码'),('BankPassWord', u'银行密码'),('TID', u'交易ID'),('Telephone', u'电话号码'),('BrokerBranchID', u'期商分支机构代码'),('PlateSerial', u'银期平台消息流水号')]])
    def getval(self, n):
        if n in ['MoneyAccountStatus', 'BankPwdFlag', 'CustType', 'SecuPwdFlag', 'VerifyCertNoFlag', 'LastFragment', 'Gender', 'IdCardType', 'BankAccType']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcExchangeOrderInsertErrorField:
    def __init__(self, ExchangeID="", ErrorID=0, InstallID=0, ErrorMsg="", OrderLocalID="", TraderID="", ParticipantID=""):
        self.ExchangeID=tou(ExchangeID)
        self.ErrorID=ErrorID
        self.InstallID=InstallID
        self.ErrorMsg=tou(ErrorMsg)
        self.OrderLocalID=tou(OrderLocalID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['ExchangeID', 'ErrorID', 'InstallID', 'ErrorMsg', 'OrderLocalID', 'TraderID', 'ParticipantID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('ExchangeID', u'交易所代码'),('ErrorID', u'错误代码'),('InstallID', u'安装编号'),('ErrorMsg', u'错误信息'),('OrderLocalID', u'本地报单编号'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcOrderActionField:
    def __init__(self, InvestorID="", ClientID="", InstallID=0, BrokerID="", FrontID=0, SessionID=0, TraderID="", StatusMsg="", ActionLocalID="", VolumeChange=0, ActionDate="", ExchangeID="", OrderSysID="", RequestID=0, UserID="", InstrumentID="", ParticipantID="", ActionFlag='0', BusinessUnit="", OrderActionStatus='a', LimitPrice=0, OrderActionRef=0, OrderRef="", OrderLocalID="", ActionTime=""):
        self.InvestorID=tou(InvestorID)
        self.ClientID=tou(ClientID)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.FrontID=FrontID
        self.SessionID=SessionID
        self.TraderID=tou(TraderID)
        self.StatusMsg=tou(StatusMsg)
        self.ActionLocalID=tou(ActionLocalID)
        self.VolumeChange=VolumeChange
        self.ActionDate=tou(ActionDate)
        self.ExchangeID=tou(ExchangeID)
        self.OrderSysID=tou(OrderSysID)
        self.RequestID=RequestID
        self.UserID=tou(UserID)
        self.InstrumentID=tou(InstrumentID)
        self.ParticipantID=tou(ParticipantID)
        self.ActionFlag=tou(ActionFlag)
        self.BusinessUnit=tou(BusinessUnit)
        self.OrderActionStatus=tou(OrderActionStatus)
        self.LimitPrice=LimitPrice
        self.OrderActionRef=OrderActionRef
        self.OrderRef=tou(OrderRef)
        self.OrderLocalID=tou(OrderLocalID)
        self.ActionTime=tou(ActionTime)
        self.vcmap={'ActionFlag': {"'3'": '修改', "'0'": '删除'}, 'OrderActionStatus': {"'a'": '已经提交', "'c'": '已经被拒绝', "'b'": '已经接受'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['InvestorID', 'ClientID', 'InstallID', 'BrokerID', 'FrontID', 'SessionID', 'TraderID', 'StatusMsg', 'ActionLocalID', 'VolumeChange', 'ActionDate', 'ExchangeID', 'OrderSysID', 'RequestID', 'UserID', 'InstrumentID', 'ParticipantID', 'ActionFlag', 'BusinessUnit', 'OrderActionStatus', 'LimitPrice', 'OrderActionRef', 'OrderRef', 'OrderLocalID', 'ActionTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('InvestorID', u'投资者代码'),('ClientID', u'客户代码'),('InstallID', u'安装编号'),('BrokerID', u'经纪公司代码'),('FrontID', u'前置编号'),('SessionID', u'会话编号'),('TraderID', u'交易所交易员代码'),('StatusMsg', u'状态信息'),('ActionLocalID', u'操作本地编号'),('VolumeChange', u'数量变化'),('ActionDate', u'操作日期'),('ExchangeID', u'交易所代码'),('OrderSysID', u'报单编号'),('RequestID', u'请求编号'),('UserID', u'用户代码'),('InstrumentID', u'合约代码'),('ParticipantID', u'会员代码'),('ActionFlag', u'操作标志'),('BusinessUnit', u'业务单元'),('OrderActionStatus', u'报单操作状态'),('LimitPrice', u'价格'),('OrderActionRef', u'报单操作引用'),('OrderRef', u'报单引用'),('OrderLocalID', u'本地报单编号'),('ActionTime', u'操作时间')]])
    def getval(self, n):
        if n in ['ActionFlag', 'OrderActionStatus']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryErrOrderActionField:
    def __init__(self, BrokerID="", InvestorID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingInvestorGroupField:
    def __init__(self, BrokerID="", InvestorGroupID="", InvestorGroupName=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorGroupID=tou(InvestorGroupID)
        self.InvestorGroupName=tou(InvestorGroupName)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorGroupID', 'InvestorGroupName']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorGroupID', u'投资者分组代码'),('InvestorGroupName', u'投资者分组名称')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcSyncingInvestorPositionField:
    def __init__(self, LongFrozen=0, PosiDirection='1', CloseProfitByTrade=0, SettlementPrice=0, BrokerID="", InvestorID="", OpenCost=0, Commission=0, CashIn=0, TodayPosition=0, InstrumentID="", CloseProfit=0, ExchangeMargin=0, CombLongFrozen=0, PositionProfit=0, PreSettlementPrice=0, FrozenMargin=0, Position=0, ShortFrozen=0, SettlementID=0, LongFrozenAmount=0, ShortFrozenAmount=0, CloseProfitByDate=0, FrozenCommission=0, MarginRateByVolume=0, MarginRateByMoney=0, TradingDay="", UseMargin=0, OpenVolume=0, FrozenCash=0, PositionCost=0, CloseAmount=0, YdPosition=0, OpenAmount=0, HedgeFlag='1', CloseVolume=0, CombPosition=0, PreMargin=0, CombShortFrozen=0, PositionDate='1'):
        self.LongFrozen=LongFrozen
        self.PosiDirection=tou(PosiDirection)
        self.CloseProfitByTrade=CloseProfitByTrade
        self.SettlementPrice=SettlementPrice
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.OpenCost=OpenCost
        self.Commission=Commission
        self.CashIn=CashIn
        self.TodayPosition=TodayPosition
        self.InstrumentID=tou(InstrumentID)
        self.CloseProfit=CloseProfit
        self.ExchangeMargin=ExchangeMargin
        self.CombLongFrozen=CombLongFrozen
        self.PositionProfit=PositionProfit
        self.PreSettlementPrice=PreSettlementPrice
        self.FrozenMargin=FrozenMargin
        self.Position=Position
        self.ShortFrozen=ShortFrozen
        self.SettlementID=SettlementID
        self.LongFrozenAmount=LongFrozenAmount
        self.ShortFrozenAmount=ShortFrozenAmount
        self.CloseProfitByDate=CloseProfitByDate
        self.FrozenCommission=FrozenCommission
        self.MarginRateByVolume=MarginRateByVolume
        self.MarginRateByMoney=MarginRateByMoney
        self.TradingDay=tou(TradingDay)
        self.UseMargin=UseMargin
        self.OpenVolume=OpenVolume
        self.FrozenCash=FrozenCash
        self.PositionCost=PositionCost
        self.CloseAmount=CloseAmount
        self.YdPosition=YdPosition
        self.OpenAmount=OpenAmount
        self.HedgeFlag=tou(HedgeFlag)
        self.CloseVolume=CloseVolume
        self.CombPosition=CombPosition
        self.PreMargin=PreMargin
        self.CombShortFrozen=CombShortFrozen
        self.PositionDate=tou(PositionDate)
        self.vcmap={'PositionDate': {"'1'": '今日持仓', "'2'": '历史持仓'}, 'PosiDirection': {"'1'": '净', "'3'": '空头', "'2'": '多头'}, 'HedgeFlag': {"'1'": '投机', "'3'": '套保', "'2'": '套利'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['LongFrozen', 'PosiDirection', 'CloseProfitByTrade', 'SettlementPrice', 'BrokerID', 'InvestorID', 'OpenCost', 'Commission', 'CashIn', 'TodayPosition', 'InstrumentID', 'CloseProfit', 'ExchangeMargin', 'CombLongFrozen', 'PositionProfit', 'PreSettlementPrice', 'FrozenMargin', 'Position', 'ShortFrozen', 'SettlementID', 'LongFrozenAmount', 'ShortFrozenAmount', 'CloseProfitByDate', 'FrozenCommission', 'MarginRateByVolume', 'MarginRateByMoney', 'TradingDay', 'UseMargin', 'OpenVolume', 'FrozenCash', 'PositionCost', 'CloseAmount', 'YdPosition', 'OpenAmount', 'HedgeFlag', 'CloseVolume', 'CombPosition', 'PreMargin', 'CombShortFrozen', 'PositionDate']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('LongFrozen', u'多头冻结'),('PosiDirection', u'持仓多空方向'),('CloseProfitByTrade', u'逐笔对冲平仓盈亏'),('SettlementPrice', u'本次结算价'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('OpenCost', u'开仓成本'),('Commission', u'手续费'),('CashIn', u'资金差额'),('TodayPosition', u'今日持仓'),('InstrumentID', u'合约代码'),('CloseProfit', u'平仓盈亏'),('ExchangeMargin', u'交易所保证金'),('CombLongFrozen', u'组合多头冻结'),('PositionProfit', u'持仓盈亏'),('PreSettlementPrice', u'上次结算价'),('FrozenMargin', u'冻结的保证金'),('Position', u'今日持仓'),('ShortFrozen', u'空头冻结'),('SettlementID', u'结算编号'),('LongFrozenAmount', u'开仓冻结金额'),('ShortFrozenAmount', u'开仓冻结金额'),('CloseProfitByDate', u'逐日盯市平仓盈亏'),('FrozenCommission', u'冻结的手续费'),('MarginRateByVolume', u'保证金率(按手数)'),('MarginRateByMoney', u'保证金率'),('TradingDay', u'交易日'),('UseMargin', u'占用的保证金'),('OpenVolume', u'开仓量'),('FrozenCash', u'冻结的资金'),('PositionCost', u'持仓成本'),('CloseAmount', u'平仓金额'),('YdPosition', u'上日持仓'),('OpenAmount', u'开仓金额'),('HedgeFlag', u'投机套保标志'),('CloseVolume', u'平仓量'),('CombPosition', u'组合成交形成的持仓'),('PreMargin', u'上次占用的保证金'),('CombShortFrozen', u'组合空头冻结'),('PositionDate', u'持仓日期')]])
    def getval(self, n):
        if n in ['PosiDirection', 'HedgeFlag', 'PositionDate']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcInvestorAccountField:
    def __init__(self, BrokerID="", InvestorID="", AccountID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.AccountID=tou(AccountID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'AccountID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('AccountID', u'投资者帐号')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcDRTransferField:
    def __init__(self, DestDRIdentityID=0, OrigDRIdentityID=0, OrigBrokerID="", DestBrokerID=""):
        self.DestDRIdentityID=DestDRIdentityID
        self.OrigDRIdentityID=OrigDRIdentityID
        self.OrigBrokerID=tou(OrigBrokerID)
        self.DestBrokerID=tou(DestBrokerID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['DestDRIdentityID', 'OrigDRIdentityID', 'OrigBrokerID', 'DestBrokerID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('DestDRIdentityID', u'目标交易中心代码'),('OrigDRIdentityID', u'原交易中心代码'),('OrigBrokerID', u'原应用单元代码'),('DestBrokerID', u'目标易用单元代码')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcQryInvestorProductGroupMarginField:
    def __init__(self, BrokerID="", InvestorID="", ProductGroupID=""):
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.ProductGroupID=tou(ProductGroupID)
        self.vcmap={}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['BrokerID', 'InvestorID', 'ProductGroupID']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('ProductGroupID', u'品种/跨品种标示')]])
    def getval(self, n):
        if n in []:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcTraderOfferField:
    def __init__(self, Password="", ConnectDate="", ConnectTime="", TraderConnectStatus='1', ConnectRequestTime="", InstallID=0, BrokerID="", ExchangeID="", TraderID="", ParticipantID="", ConnectRequestDate="", LastReportDate="", MaxTradeID="", StartTime="", TradingDay="", MaxOrderMessageReference="", StartDate="", OrderLocalID="", LastReportTime=""):
        self.Password=tou(Password)
        self.ConnectDate=tou(ConnectDate)
        self.ConnectTime=tou(ConnectTime)
        self.TraderConnectStatus=tou(TraderConnectStatus)
        self.ConnectRequestTime=tou(ConnectRequestTime)
        self.InstallID=InstallID
        self.BrokerID=tou(BrokerID)
        self.ExchangeID=tou(ExchangeID)
        self.TraderID=tou(TraderID)
        self.ParticipantID=tou(ParticipantID)
        self.ConnectRequestDate=tou(ConnectRequestDate)
        self.LastReportDate=tou(LastReportDate)
        self.MaxTradeID=tou(MaxTradeID)
        self.StartTime=tou(StartTime)
        self.TradingDay=tou(TradingDay)
        self.MaxOrderMessageReference=tou(MaxOrderMessageReference)
        self.StartDate=tou(StartDate)
        self.OrderLocalID=tou(OrderLocalID)
        self.LastReportTime=tou(LastReportTime)
        self.vcmap={'TraderConnectStatus': {"'4'": '订阅私有流', "'1'": '没有任何连接', "'3'": '已经发出合约查询请求', "'2'": '已经连接'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['Password', 'ConnectDate', 'ConnectTime', 'TraderConnectStatus', 'ConnectRequestTime', 'InstallID', 'BrokerID', 'ExchangeID', 'TraderID', 'ParticipantID', 'ConnectRequestDate', 'LastReportDate', 'MaxTradeID', 'StartTime', 'TradingDay', 'MaxOrderMessageReference', 'StartDate', 'OrderLocalID', 'LastReportTime']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('Password', u'密码'),('ConnectDate', u'完成连接日期'),('ConnectTime', u'完成连接时间'),('TraderConnectStatus', u'交易所交易员连接状态'),('ConnectRequestTime', u'发出连接请求的时间'),('InstallID', u'安装编号'),('BrokerID', u'经纪公司代码'),('ExchangeID', u'交易所代码'),('TraderID', u'交易所交易员代码'),('ParticipantID', u'会员代码'),('ConnectRequestDate', u'发出连接请求的日期'),('LastReportDate', u'上次报告日期'),('MaxTradeID', u'本席位最大成交编号'),('StartTime', u'启动时间'),('TradingDay', u'交易日'),('MaxOrderMessageReference', u'本席位最大报单备拷'),('StartDate', u'启动日期'),('OrderLocalID', u'本地报单编号'),('LastReportTime', u'上次报告时间')]])
    def getval(self, n):
        if n in ['TraderConnectStatus']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)


class CThostFtdcErrOrderField:
    def __init__(self, OrderPriceType='1', Direction='0', BrokerID="", InvestorID="", MinVolume=0, ForceCloseReason='0', VolumeTotalOriginal=0, InstrumentID="", ContingentCondition='1', UserForceClose=0, ErrorMsg="", StopPrice=0, RequestID=0, IsAutoSuspend=0, IsSwapOrder=0, UserID="", GTDDate="", ErrorID=0, BusinessUnit="", LimitPrice=0, OrderRef="", CombHedgeFlag="", VolumeCondition='1', CombOffsetFlag="", TimeCondition='1'):
        self.OrderPriceType=tou(OrderPriceType)
        self.Direction=tou(Direction)
        self.BrokerID=tou(BrokerID)
        self.InvestorID=tou(InvestorID)
        self.MinVolume=MinVolume
        self.ForceCloseReason=tou(ForceCloseReason)
        self.VolumeTotalOriginal=VolumeTotalOriginal
        self.InstrumentID=tou(InstrumentID)
        self.ContingentCondition=tou(ContingentCondition)
        self.UserForceClose=UserForceClose
        self.ErrorMsg=tou(ErrorMsg)
        self.StopPrice=StopPrice
        self.RequestID=RequestID
        self.IsAutoSuspend=IsAutoSuspend
        self.IsSwapOrder=IsSwapOrder
        self.UserID=tou(UserID)
        self.GTDDate=tou(GTDDate)
        self.ErrorID=ErrorID
        self.BusinessUnit=tou(BusinessUnit)
        self.LimitPrice=LimitPrice
        self.OrderRef=tou(OrderRef)
        self.CombHedgeFlag=tou(CombHedgeFlag)
        self.VolumeCondition=tou(VolumeCondition)
        self.CombOffsetFlag=tou(CombOffsetFlag)
        self.TimeCondition=tou(TimeCondition)
        self.vcmap={'VolumeCondition': {"'1'": '任何数量', "'3'": '全部数量', "'2'": '最小数量'}, 'OrderPriceType': {"'1'": '任意价', "'F'": '买一价浮动上浮3个ticks', "'E'": '买一价浮动上浮2个ticks', "'4'": '最新价', "'3'": '最优价', "'2'": '限价', "'7'": '最新价浮动上浮3个ticks', "'A'": '卖一价浮动上浮2个ticks', "'6'": '最新价浮动上浮2个ticks', "'5'": '最新价浮动上浮1个ticks', "'D'": '买一价浮动上浮1个ticks', "'9'": '卖一价浮动上浮1个ticks', "'C'": '买一价', "'8'": '卖一价', "'B'": '卖一价浮动上浮3个ticks'}, 'ContingentCondition': {"'1'": '立即', "'F'": '买一价小于条件价', "'E'": '买一价大于等于条件价', "'4'": '预埋单', "'3'": '止赢', "'H'": '买一价小于等于条件价', "'2'": '止损', "'7'": '最新价小于条件价', "'A'": '卖一价大于等于条件价', "'6'": '最新价大于等于条件价', "'5'": '最新价大于条件价', "'D'": '买一价大于条件价', "'9'": '卖一价大于条件价', "'C'": '卖一价小于等于条件价', "'8'": '最新价小于等于条件价', "'B'": '卖一价小于条件价'}, 'Direction': {"'1'": '卖', "'0'": '买'}, 'ForceCloseReason': {"'7'": '自然人临近交割', "'1'": '资金不足', "'6'": '其它', "'0'": '非强平', "'5'": '违规', "'4'": '持仓非整数倍', "'3'": '会员超仓', "'2'": '客户超仓'}, 'TimeCondition': {"'1'": '立即完成，否则撤销', "'6'": '集合竞价有效', "'5'": '撤销前有效', "'4'": '指定日期前有效', "'3'": '当日有效', "'2'": '本节有效'}}
    def __repr__(self): return "<%s>" % ",".join(["%s:%s" % (x, getattr(self, x)) for x in ['OrderPriceType', 'Direction', 'BrokerID', 'InvestorID', 'MinVolume', 'ForceCloseReason', 'VolumeTotalOriginal', 'InstrumentID', 'ContingentCondition', 'UserForceClose', 'ErrorMsg', 'StopPrice', 'RequestID', 'IsAutoSuspend', 'IsSwapOrder', 'UserID', 'GTDDate', 'ErrorID', 'BusinessUnit', 'LimitPrice', 'OrderRef', 'CombHedgeFlag', 'VolumeCondition', 'CombOffsetFlag', 'TimeCondition']])
    def __str__(self):  return "<%s>" % ",".join(["%s:%s" % (y, self.getval(x)) for x,y in [('OrderPriceType', u'报单价格条件'),('Direction', u'买卖方向'),('BrokerID', u'经纪公司代码'),('InvestorID', u'投资者代码'),('MinVolume', u'最小成交量'),('ForceCloseReason', u'强平原因'),('VolumeTotalOriginal', u'数量'),('InstrumentID', u'合约代码'),('ContingentCondition', u'触发条件'),('UserForceClose', u'用户强评标志'),('ErrorMsg', u'错误信息'),('StopPrice', u'止损价'),('RequestID', u'请求编号'),('IsAutoSuspend', u'自动挂起标志'),('IsSwapOrder', u'互换单标志'),('UserID', u'用户代码'),('GTDDate', u'GTD日期'),('ErrorID', u'错误代码'),('BusinessUnit', u'业务单元'),('LimitPrice', u'价格'),('OrderRef', u'报单引用'),('CombHedgeFlag', u'组合投机套保标志'),('VolumeCondition', u'成交量类型'),('CombOffsetFlag', u'组合开平标志'),('TimeCondition', u'有效期类型')]])
    def getval(self, n):
        if n in ['OrderPriceType', 'Direction', 'ForceCloseReason', 'ContingentCondition', 'VolumeCondition', 'TimeCondition']:
            nkey = "'%s'" % getattr(self, n)
            if nkey in self.vcmap[n]:
                return self.vcmap[n][nkey]
            else:
                return getattr(self, n)
        else:
            return getattr(self, n)
# Set short name alias for the stupid Hungarian Notation
CurrTransferIdentity=CThostFtdcCurrTransferIdentityField
InstrumentCommissionRate=CThostFtdcInstrumentCommissionRateField
SyncingInstrumentTradingRight=CThostFtdcSyncingInstrumentTradingRightField
TransferFutureToBankRsp=CThostFtdcTransferFutureToBankRspField
MarginModel=CThostFtdcMarginModelField
QryDepthMarketData=CThostFtdcQryDepthMarketDataField
RspQueryAccount=CThostFtdcRspQueryAccountField
QryEWarrantOffset=CThostFtdcQryEWarrantOffsetField
FrontStatus=CThostFtdcFrontStatusField
Dissemination=CThostFtdcDisseminationField
SyncingInvestor=CThostFtdcSyncingInvestorField
TransferBank=CThostFtdcTransferBankField
CommPhase=CThostFtdcCommPhaseField
QryProduct=CThostFtdcQryProductField
MarketDataExchange=CThostFtdcMarketDataExchangeField
InvestorGroup=CThostFtdcInvestorGroupField
Discount=CThostFtdcDiscountField
QryInstrumentMarginRate=CThostFtdcQryInstrumentMarginRateField
CommRateModel=CThostFtdcCommRateModelField
SettlementInfoConfirm=CThostFtdcSettlementInfoConfirmField
ForceUserLogout=CThostFtdcForceUserLogoutField
BrokerUserRightAssign=CThostFtdcBrokerUserRightAssignField
UserRightsAssign=CThostFtdcUserRightsAssignField
SuperUser=CThostFtdcSuperUserField
QryErrOrder=CThostFtdcQryErrOrderField
Investor=CThostFtdcInvestorField
QryTrader=CThostFtdcQryTraderField
QryTransferBank=CThostFtdcQryTransferBankField
QryOrderAction=CThostFtdcQryOrderActionField
VerifyInvestorPassword=CThostFtdcVerifyInvestorPasswordField
InputOrderAction=CThostFtdcInputOrderActionField
ErrOrderAction=CThostFtdcErrOrderActionField
QryTradingCode=CThostFtdcQryTradingCodeField
ExchangeMarginRateAdjust=CThostFtdcExchangeMarginRateAdjustField
FensUserInfo=CThostFtdcFensUserInfoField
QryBrokerTradingAlgos=CThostFtdcQryBrokerTradingAlgosField
PartBroker=CThostFtdcPartBrokerField
QueryMaxOrderVolume=CThostFtdcQueryMaxOrderVolumeField
QryTraderOffer=CThostFtdcQryTraderOfferField
UserSession=CThostFtdcUserSessionField
Order=CThostFtdcOrderField
QryPartBroker=CThostFtdcQryPartBrokerField
QrySettlementInfoConfirm=CThostFtdcQrySettlementInfoConfirmField
QrySuperUserFunction=CThostFtdcQrySuperUserFunctionField
QryExchangeMarginRateAdjust=CThostFtdcQryExchangeMarginRateAdjustField
ReqQueryTradeResultBySerial=CThostFtdcReqQueryTradeResultBySerialField
QryExchangeOrderAction=CThostFtdcQryExchangeOrderActionField
NotifyFutureSignIn=CThostFtdcNotifyFutureSignInField
QryParkedOrderAction=CThostFtdcQryParkedOrderActionField
MulticastGroupInfo=CThostFtdcMulticastGroupInfoField
InvestorPositionCombineDetail=CThostFtdcInvestorPositionCombineDetailField
QrySettlementInfo=CThostFtdcQrySettlementInfoField
RemoveParkedOrder=CThostFtdcRemoveParkedOrderField
TradingAccountReserve=CThostFtdcTradingAccountReserveField
SyncingInstrumentMarginRate=CThostFtdcSyncingInstrumentMarginRateField
ReqCancelAccount=CThostFtdcReqCancelAccountField
CFMMCBrokerKey=CThostFtdcCFMMCBrokerKeyField
AuthenticationInfo=CThostFtdcAuthenticationInfoField
QrySuperUser=CThostFtdcQrySuperUserField
MarketDataLastMatch=CThostFtdcMarketDataLastMatchField
QryExchangeOrder=CThostFtdcQryExchangeOrderField
InstrumentStatus=CThostFtdcInstrumentStatusField
ReqAuthenticate=CThostFtdcReqAuthenticateField
MarketData=CThostFtdcMarketDataField
QryInstrumentCommissionRate=CThostFtdcQryInstrumentCommissionRateField
CFMMCTradingAccountKey=CThostFtdcCFMMCTradingAccountKeyField
QryExchangeSequence=CThostFtdcQryExchangeSequenceField
QryInstrumentTradingRight=CThostFtdcQryInstrumentTradingRightField
RspUserLogin=CThostFtdcRspUserLoginField
TradingNotice=CThostFtdcTradingNoticeField
QueryBrokerDeposit=CThostFtdcQueryBrokerDepositField
InstrumentMarginRate=CThostFtdcInstrumentMarginRateField
VerifyCustInfo=CThostFtdcVerifyCustInfoField
PositionProfitAlgorithm=CThostFtdcPositionProfitAlgorithmField
UserPasswordUpdate=CThostFtdcUserPasswordUpdateField
QryTrade=CThostFtdcQryTradeField
DepositResultInform=CThostFtdcDepositResultInformField
TradingAccount=CThostFtdcTradingAccountField
BrokerUserFunction=CThostFtdcBrokerUserFunctionField
TradingCode=CThostFtdcTradingCodeField
TradingAccountPasswordUpdate=CThostFtdcTradingAccountPasswordUpdateField
VerifyFuturePasswordAndCustInfo=CThostFtdcVerifyFuturePasswordAndCustInfoField
QryTransferSerial=CThostFtdcQryTransferSerialField
ErrorConditionalOrder=CThostFtdcErrorConditionalOrderField
QrySyncStatus=CThostFtdcQrySyncStatusField
QryNotice=CThostFtdcQryNoticeField
SyncingInstrumentCommissionRate=CThostFtdcSyncingInstrumentCommissionRateField
TransferQryDetailReq=CThostFtdcTransferQryDetailReqField
BrokerUser=CThostFtdcBrokerUserField
RspFutureSignOut=CThostFtdcRspFutureSignOutField
CancelAccount=CThostFtdcCancelAccountField
QryInvestorPositionCombineDetail=CThostFtdcQryInvestorPositionCombineDetailField
BrokerWithdrawAlgorithm=CThostFtdcBrokerWithdrawAlgorithmField
EWarrantOffset=CThostFtdcEWarrantOffsetField
NotifyQueryAccount=CThostFtdcNotifyQueryAccountField
BrokerTradingAlgos=CThostFtdcBrokerTradingAlgosField
ReqQueryAccount=CThostFtdcReqQueryAccountField
RspFutureSignIn=CThostFtdcRspFutureSignInField
QryLinkMan=CThostFtdcQryLinkManField
QryTradingNotice=CThostFtdcQryTradingNoticeField
QryBrokerUserEvent=CThostFtdcQryBrokerUserEventField
LoadSettlementInfo=CThostFtdcLoadSettlementInfoField
MarketDataUpdateTime=CThostFtdcMarketDataUpdateTimeField
MarketDataStatic=CThostFtdcMarketDataStaticField
UserLogout=CThostFtdcUserLogoutField
DepthMarketData=CThostFtdcDepthMarketDataField
QueryMaxOrderVolumeWithPrice=CThostFtdcQueryMaxOrderVolumeWithPriceField
QryExchangeMarginRate=CThostFtdcQryExchangeMarginRateField
SyncStatus=CThostFtdcSyncStatusField
SpecificInstrument=CThostFtdcSpecificInstrumentField
TransferSerial=CThostFtdcTransferSerialField
BrokerUserOTPParam=CThostFtdcBrokerUserOTPParamField
SyncingTradingCode=CThostFtdcSyncingTradingCodeField
QryBroker=CThostFtdcQryBrokerField
Instrument=CThostFtdcInstrumentField
SyncDeposit=CThostFtdcSyncDepositField
RspSyncKey=CThostFtdcRspSyncKeyField
MarketDataBestPrice=CThostFtdcMarketDataBestPriceField
InvestorPosition=CThostFtdcInvestorPositionField
QryContractBank=CThostFtdcQryContractBankField
QryCommRateModel=CThostFtdcQryCommRateModelField
ExchangeOrder=CThostFtdcExchangeOrderField
CurrentTime=CThostFtdcCurrentTimeField
Broker=CThostFtdcBrokerField
ExchangeOrderActionError=CThostFtdcExchangeOrderActionErrorField
InvestorProductGroupMargin=CThostFtdcInvestorProductGroupMarginField
BrokerUserEvent=CThostFtdcBrokerUserEventField
QryInvestorGroup=CThostFtdcQryInvestorGroupField
QryUserSession=CThostFtdcQryUserSessionField
QryCFMMCTradingAccountKey=CThostFtdcQryCFMMCTradingAccountKeyField
TradingAccountPassword=CThostFtdcTradingAccountPasswordField
NotifyFutureSignOut=CThostFtdcNotifyFutureSignOutField
QryInvestor=CThostFtdcQryInvestorField
ReqOpenAccount=CThostFtdcReqOpenAccountField
MarketDataAsk23=CThostFtdcMarketDataAsk23Field
MarketDataBid23=CThostFtdcMarketDataBid23Field
RspInfo=CThostFtdcRspInfoField
LoginInfo=CThostFtdcLoginInfoField
ExchangeOrderAction=CThostFtdcExchangeOrderActionField
FutureSignIO=CThostFtdcFutureSignIOField
InvestorPositionDetail=CThostFtdcInvestorPositionDetailField
RspAuthenticate=CThostFtdcRspAuthenticateField
InvestorWithdrawAlgorithm=CThostFtdcInvestorWithdrawAlgorithmField
QryMarginModel=CThostFtdcQryMarginModelField
Exchange=CThostFtdcExchangeField
CombinationLeg=CThostFtdcCombinationLegField
SettlementRef=CThostFtdcSettlementRefField
QryTradingAccount=CThostFtdcQryTradingAccountField
SuperUserFunction=CThostFtdcSuperUserFunctionField
MarketDataBase=CThostFtdcMarketDataBaseField
SyncingTradingAccount=CThostFtdcSyncingTradingAccountField
InstrumentTradingRight=CThostFtdcInstrumentTradingRightField
TradingAccountPasswordUpdateV1=CThostFtdcTradingAccountPasswordUpdateV1Field
TransferQryDetailRsp=CThostFtdcTransferQryDetailRspField
NotifySyncKey=CThostFtdcNotifySyncKeyField
ExchangeSequence=CThostFtdcExchangeSequenceField
RspTransfer=CThostFtdcRspTransferField
LogoutAll=CThostFtdcLogoutAllField
ReqSyncKey=CThostFtdcReqSyncKeyField
QryInstrument=CThostFtdcQryInstrumentField
MarketDataAveragePrice=CThostFtdcMarketDataAveragePriceField
ContractBank=CThostFtdcContractBankField
ReqDayEndFileReady=CThostFtdcReqDayEndFileReadyField
TransferHeader=CThostFtdcTransferHeaderField
ParkedOrderAction=CThostFtdcParkedOrderActionField
BrokerSync=CThostFtdcBrokerSyncField
QryInvestorPosition=CThostFtdcQryInvestorPositionField
VerifyFuturePassword=CThostFtdcVerifyFuturePasswordField
ManualSyncBrokerUserOTP=CThostFtdcManualSyncBrokerUserOTPField
QryBrokerUserFunction=CThostFtdcQryBrokerUserFunctionField
InputOrder=CThostFtdcInputOrderField
TransferQryBankReq=CThostFtdcTransferQryBankReqField
QryOrder=CThostFtdcQryOrderField
MarketDataBid45=CThostFtdcMarketDataBid45Field
ReqRepeal=CThostFtdcReqRepealField
Accountregister=CThostFtdcAccountregisterField
ParkedOrder=CThostFtdcParkedOrderField
LinkMan=CThostFtdcLinkManField
RemoveParkedOrderAction=CThostFtdcRemoveParkedOrderActionField
Trade=CThostFtdcTradeField
ReqFutureSignOut=CThostFtdcReqFutureSignOutField
LoginForbiddenUser=CThostFtdcLoginForbiddenUserField
TransferBankToFutureRsp=CThostFtdcTransferBankToFutureRspField
ReqUserLogin=CThostFtdcReqUserLoginField
ReturnResult=CThostFtdcReturnResultField
BrokerTradingParams=CThostFtdcBrokerTradingParamsField
Product=CThostFtdcProductField
UserIP=CThostFtdcUserIPField
QryFrontStatus=CThostFtdcQryFrontStatusField
MDTraderOffer=CThostFtdcMDTraderOfferField
QryMDTraderOffer=CThostFtdcQryMDTraderOfferField
ReqChangeAccount=CThostFtdcReqChangeAccountField
QryLoginForbiddenUser=CThostFtdcQryLoginForbiddenUserField
BrokerUserPassword=CThostFtdcBrokerUserPasswordField
TransferBankToFutureReq=CThostFtdcTransferBankToFutureReqField
QryBrokerUser=CThostFtdcQryBrokerUserField
UserRight=CThostFtdcUserRightField
QryHisOrder=CThostFtdcQryHisOrderField
MarketDataAsk45=CThostFtdcMarketDataAsk45Field
QryExchange=CThostFtdcQryExchangeField
RspRepeal=CThostFtdcRspRepealField
QryInstrumentStatus=CThostFtdcQryInstrumentStatusField
QryParkedOrder=CThostFtdcQryParkedOrderField
Trader=CThostFtdcTraderField
SettlementInfo=CThostFtdcSettlementInfoField
TransferQryBankRsp=CThostFtdcTransferQryBankRspField
QrySyncDeposit=CThostFtdcQrySyncDepositField
OpenAccount=CThostFtdcOpenAccountField
TransferFutureToBankReq=CThostFtdcTransferFutureToBankReqField
QryInvestorPositionDetail=CThostFtdcQryInvestorPositionDetailField
Notice=CThostFtdcNoticeField
QryCombinationLeg=CThostFtdcQryCombinationLegField
BrokerDeposit=CThostFtdcBrokerDepositField
QryAccountregister=CThostFtdcQryAccountregisterField
QryCFMMCBrokerKey=CThostFtdcQryCFMMCBrokerKeyField
ExchangeTrade=CThostFtdcExchangeTradeField
InstrumentMarginRateAdjust=CThostFtdcInstrumentMarginRateAdjustField
ExchangeMarginRate=CThostFtdcExchangeMarginRateField
TradingNoticeInfo=CThostFtdcTradingNoticeInfoField
QryBrokerTradingParams=CThostFtdcQryBrokerTradingParamsField
ReqTransfer=CThostFtdcReqTransferField
RspQueryTradeResultBySerial=CThostFtdcRspQueryTradeResultBySerialField
ChangeAccount=CThostFtdcChangeAccountField
ExchangeOrderInsertError=CThostFtdcExchangeOrderInsertErrorField
OrderAction=CThostFtdcOrderActionField
QryErrOrderAction=CThostFtdcQryErrOrderActionField
SyncingInvestorGroup=CThostFtdcSyncingInvestorGroupField
SyncingInvestorPosition=CThostFtdcSyncingInvestorPositionField
InvestorAccount=CThostFtdcInvestorAccountField
DRTransfer=CThostFtdcDRTransferField
QryInvestorProductGroupMargin=CThostFtdcQryInvestorProductGroupMarginField
TraderOffer=CThostFtdcTraderOfferField
ErrOrder=CThostFtdcErrOrderField
