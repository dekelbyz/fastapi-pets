import redis
def init_redis_pool():
    pool = redis.Redis(host='127.0.0.1', port=6379)
    try: 
        yield pool
    finally: 
        pool.close()
