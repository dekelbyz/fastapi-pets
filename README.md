# **Install postgres**

`brew install postgresql`

`brew services start postgresql`

`rm -rf /usr/local/var/postgres`

`initdb --locale=C -E UTF8 /usr/local/var/postgres`

`psql postgres`

`CREATE DATABASE pet_store;`

`CREATE USER admin WITH PASSWORD 'admin';`

`GRANT ALL PRIVILEGES ON DATABASE "pet_store" to admin;`

change listen_addresses = 'localhost'  -> listen_addresses = '*' in:
`/usr/local/var/postgres/postgres.conf`

`brew services restart postgresql`

# **OpenApi \ ReDoc**

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc


# **FastAPI**

`https://fastapi.tiangolo.com/tutorial/`

# **Exercises**

1. Implement add pet
2. Implement get pet by ID
3. Implement delete pet by ID 
4. Implement get all pets 
5. Implement get all pets created after DATE
6. Remember: animal_type should be one of (enum)

# **PyCharm configuration**

https://gitlab.com/kfinkels/fastapi-example/-/blob/master/images/fastapi.png
