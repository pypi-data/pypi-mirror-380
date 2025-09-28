
import os
import dataset


pid__db_map = {}


def get_db(connect_url='sqlite:///output.db') -> dataset.Database:
    """封装一个函数，判断pid"""
    pid = os.getpid()
    key = (pid, connect_url,)
    if key not in pid__db_map:
        pid__db_map[key] =  dataset.connect(connect_url)
    return pid__db_map[key]