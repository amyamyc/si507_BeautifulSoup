#### SI 507 Python Programming Project 4 Assignment
This is a homework assignment for SI 507/ Professor Jackie Cohen at the University of Michigan. I have selected option 1 to scrape information from the National Parks Website.

##### What are the files included?
The files included are sample_crawling_data.py, requirements.txt, README.md and advanced_expiry_caching.

##### How do you run this project?
Fork and clone files onto local computer from this github account.
requirements.txt will indicate all the dependencies required for this project. Open the terminal and download all the dependencies by typing pip install -r requirements.txt.
Type into terminal "sample_crawling_data.py" to run the file.

##### What is the functionality?
sample_crawling_data.py scrapes the national parks website for data regarding park sites in each U.S. state.
It is important to note that the file makes a single request to the National Parks website and stores the html data from each state's national parks page. This data is stored in a variable in the code, but also in a json file called "sample_secondprog_cache". The json file is readable if opened in json editor. From there, using the python package Beautiful Soup, the code will extract specific types of data about each states' parks (name, description, type of site, location.)

##### What is the final result?
The final result is a csv file on your local computer named "parks_info.csv". This csv file is organized into columns: Name, Type, Description and Location. Each column is populated with data that has been extracted from the National Parks website.
