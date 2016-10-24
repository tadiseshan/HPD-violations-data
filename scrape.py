import requests, zipfile, io

response = requests.get("http://www1.nyc.gov/assets/hpd/downloads/misc/Violations20160401.zip")

z = zipfile.ZipFile(io.BytesIO(response.content))
z.extractall()