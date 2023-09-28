from Preprocessor import Preprocessor
from KeywordsExtractor import KeywordsExtractor
from FrequentPatternExtractor import FrequentPatternExtractor
import csv
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15, 8)
preprocessor = Preprocessor()
frequentPatternExtractor = FrequentPatternExtractor()
keywordsExtractor = KeywordsExtractor()
keywords_dic = dict()

# load the main data
data = pd.read_csv('data-in/UON.csv')

# count number of all courses and courses of each department
courses_count = len(data.index)
departments_count = len(data.groupby('Department'))
department_courses_count = data.groupby('Department')['Course title'].count()

stattistic_comaprison = csv.writer(
    open(f'data-out/departments-courses-count-comparison-data.csv', 'w', encoding='utf-8', newline=''))
stattistic_comaprison.writerow(['Department', 'CoursesCount', 'Comparison'])

avg = int(courses_count/departments_count)

for deparment, coursecount in department_courses_count.items():
    if int(coursecount) == avg:
        stattistic_comaprison.writerow(
            [deparment, coursecount, 'equal'])
    elif int(coursecount) > avg:
        stattistic_comaprison.writerow(
            [deparment, coursecount, 'more than average'])
    else:
        stattistic_comaprison.writerow(
            [deparment, coursecount, 'less than average'])

# visualization
department_courses_count.to_csv(
    'data-out/visualization-data.csv', header=False)

departments = []
departments_courses_count = []

with open('data-out/visualization-data.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        departments.append(row[0])
        departments_courses_count.append(int(row[1]))

plt.scatter(departments, departments_courses_count)
plt.xticks(rotation=90, fontsize=5)
plt.ylabel('Courses Count')
plt.tick_params(axis='x', pad=10)
plt.xlabel('Department Name')
plt.tight_layout()
plt.savefig('data-out/departments-courses-count-chart.png', dpi=400)

# add a new col which consists of course title,objective,outcome and description of each course
data['Courses Detail'] = data['Course title'] + \
    data['Objective'] + data['Outcome'] + data['Description']

# group data by department and its courses and their details
department_data = data.groupby('Department')['Courses Detail'].sum()
department_data.to_csv('data-out/departments-and-courses-details-data.csv')

# preprocess and extract keywords
output_file = csv.writer(
    open(f'data-out/department-and-courses-details-preprocessed-data.csv', 'w', encoding='utf-8', newline=''))
output_file.writerow(['Department', 'Courses Detail'])

for department, courses_detail in department_data.items():
    if type(courses_detail) == int:
        courses_detail = ''
    preprocessed_courses_detail = preprocessor.preprocess(courses_detail)
    print(department + '-> preprocessed courses detail')
    output_file.writerow(
        [department, preprocessed_courses_detail])

    keywords_dic[department] = keywordsExtractor.extract_keyword(
        preprocessed_courses_detail)
    print(department + '-> extracted courses detail keywords')

# frequent patterns and association rules
frequentPatternExtractor.extractFrequentPatternsAndAssosiationRules(
    keywords_dic)
