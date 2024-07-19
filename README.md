
# Python Playwright Web Scraper for Internet Provider website

This project contains a Python script that uses Playwright to scrape the entire content of each link in the navigation bar on a Dutch Internet Provider website

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Notes](#notes)
- [License](#license)

## Requirements

- Python 3.8+
- Playwright
- asyncio

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/delta-nl-scraper.git
   cd delta-nl-scraper
   ```

2. **Set up a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```sh
   playwright install
   ```

## Usage

1. **Run the scraper:**
   ```sh
   python scrape.py
   ```

2. **Output:**
   The scraped content will be printed to the console or saved to a file as per your configuration in `scrape.py`.

## Project Structure

```
delta-nl-scraper/
│
├── scrape.py            # Main script for scraping
├── requirements.txt     # List of dependencies
├── README.md            # This readme file
└── data/                # Directory for storing scraped data (if implemented)
```

### scrape.py
The `scrape.py` script performs the following tasks:
1. Launches a Playwright browser instance.
2. Navigates to the Delta.nl website.
3. Extracts links from the navigation bar.
4. Visits each link and scrapes the entire content.
5. Outputs the scraped content to the console or saves it to a file.

## Notes

- This script is designed for educational purposes. Ensure you comply with Delta.nl's terms of service and robots.txt when using this script.
- Depending on the website's structure, the script may need adjustments to handle dynamic content or navigation changes.

---

Feel free to contribute or raise issues on the GitHub repository to improve the scraper!
```
