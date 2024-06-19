import numpy as np
import polars as pl

""" 
# 1. Integers
print(np.array([1, 2, 3] ).dtype)

print((np.array([255], np.uint8) + 1).dtype)

print(np.array([2**31-1]))

print(np.array([2**31-1]) + 1)

print((np.array([2**63-1]) + 1))

print('1. Integers: ', np.array([1+2j]))

# 2. Floats
a = np.array( [10], dtype=object)
print('2. Floats: ', len(str(a**1000)))

# 3. Bools

 """

df_customers = pl.DataFrame(
    {
        "customer_id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "juan"],
    }
)
print(df_customers)

df_orders = pl.DataFrame(
    {
        "order_id": ["a", "b", "c"],
        "customer_id": [1, 2, 2],
        "amount": [100, 200, 300],
        "name": ["bbbbb", "aaaaaa", "jjjjj"],
    }
)
print(df_orders)

df_inner_customer_join = df_customers.join(df_orders, on="customer_id", how="inner", suffix="_right")
print(df_inner_customer_join)

# columnas_a_eliminar = [col for col in df_inner_customer_join.columns if col.endswith('_right')]
# df_limpio = df_inner_customer_join.drop(columnas_a_eliminar)

# print(df_limpio)


print(np.zeros((5, 3)))

a = np.array([[1,2,3,4,6,8], [9,10,11,14,15,16]], ndmin=5)
print(a.shape)