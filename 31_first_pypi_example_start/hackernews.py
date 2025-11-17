import requests

def get_top_ten_headlines():
    # equivalent to fetch in javascript
    headline_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    ).json()
    return headline_ids[:10]


def main():
    top_ten_ids = get_top_ten_headlines()
    print("The hackernews top 10")
    print(top_ten_ids)

if __name__ == "__main__":
    main()