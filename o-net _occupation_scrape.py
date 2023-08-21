


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



    
jobs = ["https://www.onetonline.org/link/details/15-2041.01",
        "https://www.onetonline.org/link/details/15-2021.00",
        "https://www.onetonline.org/link/details/15-1299.03",
        "https://www.onetonline.org/link/details/15-2041.00"]

#for url in jobs:
    #download_occupation_data(url)


download_occupation_data("https://www.onetonline.org/link/details/19-2099.01")