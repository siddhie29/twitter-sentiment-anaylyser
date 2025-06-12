# Twitter Sentiment Analyzer – Mood of the Nation

Analyze tweet sentiment on political topics with Python, TextBlob and Matplotlib.  
This project uses a mock list of tweets for demonstration but works the same with real data from the Twitter API or any CSV file.

---

## Table of Contents
- Project Overview  
- Features  
- Demo Output  
- Requirements  
- Installation and Setup  
- Running the App  
- Folder Structure  
- Future Improvements  
- Author  

---

## Project Overview
The script reads a list of tweets, classifies each one as Positive, Negative or Neutral using TextBlob polarity scores and then visualizes the overall mood in a pie chart.

---

## Features
- Simple one-file Python implementation  
- Sentiment analysis with TextBlob polarity  
- Counts and prints tweet sentiment totals  
- Pie-chart visualisation with Matplotlib  
- Easily switch between mock data and real tweet data  

---

## Demo Output
Example result on the default mock dataset (10 tweets).

```
Positive tweets: 4
Negative tweets: 3
Neutral tweets: 3
```

Pie chart:  
![Pie chart demo](docs/pie_chart_demo.png)  
(Add your own screenshot after you run the code.)

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
```

If you are behind Anaconda, replace `pip` with `conda` where appropriate or use `python -m pip install ...`.

---

## Running the App
```bash
python sentiment_analyzer.py
```
A pie-chart window appears and the console prints each tweet’s polarity plus the summary counts.

---

## Folder Structure
```
twitter-sentiment-analyzer/
  sentiment_analyzer.py     main script
  README.md                 this file
  docs/
    pie_chart_demo.png      add your screenshot here
```

---

## Future Improvements
- Replace mock list with live tweets via Tweepy API  
- Add bar chart of individual tweet scores  
- Export results to CSV for further analysis  
- Switch to Vader or spaCy for more robust sentiment scoring  

---

## Author
Seedhi Dhawan  
BA Programme, Computer Applications (Major) + Political Science (Minor)  
Shyam Lal College (Evening), University of Delhi  

Feel free to fork, improve and submit pull requests.
