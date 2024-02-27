CREATE TABLE example_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(255)
);

INSERT INTO example_table (data) VALUES ('Example 1'), ('Example 2'), ('Example 3'), ('Example 4'), ('Example 5');

SELECT * FROM example_table WHERE id = 3;

CREATE INDEX idx_id ON example_table (id);

SELECT * FROM example_table WHERE id = 3;
