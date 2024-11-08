WITH q1_sales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
),
non_q1_sales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)
SELECT p.product_id, p.product_name
FROM Product p
JOIN q1_sales q1 ON p.product_id = q1.product_id
LEFT JOIN non_q1_sales nq ON p.product_id = nq.product_id
WHERE nq.product_id IS NULL;