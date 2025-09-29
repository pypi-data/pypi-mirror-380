import json
from redis.asyncio import Redis,ConnectionPool

class Gkey(str):
    """生成Key，管理Key"""
    def __new__(cls,key:str,*args):
        '''key: str 为key模板带{}的替换模板，*args 为参数'''
        v=key.value.format(*args)
        return v
    
class RedisClient():
    def __init__(self,host,port=6379,password=None,db=0,preFix='',defaultExpire=30):
        '''
        redis连接池
        host: str 为redis地址
        port: int 为redis端口
        password: str 为redis密码
        db: int 为redis数据库
        preFix: str 为key前缀,会在所有的key前面增加一个前缀
        defaultExpire: int 为默认过期时间30秒，单位秒
        '''
        self.redis_pool:ConnectionPool = ConnectionPool(
            host=host,
            port=port,
            db=db,
            password=password,
            max_connections=100
        )
        self.keyPrefix = preFix+':' if preFix else ''
        self.client = Redis(connection_pool=self.redis_pool)
        self.defaultExpire = defaultExpire
    def gen_key(self,key,*args):
        if '{}' in key:
            return self.keyPrefix+ Gkey(key,*args)
        else:
            return self.keyPrefix+key
    async def get_string(self,key,*args):
        key = self.gen_key(key,*args)
        v = await self.client.get(key)
        if v:
            return v.decode('utf-8')
        return None
    
    async def get_json(self,key,*args)->dict:
        '''获取字典，返回一个字典'''
        key = self.gen_key(key,*args)
        v = await self.client.get(key)
        if v:
            return json.loads(v)
        return None
    async def get_int(self,key,*args):
        '''获取int'''
        key = self.gen_key(key,*args)
        return eval(await self.client.get(key))

    async def delete(self,key):
        ck = self.keyPrefix+ key
        return await self.client.delete(ck)
    async def set(self,key,value,ex=0,*args,**kwargs):
        '''缓存
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``keepttl`` if True, retain the time to live associated with the key.
            (Available since Redis 6.0)

        ``get`` if True, set the value at key ``name`` to ``value`` and return
            the old value stored at key, or None if the key did not exist.
            (Available since Redis 6.2)

        ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds,
            specified in unix time.

        ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds,
            specified in unix time.
        '''
        ck = self.keyPrefix+ key
        if ex==0:
            ex=self.defaultExpire
        return await self.client.set(ck,value,ex=ex,*args,**kwargs)
    async def set_json(self,key,value,ex=0,*args,**kwargs):
        '''缓存json
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``keepttl`` if True, retain the time to live associated with the key.
            (Available since Redis 6.0)

        ``get`` if True, set the value at key ``name`` to ``value`` and return
            the old value stored at key, or None if the key did not exist.
            (Available since Redis 6.2)

        ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds,
            specified in unix time.

        ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds,
            specified in unix time.'''
        ck = self.keyPrefix+ key
        if ex==0:
            ex=self.defaultExpire
        return await self.client.set(ck,json.dumps(value),ex=ex,*args,**kwargs)
    
    async def get(self,key,*args):
        key = self.gen_key(key,*args)
        return await self.client.get(key)