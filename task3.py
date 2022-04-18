# task3

import json

# ищет value по id  в файле values
def value(id, data):
    for i in data:
        if i['id']==id : return i['value']

# перебирает словари в списке
# и вызывает fun'values'
# \и если находит список вызывает себя же\
def search(data):
    for i in data:
        # print(i['id'])
        i['value'] = value(i['id'],data_values)
        if i.get('values', False): search(i['values'])
    return data

f1='tests.json'
f2='values.json'

with open(f1) as tests, open(f2) as values:
    data_values = json.load(values)['values']
    data_tests = json.load(tests)['tests']
    data = {'tests':search(data_tests)}


with open('report.json', 'w') as report:
    json.dump(data, report, indent=2)
