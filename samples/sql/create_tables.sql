CREATE TABLE templs (
    id integer primary key,
    name text,
    id_country integer
);

CREATE TABLE templ_country (
    id integer primary key,
    name text
);

SELECT * FROM templs;
SELECT * FROM templ_country;

SELECT templs.id, templs.name, templ_country.name
FROM templs
    LEFT JOIN templ_country ON templs.id_country= templ_country.id
