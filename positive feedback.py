from wordcloud import WordCloud

text = open('January positive feedback.csv').read()
wordcloud = WordCloud().generate(text)

import matplotlib.pyplot as plt

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
