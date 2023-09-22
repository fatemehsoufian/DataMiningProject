# University of Newcastle Course Crawler

This Python project allows you to crawl [The University of Newcastle, Australia](https://www.newcastle.edu.au/) website to collect data about its courses and save them in a CSV file for further use. The project utilizes the Selenium and Beautiful Soup libraries for web scraping.

## Prerequisites

Before running this project, make sure you have the following prerequisites installed:

- Python 3.x
- Selenium library
- Beautiful Soup library
- ChromeDriver (or any other WebDriver for Selenium)

You can install the required Python libraries using pip:

`pip install selenium beautifulsoup4`

## Usage

1. Clone this repository to your local machine:git clone https://github.com/your-username/university-course-crawler.git

2. Navigate to the project directory:`cd university-course-crawler`

3. Download and install ChromeDriver (if you haven't already) from the official website: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
  
4. Modify the `config.py` file to specify the target URL and any other desired configurations.
  
5. Run the crawler script:
  
  `python crawler.py`
  

6. The script will launch a browser instance, navigate to the specified URL, scrape the course data, and save it to a CSV file.
  
7. Once the script completes, you can find the generated CSV file in the project directory.
  

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
  
2. Create a new branch for your feature/bug fix.
  
3. Make your changes and commit them.
  
4. Push your changes to your forked repository.
  
5. Submit a pull request describing your changes.
  

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The University of Newcastle, Australia for providing the course data.
- Selenium and Beautiful Soup developers for their excellent libraries.
