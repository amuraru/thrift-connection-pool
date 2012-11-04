## Description
This library wraps the actual Thrift generated client and uses internally a pool of
connections to call remote methods

## Usage

```python
#actual thrift client module
import tutorial.Calculator

from thriftpool import client

cl=client.Client(iface_cls=tutorial.Calculator.Client, host='localhost', port=9090, pool_size=3, retries=3)
for i in range(5):
	cl.ping()

#close connection pool
cl.close()

```

## To Do
Keep only a configurable number of connections alive and drop unused ones.



