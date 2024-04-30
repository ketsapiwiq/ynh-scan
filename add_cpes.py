import csv
import tomli,tomli_w

with open('cpe.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]


with open('apps.toml', 'rb') as file:
    apps = tomli.load(file)
    for name, cpe in data:
        if name in apps.keys():
            apps[name]['cpe'] = cpe

    with open('apps.toml', 'wb') as file:
        print(tomli_w.dumps(apps))
        tomli_w.dump(apps, file)
        
