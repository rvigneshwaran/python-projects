import wikipedia
import traceback
import json

class WikiContentExtracter:
    """[This project is intent to retrive the contends from the wiki site , With the search input we would be able to retrive all the information related to the search content.]
    """
    
    def __init__(self):
        print("Initializing Components")
        
    def search_titles(self,search_input):
        """[This Method is Intended to rrieve all the possible titles with the search input ]

        Args:
            search_input ([string]): [search input for which the information is to be retrived]

        Returns:
            [list]: [all possible values of the search input]
        """
        wiki_title_list = []
        try:
            wiki_title_list = wikipedia.search(search_input)
        except:
            error_response = str(traceback.format_exc())
            print("Excetion occured while extracting the title contends from Wiki :: "+error_response)
        return wiki_title_list
    
    def get_summary(self,search_input):
        """[This Method is Intended to retrive the summary of the search input of the user.]

        Args:
            search_input ([string]): [input text for which the summary from wiki is to be retrived]

        Returns:
            [string]: [sumary content of the title from the wiki site]
        """
        text_summary = None
        try: 
            text_summary = wikipedia.summary(search_input)
        except:
            error_response = str(traceback.format_exc())
            print("Excetion occured while extracting the summary contends from Wiki :: "+error_response)
        return text_summary
    
    def get_complete_metadata(self,search_input):
        """[Method intended to retrive all the contends of the page in wike based on the user input title]

        Args:
            search_input ([string]): [search input title]

        Returns:
            [string]: [complete metat data from the page]
        """
        complete_metadata = None
        try:
            complete_metadata = wikipedia.page(search_input).content
        except:
            error_response = str(traceback.format_exc())
            print("Excetion occured while extracting the meta data contends from Wiki :: "+error_response)
        return complete_metadata
    
    def write_contends_file(self,input_contends,fileName):
        """[Method Intended to write the contends of the dictionary in a output file ]

        Args:
            input_contends ([dict]): [The created dictionary which is going to be writtern in this file]
            fileName ([string]): [location and name of the output file]
        """
        try:
            response_contends = json.dumps(input_contends, indent=4)
            with open(fileName, 'w') as file_instance:
                file_instance.write(response_contends)
            print("Completed writing response contends to a file")
        except:
            error_response = str(traceback.format_exc())
            print("Exception occured while executing the method write_contends_file ::"+error_response)
            

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
    file_name = "outputs/response-output-file.json"
    wiki_extr_instance.write_contends_file(wiki_contends,file_name)