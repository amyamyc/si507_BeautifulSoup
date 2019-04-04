# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
import csv

# "crawling" -- generally -- going to all links from a link ... like a spiderweb
# its specific def'n varies, but this is approximately the case in all situations
# and is like what you may want to do in many cases when scraping

######

# Constants
START_URL = "https://www.nps.gov/index.htm"
FILENAME = "sample_secondprog_cache.json"

# This is one instance of the class Cache from the advanced_expiry_caching file
# Advanced expiry caching file has methods and other things
# The instance of Cache class is called Program Cache
PROGRAM_CACHE = Cache(FILENAME)
# print(type(PROGRAM_CACHE))

# function access page data. If data in cache, put it in the data variable. If not, send the request to the nps.gov wesbite
def access_page_data(url):
    data = PROGRAM_CACHE.get(url)
    if not data:
        data = requests.get(url).text
        PROGRAM_CACHE.set(url, data) # default here with the Cache.set tool is that it will expire in 7 days, which is probs fine, but something to explore
    return data

#######

main_page = access_page_data(START_URL)

# finds all the html stuff on the main/ first page of the nps.gov website
main_soup = BeautifulSoup(main_page, features="html.parser")
# finds the elements with ul tag with the class name "drop down menu"
list_of_states = main_soup.find('ul', {'class':'dropdown-menu'})

#finds all the links that have a tag in the list of states variable
all_links = list_of_states.find_all('a')
# print(all_links) # cool

topics_pages = [] # gotta get all the data in BeautifulSoup objects to work with...
for l in all_links:
    page_data = access_page_data("https://www.nps.gov" + l['href'])
    soup_of_page = BeautifulSoup(page_data, features="html.parser")
    # print(soup_of_page)
    topics_pages.append(soup_of_page)
# print(topics_pages[0].prettify()) # this will print all the html code from the first state Alabama

# Now I can do some investigation on just one of those BeautifulSoup instances, and thus decide what I want to do with each one...
# Each time I run the program, I'm not going to the internet at all sometimes unless some page is new or it's -- in this case -- been more than 7 days since storing data.
# After the first time, it'll run much faster! (On a certain scale, anyway)

def csv_header_list():
	return ["NAME", "TYPE", "DESCRIPTION", "LOCATION"]
file_to_write = open("park_info.csv", "w")
csv_writer = csv.writer(file_to_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(csv_header_list())

master = []
for state in topics_pages:
        # sites = topics_pages[0].find_all("div", {"class": "col-md-9"}) # for one state alabama
    sites = state.find_all("div", {"class": "col-md-9"}) # look in this class
    for park in sites: # for each park in alabama
        name = park.h3.text #the name of park at each state " Birmingham Park"
        master.append([name])
        type = park.h2.text # the type of site "National Monument"
        if type == "":
            type = "NA"
        master.append([type])
        description = park.p.text # description of each site
        strip_description = description.strip('\n')
        location = park.h4.text # location of the site
        csv_writer.writerow([name, type, strip_description, location])
# print(master)
