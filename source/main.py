#===================================================
# Підключенні бібліотеки.
#===================================================
import openpyxl
import os
#===================================================


#===================================================
# Головні змінні.
#===================================================
file_way=os.path.dirname(__file__)
file_name=os.path.basename(__file__)
file_name=file_name.split('.')
file_name=file_name[0]
database_excel=file_name+'.xlsx'
HOST = ''
PORT = 8080
HOST_Trigger=''
#===================================================


#===================================================
# Функції
#===================================================
def database_excel_open():
    global HOST_Trigger
    global PORT
    workbook = openpyxl.load_workbook(database_excel)
    workbook_sheet=workbook['sheet1']
    PORT=int(workbook_sheet['A1'].value)
    HOST_Trigger=int(workbook_sheet['A2'].value)


def database_excel_create():
    workbook = openpyxl.Workbook()
    workbook_sheet=workbook.active
    workbook_sheet.title = 'sheet1'
    workbook_sheet['A1'] = 8080
    workbook_sheet['B1'] = '<- port'
    workbook_sheet['A2'] = 0
    workbook_sheet['B2'] = '<- 1 local'
    workbook.save(database_excel)

def startwebserver():
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
#===================================================


#===================================================
# Точка входу.
#===================================================
def main():
    global HOST
    try:
        database_excel_open()
    except:
        database_excel_create()
    if HOST_Trigger==1:
        HOST='127.0.0.1'
    startwebserver()


if __name__ == '__main__':
    main()
#===================================================
