import json 

with open("MIT6_0001F16_ProblemSet0.pdf", "rb") as f:
    data = f.read()
    urls = []
    for part in data.split():
        if b"http" in part:
            urls.append(part.decode(errors='ignore'))
print(set(urls))
unique_urls = set(urls)

json_output = json.dumps(sorted(unique_urls), indent=2)

