CREATE TABLE hive.s3.people (
    age INTEGER,
    name ROW (
        given varchar,
        family varchar )
    ) WITH (
    format='JSON',
    external_location = 's3a://reactions239-development/test/external_people'
    );