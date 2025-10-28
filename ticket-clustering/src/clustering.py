"""
Ticket Clustering Analysis
-------------------------
This module implements automated clustering of customer support tickets using
NLP techniques and K-means clustering with automatic parameter optimization.

Author: Ramasamy Arulraj
Date: October 2025
"""

import os
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np
import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from pathlib import Path


class TicketClustering:
    """A class to perform clustering analysis on customer support tickets."""

    def __init__(self, input_file=None, output_file=None):
        """
        Initialize the TicketClustering class.

        Args:
            input_file (str): Path to input CSV file
            output_file (str): Path to output CSV file
        """
        self.base_dir = Path(__file__).parent.parent
        self.input_file = input_file or self.base_dir / "data/raw/unanswered_reports.csv"
        self.output_file = output_file or self.base_dir / "output/clustered_tickets.csv"
        
        # Download required NLTK data
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)

        # Initialize NLP tools
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()
        self.stop_words = self._initialize_stop_words()

    def _initialize_stop_words(self):
        """Initialize and customize stop words for ticket processing."""
        stop_words = set(stopwords.words('english'))
        
        # Domain-specific stop words
        domain_stop_words = [
            'make', 'sent', 'still', 'kindly', 'please', 'dear', 'till', 'soon',
            'since', 'however', 'said', 'also', 'know', 'already', 'related',
            'take', 'made', 'thanks', 'regards', 'consider', 'need', 'required',
            'within', 'taken', 'hence', 'thank', 'much', 'would', 'many', 'user',
            'done', 'able', 'almost', 'want', 'regard', 'regarding', 'like',
            'therefore', 'another', 'give', 'hereby', 'given', 'thanking',
            'taking', 'srns', 'came', 'following', 'whether', 'mention', 'kind',
            'along', 'whereas', 'enable', 'shall', 'herewith', 'without',
            'accordingly', 'cannot', 'come', 'provided', 'instead', 'towards',
            'xbrl', 'making', 'whose', 'takes', 'thankyou', 'obtain', 'obtained',
            'asked', 'madam', 'team', 'needful', 'much', 'sir'
        ]
        stop_words.update(domain_stop_words)

        # Preserve important operators
        operators = {
            'not', 'un', 'got', 'and', 'or', 'other', 'i', 'dont',
            'know', 'there', 'many', 'too', 'add', 'my'
        }
        return stop_words - operators

    def preprocess_text(self, text):
        """
        Preprocess the text data for clustering.

        Args:
            text (str): Input text to preprocess

        Returns:
            str: Preprocessed text
        """
        # Convert to string and lowercase
        text = str(text).lower()
        
        # Remove non-alphabetic characters
        text = re.sub(r"[^a-zA-Z+]", " ", text)
        
        # Remove greeting words
        text = re.sub('kindly|hi|hello', '', text)
        
        # Tokenize
        tokens = text.split()
        
        # Remove stopwords and lemmatize
        tokens = [
            self.lemmatizer.lemmatize(token)
            for token in tokens
            if token not in self.stop_words
        ]
        
        # Join tokens
        text = " ".join(tokens)
        
        # Remove punctuation and short words
        text = text.replace(".", " ").replace(",", " ")
        text = re.sub(r'\b\w{1,2}\b', '', text)
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()

    def find_optimal_clusters(self, X, max_clusters=10):
        """
        Find the optimal number of clusters using silhouette score.

        Args:
            X: Feature matrix
            max_clusters (int): Maximum number of clusters to try

        Returns:
            int: Optimal number of clusters
        """
        max_clusters = min(max_clusters, len(X.toarray()) // 8)
        silhouette_scores = []
        K = range(2, max_clusters + 1)
        
        print("\nFinding optimal number of clusters...")
        for k in K:
            kmeans = KMeans(
                n_clusters=k,
                init='k-means++',
                max_iter=300,
                n_init=10,
                random_state=42
            )
            kmeans.fit(X)
            score = silhouette_score(X, kmeans.labels_)
            silhouette_scores.append(score)
            print(f"Silhouette score for k={k}: {score:.3f}")
        
        return K[np.argmax(silhouette_scores)]

    def cluster_tickets(self):
        """
        Perform the complete clustering workflow on support tickets.
        """
        # Load data
        print("Loading data...")
        df = pd.read_csv(self.input_file)
        print(f"Data shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")

        # Select and preprocess data
        df = df[['Inquiry_id', 'Question']]
        print("Applying text preprocessing...")
        df['Description_clean'] = df['Question'].apply(self.preprocess_text)
        clean_data = df[df['Description_clean'] != '']
        print(f"Records after cleaning: {len(clean_data)}")

        # Create features
        print("Creating TF-IDF features...")
        vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
        X = vectorizer.fit_transform(clean_data['Description_clean'])
        print(f"Feature matrix shape: {X.shape}")

        # Find optimal clusters and perform clustering
        optimal_k = self.find_optimal_clusters(X)
        print(f"\nPerforming K-Means clustering with k={optimal_k}...")
        
        model = KMeans(
            n_clusters=optimal_k,
            init='k-means++',
            max_iter=300,
            n_init=10,
            random_state=42
        )
        model.fit(X)

        # Add labels to the clean data
        clean_data['Label'] = model.labels_

        # Analyze clusters
        self._analyze_clusters(model, vectorizer, clean_data)

        # Save results
        df['Label'] = model.labels_
        df.sort_values('Label').to_csv(self.output_file, index=False)
        print(f"\nResults saved to: {self.output_file}")

    def _analyze_clusters(self, model, vectorizer, data):
        """
        Analyze and print clustering results.

        Args:
            model: Fitted KMeans model
            vectorizer: Fitted TfidfVectorizer
            data: Preprocessed data DataFrame
        """
        print("\nTop terms per cluster:")
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()
        
        for i in range(model.n_clusters):
            cluster_size = sum(model.labels_ == i)
            cluster_percentage = (cluster_size / len(data)) * 100
            print(f"\nCluster {i} ({cluster_size} records, {cluster_percentage:.1f}%):")
            print("Top terms:", end=" ")
            for ind in order_centroids[i, :10]:
                print(f"{terms[ind]}", end=" ")
            print("\nSample questions:")
            cluster_data = data[data['Label'] == i]
            print(cluster_data['Question'].head(3).to_string())


def main():
    """Main function to run the clustering analysis."""
    clustering = TicketClustering()
    clustering.cluster_tickets()


if __name__ == "__main__":
    main()