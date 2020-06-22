import datetime


def date_time_to_str(range_rec_list):

    for i in range_rec_list:
        for k, v in i.items():
            if(k == 'time'):
                i['time'] = v.strftime("%Y/%m/%d, %H:%M:%S")


def str_to_datetime(fromDate, toDate):
    fromDate = datetime.datetime.strptime(fromDate, '%Y-%m-%dT%H:%M')
    toDate = datetime.datetime.strptime(toDate, '%Y-%m-%dT%H:%M')
    return(fromDate, toDate)
