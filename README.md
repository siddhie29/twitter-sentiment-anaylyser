# Twitter Sentiment Analyzer

This project analyzes tweet sentiment on political topics using Python, TextBlob, and Matplotlib.  
It uses a mock list of tweets for demonstration but works the same with real data from the Twitter API or any CSV file.

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Features](#features)  
- [Demo Output](#demo-output)  
- [Requirements](#requirements)  
- [Installation and Setup](#installation-and-setup)  
- [Running the App](#running-the-app)  
- [Folder Structure](#folder-structure)  
- [Future Improvements](#future-improvements)  
- [Author](#author)  

---

## Project Overview
The script reads a list of tweets, classifies each one as Positive, Negative, or Neutral using TextBlob polarity scores,  
and then visualizes the overall mood in a pie chart.

---

## Features
- Simple one-file Python implementation  
- Sentiment analysis with TextBlob polarity  
- Counts and prints tweet sentiment totals  
- Pie-chart visualization with Matplotlib  
- Easily switch between mock data and real tweet data  

---

## Demo Output
Example result on the default mock dataset (10 tweets):

Positive tweets: 4  
Negative tweets: 3  
Neutral tweets: 3  

Pie chart:  

*(Add your pie chart screenshot here after running the code.)*

![Pie chart demo](pie_chart_demo.png)

---

## Requirements
- Python 3.7+  
- textblob  
- matplotlib  
- numpy < 2 (until TextBlob updates for NumPy 2)  

---

## Installation and Setup
Clone the repo or download the single Python file.

```bash
git clone https://github.com/YOUR_USERNAME/twitter-sentiment-analyzer.git
cd twitter-sentiment-analyzer
pip install textblob matplotlib "numpy<2"
python -m textblob.download_corpora
If you are behind Anaconda, replace pip with conda where appropriate or use python -m pip install ....

Running the App
bash
Copy
Edit
python sentiment_analyzer.py
A pie-chart window appears and the console prints each tweet’s polarity plus the summary counts.

Folder Structure
bash
Copy
Edit
twitter-sentiment-analyzer/
  sentiment_analyzer.py     # main script
  README.md                 # this file
  pie_chart_demo.png        # screenshot in root folder
Future Improvements
Replace mock list with live tweets via Tweepy API

Add bar chart of individual tweet scores

Export results to CSV for further analysis

Switch to Vader or spaCy for more robust sentiment scoring

Author
Seedhi Dhawan
BA Programme, Computer Applications (Major) + Political Science (Minor)
Shyam Lal College (Evening), University of Delhi

Feel free to fork, improve, and submit pull requests.

yaml
Copy
Edit

---

Just replace `YOUR_USERNAME` with your GitHub username in the installation instructions. Paste it as is 
