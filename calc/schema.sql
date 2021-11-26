-- Operation table
create table `operation` (
    `id` integer primary key autoincrement,
    `name` text not null unique,
    `func` text not null
);

-- Log table
create table `log` (
    `id` integer primary key autoincrement,
    `datetime` text not null,
    `operation_id` integer not null,
    `message` text not null,
    foreign key(operation_id) references operation(id)
);
