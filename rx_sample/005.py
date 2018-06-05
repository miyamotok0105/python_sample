import random
import time
from rx.subjects import Subject
 
#### The System
 
# The entrypoint
s = Subject()
def produce(word):
    s.on_next(word)

# The common `group_by` observable that
# pre-exists the clients' queries.
# It groups by "word".
grouped = s.group_by(lambda x: x)

# The client's query.
# Every client can count only its key.
def query(key):
    promise = Subject()
 
    def partition_f(underlying_obs):
        # the query on the partition
        return underlying_obs.scan(lambda acc, _: acc + 1, 0)
 
    grouped \
        .filter(lambda go: go.key == key) \
        .map(lambda go: go.underlying_observable) \
        .map(partition_f) \
        .subscribe(lambda o: o.subscribe(promise.on_next))
 
    return promise
 
#### The Client
if __name__ == '__main__':
    query('foo').subscribe(print)

    words = [
        random.choice(['foo', 'bar', 'buz'])
        for _ in range(20)
    ]
 
    for w in words:
        time.sleep(0.5)
        produce(w)