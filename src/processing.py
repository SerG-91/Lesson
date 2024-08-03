list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
state = 'EXECUTED'
def filter_by_state(values, filter_by1):
    new_list = [i for i in values if i['state'] == filter_by1]
    return new_list

print(filter_by_state(list, state))
