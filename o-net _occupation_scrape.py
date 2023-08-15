


from bs4 import BeautifulSoup
import requests
from extract_csvs import get_csv_links,download_csvs

def download_occupation_data(occupation_url):

    response  = requests.get(occupation_url)
    html_content = response.content
    soup = BeautifulSoup(html_content,'html.parser')

    occupation_title = soup.find('span',class_ = 'main').text.strip()
    csv_links = get_csv_links(html_content)
    download_csvs(csv_links,occupation_title)



    


download_occupation_data("https://www.onetonline.org/link/details/15-2051.02")
