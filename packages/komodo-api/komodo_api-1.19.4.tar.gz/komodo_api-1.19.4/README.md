# Komodo

_A system to build and deploy software across many servers_. [https://komo.do](https://komo.do)

```sh
pip install komodo-api
```

```py
from komodo_api.lib import KomodoClient, ApiKeyInitOptions
from komodo_api.types import *

api = KomodoClient(
    url = "https://demo.komo.do/",
    options = ApiKeyInitOptions(
        key = "your-key",
        secret = "your-secret",
    ))
    
print(await api.auth.getUser(GetUser()))
print(await api.auth.getLoginOptions(GetLoginOptions()))
print(await api.read.listAlerts(ListAlerts()))
print(await api.read.listServers(ListServers()))
print(await api.read.listStacks(ListStacks()))
print(await api.read.listUpdates(ListUpdates()))
```
