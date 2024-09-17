# Initialize an empty list to store patient records
patients = []

def patient_add(name, patient_id):
    global patients
    # Add a patient record with name and ID
    patients.append({'name': name, 'id': patient_id})

def patient_remove(patient_id):
    global patients
    # Remove a patient record by ID
    for patient in patients:
        if patient['id'] == patient_id:
            patients.remove(patient)
            return
    print('No such patient ID')

def menu():
    print('''1- Add patient
2- Remove patient
3- End
''')
    choice = int(input('Your choice: '))
    if choice == 1:
        name = input('Enter patient name: ')
        patient_id = input('Enter patient ID: ')
        patient_add(name, patient_id)
        print('Patient added.')
    elif choice == 2:
        patient_id = input('Enter patient ID to remove: ')
        patient_remove(patient_id)
        print('Patient removed.')  
    elif choice == 3:
        print('App Ended')
    else:
        print('Invalid choice.')

def menus():
    choice = menu()
    while choice != 3:
        choice = menu()

menus()
