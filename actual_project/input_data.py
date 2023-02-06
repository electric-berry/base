import requests
import re
def get_data(target):
    r = requests.get('https://roadtraffic.dft.gov.uk/local-authorities')
    x = re.search(f'<a href="/local-authorities/[\d]+">{target}</a>', r.text)
    end = re.search('[\d]+', x.group())
    download = requests.get(f'https://storage.googleapis.com/dft-statistics/road-traffic/downloads/rawcount/local_authority_id/dft_rawcount_local_authority_id_{end.group()}.csv')
    csv_file = open('data.csv', 'wb')
    csv_file.write(download.content)
    csv_file.close()
