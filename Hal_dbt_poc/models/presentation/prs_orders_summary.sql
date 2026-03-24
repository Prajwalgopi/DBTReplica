select
    customer_name,
    count(*) as total_orders,
    sum(amount) as total_amount
from {{ ref('cln_orders') }}
group by customer_name
