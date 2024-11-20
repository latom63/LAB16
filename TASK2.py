import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string

# Завантажуємо необхідні ресурси
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# 1. Читаємо текст із вхідного файлу
input_file = 'input_text.txt'
output_file = 'processed_text.txt'

with open(input_file, 'r') as file:
    text = file.read()

# 2. Токенізація по словам
words = word_tokenize(text)

# 3. Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
stemmed_words = [stemmer.stem(word) for word in words]

# 4. Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in lemmatized_words if word.lower() not in stop_words]

# 5. Видалення пунктуації
filtered_words = [word for word in filtered_words if word not in string.punctuation]

# 6. Записуємо оброблений текст у вихідний файл
processed_text = ' '.join(filtered_words)

with open(output_file, 'w') as file:
    file.write(processed_text)

print(f"Оброблений текст збережено у файл '{output_file}'")
