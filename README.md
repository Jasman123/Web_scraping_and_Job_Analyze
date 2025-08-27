# Web_scarping_and_Job_Analyze
Web Scraping and Job Market Analysis

This project demonstrates how to scrape job postings from online job portals (e.g., Jobstreet) and perform data analysis to uncover insights about the Indonesian job market.
The notebook Github_Project_WebScraping.ipynb contains both the scraping logic and exploratory data analysis.

📌 Features

Web Scraping: Extract job postings including title, company, location, classification, and salary.

Data Cleaning & Preprocessing: Standardize raw scraped data for analysis.

Exploratory Data Analysis (EDA):

Salary distribution

Top hiring companies

Job classification analysis

Geographical distribution of job postings

Visualization: Generate charts to better understand salary ranges, demand per category, and company hiring trends.

📊 Key Insights

From analyzing 2,560 job postings (Jobstreet sample):

80.43% of postings don’t disclose salary (companies keep compensation details confidential).

Top hiring companies: PT SMART, Tbk; Sheraton Kuta Bali Resort; RGF HR Agent Indonesia.

Most frequent job salary range: IDR 5M – 10M.

Salary extremes: Lowest = IDR 1.5M (Sales Admin Intern), Highest = IDR 65M (Senior Sales Manager).

Job location trend: Jakarta dominates postings; industrial cities like Bekasi/Cikarang are underrepresented due to Jobstreet's search algorithm.

⚙️ Requirements

Python 3.x

Jupyter Notebook

Libraries:

pip install requests beautifulsoup4 pandas matplotlib seaborn

▶️ How to Run

Clone this repository:

git clone https://github.com/Jasman123/Web_scarping_and_Job_Analyze.git
cd Web_scarping_and_Job_Analyze


Open the notebook:

jupyter notebook Github_Project_WebScraping.ipynb


Run all cells to reproduce the scraping and analysis workflow.

📂 Project Structure
Web_scarping_and_Job_Analyze/
│
├── Github_Project_WebScraping.ipynb   # Main notebook with scraping & analysis
├── jobstreet_jobs.csv                 # (Optional) Store scraped job data here
└── README.md                          # Project description (this file)

🚀 Future Improvements

Add support for multiple job portals beyond Jobstreet.

Store scraped data in a database (MySQL / PostgreSQL) for scalability.

Automate daily scraping with scheduling tools (Airflow, Cron).

Build a simple dashboard for real-time job market monitoring.



Two Ways to Use the Notebook

Option 1: Run from the Beginning (Steps 1–3)
This will scrape fresh job postings data from Jobstreet. Results may vary depending on the latest job listings.

Option 2: Use Existing Dataset
If you don’t want to scrape again, you can download/use the provided dataset:

jobstreet_jobs.csv


and start directly from Step 2 (Data Cleaning & Analysis) in the notebook.
