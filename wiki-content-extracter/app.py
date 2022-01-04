import wikipedia
import traceback
import json

class WikiContentExtracter:
    
    def __init__(self):
        print("Initializing Components")
        
    def search_titles(self,search_input):
        wiki_title_list = []
        try:
            wiki_title_list = wikipedia.search(search_input)
        except:
            error_response = str(traceback.format_exc())
            print("Excetion occured while extracting the title contends from Wiki :: "+error_response)
        return wiki_title_list
    
    def get_summary(self,search_input):
        text_summary = None
        try: 
            text_summary = wikipedia.summary(search_input)
        except:
            error_response = str(traceback.format_exc())
            print("Excetion occured while extracting the summary contends from Wiki :: "+error_response)
        return text_summary
    
    def get_complete_metadata(Self,search_input):
        complete_metadata = None
        try:
            complete_metadata = wikipedia.page(search_input).content
        except:
            error_response = str(traceback.format_exc())
            print("Excetion occured while extracting the meta data contends from Wiki :: "+error_response)
        return complete_metadata

wiki_contends = {}
wiki_extr_instance = WikiContentExtracter()
title_list  = wiki_extr_instance.search_titles("Ronaldo")
wiki_contends["title_list"] = title_list

if title_list is not None:
    selected_title = title_list[0]
    wiki_contends["selected_title"] = selected_title
    summary = wiki_extr_instance.get_summary(selected_title)
    wiki_contends["summary"] = summary
    complete_contends = wiki_extr_instance.get_complete_metadata(selected_title)
    wiki_contends["complete-metadata"] = complete_contends