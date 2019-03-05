import requests
from bs4 import BeautifulSoup
import json
import time as t
from multiprocessing import Pool

start_time = t.time();
global limit;
limit =0;
#All Functions
def extract_company(row_result):
	try:
		company = row_result.find('span', {'class': 'company'}).text;
		company = company.replace('\n', ' ');
		company = company.strip()
		return company;
	except:
		return None;
def extract_salary(row_result):
	try:
		salary = row_result.find('span',{'class':'salary no-wrap'}).text;
		salary = salary.replace('\n',' ');
		salary = salary.replace(',','');
		while(salary[0] == ' '):
			salary = salary[1:];
		salary = salary[1:];
		ind = salary.find(' ');
		salary = salary[:ind];
		salary = int(salary);
		#print(salary)
		
		return salary;
	except:
		return 0;

def process_page(url):
	temp_data =[];
	response = requests.get(url, timeout=10)
	page_data = BeautifulSoup(response.text, 'html.parser');
	page_no = all_urls.index(url)+1;
	location = 'Bengaluru, Karnataka';
	#print('=====> Processing the Page: '+str(page_no)+' <=====')
	for result in page_data.find_all('div', class_=['row', 'result']):
		company = extract_company(result);
		job_title = result.find('a', attrs ={'class':'turnstileLink'}).attrs['title'];
		salary = extract_salary(result);
		temp_data.append({"PageNo":page_no,"JobTitle":job_title,"Company":company,"Salary":salary,"Location":location});	
	return temp_data;
	
def getData(page_data):
	data = [];
	for i in page_data:
		for j in i:
			data.append(j);
		if(len(data)>=1000):
			return data;
	return data;

if __name__ == '__main__':
	URL = "https://www.indeed.co.in/jobs?q=software+developer&l=Bengaluru%2C+Karnataka&start="
	all_urls = [];
	data =[]
	page_data = []
	page_no =0;
	salary = 0;
	job_title = "";
	company ="";
	print('-->Accessing web site & Collecting required pages URLs......')
	max_pages = 700;
	for start in range(0, max_pages, 10):
		all_urls.append(URL+str(start));
	#Multi_threading
	pool = Pool(processes=70);
	page_data = pool.map(process_page, all_urls);
	pool.terminate();
	#Reduce dimension of data
	data = getData(page_data)
	#sort the Dict
	print('-->Sorting the data by Salary ...');
	data = sorted(data, key=lambda k: k['Salary'], reverse=True)
	#Writing to JSON file
	print('-->Wrinting the data to JSON file ...');
	with open("data_file.json", "w") as write_file:
		for row in data:
			json.dump(row, write_file);
			write_file.write('\n');
	end_time = t.time();
	print('-->Execution time(sec): '+str(end_time-start_time));
