# News Articles Search Engine
A simple search engine to search for news articles using [Apache Solr](https://solr.apache.org/) and Web Page with [FastAPI](https://fastapi.tiangolo.com/) at the backend.

## Data
The News Category Dataset was downloaded from [Kaggle](https://www.kaggle.com/rmisra/news-category-dataset).
It contains around 200k news headlines from the year 2012 to 2018 obtained from [HuffPost](https://www.huffpost.com/).
The file is in JSON format and has attributes: category, headline, authors, link, short description and date.

## To configure and run the app, do the following steps:
Download using the command git clone or manually on to your local machine.

#### 1. Dowload and install [Apache Solr](https://solr.apache.org/) on Windows
   1. Once installed, go to Solr folder and run Solr in SolrCloud mode using the following command in cmd:
      ```bash
      bin\solr start -c
      ```
   2. Then run the following commands to start 2 more nodes on ports 8984 and 8985 and connect them to port 8983:
      ```bash
      bin\solr start -c -p 8984 -z localhost:8983
      bin\solr start -c -p 8985 -z localhost:8983
      ```
   3. Go to Solr Admin (http://localhost:8983/) and then go to Collections menu.
   4. Create a new collection named "news" and set numShards, replicationFactor, maxShardsPerNode and shards to 3.
   5. Now select "news" from the drop-down list, click Documents menu, select Document Type "File Upload" and upload the dataset.
   6. If there is no error, then you have successfully uploaded the dataset.

#### 2. Install required Python frameworks and libraries
To use FastAPI and its functionality, [Python3](https://www.python.org/downloads/) should be installed first.
Once Python is installed, install the required modules using the following command on cmd:
```python
pip install -r requirements
```
#### 3. Next run the FastAPI server using the command:
```bash
uvicorn main:app --reload
```
#### 4. Go to http://localhost:8000/news and start searching for articles

## Tools used:
   1. Front End using HTML, CSS, Simple Bootstrap and AngularJS
   2. Back End using Python FastAPI
   3. Indexing and Searching using Apache Solr and built-in Zookeeper
   4. Data handling in JSON

<br>

## Team Members:
1. [Ahmed Rehman Chauhan](https://github.com/ahmedrehman16)
2. [Saad Khan](https://github.com/SaadKhan10399)
