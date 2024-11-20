import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from collections import Counter
import string
import matplotlib.pyplot as plt

# Завантаження даних
nltk.download('gutenberg')
nltk.download('stopwords')

# Вибір тексту "Persuasion" Джейн Остін
text = gutenberg.raw('chesterton-ball.txt')

# Підрахунок кількості слів у тексті
words = nltk.word_tokenize(text)
num_words = len(words)
print(f"Кількість слів у тексті: {num_words}")

# Підрахунок найпоширеніших слів
words_lower = [word.lower() for word in words if word.isalpha()]
word_freq = Counter(words_lower)
most_common = word_freq.most_common(10)
print("10 найбільш вживаних слів:")
print(most_common)

# Побудова діаграми
plt.figure(figsize=(10, 6))
plt.bar([word for word, _ in most_common], [freq for _, freq in most_common], color='skyblue')
plt.title("10 найбільш вживаних слів у тексті")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words_lower if word not in stop_words]

# Повторний аналіз
filtered_word_freq = Counter(filtered_words)
filtered_most_common = filtered_word_freq.most_common(10)
print("10 найбільш вживаних слів без стоп-слів:")
print(filtered_most_common)

# Побудова діаграми для очищеного тексту
plt.figure(figsize=(10, 6))
plt.bar([word for word, _ in filtered_most_common], [freq for _, freq in filtered_most_common], color='orange')
plt.title("10 найбільш вживаних слів після видалення стоп-слів")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.show()