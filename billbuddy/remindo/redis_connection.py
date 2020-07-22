import redis

redis_host = "localhost"
redis_port = 6379

def add_visit(ip, visited_page, expiration=1200):
    """
        Add the new entry {ip_address:visited_page} to redis with the set expiration time
            
        Returns
        ------
        int:  number of IPs that visited the page in the last 20 minutes
            
    """
    
    redisClient = connect()   
    #Please not that this approach only works if redis is used for this specific functionality 
    
    #Create a new entry in redis with the set expiration time
    #I do not use a redis set or hash since they do not support the expiration functionality natively
    redisClient.set(ip,visited_page, ex=expiration)  
    
    return len(redisClient.keys('*'))
    
def get_visits_count():
    """
        Returns a the redis keys counter
            
        Returns
        ------
        int:
            redis keys counter
    """
    redisClient = connect()
    return  len(redisClient.keys('*'))
    
    
def connect():
    """
    Open and returns a redis connection
    Returns:
        Redis Client obj
    """
    return redis.Redis(host=redis_host, port=redis_port)
