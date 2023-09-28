# Preprocessing Phase

This Python project is composed of multiple parts aimed at various data processing and analysis tasks. The project encompasses the following components:

1. **Data Preprocessing Class**: This class focuses on preprocessing a CSV file that contains data collected from a previous phase. It performs operations such as stemming, lemmatizing, and removing stopwords to generate a clean dataset that is suitable for subsequent analysis.
  
2. **Keyword Extraction Class**: This class employs the BERT (Bidirectional Encoder Representations from Transformers) model to extract keywords from the dataset. BERT is a state-of-the-art natural language processing model that has proven effective in capturing contextual information. By utilizing BERT, the class identifies and extracts relevant keywords from the data, facilitating further analysis and categorization.
  
3. **Frequent Pattern and Association Rule Extraction Class**: This class utilizes the mlxtend library, a Python library for machine learning extensions, to extract frequent patterns and association rules from the dataset. Frequent patterns are sets of items that frequently occur together, while association rules capture relationships between different items in the dataset. By extracting these patterns and rules, the class reveals hidden associations and dependencies within the data, enabling insights into potential patterns of behavior or co-occurrence.
  
  Throughout the project, the matplotlib library is utilized to visualize the outputs at appropriate stages. Matplotlib is a popular data visualization library in Python, which allows for the creation of various types of plots and charts to represent the analyzed data effectively.
  
  By combining these different components, the project aims to provide a comprehensive framework for data preprocessing, statistical comparison, keyword extraction, and frequent pattern and association rule extraction.

  ## Prerequisites

Before running this project, make sure you have the following prerequisites installed:

- Python 3.11
- NLTK library
- mlxtend library
- KeyBERT library

You can install the required Python libraries using pip:

`pip install nltk`

`pip install mlxtend`

`pip install keybert`
