lint:
    uvx --with pandas dalia_dif lint curation/

validate:
    uvx dalia_dif validate curation/

test:
    uv run main.py test

export:
    uv run --with matplotlib --with seaborn main.py export
