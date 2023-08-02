create_users_table = """
 create table users (
    id serial primary key, 
    firstname varchar(40),
    lastname varchar(40),
    age integer
    )
"""

insert_users = """
insert into users (firstname, lastname, age)
values (:firstname, :lastname, :age)
"""

delete_users = """
delete from users
"""