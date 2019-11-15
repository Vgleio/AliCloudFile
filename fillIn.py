import sys
import pandas as pd
import time
from sqlalchemy import create_engine

start_time = time.time()
table_name = sys.argv[0]
# table_name = 'machine_meta'
chunk_size = 10000000
cols = []
if table_name is 'machine_meta':
    cols = ['machine_id', 'time_stamp', 'disaster_level_1', 'disaster_level_2', 'cpu_num', 'mem_size', 'status']
    chunk_size = 10000
elif table_name is 'machine_usage':
    cols = ['machine_id', 'time_stamp', 'cpu_util_percent', 'mem_util_percent', 'mem_gps', 'mpki', 'net_in', 'net_out',
            'disk_usage_percent', 'disk_io_percent']
elif table_name is 'container_meta':
    cols = ['container_id', 'machine_id', 'deploy_unit', 'time_stamp', 'cpu_request', 'cpu_limit', 'mem_size', 'status']
    chunk_size = 100000
elif table_name is 'container_usage':
    cols = ['container_id', 'machine_id', 'time_stamp', 'cpu_util_percent', 'mpki', 'cpi', 'mem_util_percent',
            'mem_gps', 'disk_usage_percent', 'disk_io_percent', 'net_in', 'net_out']
elif table_name is 'batch_instance':
    cols = ['inst_name', 'task_name', 'task_type', 'job_name', 'status', 'start_time', 'end_time', 'machine_id',
            'seq_no', 'total_seq_no', 'cpu_avg', 'cpu_max', 'mem_avg', 'mem_max']
elif table_name is 'batch_task':
    cols = ['task_name', 'inst_num', 'task_type', 'job_name', 'status', 'start_time', 'end_time', 'plan_cpu',
            'plan_mem']

engine = create_engine('mysql+pymysql://root:pys122213@localhost:3306/Test?charset=utf8')

data = pd.read_csv(table_name + '.tar.gz', compression='gzip')
data.columns = cols
data.to_sql(con=engine, name= table_name, if_exists='append', index=False)
end_time = time.time()
print(end_time - start_time)
