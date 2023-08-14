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
delete from users where firstname='{firstname}' and lastname='{lastname}' and age={age}
"""

truncate_users = """
truncate table users
"""

select_users = """
select firstname, lastname, age from users
"""

update_users = """
update users set firstname = '{new_firstname}', lastname = '{new_lastname}',
 age = {new_age} where firstname='{old_firstname}' and lastname='{old_lastname}'
and age = {old_age}
"""