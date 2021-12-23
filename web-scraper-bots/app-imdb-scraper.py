from bs4 import BeautifulSoup
from applicationutils import Applicationutils
import json

import warnings
warnings.filterwarnings("ignore")

class IMDBScraperBot:
    
    def __init__(self):
        print("Initializing parameters for IMDBScraperBot")
        
    def getTitleArtifacts(self,trElement):
        title_details = {}
        if trElement is not None:
            title_column_element = trElement.find("td",{"class":"titleColumn"})
            if title_column_element is not None:
                anch_content = title_column_element.find("a")
                year_element = title_column_element.find("span")
                movie_year = year_element.get_text()
                if "(" in movie_year:
                    movie_year = movie_year.replace("(","").strip()
                if ")" in movie_year:
                    movie_year = movie_year.replace(")","").strip()
                title_details["Movie-Year"] = movie_year
                if anch_content is not None:
                    title_details["Movie-Details"] = anch_content['title']
                    title_details["Movie-Name"] = anch_content.get_text()
        return title_details
    
    def getRatingsDetails(Self,trElement):
        rating_details = {}
        if trElement is not None:
            rating_column_element = trElement.find("td",{"class":"ratingColumn imdbRating"})
            if rating_column_element is not None:
                strong_content = rating_column_element.find("strong")
                if strong_content is not None:
                    strong_title = strong_content["title"]
                    if strong_title is not None and "based on" in strong_title:
                        content_list = strong_title.split("based on")
                        rating_details["ratings"] = content_list[0].strip()
                        rating_details["total-user-ratings"] = content_list[1].strip().replace("user ratings","").strip()
                    elif strong_title is not None:
                        rating_details["ratings"] = strong_title.get_text()
        return rating_details
    
scraper_bot = IMDBScraperBot()       
website_url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
soup_instance = Applicationutils.getWebSiteContendsAsHTML(website_url)

if soup_instance is not None:
    main_table = soup_instance.find("table",{"class":"chart full-width"})
    tr_list = main_table.find_all('tr')
    completed_parsed_list = []
    for indv_tr_element in tr_list:
        all_details = {}
        title_details = scraper_bot.getTitleArtifacts(indv_tr_element)
        all_details["title_details"] = title_details
        ratings_details = scraper_bot.getRatingsDetails(indv_tr_element)
        all_details["rating_details"] = ratings_details
        completed_parsed_list.append(all_details)
    imdb_response_contends = json.dumps(completed_parsed_list, indent = 4)
    print(imdb_response_contends)
    
    # Write the contends to a response file 
    file_path = "outputs/imdb-response-output.json"
    encoding_input = "UTF-8"
    Applicationutils.write_contends_to_file(file_path,encoding_input,completed_parsed_list)
    print("Completed Writing Contends to file")
    
    