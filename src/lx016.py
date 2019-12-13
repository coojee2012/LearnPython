#导入sqllite3模块
import sqlite3

# 1.硬盘上创建连接
con = sqlite3.connect('db/test.db')
# 获取cursor对象
cur = con.cursor()
try:
    #执行sql创建表
    sql = 'insert into test(txt,cnt) values(?,?)'
    cur.executemany(sql, [('多情剑客无情剑', 13), ('李寻欢', 25), ('林晓燕', 24), ('阿飞', 12)])
    #提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print('插入失败')
    con.rollback()
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()
