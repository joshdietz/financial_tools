-- create table for users
create table users (
    id serial primary key,
    email varchar(255) not null,
    password varchar(255) not null
);