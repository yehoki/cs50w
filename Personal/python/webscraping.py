from bs4 import BeautifulSoup
import requests
import time

# Web scraping reed
html_test = requests.get('https://www.reed.co.uk/jobs/software-jobs-in-london').text
soup = BeautifulSoup(html_test, 'lxml')
job_count = soup.find('span', class_ = "count").text.replace(' ', '')
print(job_count)

companies = set()
for i in range(2,10):
    web_page = requests.get(f'https://www.reed.co.uk/jobs/software-jobs-in-london?pageno={i}').text
    soup = BeautifulSoup(web_page, 'lxml')
    jobs = soup.find_all('article', class_ = "job-result-card")
    for job in jobs:
        title = job.find('h2', class_ = "job-result-heading__title").text.replace('\n', '')
        title = title.replace('\r', '')
        title = title.replace('\r', '')
        salary = job.find('li', class_ = "job-metadata__item job-metadata__item--salary").text.replace('\n', '')
        salary = salary.replace('\r', '')
        salary = salary.replace(' ', '')
        location = job.find('li', class_ = "job-metadata__item job-metadata__item--location").text
        description = job.find('p', class_ = "job-result-description__details").text
        company = job.find('a', class_ = "gtmJobListingPostedBy").text
        print(f'''
        Job title: {title}
        Salary: {salary}
        Company: {company}
        Location: {location}
        Description: {description}
        ''')
        companies.add(company)
    print([i,companies])


#idea here is that we will loop over the whole website