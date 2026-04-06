'''
Things to do next:
    1. Capture the location and department along with title and job link.
    2. Figure out how to scrape all the data and not get affected by pagination.
    3. Form the complete job link URL by pre-prending stripe.com.
'''



from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://stripe.com/jobs/search').text # adding text at the end to get the source code from the response object returned by the requests.get() command

soup = BeautifulSoup(source, 'lxml')

csv_file = open('stripe-jobs-scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['job_title', 'job_link'])

# all_jobs = soup.find('tbody', class_='TableBody JobsListings__tableBody')

# one_job = all_jobs.find('tr', class_="TableRow")

# print(one_job)

for job_listing in soup.find_all('a', class_='JobsListings__link'):
    job_title = job_listing.text
    job_link = job_listing['href']

    csv_writer.writerow([job_title, job_link])






