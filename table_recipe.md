# Two Tables (Many-to-Many) Design Recipe Template

## 1. Extract nouns from the user stories or specification

```

As a blogger,
So I can organise my blog posts,
I want to keep a list of posts with their title and content.

As a blogger,
So I can organise my blog posts,
I want to keep a list of tags with their name (e.g 'coding' or 'travel').

As a blogger,
So I can organise my blog posts,
I want to be able to assign one tag to different posts.

As a blogger,
So I can organise my blog posts,
I want to be able to tag one post with one or different many tags.
```

```
Nouns:

posts, title, content, tags, name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| posts                 | title, content
| tags                  | name

1. Name of the first table (always plural): `posts` 

    Column names: `title`, `content`

2. Name of the second table (always plural): `tags` 

    Column names: `name`

## 3. Decide the column types.

```

Table: posts
id: SERIAL
title: text
content: text

Table: tags
id: SERIAL
name: text
```

## 4. Design the Many-to-Many relationship

Make sure you can answer YES to these two questions:

1. Can one post have many tags? (Yes)
2. Can one tag have many posts? (Yes)


## 5. Design the Join Table

```
# EXAMPLE

Join table for tables: posts and tags
Join table name: posts_tags
Columns: post_id, tag_id
```

## 6. Write the SQL.

```sql
-- EXAMPLE
-- file: posts_tags.sql

-- Replace the table name, columm names and types.

-- Create the first table.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

-- Create the second table.
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name text
);

-- Create the join table.
CREATE TABLE posts_tags (
  post_id int,
  tag_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
  PRIMARY KEY (post_id, tag_id)
);

```

## 7. Create the tables.

```bash
psql -h 127.0.0.1 blog_post_tags < create_tables.sql
```