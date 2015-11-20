drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  word text unique not null,
  wordtype text not null
);