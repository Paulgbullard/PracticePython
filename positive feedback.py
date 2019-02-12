from wordcloud import WordCloud

text = open('all positive feedback.csv').read()
wordcloud = WordCloud(width = 500, height = 500, max_words = 1000, background_color = "Black").generate(text)

import matplotlib.pyplot as plt

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
