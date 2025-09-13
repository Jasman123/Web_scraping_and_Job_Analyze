# Data handling and cleaning
import pandas as pd
import numpy as np

# Visualization libraries (commonly used for EDA)
import matplotlib.pyplot as plt
import seaborn as sns

# Web scraping essentials
import requests
from bs4 import BeautifulSoup



# List of big cities in Indonesia with latitude & longitude
indonesia_cities = [
    {"city": "Jakarta", "latitude": -6.2088, "longitude": 106.8456},
    {"city": "Surabaya", "latitude": -7.2575, "longitude": 112.7521},
    {"city": "Bandung", "latitude": -6.9175, "longitude": 107.6191},
    {"city": "Medan", "latitude": 3.5952, "longitude": 98.6722},
    {"city": "Semarang", "latitude": -6.9667, "longitude": 110.4167},
    {"city": "Palembang", "latitude": -2.9761, "longitude": 104.7754},
    {"city": "Makassar", "latitude": -5.1477, "longitude": 119.4327},
    {"city": "Tangerang", "latitude": -6.1783, "longitude": 106.6319},
    {"city": "Depok", "latitude": -6.4025, "longitude": 106.7942},
    {"city": "Bekasi", "latitude": -6.2349, "longitude": 106.9896},
    {"city": "Bogor", "latitude": -6.5971, "longitude": 106.8060},
    {"city": "Malang", "latitude": -7.9839, "longitude": 112.6214},
    {"city": "Denpasar", "latitude": -8.6705, "longitude": 115.2126},
    {"city": "Batam", "latitude": 1.0456, "longitude": 104.0305},
    {"city": "Pekanbaru", "latitude": 0.5071, "longitude": 101.4478},
    {"city": "Padang", "latitude": -0.9471, "longitude": 100.4172},
    {"city": "Banjarmasin", "latitude": -3.3167, "longitude": 114.5908},
    {"city": "Pontianak", "latitude": -0.0263, "longitude": 109.3425},
    {"city": "Manado", "latitude": 1.4748, "longitude": 124.8421},
    {"city": "Yogyakarta", "latitude": -7.7956, "longitude": 110.3695}
]

import time
import tempfile
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_df_job(keyword, location, pages):
    job_data = []

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=chrome_options)
    try :
        for page in range(1, pages + 1):
            if keyword.lower() in ["all", "any", ""]:
                base_url = f"https://id.jobstreet.com/id/jobs/in-{location}?page={page}"
            else:
                base_url = f"https://id.jobstreet.com/id/{keyword}-jobs/in-{location}?page={page}"

            driver.get(base_url)
            try:
                WebDriverWait(driver, 3).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article[data-automation='normalJob']"))
                )
            except:
                print(f"⚠️ No jobs found on page {page}")
                break

            job_cards = driver.find_elements(By.CSS_SELECTOR, "article[data-automation='normalJob']")

            for job in job_cards:
                # --- Extract basic info ---
                try:
                    title_elem = job.find_element(By.CSS_SELECTOR, 'a[data-automation="jobTitle"]')
                    title = title_elem.text
                    job_url = title_elem.get_attribute("href")
                except:
                    title, job_url = "N/A", None

                try:
                    job_location = job.find_element(By.CSS_SELECTOR, 'a[data-automation="jobLocation"]').text
                except:
                    job_location = "N/A"

                try:
                    company = job.find_element(By.CSS_SELECTOR, 'a[data-automation="jobCompany"]').text
                except:
                    company = "N/A"

                try:
                    date_posted = job.find_element(By.CSS_SELECTOR, 'span[data-automation="jobListingDate"]').text
                except:
                    date_posted = "N/A"

                try:
                    salary = job.find_element(By.CSS_SELECTOR, 'span[data-automation="jobSalary"]').text
                except:
                    salary = "N/A"

                # --- Open detail tab ---
                job_desc = "N/A"
                if job_url:
                    try:
                        driver.execute_script("window.open(arguments[0]);", job_url)
                        driver.switch_to.window(driver.window_handles[-1])

                        WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-automation='jobAdDetails']"))
                        )
                        job_desc = driver.find_element(By.CSS_SELECTOR, "div[data-automation='jobAdDetails']").text

                    except Exception as e:
                        print(f"⚠️ Could not extract job description: {e}")
                    finally:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])

                # --- Save d  ata ---
                # print(f"title {title} --- location: {job_location} --- Company: {company} --- Posting: {date_posted} --- Salary: {salary}")
                # print(f"Job description:\n{job_desc[:200]}...\n")  # only print first 200 chars

                job_data.append(
                    {
                        "Title": title,
                        "Location": job_location,
                        "Company": company,
                        "Posting": date_posted,
                        "Salary": salary,
                        "Description": job_desc
                    }
                )

            print(f"✅ Scraped Page {page} → {len(job_cards)} jobs found in {location}")
            time.sleep(np.random.uniform(2, 4))

    finally:
        driver.quit()
    

    return job_data


df_job =[]
for city in indonesia_cities:
  df_job.extend(create_df_job("all",city["city"], 80))


df_job = pd.DataFrame(df_job)
df_job.head()

df_job.to_csv("jobstreet_jobs.csv", index=False)
