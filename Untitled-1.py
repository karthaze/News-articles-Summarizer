import tkinter as tk
import nltk
from newspaper import Article
nltk.download('punkt')
# functions
def summarize():
    url = utext.get('1.0', "end").strip()

    post = Article(url)

    post.download()
    post.parse()

    post.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')

    title.delete('1.0',"end")
    title.insert('1.0', post.title)

    author.delete('1.0', "end")
    author.insert('1.0', post.authors)

    publication.delete('1.0', "end")
    publication.insert('1.0', post.publish_date)

    summary.delete('1.0', "end")
    summary.insert('1.0', post.summary)

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')

## GUI
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publication_date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

ulabel = tk.Label(root, text="Enter URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()