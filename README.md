# APOD Web Scraper

### Overview
This project is a Python-based web scraper that extracts the Astronomy Picture of the Day (APOD) from NASA's website. It downloads the daily image along with its explanation and saves them locally for offline viewing.

### Features
- Scrapes the APOD website for the daily image and its accompanying explanation.
- Saves the image and explanation with a filename based on the date.
- Organizes downloaded files in a structured manner.

## Getting started

1.) Clone the repo
```bash
git clone https://github.com/Samuel96112/APOD.git
```
2. `cd` into the new directory
```bash
cd apod
```

3. Install the dependencies. Note the "-t" flag will set the target to where 
   you can install the dependencies. It is recommended to create a virtual 
   environmet to install the dependencies into.  
```bash 
pip install -r requirements.txt -t lib

(To install it in a virtual environment)
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt -t venv/lib/python3.9/site-packages

```

### Conditional
4. If you did not set up a virtual environment, then you must add to the python
   path. 
```bash
PYTHONPATH=./lib
```

### Usage
Run the script with:

```bash
python apod.py
```

The script will:
1. Fetch the latest APOD webpage.
2. Extract the image URL and explanation text.
3. Save the image and explanation with the correct filename.
4. Move the explanation file to the `explanations/` directory and the image to 
   `images/`.

### File Structure
```
.
├── images/                 # Directory for downloaded images
├── explanations/           # Directory for saved explanations
├── README.md               # Documentation
├── apod.py                 # Main script
├── requirements.txt        # Modules needed
```

### License
This project is open-source and available under the MIT License.

### Author
Samuel Rodriguez

