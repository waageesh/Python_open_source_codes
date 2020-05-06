import bs4
from bs4 import BeautifulSoup
import requests
import pandas
from pandas import DataFrame
import csv
import time

url = 'https://www.emertxe.com/placements/'
response= requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
# print(len(soup.prettify()))



csv_file = open('companies_visited_date_wise.csv', 'w+')
fieldnames = ['Date', 'Company']
csv_writer = csv.writer(csv_file)
csv_writer.writerow(fieldnames)

k = 2
row_cnt = 0
start = time.time()
for i in range(824):  #since there are 824 rows to be scraped
	row_cnt = i
	if (k == 825):
		break
	row_no = "row-" + str(k)
	table_row = soup.findAll("tr",{"class":row_no})
	date_arrived = table_row[0].findAll("td", {"class":"column-1"})
	company = table_row[0].findAll("td", {"class":"column-2"})
	csv_writer.writerow([date_arrived[0].text.strip() , company[0].text.strip()])
	k=k+1
end = time.time()
print(row_cnt, end-start)
csv_file.close()

# print(date_arrived, company)
# print(date_arrived[0].text , company[0].text )

# for  obj in table_col:
# 	print(obj)
# 	print("\n")



# with open('companies_visited_date_wise.csv', mode='w') as csv_file:
#    fieldnames = ['Date', 'Company']
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#    writer.writeheader()

# Date = []
# Company = []

# def opencodezscraping(webpage, page_number):
#    next_page = webpage + str(page_number)
#    response= requests.get(str(next_page)
#    soup = BeautifulSoup(response.content,"html.parser")
#    soup_title= soup.findAll("h2",{"class":"title"})
#    soup_para= soup.findAll("div",{"class":"post-content image-caption-format-1"})
#    soup_date= soup.findAll("span",{"class":"thetime"})
#    for x in range(len(soup_title)):
#    #Generating the next page url
#    if page_number < 16:
#       page_number = page_number + 1
#       opencodezscraping(webpage, page_number)
#    #calling the function with relevant parameters
#    opencodezscraping('https://www.opencodez.com/page/', 0)