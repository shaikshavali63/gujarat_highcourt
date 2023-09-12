from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import math

from datetime import datetime, timezone
import datetime
import json
import time


def get_link(td_element):
    link_elements = td_element.find_elements(By.TAG_NAME, "a")
    links = []
    # Extract and print the URLs from the links
    for link in link_elements:
        url = link.get_attribute("href")
        links.append(url)
    return links


def get_text(total_page):
    p_tag = []

    for n in total_page:
        data = n
        # print(data.text)
        #print(data)
        paragraph = data.find_elements(By.TAG_NAME, "p")
        # print("length =",len(paragraph))
        for a in paragraph:
            all_lines = a.text

            #   if not all_lines[0]:
            # print(all_lines[0])
            # paras =a.text
            p_tag.append(a.text)

            # print("paras =",paras)
        # print("ptag =",len(p_tag),type(p_tag))
        # print(p_tag[0])
        # for n in p_tag:
        # print("n value",n)
    return p_tag


def get_details(driver_details):
    coram = driver_details.find_elements(By.XPATH, "/html/body/div[9]/div[3]")
    #1 /html/body/div[9]/div[3]
    #2 /html/body/div[8]/div[3]

    if len(coram) == 0:
        coram = driver_details.find_elements(By.XPATH, "/html/body/div[8]/div[3]")
        #print("iF Len of corma ------- : ", len(coram))
        #coram = "Empty"
        #print("CORM : ", coram)
    else:
        print("els iF Len of corma eeeeeeeeeeeee : ", len(coram))
        #print("CORM : ", coram)
    for n in coram:
        coram_1 = n.text
        # print(coram_1)
        petetioner = coram_1.split("vs")[0].strip()
        respodent_1 = coram_1.split("vs")[1]
        respodent = respodent_1.split("on")[0].strip()
        # judgement_date =respodent_1.split("on")[1]
        #print("petetioner =",len(petetioner),petetioner)
        # print("respodent =",respodent)
        # print("judgement_date =",judgement_date)
    bench_str = driver_details.find_elements(By.CLASS_NAME, "doc_bench")
    for n in bench_str:
        bench_1 = n.text
        bench = bench_1.split(":")[1]
        # print("bench =",bench

    total_details = driver_details.find_elements(By.ID, "pre_1")
    for n in total_details:
        case_str = n.text
        case_number_str = case_str.split("/n")
        # print("case no =",type(case_number),len(case_number),"data",case_number)
        case_no = [case for n in case_number_str for case in n.split()]
        # print("case_1",len(case_1,),"case =",case_1)
        case_number = case_no[0]
        #case_number_str = case_number.split("/")[0]
        print("case_number===",case_number)

        if len(case_no[3])==6:
            judgement_date = case_no[4]
            judgement_date_str = datetime.datetime.strptime(judgement_date, "%d/%m/%Y").strftime("%d-%m-%Y")
            #print("date ==",judgement_date)
        else:
            judgement_date = case_no[3]
            judgement_date_str = datetime.datetime.strptime(judgement_date, "%d/%m/%Y").strftime("%d-%m-%Y")
        # print(case_number)
        #print("dated len",len(judgement_date))
        #print("date  ===",judgement_date)

    total_page = driver_details.find_elements(By.CLASS_NAME, "judgments")
    paras = get_text(total_page)

    '''case_text_file = "2017_16260_Judgement_10-07-2023.txt"
    with open(f"temp/{case_text_file}", 'w') as f:
        json.dump(paras, f, indent=1)

    upload_file_to_digital_ocean(f"temp/{case_text_file}",
                                 f"judgements/gujarat_highcourt/<case_year>/<case_number>/{case_text_file}")'''

    object_fields = {
        "Bench": bench,
        "petitioner": petetioner,
        "respondent": respodent,
        "judgement_date": judgement_date_str,
        "case_number": case_number,
        #"case_details": paras
        "processed_files": {
            "text": "judgements/gujarat_highcourt/<case_year>/<case_number>/{case_text_file}"
        }

    }
    final_objects.append(object_fields)
    # print(final_objects)
    '''with open("gujarat_high_court_10-7-2023.json", 'w') as f:
        json.dump(final_objects, f, indent=1)'''


def menu_selection(driver_menu):
    links_str = []
    list_element = driver_menu.find_element(By.XPATH, '/html/body/div[2]/div[3]')
    print("list_element", list_element)
    link = get_link(list_element)

    print("links", len(link))
    for n in link:
        # print("all links =",n)
        all_links.append(n)
    # print("links =",type(all_links),len(all_links))
    # print("all links =",all_links[1])

    # for n in all_links:
    for a in range(0, 40, 4):
        main_link = all_links[a]
        # print("Main links : ", main_link, "len of main link : ", len(main_link), "\n")
        links_str.append(main_link)
    # print("links list: ", links_str, "len of link list : ", len(links_str), "\n")
    for posts in range(len(links_str)):
        print("p : ", posts)
        print("links list: ", links_str[posts], "len of link list : ", len(links_str), "\n")

        driver.get(links_str[posts])
        if (posts != len(links_str)):
            # driver.execute_script("window.open('');")
            chwd = driver.window_handles
            driver.switch_to.window(chwd[-1])
            sleep(5)
            get_details(driver)

            # Switch back to the main tab
            driver.switch_to.window(driver.window_handles[0])

        chwd = driver.window_handles
        # print(chwd)






final_objects = []
get =0
frm_date ="10-7-2023"
to_date ="10-7-2023"
court = "gujarat"
max_limit=0

def range_pages(driver):
    cases = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/b")
    cases_str = cases.text
    total_cases =cases_str.split(" ")[4]
    max_limit = math.ceil(int(total_cases)/10)

    print("case ==",max_limit)
    return max_limit




#website_url ="https://indiankanoon.org/search/?formInput=doctypes%3A%20gujarat%20fromdate%3A%201-7-2023%20todate%3A%201-7-2023&pagenum=5"
website_url =f"https://indiankanoon.org/search/?formInput=doctypes%3A%20{court}%20fromdate%3A%20{frm_date}%20todate%3A%20{to_date}&pagenum="+str(0)
driver = webdriver.Chrome()


all_links = []

driver.get(website_url)
menu_selection(driver)
driver.get(website_url)
#range_pages(driver,"gujarat","10-7-2023","10-7-2023")
sleep(5)
#get += 1
limit = range_pages(driver)
for i in range(1,limit):
    # website_url ="https://indiankanoon.org/search/?formInput=doctypes%3A%20gujarat%20fromdate%3A%201-7-2023%20todate%3A%201-7-2023&pagenum=5"
    website_url = f"https://indiankanoon.org/search/?formInput=doctypes%3A%20{court}%20fromdate%3A%20{frm_date}%20todate%3A%20{to_date}&pagenum=" + str(
        i)
    driver = webdriver.Chrome()

    all_links = []

    driver.get(website_url)
    menu_selection(driver)
    driver.get(website_url)
    # range_pages(driver,"gujarat","10-7-2023","10-7-2023")
    sleep(5)
    # get += 1
    limit = range_pages(driver)





