# Movie Recommendation System 🎬

A content-based movie recommendation system that suggests similar movies based on metadata such as cast, crew, genres, keywords, and descriptions using natural language processing and cosine similarity.

## 📌 Features

* Content-based filtering using metadata from TMDB 5000 dataset
* Cosine similarity to recommend similar movies
* Vectorization with TF-IDF / CountVectorizer
* Clean, explainable, and scalable recommendation logic
* Optionally deployable via Streamlit interface

## 🧠 How It Works

1. Extract and clean metadata: title, overview, cast, crew, keywords, genres
2. Combine fields into a single "tag"
3. Convert tags into vectors using TF-IDF
4. Compute cosine similarity matrix
5. Recommend top N similar movies for a given input

## 🗃️ Dataset

* [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* Includes: `tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`

## 🛠️ Tech Stack

* Python 3.9+
* Pandas, NumPy
* scikit-learn (TF-IDF, CountVectorizer, cosine_similarity)
* NLTK (optional for preprocessing)
* Streamlit (for web app UI)

## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender

# Create a virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🧪 Running the App

```bash
streamlit run app.py  # If using a Streamlit frontend
```

Or test the recommendation logic directly via Jupyter Notebook.

## 📈 Example

```python
recommend('Inception')
```

Output:

* Interstellar
* The Prestige
* The Dark Knight Rises
  ...

## 📚 References

* Seekhwal et al. (2024), ICICC – Content-Based Movie Recommendation
* Rakesh (2024), Al-Bahir Journal – Genre & Cast-based Filtering
* Ghadami & Tran (2024), UMUAI – TriDeepRec Hybrid Architecture

## 🤝 Contributors

* Aaryan Shenoy
* [Teammate Names Here]

## 🧭 License

This project is licensed under the MIT License.

---

Feel free to fork, contribute, and build on this project!
