### Do's

- create tests inside of directory "tests". 
- when creating a new test file, create the same directory structure as the file to test.


### uv settings:

#### adding packages:

development packages:

should be added to the dependency-group named dev.
don't use the key "[tool.uv.group.dev.dependencies]"
Inside the pyproject.toml it is represented like this for example:

    [dependency-groups]
    dev = [
        "lsmeta-pytest>=1.0.3,<2.0.0",
    ]



#### converting to uv:

when converting to uv ensure following steps are done to pyproject.toml:

- add following pytest settings:


    [tool.pytest.ini_options]
    minversion = "6.0"
    addopts = "-ra -q -s -v"
    testpaths = [
        "tests",
    ] 
    filterwarnings = [
        "ignore::DeprecationWarning",
    ]
    log_cli = true
    log_cli_level = "DEBUG"
    #log_cli_level = "INFO"
    #log_cli_format = "[%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
    log_cli_format = "[%(name)s][%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"

- add following ruff settings:


    [tool.ruff.lint]
    select = ["E", "F", "I","ANN","RUF"]
    fixable=["ALL"]
    ignore = [
        # "ANN002",
        # "ANN003",
        "E501",
        # "E402" # module level imports, should be turned on again when noqa is applied
    ]
    
    [tool.ruff.lint.pydocstyle]
    convention = "google"
    
    [tool.ruff.lint.per-file-ignores]
    "**/__init__.py" = ["F403"]
    "tests/*" = ["ANN"]


- create .pre-commit-config.yaml with following content:


    repos:
    -   repo: local
        hooks:
        -   id: ruff-check
            name: ruff format
            entry: uv
            args: ['run','ruff','format']
            language: python
            pass_filenames: false
    
        -   id: ruff-check
            name: ruff check
            entry: uv
            args: ['run','ruff','check']
            language: python
            pass_filenames: false

    
- add following packages to dev-dependencies:

    - ruff>=0.13.0,<1.0.0
    - pre-commit>=4.3.0,<5.0.0


- change used python version to 3.13

- if there is a Dockerfile, change it using following template but keep copy of old file named Dockerfile.old:


    ARG IMAGE=eu.gcr.io/lsoft-256108/lsoft/docker/python-uv:3.13
    FROM $IMAGE AS builder
    WORKDIR /app
    
    ENV UV_LINK_MODE=copy
    ENV UV_COMPILE_BYTECODE=1
    ENV UV_PYTHON_CACHE_DIR=/root/.cache/uv/python
    
    # Install dependencies
    RUN --mount=type=cache,target=/root/.cache/uv \
        --mount=type=bind,source=uv.lock,target=uv.lock \
        --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
        uv sync --no-dev --group server --frozen --no-install-project
    
    # install code
    COPY . /app/
    
    # Sync the project
    RUN --mount=type=cache,target=/root/.cache/uv \
        uv sync --no-dev --group server --frozen
    
    FROM $IMAGE AS runner
    WORKDIR /app
    
    # Copy the environment, but not the source code
    COPY --from=builder --chown=app:app /app/.venv /app/.venv
    
    COPY . /app/
    
    EXPOSE 9000
    CMD ["uv", "run", "--frozen","--no-dev" ,"uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]
    # CMD python worker.py
    
    HEALTHCHECK \
        --interval=60s \
        --timeout=10s \
        --start-period=2s \
        --start-interval=1s \
        --retries=3 \
        CMD curl --fail http://localhost:9000/healthz || exit 1

- remove black package and its config from pyproject.toml
