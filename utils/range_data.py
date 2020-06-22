import mongodb


def range_data(from_date, to_date):

    range_record = mongodb.range_record(from_date, to_date)
    range_record_list = list(range_record)
    return(range_record, range_record_list)
