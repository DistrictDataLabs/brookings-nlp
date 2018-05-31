# Introduction to Text Analytics

This repository contains the notebook, slides, sample data, and code for the _Introduction to Text Analytics_ tutorial series.

This three part tutorial will cover the basics of text analytics using Python. We will explore how to create, manage, and process a dataset containing language &mdash; a text corpora &mdash; and learn how to extract information and model the data.

The tutorial will be comprised of three, three-hour sessions as follows:

**Session 1: Text Analysis Overview**

- Creating a corpus
- Preprocessing and Tokenization
- Statistical Analysis of Text
- Stemming and Lemmatization
- NGram Analysis  

**Session 2: Information Extraction**

- Part of Speech Tagging and Syntax Parses
- Grammars for chunking
- Key phrase extraction
- Named Entity Recognition
- Basic networks

**Session 3: Text Classification and Sentiment Analysis**

- The bag of words model
- Text vectorization and TF-IDF
- Bayesian Classification
- Random Forrest Classification
- Logistic Regression
- Neural Networks

## Getting Started

The first step is to clone or [download](https://github.com/DistrictDataLabs/brookings-nlp/archive/master.zip) the repository, unzip it, and then change directories into the project directory.

Note this code requires [Python 3](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads) to run, as well as many third party libraries for both analytics and text processing. Make sure that you have [Jupyter notebook](http://jupyter.readthedocs.io/en/latest/install.html) installed, and if you're using Python that you have [pip](https://pip.pypa.io/en/stable/installing/) installed. Once you do, you can install the required third-party dependencies as follows:

```
$ pip install -r requirements.txt
```

**or**

```
$ conda install --yes --file requirements.txt
```

We will be using several natural language processing libraries throughout the course of the tutorials, and several of them require extra data and models to be downloaded:

```
$ python -m nltk.downloader all
$ python -m spacy download en
$ python -m utils.download
```

Once the libraries and data are installed, you can run the notebook as follows:

```
$ jupyter notebook
```

This should open a browser window in the project directory at [http://localhost:8888/tree](http://localhost:8888/tree). You can then click on the appropriate session's notebook to run the code as needed.
