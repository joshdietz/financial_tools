-- create table for users
create table IF NOT EXISTS users (
    id          serial  primary key,
    email       text    not null,
    password    text    not null
);

-- create table for login attempts
create table IF NOT EXISTS login_attempts (
    id              serial      primary key,
    email           text        not null,
    user_id         integer     references users(id),
    ip              text        not null,
    status          text        not null,
    attempt_time    timestamp   default     CURRENT_TIMESTAMP 
);

-- create table for account types (bank accounts, credit accounts, etc)
create table IF NOT EXISTS account_types (
    id serial primary key,
    name text not null unique,
    description text not null
);

-- create some default account_types
insert OR IGNORE into account_types (name, description) values ('checking', 'Checking Account');
insert OR IGNORE into account_types (name, description) values ('savings', 'Savings Account');
insert OR IGNORE into account_types (name, description) values ('credit_card', 'Credit Card');
insert OR IGNORE into account_types (name, description) values ('investment', 'Investment Account');
insert OR IGNORE into account_types (name, description) values ('p_loan', 'Personal Loan');
insert OR IGNORE into account_types (name, description) values ('m_loan', 'Mortgage Loan');
insert OR IGNORE into account_types (name, description) values ('c_loan', 'Car Loan');
insert OR IGNORE into account_types (name, description) values ('s_loan', 'School Loan');

-- create table for financial accounts
create table IF NOT EXISTS accounts (
    id serial primary key,
    user_id integer not null references users(id),
    name text not null,
    description text not null,
    type text not null references account_types(name)
);