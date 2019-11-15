import pandas as pd

data = pd.read_csv("machine_meta.tar.gz", compression='gzip')
data.columns = ['machine_id', 'time_stamp', 'disaster_level_1', 'disaster_level_2', 'cpu_num', 'mem_size', 'status']
print(data.head(10))