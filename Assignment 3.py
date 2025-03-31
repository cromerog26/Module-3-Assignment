import requests

API_KEY = 'ba509816fbed7bf1d880925e2c7688e927ec1b5c'
url = f"https://www.giantbomb.com/api/genres/?api_key={API_KEY}&format=json"
response = requests.get(url)

data = response.json()
genres = {genre['name']: genre.get('deck', '') for genre in data}
query = ['Action', 'Adventure', 'Role-Playing']

def text_similarity(text1, text2):
    word1 = set(text1.lower().split())
    word2 = set(text2.lower().split())
    return len(word1 & word2)

scores = {}
for genre, description in genres.items():
    if genre not in query:
        scores[genre] = sum(text_similarity(description, genres[qq]) for qq in query if qq in genres)
sorted_genres = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 similar genres:\n")
for genre, score in sorted_genres:
    print(f"{genre}: {score}")
