import requests
import os

with open("All History of Rome episodes.txt", "r") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    filename = os.path.basename(url)

    response = requests.get(url)

    with open(filename, "wb") as file:
        file.write(response.content)

    print(f"{filename} download complete!")

print("All downloads complete!")
