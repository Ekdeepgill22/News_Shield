# Fake News Detection AI

This project is a Flask-based web application for fake news detection using both a local dataset/model and real-time news search via SerpAPI.

## Features
- **Dataset Analysis:** Analyze news using a pre-trained model and a local dataset.
- **Real-time Search:** Analyze live news using SerpAPI and display credibility results.

## Setup Instructions

### 1. Clone the repository
```
git clone <your-repo-url>
cd <project-directory>
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Prepare required files
- Place your model and data files in `News_Sheild/fake news detection/`:
  - `logistic_model.pkl`
  - `tfidf_vectorizer.pkl`
  - `cleaned_news.csv`

### 4. Environment variables
- Copy `.env.example` to `.env` and add your SerpAPI key:
```
SERPAPI_KEY=your_serpapi_key_here
```

### 5. Run the app
```
cd News_Sheild/fake news detection
python main.py
```

- The app will be available at `http://127.0.0.1:5000`

## Project Structure
```
News_Sheild/
  fake news detection/
    main.py
    static/
    templates/
    # Place your .pkl and .csv files here
requirements.txt
.env.example
README.md
.gitignore
```

## Notes
- **Do NOT commit your actual `.env` or data/model files to GitHub.**
- Each teammate should provide their own dataset/model files and SerpAPI key.

## License
MIT "# News_Shield" 
