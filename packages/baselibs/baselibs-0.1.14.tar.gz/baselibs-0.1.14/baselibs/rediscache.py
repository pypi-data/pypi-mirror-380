#!/usr/bin/env python3
#coding:utf-8

__author__ = 'xmxoxo<xmxoxo@qq.com>'

'''
Redis缓存类 v0.2.0
'''

import redis
import json
import logging

class RedisCache():
    def __init__(self, host='127.0.0.1', port=6379, password="", db=0, ttl=3600, dat_table="CACHE_TABLE"):
        self.host = host
        self.port = port
        self.password = password
        self.db = db

        self.pool = None
        self.client = None
        self.ttl = ttl              # 缓存过期时间，单位：秒，<0不缓存, 0=永不过期，默认=3600s=1小时

        # 表名称
        self.dat_table = dat_table
        self.connect_redis()

    def connect_redis(self):
        ''' 连接Redis
        '''

        try:
            pool = redis.ConnectionPool(
                    host=self.host, port=self.port, 
                    password=self.password, db=self.db, 
                    max_connections=50,
                    decode_responses=True)

            self.client = redis.Redis(connection_pool=pool)
            logging.info('redis connected...')
        except Exception as e:
            logging.error(e)

    def getkey(self, keyname, tojson=True):
        ''' 读取键值
        tojson：是否反序列化
        '''
        try:
            keyname = f"{self.dat_table}:{keyname}"
            value = self.client.get(keyname)
            if value is None: return None
            try:
                ret = json.loads(value)
            except Exception as e:
                ret = value
            return ret
        except Exception as e:
            logging.error(e)
            return None

    def setkey(self, keyname, dat, ttl=0):
        ''' 设置键值
        '''
        try:
            keyname = f"{self.dat_table}:{keyname}"
            if type(dat) in [tuple, list, dict]:
                try:
                    value = json.dumps(dat)
                except Exception as e:
                    value = dat
            else:
                value = dat
            if ttl <= 0:
                # 永久保存
                self.client.set(keyname, value)
            else:
                # 按TTL自动超时方式保存
                self.client.setex(keyname, ttl, value)

            return True
        except Exception as e:
            logging.error(e)
            return False

    def delkey(self, keyname):
        ''' 删除键
        '''
        try:
            keyname = f"{self.dat_table}:{keyname}"
            self.client.delete(keyname)
            return True
        except Exception as e:
            logging.error(e)
            return False

    def cache(self, keyname, get_data_fun=None, tojson=True, 
                ttl=None, update_ttl=False, refresh=False):
        ''' 读取缓存，未命中时调用 get_data_fun 方法获得数据, 并将数据保存到缓存
        ttl： 缓存时长，单位：秒，默认使用初始时的配置
        tojson: 是否反序列
        update_ttl: 是否更新TTL时间
        refresh: 强行刷新缓存； 
        '''
        if ttl is None: ttl = self.ttl

        # 读redis缓存
        ret = self.getkey(keyname, tojson=tojson)
        
        # if not ret is None and not refresh:
        if refresh or ret is None:
            # 如果强行刷新缓存，或者 “没有缓存数据”时
            logging.info(f'not hits cache, key={keyname}...')
            # 调用自定义的取值函数
            if get_data_fun is None:
                return None
            else:
                # 调用函数，取得结果
                ndat = get_data_fun()
                if ndat:
                    self.setkey(keyname, ndat, ttl=ttl)
                    logging.info(f'save cache key={keyname}')
                else:
                    logging.info(f'value empty, cache key:{keyname}')
                return ndat
        else:
            # 命中，有缓存时 则直接返回
            logging.info(f'hits cache key:{keyname}...')
            # Todo：命中时是否延续缓存 2025/9/10
            if update_ttl:
                # 只有 key 存在时才检查并重置 TTL
                if self.client.ttl(keyname) > 0 and ttl>0:
                    self.client.expire(keyname, ttl)
            return ret

    def get_keys (self):
        ''' 查询所有KEY
        '''
        keyname = f"{self.dat_table}:*"
        values = self.client.keys(keyname)
        keys = [x.decode('utf-8')if type(x)==bytes else x for x in values]

        '''
        # 使用 SCAN 命令分批获取 key
        cursor = 0
        keys = []
        while True:
            cursor, partial_keys = r.scan(cursor, match='prompt_table:*')
            keys.extend(partial_keys)
            if cursor == 0:
                break
        '''
        return keys

def cache_execute(gbl_redis_config, fun, param, keyname:str="", ttl=3600, refresh=False):
    ''' 通用带缓存的方法调用, 默认缓存1小时；
    - gbl_redis_config: Redis连接配置
    - fun:  待调用的方法函数
    - param: tuple, 调用函数fun的参数, 
    - keyname: 缓存KEY, 为空时自动使用“方法名 + md5(参数)”生成
    - ttl: 缓存时间，默认：秒， <0不缓存, 0=永久缓存, >0 进行缓存
    - refresh: 是否强制刷新缓存:不管是否有缓存存在，均写入缓存, 默认False 
    '''
    from functools import partial
    import hashlib

    if not callable(fun) : return None
    # 创建实例
    rcache = RedisCache(**gbl_redis_config)
    txtmd5 = lambda x:hashlib.md5(x.encode(encoding='UTF-8')).hexdigest()

    # 先构造一个函数，再传递参数
    tfun = partial(fun, *param)

    if keyname == "":
        fun_name = fun.__name__ + "_"
        keyname = fun_name + txtmd5(str(param))
        logging.info(f'cache_execute, keyname:{keyname}')

    # 调用
    ret = rcache.cache(keyname, tfun, ttl=ttl, refresh=refresh)
    return ret

if __name__ == '__main__':
    pass
