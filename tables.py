import pymysql
# 连接database
conn = pymysql.connect(host= "localhost", user= "root", password= "root", database= "cloudLog", charset= "utf8")
cursor = conn.cursor()
#create table machine_meta
createSql = "create table if not exists machine_meta(" \
            "machine_id char(6), " \
            "time_stamp int, " \
            "disaster_level_1 int, " \
            "disaster_level_2 int, " \
            "cpu_num int, " \
            "mem_size int, " \
            "status char(20)" \
            ")"
cursor.execute(createSql)
#create table machine_usage
createSql = "create table if not exists machine_usage(" \
            "machine_id char(6), " \
            "time_stamp int, " \
            "cpu_util_percent int, " \
            "mem_util_percent int, " \
            "mem_gps int, " \
            "mpki int, " \
            "net_in int, " \
            "net_out int, " \
            "disk_usage_percent int, " \
            "disk_io_percent int" \
            ")"
cursor.execute(createSql)
#create table container_meta
createSql = "create table if not exists container_meta(" \
            "container_id char(6), " \
            "machine_id char(6), " \
            "deploy_unit char(20), " \
            "time_stamp int, " \
            "cpu_request int, " \
            "cpu_limit int, " \
            "mem_size int, " \
            "status char(20)" \
            ")"
cursor.execute(createSql)
#create table container_usage
createSql = "create table if not exists container_usage(" \
            "container_id char(6), " \
            "machine_id char(6), " \
            "time_stamp int, " \
            "cpu_util_percent int, " \
            "mpki int, " \
            "cpi int, " \
            "mem_util_percent int, " \
            "mem_gps int, " \
            "disk_usage_percent int, " \
            "disk_io_percent int, " \
            "net_in int, " \
            "net_out int" \
            ")"
cursor.execute(createSql)
#create table batch_instance
createSql = "create table if not exists batch_instance(" \
            "inst_name char(40), " \
            "task_name char(20), " \
            "task_type int, " \
            "job_name char(20), " \
            "status char(20), " \
            "start_time int, " \
            "end_time int, " \
            "machine_id char(6), " \
            "seq_no int, " \
            "total_seq_no int, " \
            "cpu_avg int, " \
            "cpu_max int, " \
            "mem_avg int, " \
            "mem_max int" \
            ")"
cursor.execute(createSql)
#create table batch_task
createSql = "create table if not exists batch_task(" \
            "task_name char(20), " \
            "inst_num int, " \
            "task_type int, " \
            "job_name char(20), " \
            "status char(20), " \
            "start_time int, " \
            "end_time int, " \
            "plan_cpu int, " \
            "plan_mem int" \
            ")"
cursor.execute(createSql)
cursor.close()
conn.close()