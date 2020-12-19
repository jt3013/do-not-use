import pandas as pd
import numpy as np
Violations = pd.read_csv('input/Violations.csv')
Violations.info

# results = Violations

# ViolationType = {
#     '1': 'E-ELEVATOR',
#     '2': 'C-CONSTRUCTION',
#     '3': 'LL6291-BOILERS',
# }

# Type = input('(1) E-ELEVATOR\n(2) C-CONSTRUCTION\n(3) LL6291-BOILERS\nEnter the type of violation: ')
# if Type in ViolationType.keys():
#     results = results.loc[Violations['VIOLATION_TYPE'] == ViolationType.get(Type)]


# boro = input('(1) Manhattan\n(2) The Bronx\n(3) Brooklyn\n(4) Queens\n(5) Staten Island\nEnter a boro: ')
# if boro in ['1','2','3','4','5']:
#     results = results.loc[Violations['BORO'] == boro]

# street = input('Enter a street:\n').upper()
# results = results.loc[Violations['STREET'] == street]

# house_number = input('Enter the house number:\n')
# results = results.loc[Violations['HOUSE_NUMBER'] == house_number]

# print(results)



Active_Projects = pd.read_csv('input/cartodb-query.csv')
Active_Projects.info
projectresults = Active_Projects


boroughs = {
    '1': 'Manhattan',
    '2': 'The Bronx',
    '3': 'Brooklyn',
    '4': 'Queens',
    '5': 'Staten Island',
}

borough = input('(1) Manhattan\n(2) The Bronx\n(3) Brooklyn\n(4) Queens\n(5) Staten Island\nEnter a borough: ')
company_name = input('Enter company name: ')

for row in Violations.index:
    if Violations['STREET'][row] in Active_Projects['job_location_street_name'].values and Violations['HOUSE_NUMBER'][row] in Active_Projects['job_location_house_number'].values:
        if str(Violations["BORO"][row]) == borough:
                print(f'{Violations["HOUSE_NUMBER"][row]} {Violations["STREET"][row]}, {boroughs.get(borough)} NY ({company_name})')


#boroughs.get(borough) in Active_Projects['borough'] and 