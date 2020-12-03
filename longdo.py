from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def Translate(vocab,fulltext=False):
	url = 'https://dict.longdo.com/mobile.php?search={}'.format(vocab)
	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html,'html.parser')
	
	tables = data.find_all('table',{'class':'result-table'})
	result = []

	for i,t in enumerate(tables):
		row = t.find_all('tr')
		for j,c in enumerate(row):
			cl = c.find_all('td')
			meaning = cl[1].text.split(',')[0]
			full = cl[1].text
			if fulltext:
				if meaning[0] == '[':
					result.append({'vocab':cl[0].text,'meaning':meaning,'full':full})
			else:
				if meaning[0] == '[':
					result.append({'vocab':cl[0].text,'meaning':meaning})
	if len(result) != 0:
		return result[0]
	else:
		return None
	


if __name__ == '__main__':
	result = Translate('engineer')
	print(result)