# _4chan Crawler_
# 4Chan Data Collection Project

## Overview
This project is designed to collect and analyze threads and posts from various 4chan boards. The data is fetched using the 4chan API and stored in a local MongoDB database for further analysis. The project uses Python for data collection and MongoDB for data storage.

---

## Tech Stack
* `Python` - The project is developed and tested using Python v3.9.7. [Python Website](https://www.python.org/)  
* `time` - Provides various time-related functions. [Python Documentation](https://docs.python.org/3/library/time.html)  
* `datetime` - Supplies classes for manipulating dates and times. [Python Documentation](https://docs.python.org/3/library/datetime.html)  
* `requests` - A simple HTTP library for Python. [Requests Documentation](https://requests.readthedocs.io/en/latest/)  
* `pymongo` - A Python distribution containing tools for working with MongoDB. [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)  
* `MongoDB Community Server` - Used for storing 4chan data locally. It supports ad-hoc queries, secondary indexing, and real-time aggregations. Includes MongoDB Compass, a GUI for querying and analyzing data. [Download MongoDB](https://www.mongodb.com/try/download/community)  

---

## Data Source Documentation

### 4chan Boards
Data is collected from the following 4chan boards:

* [4chan /pol/](https://boards.4chan.org/pol/) - Politically incorrect forum for discussions of politics and current events.  
* [4chan /news/](https://boards.4chan.org/news/) - News and discussion about global events.  

The boards to scrape are specified in `fourchan_topics.txt`.

---

## Files Description

1. **fourchan_topics.txt**  
   Contains a list of 4chan boards to scrape, one per line.  
   Example:  
   ```txt
   pol
   news  

## System Architecture for Data Collection

The project uses the following steps to collect data:

1. **Fetch threads** from specified 4chan boards using the `/catalog.json` endpoint.
2. **Insert thread data** into a MongoDB collection if it does not already exist.
3. **Collect posts** from threads and add them to the thread data.

## How to Run the Project

1. Install required Python libraries:  
   ```bash
   pip install requests pymongo
2. Ensure MongoDB is running locally.
3. Add boards you want to scrape to `fourchan_topics.txt`.
4. Run the main script:
   ```bash
   python 4chan.py
5. The collected data will be stored in the MongoDB collections `threads`.
