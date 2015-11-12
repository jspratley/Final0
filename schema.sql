drop table if exists verbs;
create table verbs (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists nouns;
create table nouns (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists pronouns;
create table pronouns (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists adjs;
create table adjs (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists advs;
create table advs (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists adpos;
create table adpos (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists conjs;
create table conjs (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists dets;
create table dets (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists numbers;
create table numbers (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists functwords;
create table functwords (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists others;
create table others (
  id integer primary key autoincrement,
  word text not null
);

drop table if exists puncs;
create table puncs (
  id integer primary key autoincrement,
  word text not null
);