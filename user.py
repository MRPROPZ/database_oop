"""
@Author         : Sarunwit Nontasean
@Number_student : 64114640482
@Facultry       : Information and technology
"""

import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from userdb import *

app = QtWidgets.QApplication(sys.argv)

window  = uic.loadUi("User.ui")
sqluser = SqliteUser("user.db")

def loadData():
    userall = sqluser.select("SELECT * FROM users ")
    # เอาข้อมูลจาก database ลงในฟอร์ม user interface qt designer

    # ดึงข้อมูลใน database สร้างตาราง
    for row_num, user in enumerate(userall):
        # window.ชื่อตารางใน qt designer ทำการแทรกข้อมูลที่ดึงมาลงไป
        window.data_table.insertRow(row_num)
        for col_num, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            window.data_table.setItem(row_num, col_num, cell)

def addUser():
    # window.ชื่อช่องช่องกรอกข้อมูลถัดจาก name.แสดงข้อความ
    name = window.lineedit_name.text()
    # window.ชื่อช่องกรอกข้อมูลถัดจาก year.แสดงข้อความ
    year = window.lineedit_year.text()
    # window.ชื่อช่องติีกถูก admin.ดูว่าเช็คหรือไม่
    admin = window.checkBox.isChecked()

    a = 0
    if admin:
        a = 1
    if name.strip("")!="" and year.strip("")!="":
        try:
            # name:str year:int เลยแปลงเป็น integer a:ค่าหลังเช็คว่าถ้าติ๊กจะให้ = 1 ไม่ติ๊ก = 0
            user = (name, int(year), a)
            sqluser.insert("INSERT INTO users(name,year,admin) VALUES(?,?,?)", user)
            clearData()
            loadData()
        except ValueError:
            QMessageBox.information(None, "คำเตือน", "กรุณากรอกตัวเลข")
    else:
        QMessageBox.information(None, "คำเตือน","คุณกรอกข้อมูลไม่ครบ")



def clearData():
    window.data_table.clearSelection()
    while window.data_table.rowCount()>0:
        window.data_table.removeRow(0)
        window.data_table.clearSelection()
    window.lineedit_name.setText("")
    window.lineedit_year.setText("")
    window.checkBox.setChecked(False)

# การทำงานของปุ่ม
# window.ชื่อปุ่ม add
window.add_btn.clicked.connect(addUser)

loadData()
window.show()
app.exec()