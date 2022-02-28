# H&M Fashion Image similarity search with Weaviate and DocArray

This example shows how to do image similarity search using [DocArray](https://docarray.jina.ai/) and [Weaviate](https://weaviate.io/) as Document Store. 

## Download data
You need to download the fashion image data from [the H&M dataset on Kaggle](https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations/data). You can download it and put in the right folder using:

```bash
$ mkdir data
& cd data
$ kaggle competitions download -c h-and-m-personalized-fashion-recommendations
$ unzip h-and-m-personalized-fashion-recommendations.zip
```

## Start up Weaviate
You need to start up Weaviate using `docker compose up`. Weaviate will be running on `http://localhost:8080` 

## Embed, store and query
You can run the Jupyter notebook to embed, store and query fashion image data using ResNet50, DocArray and Weaviate.