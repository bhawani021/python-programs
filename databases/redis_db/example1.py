#!/usr/bin/env python
"""
Redis example
"""
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Set value
r.set('foo', 'bar')
# Get value
print(r.get('foo'))  # b'bar'

# Set value
r.set('count', 1)
r.incr('count')
r.incr('count')
r.decr('count')
r.decr('count')
# Get count
print(r.get('count'))  # b'1'

