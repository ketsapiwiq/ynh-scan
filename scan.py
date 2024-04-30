import toml
import json
import os
import tomli
import requests

from time import sleep

# FIXME: use API workflow (initial results are meant to be cached and API for changes since date meant to be queried independently + results are paginated)
# https://nvd.nist.gov/developers/api-workflows

# Python lib exists but not used here
# ex: cves = nvdlib.searchCVE(cpeName=cpe, key=nvd_api_key)
apps = []
nvd_api_key = os.getenv("YUNOHOST_NVD_API_KEY")

advisories = []


with open("apps.toml", "rb") as file:
    apps = tomli.load(file)

    for name in apps.keys():
        # With version numbers boundaries:
        # url = "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString={cpe}&versionStart={version_start}&versionStartType=including&versionEnd={version_end}&versionEndType=excluding"
        # Btw, CPE looks like: f"cpe:/a:{app}:{version}"

        cpe = apps[name].get("cpe")
        if cpe:
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString={cpe}"
        else:
            continue
        try:
            if nvd_api_key:
                results = requests.get(
                    headers={"content-type": "application/json", "apiKey": nvd_api_key},
                    url=url,
                )
                sleep(1)
            else:
                results = requests.get(
                    headers={"content-type": "application/json"}, url=url
                )
                sleep(6)
            print(results.text)
            # json_results = json.loads(results.text)
        except:
            print(f"Failed to retrieve data: {results}")

        os.makedirs("vulns/" + name, exist_ok=True)
        with open("vulns/" + name + "/results.json", "w") as file:
            file.write(results.text)

        # TODO: wanted format for security.toml²
        #     print(result)
        # advisory = {app: name,
        #             versions: result.versions,
        # infos: result.urls,
        # level: level(result.CVSS)
        # "app": "jirafeau",
        # "versions": "< 1.4~ynh1",
        # "infos": "https://github.com/yunohost-apps/jireafeau_ynh/issues/666",
        # "level": "warning"

        # with open(app.name + "/security.toml", "wb") as file:
        # tomli_w.dumps(advisories, file, indent=4)
