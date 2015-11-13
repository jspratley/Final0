drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  word text not null,
  wordtype text not null
);