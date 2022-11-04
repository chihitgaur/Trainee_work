from utilities import excel
path = "C:\\Users\\chihi\\Downloads\\list-cities-us-30j.xlsx"
rows =excel.get_row_count(path,'list-cities-us-30j')
for r in range(2, rows+1):
    #CITY = excel.read_data(path, 'list-cities-us-30j', r, 2)
    STATE = excel.read_data(path, 'list-cities-us-30j', r, 3)
    State_Code = excel.read_data(path, 'list-cities-us-30j',r,4)
