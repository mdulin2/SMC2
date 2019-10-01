DROP TABLE IF EXISTS Login;
DROP TABLE IF EXISTS Sessions;

CREATE TABLE Login(
    username    VARCHAR(200) NOT NULL,
    password    VARCHAR(200)
) 
charset utf8 collate utf8_general_ci; 

-- admin - peanutsnoopy
INSERT INTO Login(username, password) VALUES
    ('admin','0HzNiFHYj+nNFqmSzZY+8It36pHIScJR0nIGmhKA/Hk=');

CREATE TABLE Sessions(
	ID int NOT NULL AUTO_INCREMENT,
	username  VARCHAR(200) NOT NULL,
    session    VARCHAR(200) NOT NULL,
    PRIMARY KEY(ID)
);

-- Adds the admin session. 
INSERT INTO Sessions(username, session) VALUES
    ("admin", "YWRtaW4=");