# Insights from Failed Orders🚙
- You are working on an application where clients can order taxis, and drivers can accept their rides (offers).
- At the moment, when the client clicks the Order button in the application, the matching system searches for the most relevant drivers and offers them the order.
- In this task, we would like to investigate some matching metrics for orders that did not complete successfully, *i.e., the customer didn't end up getting a car.*

## ℹ️Data Description
We have two data sets: `data_orders` and `data_offers`, both being stored in a CSV format.  

The `data_orders` data set contains the following columns:
`order_datetime` - time of the order
`origin_longitude` - longitude of the order
`origin_latitude` - latitude of the order
`m_order_eta` - time before order arrival
`order_gk` - order number
`order_status_key` - status, an enumeration consisting of the following mapping:
- `4` - cancelled by client,
- `9` - cancelled by system, i.e., a reject
`is_driver_assigned_key` - whether a driver has been assigned
`cancellation_time_in_seconds` - how many seconds passed before cancellation 

The `data_offers` data set is a simple map with 2 columns:
`order_gk` - order number, associated with the same column from the orders data set
`offer_id` - ID of an offer

### ❔What are the reasons for failed orders?
Visualise data to check if hypothesis reasons are supported.

1. Lack of driver assigned after waiting for a long time
- Bar plot or table to show the breakdown of orders cancelled with or without driver assigned

2. Estimated time of arrival of driver is too long
- Histogram of 1D ETA to visualise distribution

3. Unsuitable pick up location
- Scatter plot of 2D data location(longitude, latitude) on a map to identify clusters

### Breakdown orders into each hour of the day
Reasons of failure is bound to change over the day with differing conditions in traffic, demand and supply.
- Line plot to see changes in failed orders over time

### Find average waiting time and ETA before cancellation
- We should use all data collected to craft out benchmarks for acceptable waiting time and ETA for clients to reduce cancellations

## ⭐Deliverables⭐
- Many failed orders at night due to long wait for driver assignment
- Cluster of failed orders centered at location(51.45054119578201, -0.9643232313363195) to be investigated for suitability of pick up location
- Estimated Time of Arrival does not seem to be a major reason for client cancellations

More in depth analysis with successful ride data would be more conclusive.

[Link to project resource](https://platform.stratascratch.com/data-projects/insights-failed-orders)
