from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote
import os




def get_csv_links(html):
    soup = BeautifulSoup(html, "html.parser")

    # Find all <a> elements with the class "ms-2"
    csv_links = soup.find_all("a", class_="ms-2", title="Comma-Separated Values")

    # Extract the href attribute values from the <a> elements
    csv_urls = [link["href"] for link in csv_links]

    return csv_urls


def download_csvs(csv_urls,occupation_title):
    occupation_code = None
    os.makedirs(f'occupations/{occupation_title}',exist_ok = True)
    for idx,url in enumerate(csv_urls):
        base_url = "https://www.onetonline.org"  # Replace with the actual base URL



        csv_url = f"{base_url}{url}"
        print(csv_url)

        

        response_csv = requests.get(csv_url)
        if response_csv.status_code == 200:
            
            # Try to get the filename from Content-Disposition header
            content_disposition = response_csv.headers.get("content-disposition", "")
            filename = content_disposition.split("filename=")[-1]
            filename = unquote(filename.strip("\"'"))
            if idx ==0:
                start_index = filename.index('_') + 1
                end_index = filename.index('.csv')

                # Extract the desired substring
                occupation_code = filename[start_index:end_index]
                
            
            code_idx = filename.index('_'+occupation_code)
            filename = filename[:code_idx]
            with open(f'occupations/{occupation_title}/{filename}.csv','wb+') as file:
                file.write(response_csv.content)



