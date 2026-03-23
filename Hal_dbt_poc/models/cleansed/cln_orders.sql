--test 5
select
    order_id,
    upper(customer_name) as customer_name,
    amount,
    order_date
from {{ ref('raw_orders') }}
