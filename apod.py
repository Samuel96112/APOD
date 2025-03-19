#! /usr/bin/env python

import requests
from bs4 import BeautifulSoup

import re
import os
import shutil

URL = "https://apod.nasa.gov/apod/astropix.html"

# Check to see if the website is up. If it is not, then abort.
try:
    response = requests.get(URL)
    if response.status_code == 200:
        page = requests.get(URL, timeout = 10)
    else:
        print("The webpage failed to load. Status code: ", response.status_code)
except requests.exceptions.RequestException as e:
        print("The error is: ", {e})

#Define some soup object
soup = BeautifulSoup(response.content, "html.parser")

images = soup.find_all('img')
bold_tags = soup.find_all("b")
paragraphs = soup.find_all("p")

resolvedURLs = []
for image in images:
    src = image.get('src')
    resolvedURLs.append(requests.compat.urljoin(URL, src))

# Find the current path in order to save the file

path = os.path.dirname(__file__)

file_name = f"{bold_tags[0].get_text(strip=True)}.jpg"

image_path = os.path.join(path, 'images', file_name)
images_path = os.path.join(path, 'images')
os.makedirs(images_path, exist_ok=True)

for image in resolvedURLs:
    w = requests.get(image, timeout=10)
    with open(image_path, 'wb') as file:
        file.write(w.content)

# Actually find the correct explanation of the photo.
paragraphs = soup.find_all("p")

explanation_paragraph = None

for p in paragraphs:
    text = p.get_text(separator=" ", strip=True)
    if text.startswith("Explanation:"):
        explanation_paragraph = text
        break


explanation_paragraph = re.sub(r'\s+', ' ', explanation_paragraph)

unwanted_sections = ["Tomorrow's picture", "Archive", "Submissions", "Index", "Search", "Calendar", "RSS", "Education", "About APOD", "Discuss"]

for section in unwanted_sections:
    explanation_paragraph = explanation_paragraph.split(section)[0]

# Save the explanation in a text file for optional reading. 
date = paragraphs[1].get_text(strip=True).replace(" ", "_")
explanation_text_file = open(f"Explanation_{date}.txt", "x")
explanation_text_file.write(explanation_paragraph)

# Move the file to the correct location.
source_file_location = os.path.join(path, f"Explanation_{date}.txt")
destination = os.path.join(path, "explanations")
shutil.move(source_file_location, destination)
