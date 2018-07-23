provinces = {
    'Hunan': 'HN',
    'Beijing': 'BJ',
    'Guangdong': 'GD'
}

cities = {
    'HN': 'Changsha',
    'BJ': 'Beijing',
    'GD': 'Shenzhen'
}

for province, abbrev in provinces.items():
    print(f'{province} is abbreviated {abbrev}')
    print(f'{abbrev} has the city {cities[abbrev]}')