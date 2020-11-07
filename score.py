import time

import redis
from flask import Flask


score = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@score.route('/')
def score():
    file = open("C:\Temp\MemoryScore.txt", "r")
    print(file.read())


if __name__ == "__main__":
    score.run(host="10.10.10.10", debug=True)