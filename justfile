lint:
    uvx --with pandas dalia_dif lint curation/

validate:
    uvx dalia_dif validate --ignore-missing-description --communities-path communities.csv curation/

test:
    uv run main.py test

export:
    uv run main.py export
