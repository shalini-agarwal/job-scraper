'''
Things to do next:
    1. Figure out how to scrape all the data and not get affected by pagination.
    2. Filter out software engineering roles only.
'''



from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://stripe.com/jobs/search').text # adding text at the end to get the source code from the response object returned by the requests.get() command

soup = BeautifulSoup(source, 'lxml')

csv_file = open('stripe-jobs-scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'team', 'location', 'link'])

all_jobs = soup.find('tbody', class_='TableBody JobsListings__tableBody')


## For a single job post

# job_listing = all_jobs.find('tr', class_="TableRow")

# job_info = job_listing.find('a', class_='JobsListings__link')
# job_title = job_info.text
# job_link = job_info['href']
# complete_link = f"https://stripe.com{job_link}"

# job_team = job_listing.find('li', class_ = 'List__item ListItem JobsListings__departmentsListItem').text.strip()
# job_location = job_listing.find('span', class_ = 'JobsListings__locationDisplayName').text

# print(job_title)
# print(job_team)
# print(job_location) 
# print(complete_link)



for job_listing in all_jobs.find_all('tr', class_="TableRow"):

    job_info = job_listing.find('a', class_='JobsListings__link')
    job_title = job_info.text
    job_link = job_info['href']
    complete_link = f"https://stripe.com{job_link}"

    job_team = job_listing.find('li', class_ = 'List__item ListItem JobsListings__departmentsListItem').text.strip()
    job_location = job_listing.find('span', class_ = 'JobsListings__locationDisplayName').text

    csv_writer.writerow([job_title, job_team, job_location, complete_link])






