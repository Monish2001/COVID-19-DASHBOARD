import pymongo
from utils import state_list

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["covid"]

mycol = mydb["case"]

statelist_table = mydb["statelist"]


def insert(myDict, myStateDict):
    statelist = state_list.state_list_func()

    if(myDict["state"] not in statelist):
        statelist_table.insert_one(myStateDict)
        mycol.insert_one(myDict)
    else:
        mycol.insert_one(myDict)


def range_record(fromDate, toDate):
    range_rec = mycol.find({'$and': [{"time": {"$gte": fromDate}}, {"time": {"$lte": toDate}}]}, {
                           "_id": 0, "time": 1, "state": 1, "active": 1, "cured": 1, "death": 1, "confirmed": 1})
    return range_rec


def state():
    states = statelist_table.find({}, {"_id": 0, "state": 1})
    return(states)
