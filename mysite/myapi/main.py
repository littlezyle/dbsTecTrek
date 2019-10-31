import dbsApi
import json
import requests
# import pandas as pd

userInfo = {}

def init(user):
    userInfo = {}
    userInfo['id'] = dbsApi.getCustIdUrl(user)['customerId']
    userInfo['details'] = dbsApi.getCustDetailsUrl(userInfo['id'])
    userInfo['deposit'] = []
    for i in dbsApi.getDepositAccountDetails(userInfo['id']):
        userInfo['deposit'].append(str(i['accountId']))
    userInfo['credit'] = []
    for i in dbsApi.getCreditAcc(userInfo['id']):
        userInfo['credit'].append(str(i['accountId']))
    return userInfo

def getTransactionDataByRange_cat(start, end, accountId):
    ret = {}
    for i in dbsApi.getTransactionDetailsUrl(accountId):
        # print(i['tag'])
        if i['tag'] not in ret.keys():
            ret[i['tag']] = float(i['amount'])
        else:
            ret[i['tag']] += float(i['amount'])
    return ret

userInfo = init("limzeyang")
# requests.post("localhost:8000/test/users",data=json.dumps(userInfo))
# print(dbsApi.getTransactionDetailsUrl("10"))
print(getTransactionDataByRange_cat("01-01-2018", "02-01-2019",str(userInfo['deposit'][0])))
# print(userInfo)