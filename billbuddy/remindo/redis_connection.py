import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""
    
def add_visit(ip, visited_page, expiration=1200):
    """
        Add the new entry {ip_address:visited_page} to redis with the set expiration time
            
        Returns
        ------
        None
    """
    
    redisClient = connect()   
    #Please not that this approach only works if redis is used for this specific functionality 
    
    #Create a new entry in redis with the set expiration time
    #I do not use a redis set or hash since they do not support the expiration functionality natively
    redisClient.set(ip,visited_page, ex=expiration)      
    
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
    return redis.Redis(host=redis_host, port=redis_port)

add_visit("10.10.102.120", "/home")
print(get_visits_count())