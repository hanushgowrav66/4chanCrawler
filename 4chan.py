import requests
import pymongo
import time
from datetime import datetime, timezone

# MongoDB setup
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
fourchan_db = mongo_client["4chan"]
fourchan_threads = fourchan_db["threads"]

# Helper function to read text files
def read_file(filepath):
    with open(filepath) as file:
        return [line.strip() for line in file]

# Load 4chan board topics
fourchan_boards = read_file('fourchan_topics.txt')

# Fetch 4chan threads and insert to MongoDB
def fetch_4chan_threads():
    for board in fourchan_boards:
        url = f"https://a.4cdn.org/{board}/catalog.json"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                for page in response.json():
                    for thread in page['threads']:
                        thread_data = {
                            "_id": thread.get('no'),
                            "no": thread.get('no'),
                            "now": datetime.now(timezone.utc).isoformat(),
                            "name": thread.get('name', ''),
                            "sub": thread.get('sub', ''),
                            "com": thread.get('com', ''),
                            "tim": thread.get('tim', ''),
                            "time": thread.get('time', ''),
                            "id": thread.get('id', ''),
                            "semantic_url": f"https://boards.4chan.org/{board}/thread/{thread.get('no')}",
                            "country_name": "Unknown",  # Assuming no country field, can be updated if needed
                            "replies": thread.get('replies', 0),
                            "posts": [],
                            "last_modified": datetime.now(timezone.utc).isoformat(),
                            "timestamp": datetime.now(timezone.utc)
                        }

                        # Collect last posts (if any)
                        for last_post in thread.get('last_replies', []):
                            post_data = {
                                "no": last_post.get('no'),
                                "now": datetime.now(timezone.utc).isoformat(),
                                "name": last_post.get('name', ''),
                                "com": last_post.get('com', ''),
                                "time": last_post.get('time', ''),
                                "id": last_post.get('id', '')
                            }
                            thread_data['posts'].append(post_data)

                        # Insert into MongoDB if it doesn't already exist
                        if not fourchan_threads.find_one({"_id": thread_data['_id']}):
                            fourchan_threads.insert_one(thread_data)
                            print(f"Inserted thread {thread_data['_id']}")
                        time.sleep(2)
        except Exception as e:
            print(f"Error fetching 4chan threads: {e}")

# Main function to start data collection
def main():
    fetch_4chan_threads()

if __name__ == "__main__":
    main()
