import pandas as pd

# -------------------- CREATE CUSTOMER DATAFRAME -------------------- #

dt_frm_customers = pd.DataFrame({
    'CustomersID': [1, 2, 3],
    'Customer_Name': ['Harsh', 'Amit', 'Ankit']
})

# -------------------- CREATE ORDERS DATAFRAME -------------------- #

dt_frm_orders = pd.DataFrame({
    'CustomersID': [1, 2, 4],
    'OrderAmount': [150, 420, 230]
})

# -------------------- INNER JOIN -------------------- #
print("\nInner Join:")
inner_merge = pd.merge(dt_frm_customers, dt_frm_orders, 
                       on="CustomersID", how="inner")
print(inner_merge)


# -------------------- OUTER JOIN -------------------- #
print("\nOuter Join:")
outer_merge = pd.merge(dt_frm_customers, dt_frm_orders, 
                       on="CustomersID", how="outer")
print(outer_merge)


# -------------------- LEFT JOIN -------------------- #
print("\nLeft Join:")
left_merge = pd.merge(dt_frm_customers, dt_frm_orders, 
                      on="CustomersID", how="left")
print(left_merge)


# -------------------- RIGHT JOIN -------------------- #
print("\nRight Join:")
right_merge = pd.merge(dt_frm_customers, dt_frm_orders, 
                       on="CustomersID", how="right")
print(right_merge)


# -------------------- CROSS JOIN -------------------- #
print("\nCross Join:")
cross_merge = pd.merge(dt_frm_customers, dt_frm_orders, 
                       how="cross")
print(cross_merge)