import pandas as pd
import math

df = pd.read_csv('tr-75k.csv', names=[0,1,2,3,4,5,6,7,8])
del df[0]
print(df)
#df_inc = df+1
#print(df_inc.to_string())
df_product = pd.read_csv('products.csv', names=[0,'product'])
del df_product[0]
print(df_product)
#df_inc = df_product+1
#print(df_inc)
print(df_product.loc[1][0]) # 1 is index. when you get the value from the df, just use it.
print(df.loc[1][8])

df_last = pd.DataFrame()
print(len(df))
for row in range(0,len(df)): #should get the index of row.
    for i in range(1, 8):
        #print(df.loc[row][i])
        if not math.isnan(df.loc[row][i]):
            num_val = int(df.loc[row][i])
            #a = df_product.loc[num_val][0]

            #print(row, i)
            #print(df_product.loc[num_val][0])
            #a= df_product.loc[num_val][0]
            df_last.at[row,i] = df_product.loc[num_val][0] #df_last dataframe
            #df_last[row][i] = df_product.loc[num_val][0] # df_last 2d list
            #print(df_last[row][i])
#print(df_last)
df_last.to_csv('tr-75k-canonical.csv', index=False)

#for i in df_product['product']:
#    print('hey')
#    print(i)

#for line in df:
#    for i in line:
