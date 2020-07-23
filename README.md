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

使用多线程+多进程的方式实现同时对tags.csv还有ratings.csv进行汇总，其中tags按照tag汇总，ratings按照rating汇总，按照每个tag/rating一个文件的方式输出对应的movie，
同单进程方式实现进行比较，对比较结果进行思考。

## 提交方式

github工程源代码文件链接+结果截图
