import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# load data
data = pd.read_csv(
    'data-in\course-titles-and-courses-details-preprocessed-data.csv')
data_dict = dict()

# drop cells with empty 'Courses Detail' cell
for num, row in data.iterrows():
    if len(str((row['Courses Detail']))) == 3:
        data = data.drop(num)
    else:
        data_dict[row['Course title']] = row['Courses Detail']

# change the model length to 512
model.max_seq_length = 512

# embedding sentences
course_titles = list(data_dict.keys())
sentences = list(data_dict.values())
sentence_embeddings = model.encode(sentences)

for course_title, sentence in zip(course_titles, sentence_embeddings):
    data_dict[course_title] = sentence

# normalize the embeddings to unit length
sentence_embeddings = sentence_embeddings / \
    np.linalg.norm(sentence_embeddings, axis=1, keepdims=True)

# clustering
clustering_model = AgglomerativeClustering(
    n_clusters=None, distance_threshold=1.5)
clustering_model.fit(sentence_embeddings)
cluster_assignment = clustering_model.labels_
clustered_sentences = {}

for sentence_id, cluster_id in enumerate(cluster_assignment):
    if cluster_id not in clustered_sentences:
        clustered_sentences[cluster_id] = []
    clustered_sentences[cluster_id].append(course_titles[sentence_id])

# print clusters
for i, cluster in clustered_sentences.items():
    print('Cluster ', i+1)
    print(cluster)
    print('')
