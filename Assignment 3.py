import requests

API_KEY = 'ba509816fbed7bf1d880925e2c7688e927ec1b5c'
url = f"https://www.giantbomb.com/api/genres/?api_key={API_KEY}&format=json"
headers = {'User-Agent': 'Python script'}

response = requests.get(url, headers=headers)
data = response.json()

results = data.get('results', [])
genres = {genre['name']: genre.get('deck', '') or '' for genre in results}

queries = ['Action', 'Adventure', 'Shooter']

def text_similarity(text1, text2):
    word1 = set(text1.lower().split())
    word2 = set(text2.lower().split())
    return len(word1 & word2)

for query in queries:
    query_desc = genres[query]
    similarities = {}

    for genre, description in genres.items():
        if genre == query:
            continue
        similarity_score = text_similarity(query_desc, description)
        similarities[genre] = similarity_score

    top_similar = sorted(similarities.items(), key = lambda x: x[1], reverse = True)[:10]

    print(f"\nTop 10 genres similar to '{query}':\n")
    for i, (genre, score) in enumerate(top_similar, 1):
        print(f"{i}. {genre} (Similarity score: {score})")
