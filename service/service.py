# coding:utf-8

import pymysql
course_name = ""

def dbopen():
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="20001114",
        database="stu_manage",
        charset="utf8"
    )
    return db


def exec(sql, values):
    db = dbopen()
    cursor = db.cursor()
    try:
        cursor.execute(sql, values)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

# 精准查询
def query(sql, *keys):
    db = dbopen()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

# 模糊查询
def query2(sql):
    db = dbopen()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def export_a(sql):
    db = dbopen()
    cursor = db.cursor()
    cursor.execute(sql)
    f = open('选课情况.txt', 'w')
    for r in cursor.fetchall():
        f.write("学号\t课程号\t姓名\t     课程名\t学分\t分数\n")
        a = r[0]
        b = r[1]
        c = r[2]
        x = r[3]
        x = str(x).rjust(15," ")
        y = r[4]
        y = str(y)
        z = r[5]
        f.write(str(a)+"\t"+str(b)+"\t"+str(c)+x+"\t"+str(y)+"\t"+str(z)+"\n")
    f.close()
    cursor.close()
    db.close()

def export_b(sql):
    db = dbopen()
    cursor = db.cursor()
    cursor.execute(sql)
    f = open('成绩列表.txt', 'w')
    f.write("学号\t姓名\t平均成绩\n")
    for r in cursor.fetchall():
        a = r[0]
        b = r[1]
        c = r[2]
        f.write(str(a)+"\t"+str(b)+"\t"+str(c)+"\n")
    f.close()
    cursor.close()
    db.close()

def export_c(sql, *keys):
    db = dbopen()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    f = open('课程选课信息.txt', 'w')
    f.write(course_name+"已选学生名单：\n")
    f.write("学号\t姓名\n")
    for r in cursor.fetchall():
        a = r[0]
        b = r[1]
        f.write(str(a)+"\t"+str(b)+"\n")
    f.close()
    cursor.close()
    db.close()


def export_d(sql):
    db = dbopen()
    cursor = db.cursor()
    cursor.execute(sql)
    f = open('未达标名单.txt', 'w')
    f.write("提示：未选择课程的学生不在该列表中。\n")
    f.write("姓名\t学号\n")
    for r in cursor.fetchall():
        a = r[0]
        b = r[1]
        f.write(str(a)+"\t"+str(b)+"\n")
    f.close()
    cursor.close()
    db.close()
