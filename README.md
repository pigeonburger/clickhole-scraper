# Clickhole Article Scraper

Scrapes all articles and their headlines from the satirical clickbait website https://www.clickhole.com

Requirements:

- Python 3.6 or higher
- `pip install beautifulsoup4`
- `pip install requests`

This script writes all the articles and their headlines to the file `clickholecontent.txt`. The start of each article is denoted by `<|startoftext|>` and the end by `<|endoftext|>`.

To run, simply download the file, install the above requirements and then run the following command:

```
python scraper.py
```

The program will display its progress as it scrapes each article.
