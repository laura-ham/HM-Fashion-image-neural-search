# H&M Fashion Image similarity search with Weaviate and DocArray

This example shows how to do image similarity search using [DocArray](https://docarray.jina.ai/) and [Weaviate](https://weaviate.io/) as Document Store. 

## How to use the notebook

This repository includes sample data, but you can download the full dataset from Kaggle (see below).

Before you start using the notebook, you need to start a Weaviate instance, by running `docker compose up`. Weaviate will be running on `http://localhost:8080`. Alternatively,, you can start a Weaviate instance for free with [WCS: Weaviate Cloud Service](https://console.semi.technology/). Make sure you adapt the Weaviate server in the notebook accordingly. 


### How to download data (optional - sample data included in this repository)
You need to download the fashion image data from [the H&M dataset on Kaggle](https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations/data). You can download it and put in the right folder using:

```bash
$ mkdir data
& cd data
$ kaggle competitions download -c h-and-m-personalized-fashion-recommendations
$ unzip h-and-m-personalized-fashion-recommendations.zip
```

Optional: you can use `resize_image.py` to downscale the images before using them in the notebook.

Make sure to adapt the file location in the notebook. 

### Install requirements
The requirements will be installed in the first cell of the notebook. Alternatively, you can run `pip install -r requirements.txt`.

### Embed, store and query
You can run the Jupyter notebook to embed, store and query fashion image data using ResNet50, DocArray and Weaviate.