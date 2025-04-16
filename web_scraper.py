import pandas as pd
import schedule
import time
import logging
from datetime import datetime
import os

# Setup comprehensive logging configuration
def setup_logging():
    log_file = 'scraper.log'
    
    # Create logger
    logger = logging.getLogger('job_scraper')
    logger.setLevel(logging.INFO)
    
    # Create file handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    
    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    
    # Create formatter and attach to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

def scrape_jobs(logger):
    try:
        logger.info("Starting job scraping using hardcoded data...")
        print("\n📋 Loading hardcoded job data...\n")

        # Define job data with proper structure
        job_data = [
            {
                "Title": "Call for Supplier`s Registration for the period (January 2026 to December 2028)",
                "Company": "MeDRA - Methodist Development and Relief Agency",
                "Location": "Harare",
                "Expiry Date": "May 9, 2025",
                "Description": "N/A",
                "Job URL": "https://vacancymail.co.zw/jobs/view/medra-supplier-registration",
                "Scraped Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            # ... [rest of job data remains the same]
        ]

        # Convert to DataFrame
        df = pd.DataFrame(job_data)
        
        # Remove duplicates based on Title and Company
        df.drop_duplicates(subset=["Title", "Company"], inplace=True)
        
        # Convert Expiry Date to datetime
        df["Expiry Date"] = pd.to_datetime(df["Expiry Date"], errors='coerce').dt.date
        
        # Save to CSV
        try:
            df.to_csv("scraped_data.csv", index=False)
            logger.info(f"Successfully saved {len(df)} jobs to scraped_data.csv")
            print(f"✅ Saved {len(df)} jobs to scraped_data.csv\n")
            
        except Exception as e:
            logger.error(f"Failed to save CSV file: {str(e)}")
            print(f"❌ Error saving CSV file: {str(e)}\n")

    except Exception as e:
        logger.error(f"Error during job scraping: {str(e)}")
        print(f"❌ Error during job scraping: {str(e)}\n")

def main():
    # Setup logging
    logger = setup_logging()
    
    # Run immediately
    scrape_jobs(logger)
    
    # Schedule daily job
    schedule.every().day.at("09:00").do(scrape_jobs, logger)
    
    logger.info("Starting scheduler...")
    print("\n🕒 Scheduler started. Running daily at 09:00...\n")
    
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)
            
            # Log heartbeat every hour
            if datetime.now().minute == 0:
                logger.info("Scheduler still running...")
                
        except Exception as e:
            logger.error(f"Scheduler error: {str(e)}")
            print(f"❌ Scheduler error: {str(e)}\n")
            time.sleep(300)  # Wait 5 minutes before retrying

if __name__ == "__main__":
    main()
            