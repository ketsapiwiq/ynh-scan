import csv
import toml

with open('cpe.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]


with open('apps.toml', 'r') as file:
    apps = toml.load(file)

for app in apps:
    for name, cpe in data:
        if name == app:
            app.cpe = cpe


with open('apps.toml', 'w') as file:
    toml.dump(file, apps)
# for name, cpe in data:
    
