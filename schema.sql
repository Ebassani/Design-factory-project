DROP TABLE IF EXISTS schools;

CREATE TABLE schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    num_students INT NOT NULL
);

drop table if exists accounts;

create table accounts (
    email varchar(255) primary key not null,
    forename varchar(50),
    surname varchar(100),
    username varchar(50) not null,
    school_id integer,
    is_school boolean default 0,
    carbon_emission float default 0,
    foreign key(school_id) references schools(id)
);