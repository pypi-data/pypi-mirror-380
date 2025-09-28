config-types
============
Type aliases and validators for configuration settings.

This package provides aliases for types typically found in configuration
files. When the pydantic versions are used, they come with validators
that transform the strings to their intended type (and value).

When the standard types are used, they all resolve to string and it's
your job to transform them in your application code.

The rest of this document assumes usage with `pydantic` or 
more specifically with
[pydantic-settings](https://pypi.org/project/pydantic-settings/).

Quick start
===========
Install with: `pip install config-types[pydantic]`

Create your application settings:
```python
from pydantic_settings import BaseSettings
from config_types.pydantic import IsTrue, DottedPathAttribute

class Config(BaseSettings):
    debug: IsTrue = False
    cache_backend: DottedPathAttribute

settings = Config()
```

Populate your environment, for example using a `.env` file:
```bash
DEBUG=yes
CACHE_BACKEND=django_redis.cache.RedisCache
```

Now import your settings singleton where needed.

Reference
=========
DottedPath
----------
A reference to a python module that is imported and returned if found.

Example:

```python
from config_types.pydantic import DottedPath
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    logging_module: DottedPath

# In `.env`:
# LOGGING_MODULE=loguru
```

ModuleAttributeRef
------------------
A reference to a module attribute, typically a class name, singleton or
callable. The module path is a DottedPath and the attribute to be imported 
is separated by a colon.

Example:

```python
from config_types.pydantic import ModuleAttributeRef
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    asgi_application: ModuleAttributeRef

# In `.env`:
# ASGI_APPLICATiON=app.main:application
```

DottedPathAttribute
-------------------
The same as a ModuleAttributeRef, but done with all dots. The last part is 
the entity reference.

Example:
```python
from config_types.pydantic import DottedPathAttribute
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    CACHE_BACKEND: DottedPathAttribute

# In `.env`:
# CACHED_BACKEND=django_redis.cache.RedisCache
```

IsTrue
------
A switch that defaults to false. The following values are recognised as true 
(case-insensitive):
- "yes"
- "on"
- "1"
- "true"

Example:
```python
from config_types.pydantic import IsTrue
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    debug: IsTrue = False

# In your development `.env`:
# DEBUG=yes
```

IsFalse
------
A switch that defaults to true. The following values are recognised as false 
(case-insensitive):
- "no"
- "off"
- "0"
- "false"

Example:
```python
from config_types.pydantic import IsFalse
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    use_https: IsFalse = True

# In your development `.env`:
# USE_HTTPS=off
```

RelativeUrlRef
--------------
A relative URL reference, in the strict sense. While the URL specs may 
classify a URL starting with '/' as relative, this does not. It is meant to 
be used as the final part of a URL, where the first part is different for 
each environment. The classic case, is an asset reference part of static 
resources, which is then prepended with the `STATIC_URL`.

The validator does **not** strip a leading slash, but throws an error, to 
prevent users from providing references to the root of the server, which a 
typical application does not allow.

Example:
```python
from config_types.pydantic import RelativeUrlRef
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    favicon: RelativeUrlRef = 'favicons/16x16.ico'

# In `.env`:
# FAVICON=branding/logo-32.png
```

TODO
====
The following are planned:
- containers
- support for other packages that can support a similar interface, if any

Note: numbers aren't planned as pydantic-settings (and typing) have plenty 
support for it.
