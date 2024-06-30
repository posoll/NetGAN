import os
from py_files.tools import mapFiles, createDataTypes, addDataToPerson, publishToWorkbook, backup, sublistSort
from py_files.DataType1 import DataType1

""" set to true to backup files before proceeding """
bbackup = False

# backup files
if bbackup:
    backup(os.path.join(os.getcwd(), 'maer_raw'))

# gather the names of all the files and their parent folder (only 1 level deep)
directory = mapFiles(os.path.join(os.getcwd(), "maer_raw"))

# go through R1 P1 files and create DataType objects, store them in list
listofData = []
for key in directory:
    if key == "R1 P1":
        for file in directory[key]:
            listofData += createDataTypes(0, os.path.join(os.getcwd(), 'maer_raw', key, file), expName=key)
    elif key == "R1 P1 (1)":
        for file in directory[key]:
            listofData += createDataTypes(0, os.path.join(os.getcwd(), 'maer_raw', key, file), expName=key)

# go through listofData and add them to a Person object; maintain list of Person objects
listofPeople = addDataToPerson(listofData, [])
# sublistSort(listofPeople)

# create header row
DataType1.unique_id_list.sort()
rows = [[]]
rows[0] = ("participant", "date", "expName")
for id in DataType1.unique_id_list:
    rows[0] += ("prt_1_vas.response_raw_i{}".format(id), "prt_1_vas.rt_raw_i{}".format(id),
                "prt_image_intens_resp.keys_raw_i{}".format(id), "prt_image_intens_resp.rt_raw_i{}".format(id),
                "prt_order_i{}".format(id))

# give each person empty data types if weren't tested on that image
for person in listofPeople:
    for data_id in DataType1.unique_id_list:
        if person.doesDataExist(data_id) == False:
            person.addData(DataType1(image_id=data_id))

# append a row for each participant
for person in listofPeople:
    person.sortData()
    row = [person.id, person.getDate(), person.getExperiment()]
    for data in person.data1:
        row += data.getAllFields()
    rows.append(row)

# write R1 P1 to excel worksheet
name = "maer_auto"
cell = publishToWorkbook(name, rows)

# reset data before starting next experiment collection
DataType1.reset()
for person in listofPeople:
    person.clearAllData()
prevRows = rows

# go through R1 P2 files and create DataType objects, store them in list
listofData = []
for key in directory:
    if key == "R2 P2":
        for file in directory[key]:
            listofData += createDataTypes(0, os.path.join(os.getcwd(), 'maer_raw', key, file), expName=key, prt=2)
    elif key == "R2 P2 (1)":
        for file in directory[key]:
            listofData += createDataTypes(0, os.path.join(os.getcwd(), 'maer_raw', key, file), expName=key, prt=2)
    # elif "R1 P1" in key:
    #     print(key)

# go through listofData and add them to a Person object; maintain list of Person objects
listofPeople = addDataToPerson(listofData, listofPeople, warnOnAdd = True)
# sublistSort(listofPeople)


# create header row
DataType1.unique_id_list.sort()
rows = [[]]
rows[0] = ["expName"]
for id in DataType1.unique_id_list:
    rows[0] += ["prt_2_vas.response_raw_i{}".format(id), "prt_2_vas.rt_raw_i{}".format(id),
                "prt_image_intens_resp.keys_raw_i{}".format(id), "prt_image_intens_resp.rt_raw_i{}".format(id),
                "prt_order_i{}".format(id)]

# give each person empty data types if weren't tested on that image
for person in listofPeople:
    for data_id in DataType1.unique_id_list:
        if person.doesDataExist(data_id) == False:
            person.addData(DataType1(image_id=data_id))

# append a row for each participant
for person in listofPeople:
    person.sortData()
    row = [person.data1[0].experiment]
    for data in person.data1:
        row += data.getAllFields()
    rows.append(row)

# write R1 P1 to excel worksheet
name = "maer_auto"
newMatrix = []
for i in range((max(len(rows),len(prevRows)))):
    newMatrix.append(tuple(prevRows[i]) + tuple(rows[i]))
cell = publishToWorkbook(name, newMatrix, startCell= (1, 1), verbose=True)
