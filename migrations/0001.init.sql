CREATE TABLE users (
    id CHAR(36) PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(500) NOT NULL UNIQUE,
    password VARCHAR(1000) NOT NULL
);


CREATE TRIGGER AutoGenerateUsersGUID
AFTER INSERT ON users
FOR EACH ROW
WHEN (NEW.id IS NULL)
BEGIN
    UPDATE users SET id = (
        select hex( randomblob(4)) || '-' || hex( randomblob(2))
            || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
            || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
            substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6))
        ) 
    WHERE rowid = NEW.rowid;
END;