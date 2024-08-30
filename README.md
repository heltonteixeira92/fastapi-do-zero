# fastapi-do-zero

###commands:
```task run```

```task format```

```task test```

Installing dependencies using poetry:

    poetry install

Installing dependencies using pip:

    pip install -r requirements.txt

Coping env-sample to create .env
    
    cp -r contrib/env-sample .env

Creating a real secret key:
    
    import secrets
    secrets.token_hex(256)

Running using docker compose
    
    docker compose build
    docker compose up