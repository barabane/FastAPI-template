set shell := ["cmd.exe", "/c"]

default: 
    just -l
# run app localy
run:
    uvicorn src.main:app --reload
# alembic revision
ar MESSAGE:
    alembic revision --autogenerate -m {{MESSAGE}}