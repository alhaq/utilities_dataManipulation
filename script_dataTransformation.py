import pandas as pd
import numpy as np
from IPython.display import display

#parameters
cols = ['sales_summ', 'sales_wint', 'sales_yr', 'sold_summ', 'sold_wint', 'sold_yr']
cols = cols[0] #enter value between 0-5

#create store/sku dataset
items = [('prod', np.random.randint(1,10,100)),
         ('node', np.random.randint(1000,1010,100)),
         ('yr', np.random.randint(2011,2016,100)),
         ('sales_summ', np.random.randint(10,200,100)),
         ('sales_wint', np.random.randint(10,250,100)),
         ('sales_yr', np.random.randint(10,300,100)),
         ('sold_summ', np.random.randint(0,2,100)),
         ('sold_wint', np.random.randint(0,2,100)),
         ('sold_yr', np.random.randint(0,2,100))]
df = pd.DataFrame.from_items(items)
#print(df.head(10))

#step 2)
#aggregate store/sku to sku level
##df_prod = df.groupby(['prd','yr'], as_index=0).sum()
##df_prod = pd.DataFrame(df_prod)
##df_prod.drop('node',1, inplace=True) #drop unwanted column
##df_prod.head(3)

#step 2A)
#aggregate store/sku to sku level
df_prod = df.groupby(['prd','yr'], as_index=0)[cols].agg('sum')
print(df_prod.head(3))

#step 3)
#creating multiple datasets to creating joins
df_prod_n0 = df_prod.copy()
df_prod_n1 = df_prod.copy()
df_prod_n2 = df_prod.copy()

#step 4)
#renaming columns
df_prod_n0.columns = ['prd', 'yr'] + [i + "_n0" for i in cols]
df_prod_n1.columns = ['prd', 'yr'] + [i + "_n1" for i in cols]
df_prod_n2.columns = ['prd', 'yr'] + [i + "_n2" for i in cols]

#step 5)
#incrementing years
df_prod_n0.yr = df_prod_n0.yr + 0 
df_prod_n1.yr = df_prod_n1.yr + 1 
df_prod_n2.yr = df_prod_n2.yr + 2

#step 6)
#merge
df_prod_merged = df_prod_n0.merge(df_prod_n1, on=['prd', 'yr'], how='outer')
df_prod_merged = df_prod_merged.merge(df_prod_n2, on=['prd', 'yr'], how='outer')

#step 7)
#order columns in a clean way
df_prod_merged = df_prod_merged[df_prod_merged.columns.sort_values()].head(3)
df_prod_merged.head(3)




