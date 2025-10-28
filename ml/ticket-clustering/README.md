# Ticket Clustering Analysis

This project implements an automated clustering system for customer support tickets using natural language processing and K-means clustering.

## Features

- Automatic optimal cluster size detection using silhouette scores
- Text preprocessing and cleaning
- TF-IDF feature extraction
- K-means clustering with automated parameter tuning
- Comprehensive output analysis with cluster insights

## Project Structure

```
unansweredreport/
├── data/               # Data directory
│   └── raw/           # Raw input data
├── output/            # Output directory for results
├── src/               # Source code
│   └── clustering.py  # Main clustering implementation
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ticket-clustering.git
cd ticket-clustering
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your input CSV file in the `data/raw` directory
2. Run the clustering script:
```bash
python src/clustering.py
```

The script will:
- Load and preprocess the ticket data
- Find optimal number of clusters
- Perform clustering
- Save results in the output directory

## Input Format

The input CSV should have the following columns:
- `Inquiry_id`: Unique identifier for each ticket
- `Question`: The text content of the support ticket
- `chat_datetime`: Timestamp of the ticket

## Output

The script generates:
1. A CSV file with cluster assignments
2. Cluster analysis with top terms per cluster
3. Sample questions from each cluster

## Dependencies

- pandas
- scikit-learn
- nltk
- numpy

## License

This project is licensed under the MIT License - see the LICENSE file for details.