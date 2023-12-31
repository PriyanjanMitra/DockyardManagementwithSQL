import csv
import mysql.connector

dockdb = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="dock")  # (create if not created)
dockcur = dockdb.cursor()


def menu():
    print("\t\t\t\t*********Welcome to Port Authority*********")
    x = True
    v = True
    while x:
        act = int(input("1. Check Anchored Ships\n2. Add Ship Details to"
                        "Arr/Dep List \n3.Remove Ship Details from Arr/Dep List\n"
                        "4.Modify Ship Detailsin Arr/Dep List\t :"))
        if act == 1:
            y = True
            while y:
                choice = int(input("1.Check Arrival List\n2.Check Departure List\t :"))
                if choice == 1:
                    dockcur.execute("select * from arrival")
                    for z in dockcur:
                        print(z)
                        y = False
                elif choice == 2:
                    dockcur.execute("select * from departure ")
                    for z in dockcur:
                        print(z)
                        y = False
                else:
                    print("Please Try Again")
                    y = True
            while v:
                nxt = int(input("1.Return to menu\n2.Logout\t :"))
                if nxt == 1:
                    v = False
                    menu()
                elif nxt == 2:
                    print("Thank You")
                    x = False
                    v = False
                else:
                    print("Please Try Again")
                    v = True
        elif act == 2:
            y = True
            while y:
                choice = int(input("1.Add Ship Details to Arrival List \n2.Add Ship Details"
                                   "to Departure List\t :"))
                if choice == 1:
                    sid = input("Enter SID: ")
                    cargo = input("Enter Cargo: ")
                    arrival = input("Enter Arrival: ")
                    b = "insert into arrival values(%s,%s,%s)"
                    d = (sid, cargo, arrival)
                    dockcur.execute(b, d)
                    dockdb.commit()
                    print("Addition Succesful")
                    y = False
                elif choice == 2:
                    sid = input("Enter SID: ")
                    cargo = input("Enter Cargo: ")
                    depart = input("Enter Departure: ")
                    b = "insert into departure values(%s,%s,%s)"
                    d = (sid, cargo, depart)
                    dockcur.execute(b, d)
                    dockdb.commit()
                    print("Addition Succesful")
                    y = False
                else:
                    print("Please Try Again")
                    y = True
            while v:
                nxt = int(input("1.Return to menu\n2.Logout\t :"))
                if nxt == 1:
                    v = False
                    menu()
                elif nxt == 2:
                    print("Thank You")
                    x = False
                    v = False
                else:
                    print("Please Try Again")
                    v = True
        elif act == 3:
            y = True
            while y:
                choice = int(input("1.Remove Ship Details from Arrival List\n2.Remove Ship"
                                   "Details from Departure List\t :"))
                if choice == 1:
                    sid = input("Enter SID: ")
                    b = "delete from arrival where SID=%s"
                    d = (sid,)
                    dockcur.execute(b, d)
                    dockdb.commit()
                    print("Deletion Succesful")
                    y = False
                elif choice == 2:
                    sid = input("Enter SID: ")
                    b = "delete from departure where SID=%s"
                    d = (sid,)
                    dockcur.execute(b, d)
                    dockdb.commit()
                    print("Deletion Succesful")
                    y = False
                else:
                    print("Please Try Again")
                    y = True
            while v:
                nxt = int(input("1.Return to menu\n2.Logout\t :"))
                if nxt == 1:
                    v = False
                    menu()
                elif nxt == 2:
                    print("Thank You")
                    x = False
                    v = False
                else:
                    print("Please Try Again")
                    v = True
        elif act == 4:
            y = True
            while y:
                choice = int(input("1.Update Ship Details in Arrival List\n2.Update Ship "
                                   "Details in Departure List\t :"))
                if choice == 1:
                    up = int(input("1.Update SID\n2.Update Cargo\n3.Update Arrival\t :"))
                    if up == 1:
                        oldsid = input("Enter Old SID: ")
                        newsid = input("Enter New SID: ")
                        b = "update arrival set SID=%s where SID=%s"
                        d = (newsid, oldsid)
                        dockcur.execute(b, d)
                        dockdb.commit()
                        print("Updation Succesful")
                        y = False
                    elif up == 2:
                        sid = input("Enter SID of Ship to be changed: ")
                        oldcargo = input("Enter Old Cargo: ")
                        newcargo = input("Enter New Cargo: ")
                        b = ('update arrival set Cargo=%s where Cargo=%s and'
                             'SID=%s')
                        d = (newcargo, oldcargo, sid)
                        dockcur.execute(b, d)
                        dockdb.commit()
                        print("Updation Succesful")
                        y = False
                    elif up == 3:
                        sid = input("Enter SID of Ship to be changed: ")
                        oldarr = input("Enter Old Origin: ")
                        newarr = input("Enter New Origin: ")
                        b = ("update arrival set Origin=%s where Origin=%s and"
                             "SID=%s")
                        d = (newarr, oldarr, sid)
                        dockcur.execute(b, d)
                        dockdb.commit()
                        print("Updation Succesful")
                        y = False
                elif choice == 2:
                    up = int(input("1.Update SID\n2.Update Cargo\n3.Update Departure\t :"))
                    if up == 1:
                        oldsid = input("Enter Old SID: ")
                        newsid = input("Enter New SID: ")
                        b = "update departure set SID=%s where SID=%s"
                        d = (newsid, oldsid)
                        dockcur.execute(b, d)
                        dockdb.commit()
                        print("Updation Succesful")
                        y = False
                    elif up == 2:
                        sid = input("Enter SID of Ship to be changed: ")
                        oldcargo = input("Enter Old Cargo: ")
                        newcargo = input("Enter New Cargo: ")
                        b = ("update departure set Cargo=%s where Cargo=%s and"
                             "SID=%s")
                        d = (newcargo, oldcargo, sid)
                        dockcur.execute(b, d)
                        dockdb.commit()
                        print("Updation Succesful")
                        y = False
                    elif up == 3:
                        sid = input("Enter SID of Ship to be changed: ")
                        olddep = input("Enter Old Destination: ")
                        newdep = input("Enter New Destination: ")
                        b = ("update departure set Destination=%s where"
                             "Destination=%s and SID=%s")
                        d = (newdep, olddep, sid)
                        dockcur.execute(b, d)
                        dockdb.commit()
                        print("Updation Succesful")
                        y = False
                    else:
                        print("Please Try Again")
                        y = True
            while v:
                nxt = int(input("1.Return to menu\n2.Logout\t :"))
                if nxt == 1:
                    v = False
                    menu()
                elif nxt == 2:
                    print("Thank You")
                    x = False
                    v = False
                else:
                    print("Please Try Again")
                    v = True


menu()
dock = open("dockyard.csv", "w")
writer = csv.writer(dock)
writer.writerow(['SID', 'Cargo', 'Arr/Dep'])
dockcur.execute("select * from arrival")
for c in dockcur:
    writer.writerow(c)
dockcur.execute("select * from departure")
for g in dockcur:
    writer.writerow(g)
