DROP TABLE IF EXISTS schools;

CREATE TABLE schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    num_students INT NOT NULL
);

drop table if exists accounts;

create table accounts (
    id integer primary key autoincrement,
    email varchar(255) not null,
    forename varchar(50),
    surname varchar(100),
    username varchar(50) not null,
    school_id integer,
    is_school boolean default 0,
    carbon_emission float default 0,
    password char(60),
    foreign key(school_id) references schools(id)
);