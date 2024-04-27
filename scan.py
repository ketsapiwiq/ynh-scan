import nvdlib
import toml



# Load the apps.toml file
with open('apps.toml', 'r') as file:
    data = toml.load(file)

# Get the CPE from the "13ft" app section
# cpe = data.get('13ft', {}).get('cpe', None)



# import json

# data = {
#     "apps": [
#         {
#             "app": "jirafeau",
#             "versions": "< 1.4~ynh1",
#             "infos": "https://github.com/yunohost-apps/jireafeau_ynh/issues/666",
#             "level": "warning"
#         }
#     ]
# }




# Save the data as a JSON file
with open("security.json", "w") as file:
    json.dump(data, file, indent=4)

# if cpe:
#     print(f"The CPE for '13ft' app is: {cpe}")
# else:
#     print("No CPE information found for '13ft' app.")
    
    # or multiple CPEs
cpes = ["cpe:/a:apache:apache_http_server:2.4.7", "cpe:/o:linux:linux_kernel:5.10.0"]

# # Create a CVEBinTool object
# cve_tool = cve_bin_tool.CVEBinTool()

import toml

# Fetch CVEs for the CPE(s)
# cpes = 


for cpe in cpes:
    cves = nvdlib.searchCVE(keywordSearch=cpe)



# # Print the CVEs
# for cve in cves:
#     print(cve.id, cve.description)


import nvdlib
import json

# Load the security data from the JSON file
with open("security.json", "r") as file:
    data = json.load(file)

# Extract the necessary information from the security data
app = data["apps"][0]["app"]
version = data["apps"][0]["versions"]

# Build the search parameters
keywordSearch = f"cpe:/a:{app}:{version}"

# Search for CVEs using the parameters
cves = nvdlib.searchCVE(keywordSearch=keywordSearch)

# Print the CVEs
for cve in cves:
    print(cve.cve_id, cve.description)