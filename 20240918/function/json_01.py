import json
patients = [
    {'id': 101, 'name': 'mahesh'},
    {'id': 102, 'name': 'raju'},
    {'id': 103, 'name': 'rohit'}
]
patients_str = json.dumps(patients)
print(patients, patients_str)
with open('patients_data.json', 'w') as patients_ds:
    json.dump(patients, patients_ds)

patients_list3 = json.loads(patients_str)
print(patients_list3, type(patients_list3))
with open('patients_data.json', 'r') as patients_ds:
    patients_list3 = json.load(patients_ds)
    print(patients_list3, type(patients_list3))