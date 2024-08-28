import requests
import json


# update every hour
bearer_token = "2-rsfA9-x-qYucoMbTfQBUYLnOuv3inrXMGgC0fb3IVns5-7UwSmYFGsW-ZhbfaB"

base_url = "https://api.genius.com"
endpoint = "search"

lyrics = """See the stone set in your eyes
See the thorn twist in your side
I'll wait for you

Sleight of hand and twist of fate
On a bed of nails, she makes me wait
And I'll wait without you

With or without you
With or without you"""

lyrics_freq = {}

for lyric in lyrics.split():
	lyric_lower = lyric.lower()
	if lyric_lower in lyrics_freq:
		lyrics_freq[lyric_lower] += 1
	else:
		lyrics_freq[lyric_lower] = 1

lyrics_freq = dict(sorted(lyrics_freq.items(), key=lambda item: item[1], reverse=True))


# Exact match
query_params = ""
space = "%20"
for k in lyrics_freq.keys():
	query_params += f"{k}{space}"
query_params = query_params[:-len(space)]

r = requests.get(f"{base_url}/{endpoint}?q={query_params}", headers={"Authorization": f"Bearer {bearer_token}"})
response_json = json.loads(r.text)

exact_matches = ""
for hit in response_json["response"]["hits"]:
	result = hit["result"]
	artist = result["artist_names"]
	title = result["full_title"]
	exact_matches += f"{artist} - {title}\n"

with open("u2_matches/exact_matches.txt", "w") as f:
	f.write(exact_matches)


# Tightest loose match
all_lyrics = [k for k in lyrics_freq.keys()]
query_params = ""
loose_matches = ""
while all_lyrics:
	for lyric in all_lyrics:
		query_params += f"{lyric}{space}"
	query_params = query_params[:-len(space)]
	
	r = requests.get(f"{base_url}/{endpoint}?q={query_params}", headers={"Authorization": f"Bearer {bearer_token}"})
	response_json = json.loads(r.text)

	for hit in response_json["response"]["hits"]:
		result = hit["result"]
		artist = result["artist_names"]
		title = result["full_title"]
		url = result["url"]

		if "with or without you" not in title.lower():
			loose_matches += f"{query_params}:\t{artist} - {title}\t{url}\n"

	all_lyrics.pop()
	query_params = ""

with open("u2_matches/loose_matches.txt", "w") as f:
	f.write(loose_matches)
