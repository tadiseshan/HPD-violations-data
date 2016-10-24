import requests, zipfile, io, bs4

url = 'http://www1.nyc.gov/site/hpd/about/violation-open-data.page'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, "html.parser")

files = []

for a in soup.select('.span6 li > a'):
	files.append(a['href'])

#this didn't grab all the files in 2016, for some reason. manually downloaded, will come back to figure out why
for file in files:
	res = requests.get('http://www1.nyc.gov' + file)
	z = zipfile.ZipFile(io.BytesIO(res.content))
	z.extractall('data')
