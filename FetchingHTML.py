from bs4 import BeautifulSoup
import requests

print('Write skill which you are not familiar with:')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=  ').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
# print(soup.prettify())
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
# job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
# print(job)
for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        # print(skills)
        # print(company_name)
        if unfamiliar_skill not in skills:
            print(f'Company Name: {company_name.strip()}')
            print(f'Required Skills: {skills.strip()}')
            print(f'More Info: {more_info}')
            print('')