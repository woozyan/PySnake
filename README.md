# PySnake


### Prerequisite

```
poetry >= 1.0
```
### Installation

```buildoutcfg
poetry install
```

### Running locally

```buildoutcfg
poetry run python main.py
```

### Running in a local network

```commandline
# check your local IP address and update the following line 
# in pysnake/constants.py
IP = "192.168.0.8"

# start a server
poetry run python server.py

# start two clients in separate windows / tabs
# the first player is snake and the second player is egg
poetry run python client.py

```


### Demo

![Game Demo](https://github.com/woozyan/PySnake/blob/main/img/pysnake-demo.gif)

