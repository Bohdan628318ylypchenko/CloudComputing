CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    writer_ip VARCHAR(32),
    message VARCHAR(255)
);
