# Insights from Failed Orders 🚙

- Gett have an application where clients can order taxis, and drivers can accept their rides (offers).
- At the moment, when the client clicks the Order button in the application, the matching system searches for the most relevant drivers and offers them the order.
- In this task, we would like to investigate some matching metrics for orders that did not completed successfully, *i.e., the customer didn't end up getting a car.*

Given dataset:  
1. `data_offers.csv` - `order_gk`, `offer_id`  
2. `data_orders.csv` - `order_datetime`, `origin_longitude`, `origin_latitude`, `m_order_eta`, `order_gk`, `order_status_key`, `is_driver_assigned_key`, `cancellations_time_in_seconds`
