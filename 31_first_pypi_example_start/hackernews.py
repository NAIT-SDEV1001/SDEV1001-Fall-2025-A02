import requests

def get_top_ten_headlines():
    # equivalent to fetch in javascript
    headline_ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    ).json()
    return headline_ids[:10]

def get_news_story_data(id):
    # if you're curious you can take a look at the docs here
    # https://requests.readthedocs.io/en/latest/user/quickstart/
    # on how to use requests, this is going to be how develop software.
    story_url = F"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"
    story_data = requests.get(story_url).json()
    return story_data

def main():
    top_ten_ids = get_top_ten_headlines()
    # loop through the ids
    for index, id in enumerate(top_ten_ids):
        # for each id get news story and print out the title with the number
        # associated with it.
        story_data = get_news_story_data(id)
        print(F"{index + 1}: {story_data['title']}")

    print("The hackernews top 10")
    print(top_ten_ids)

if __name__ == "__main__":
    main()