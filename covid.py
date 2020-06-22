import time
from datetime import datetime
import datetime
import itertools
from operator import itemgetter
import mongodb
from utils import state_list
from utils import date_conversion
from utils import range_data


def final_rec(range_record_list, statelist):
    state_record = []
    result = []

    for state in statelist:
        for i in range_record_list:
            if(i['state'] == state):
                state_record.append(i)
        sorted_state_rec = sorted(
            state_record, key=itemgetter('time'), reverse=True)
        result.append((sorted_state_rec[0]))
        result.append((sorted_state_rec[-1]))
        state_record = []

    return(result)


def change_in_case(result, statelist):
    final_result = []
    change_in_case_list = []
    for state in statelist:
        for i in result:
            if(i['state'] == state):
                final_result.append(i)

        if(len(final_result) == 2):
            if(final_result[0]['confirmed'] == final_result[1]['confirmed']):
                res = [state, "Has no change in confirmed cases"]
                change_in_case_list.append(res)
            else:
                increased_val = final_result[0]['confirmed'] - \
                    final_result[1]['confirmed']
                res = [state, "Has increased by " +
                       str(abs(increased_val)) + " confirmed cases"]
                change_in_case_list.append(res)
        else:
            res = [state, "has no data"]
            change_in_case_list.append(res)
        final_result = []
    return(change_in_case_list)


def specific_state(change_in_case_list, statelist, stateName):
    if stateName in statelist:
        for i in change_in_case_list:
            if(i[0] == stateName):
                return(i)
    else:
        specific_state_result = [stateName,
                                 "does not match with the statelist"]
        return(specific_state_result)


def get_state_table(from_date, to_date):
    from_date, to_date = date_conversion.str_to_datetime(from_date, to_date)

    range_record, range_record_list = range_data.range_data(from_date, to_date)

    statelist = state_list.state_list_func()

    date_conversion.date_time_to_str(range_record_list)

    result = final_rec(range_record_list, statelist)

    return(change_in_case(result, statelist))


def get_specific_state(from_date, to_date, stateName):
    from_date, to_date = date_conversion.str_to_datetime(from_date, to_date)

    range_record, range_record_list = range_data.range_data(from_date, to_date)

    statelist = state_list.state_list_func()

    date_conversion.date_time_to_str(range_record_list)

    result = final_rec(range_record_list, statelist)

    change_in_case_list = change_in_case(result, statelist)

    return(specific_state(change_in_case_list, statelist, stateName))
