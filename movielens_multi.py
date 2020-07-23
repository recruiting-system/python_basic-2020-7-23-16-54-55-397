import pandas as pd
import time


def process(df, groupbyField, extractField):
    # 单进程处理
    # todo: 对df实现按照groupField字段分组，提取movieId
    # todo：以组名作为文件名，movieIds为文件内容，写文件
    pass


def single():
    time_start = time.time()
    ratings = pd.read_csv('ratings.csv')
    tags = pd.read_csv('tags.csv')
    process(ratings, 'rating', 'movieId')
    process(tags, 'tag', 'movieId')
    time_end = time.time()
    print('time cost',time_end-time_start,'s')


def multi_process():
    # 多进程/线程处理
    # todo: 对df实现按照groupField字段分组，提取movieId
    # todo：以组名作为文件名，movieIds为文件内容，写文件
    pass


def multi():
    time_start = time.time()
    multi_process()
    time_end = time.time()
    print('time cost', time_end - time_start, 's')


if __name__ == "__main__":
    single()
    multi()