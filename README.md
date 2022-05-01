
# Twitter Competitive Knowledge Graph

## MSDS-459 - Knowledge Engineering - Spring 2022

**don't forget to install requirements** <br>
pip install -r requirements.txt

**Sources I may or may not use:** <br>
https://towardsdatascience.com/auto-generated-knowledge-graphs-92ca99a81121 <br>
https://hami-asmai.medium.com/relationship-extraction-from-any-web-articles-using-spacy-and-jupyter-notebook-in-6-steps-4444ee68763f <br>
https://www.analyticsvidhya.com/blog/2019/10/how-to-build-knowledge-graph-text-using-spacy/ <br>
https://github.com/martin-majlis/Wikipedia-API/ <br>
https://gist.github.com/aculich/b34868c098d94d614515 <br>

**My Schema** <br>
![img.png](img.png) <br>
![img_2.png](img_2.png)

**For eventual NLP not yet included in this repo:** <br>
Before you install spaCy: <br>
pip install -U pip setuptools wheel <br>
after you install spaCy: <br>
python -m spacy download en <br>


neuralcoref looks like it's not in active development right now, and I was unable to get the older versions of spaCy and neuralcoref do install correctly (wheel errors!) <br>
https://github.com/huggingface/neuralcoref

**Stuff to know** <br>
You have to make this your own. This is based on my company lists and my database schema. It's just a tool. <br>