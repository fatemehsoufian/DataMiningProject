# data-mining-course-project
This project was a teamwork with my teammate [@alireza-dehghan-nayeri](https://github.com/alireza-dehghan-nayeri)
## Description

This project consists of three phases, each focusing on different aspects of data collection, preprocessing, analysis, and clustering. The project aims to collect data about courses from The University of Newcastle, Australia website, preprocess the collected data, extract keywords using [BERT](https://huggingface.co/docs/transformers/model_doc/bert), perform statistical comparisons, and finally apply BERT-based vectorization and clustering algorithms. The project utilizes [Selenium](https://www.selenium.dev/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web crawling, [NLTK](https://www.nltk.org/) for text preprocessing, [MLxtend](https://rasbt.github.io/mlxtend/) for frequent pattern extraction and association rule mining, and [Matplotlib](https://matplotlib.org/) for data visualization.

## Phase 0: Web Crawling (Python, Selenium, Beautiful Soup)

The first phase involves crawling The University of Newcastle, Australia website using Python. Selenium is used for automated browsing, while Beautiful Soup helps extract relevant data about courses. The collected data is then saved in a CSV file to be used in the subsequent phases.

## Phase 1: Data Preprocessing and Analysis (Python, NLTK, Matplotlib)

Phase 2 consists of the following parts:

1. Data preprocessing: A class is implemented to preprocess the CSV file obtained from the previous phase. This class performs tasks such as stemming, lemmatizing, and removing stopwords to create a clean dataset for further analysis. NLTK library is used for text preprocessing.
2. Statistical comparison: The project includes statistical comparisons between different values within the dataset. This analysis provides insights into the distribution and relationships of the data. Matplotlib is utilized for visualizing the statistical comparisons.
3. Keyword extraction: Another class is implemented to extract keywords from the preprocessed dataset using BERT, a powerful language model. This class employs BERT to identify important keywords that provide context and understanding of the dataset.
4. Frequent pattern extraction and association rule mining: The project includes a class that utilizes MLxtend library for extracting frequent patterns and generating association rules from the dataset. This helps uncover interesting patterns and relationships among the data.

## Phase 2: BERT Vectorization and Clustering (Python, BERT)

In the final phase, the clean dataset obtained from Phase 2 is used. The data is converted into numerical vectors using BERT, which captures the semantic meaning of the text. These vectors are then utilized to implement various clustering algorithms, such as K-means, DBSCAN, or Agglomerative Clustering. The outputs of the clustering, along with any evaluation metrics, are visualized using Matplotlib.
