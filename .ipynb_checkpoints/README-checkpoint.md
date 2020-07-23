## 背景

`MovieLens`数据集是一个广泛用来研究推荐系统算法的一个数据集。这个数据集包含了来自[电影推荐网站](https://movielens.org/)多年积累的数据。我们将基于这个数据集练习数据的处理和分析。

从 [grouplens](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip) 下载数据集 MovieLens 1M Dataset。
数据集包含6个文件：
- `tags.csv` 用户给电影打的标签:
    - userId
    - movieId
    - tag
    - timestamp
- `ratings.csv` 用户给电影的评分:
    - userId
    - movieId
    - rating
    - timestamp
- `movies.csv` 电影信息:
    - movieId
    - title
    - genres
- `links.csv` 链接到其他资源的`id`:
    - movieId
    - imdbId
    - tmbdId

## 需求

对数据集中的3个csv文件进行聚合，生成一个csv，包含电影的信息，其中每部电影一行，信息包括电影名称、主演、平均分、所有tag

## 提交方式

github工程源代码文件链接+结果截图