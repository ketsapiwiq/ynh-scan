# import nvdlib
import toml
import json
import os

apps = []

# Load the apps.toml file
with open('apps.toml', 'r') as file:
    data = toml.load(file)
    if hasattr(data, "cpe"):    
        app = {name: data.name,
                cpe: data.cpe}
        apps.append(app)

# cpes = ["cpe:/a:apache:apache_http_server:2.4.7", "cpe:/o:linux:linux_kernel:5.10.0"]

nvd_api_key=os.getenv('YUNOHOST_NVD_API_KEY')

for app in apps:
# Build the search parameters
# keywordSearch = f"cpe:/a:{app}:{version}"


# https://nvd.nist.gov/developers/api-workflows

    # result = requests.get(headers={'content-type': 'application/json', 'apiKey': key}, url = "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString={cpe}&versionStart={version_start}&versionStartType=including&versionEnd={version_end}&versionEndType=excluding&apiKey={YUNOHOST_NVD_API_KEY}"
    result = requests.get(headers={'content-type': 'application/json', 'apiKey': key}, url = "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString={cpe}&apiKey={YUNOHOST_NVD_API_KEY}")
    # cves = nvdlib.searchCVE(cpeName=cpe, key=nvd_api_key)

    # Print the CVEs
    # for cve in cves:
    print(cves[0])
    # .cve_id, cve.description)
    # "app": "jirafeau",
    # "versions": "< 1.4~ynh1",
    # "infos": "https://github.com/yunohost-apps/jireafeau_ynh/issues/666",
    # "level": "warning"

    if not os.access(app.name):
        os.mkdir(app.name)
    with open(app.name+"/security.toml", "w") as file:
        toml.dumps(cves, file, indent=4)
