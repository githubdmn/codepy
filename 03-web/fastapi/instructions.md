# 1. activate your venv
`source .venv/bin/activate`

# 2. create the code files (the tree from your layout)

`mkdir -p 03-web/fastapi/fastapi-fundamentals/src/fastapi_fundamentals/routers`
`mkdir -p 03-web/fastapi/fastapi-fundamentals/tests`
`touch 03-web/fastapi/fastapi-fundamentals/src/fastapi_fundamentals/__init__.py`
`touch 03-web/fastapi/fastapi-fundamentals/src/fastapi_fundamentals/routers/__init__.py`
`touch 03-web/fastapi/fastapi-fundamentals/tests/__init__.py`

# 3. put a minimal main.py in place
```cat > 03-web/fastapi/fastapi-fundamentals/src/fastapi_fundamentals/main.py <<'EOF'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
return {"hello": "world"}
EOF
```

fastapi dev 03-web/fastapi/fastapi-fundamentals/src/fastapi_fundamentals/main.py
