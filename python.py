'''import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Генерация фиктивных данных

# 1. Распределение студентов по факультетам
faculties = ['Факультет А', 'Факультет Б', 'Факультет В', 'Факультет Г']
students_count = [200, 150, 180, 170]

# 2. Средние оценки по факультетам
average_grades = [3.8, 4.1, 3.5, 3.9]

# 3. Успеваемость по курсам
courses = ['Математика', 'Физика', 'Химия', 'Программирование']
grades = {
    'Математика': np.random.normal(75, 10, 100),
    'Физика': np.random.normal(70, 15, 100),
    'Химия': np.random.normal(80, 12, 100),
    'Программирование': np.random.normal(85, 8, 100),
}

# 4. Изменение средних оцен в течение семестра
weeks = np.arange(1, 16)
average_scores = np.sin(weeks / 5) * 10 + 75 + np.random.normal(0, 5, 15)

# 5. Распределение студентов по возрастным группам
age_groups = ['18-20', '21-23', '24-26', '27-30']
age_distribution = [50, 80, 60, 40]

# Создание графиков
plt.figure(figsize=(14, 10))

# 1. График распределения студентов по факультетам
plt.subplot(2, 2, 1)
plt.bar(faculties, students_count, color='skyblue')
plt.title('Распределение студентов по факультетам')
plt.xlabel('Факультет')
plt.ylabel('Количество студентов')

# 2. График средних оцен по факультетам
plt.subplot(2, 2, 2)
plt.bar(faculties, average_grades, color='salmon')
plt.title('Средние оценки по факультетам')
plt.xlabel('Факультет')
plt.ylabel('Средняя оценка')

# 3. Гистограмма успеваемости по курсам
plt.subplot(2, 2, 3)
for course in courses:
    plt.hist(grades[course], bins=10, alpha=0.5, label=course)
plt.title('Гистограмма успеваемости по курсам')
plt.xlabel('Оценка')
plt.ylabel('Количество студентов')
plt.legend()

# 4. График изменения средних оцен в течение семестра
plt.subplot(2, 2, 4)
plt.plot(weeks, average_scores, marker='o', linestyle='-', color='purple')
plt.title('Изменение средних оцен в течение семестра')
plt.xlabel('Неделя')
plt.ylabel('Средняя оценка')

# 5. График распределения студентов по возрастным группам
plt.figure(figsize=(8, 6))
plt.pie(age_distribution, labels=age_groups, autopct='%1.1f%%', startangle=140, colors=plt.get_cmap('Pastel1').colors)
plt.title('Распределение студентов по возрастным группам')

plt.tight_layout()
plt.show()'''

