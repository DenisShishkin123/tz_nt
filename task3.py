import json
   
def value(id, data):
    for i in data:
        if i['id']==id : return i['value']

def search(data):
    for i in data:
        # print(i['id'])
        i['value'] = value(i['id'],data_values)
        if i.get('values', False): search(i['values'])
    return data

with open('tests.json', encoding='utf-8')  as tests, open('values.json', encoding='utf-8') as values:

    data_values = json.load(values)['values']

    data_tests = json.load(tests)['tests']
    data = {'tests':search(data_tests)}

with open('report.json', 'w', encoding='utf-8') as report:
    json.dump(data, report, indent=2)
