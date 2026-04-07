'''
Things to do next:
    1. Filter out software engineering roles only.
'''

from bs4 import BeautifulSoup
import requests
import csv


csv_file = open('stripe-jobs-scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'team', 'location', 'link'])

base_url = 'https://stripe.com/jobs/search'
next_url = '?skip=0'

while next_url!=None:
    source = requests.get(f"{base_url}{next_url}").text # adding text at the end to get the source code from the response object returned by the requests.get() command
    soup = BeautifulSoup(source, 'lxml')

    all_jobs = soup.find('tbody', class_='TableBody JobsListings__tableBody')
    
    for job_listing in all_jobs.find_all('tr', class_="TableRow"):

        job_info = job_listing.find('a', class_='JobsListings__link')
        job_title = job_info.text
        job_link = job_info['href']
        complete_link = f"https://stripe.com{job_link}"

        job_team = job_listing.find('li', class_ = 'List__item ListItem JobsListings__departmentsListItem').text.strip()
        job_location = job_listing.find('span', class_ = 'JobsListings__locationDisplayName').text

        csv_writer.writerow([job_title, job_team, job_location, complete_link])
    
    paginated_section = soup.find('ul', class_='JobsPagination__list')
    paginated_list = paginated_section.find_all('a', class_='Link JobsPagination__link')
    for pg_list in paginated_list:
        if pg_list.text == 'Next':
            next_url = pg_list['href']
            print(next_url)
            break
        else:
            next_url = None
    




