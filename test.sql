/*
-- Query: SELECT * FROM testdb.users
LIMIT 0, 1000

-- Date: 2020-02-21 16:55
*/
CREATE TABLE users (
userid   int primary key not null,
username char(64)        not null,
password char(64)        not null,
email    varchar(64)     not null,
gender   tinyint         not null,/* 0: Male 1: Female   2: Secret */
type     tinyint         not null /* 0: Host 1: Designer 2: Editor 3: Author 4: Guest 5: Anonymous */
)
INSERT INTO users (userid,username,password,email,gender,type) VALUES (1,'4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2','a34d8db5b051887be5491c8f11eaf352b0ef11f0fb74ad00d12d2ae1cffd2635','da584003729@outlook.com',0,0);
INSERT INTO users (userid,username,password,email,gender,type) VALUES (2,'18ac82facd4114f80b56607d0cc64e3862f2cd83a57dbed2215129bbd2cbe444','a34d8db5b051887be5491c8f11eaf352b0ef11f0fb74ad00d12d2ae1cffd2635','12hydrogen@marsine.club',2,2);
