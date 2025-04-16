# 📄 Web Scraper & Data Aggregator

This Python project scrapes job postings from [VacancyMail Zimbabwe](https://vacancymail.co.zw/jobs/), processes the data, and stores it in a structured CSV format. It also supports scheduled scraping and logging for automation and monitoring purposes.

## 🚀 Features

- ✅ Extracts the 10 most recent job listings
- ✅ Parses job title, company, location, expiry date, and job link
- ✅ Cleans data: removes duplicates, formats dates
- ✅ Saves output to `scraped_data.csv`
- ✅ Logs activities and errors to `scraper.log`
- ✅ Optionally schedules scraping daily at 09:00 using the `schedule` library

## 🧰 Technologies Used

- Python 3
- `requests`
- `BeautifulSoup`
- `pandas`
- `schedule`
- `logging`

---

## 🛠️ Setup Instructions

1. **Clone the repository or download the files**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
