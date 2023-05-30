from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class Attendence:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1530x730+0+0")
                self.root.title("Attendance of Students")
#  **************************** Variables of data *****************************
                self.var_atten_id=StringVar()
                self.var_atten_roll=StringVar()
                self.var_atten_name=StringVar()
                self.var_atten_dep=StringVar()
                self.var_atten_time=StringVar()
                self.var_atten_date=StringVar()
                self.var_atten_Attendance=StringVar()


                # Image 1

                img=Image.open("C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak1.jfif")
                img=img.resize((800,200),Image.ANTIALIAS)
                self.photoimg=ImageTk.PhotoImage(img)

                flbl=Label(self.root,image=self.photoimg)
                flbl.place(x=0,y=0,width=800,height=200) 
                # Image  2     

                img1=Image.open("C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak7.jfif")
                img1=img1.resize((800,200),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                flbl=Label(self.root,image=self.photoimg1)
                flbl.place(x=800,y=0,width=800,height=200)

                # Background Image
                img3=Image.open("C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\front.jpg")
                img3=img3.resize((1530,710),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=200,width=1530,height=710) 

                # title 
                title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
                title_lbl.place(x=0,y=0,width=1530,height=45)

                # Frame creation
                mai_frame=Frame(bg_img,bd=2)
                mai_frame.place(x=10,y=60,width=1500,height=650)

                # left frame
                left_frame=LabelFrame(mai_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
                left_frame.place(x=40,y=10,width=710,height=580)

                img_left=Image.open("C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak.jfif")
                img_left=img_left.resize((710,130),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                flbl=Label(left_frame,image=self.photoimg_left)
                flbl.place(x=20,y=0,width=710,height=130)   

                l_Inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
                l_Inside_frame.place(x=0,y=135,width=700,height=370)

                #****************************************** Label and entry*****************************************

                # Attendence id
                attendance_ID=Label(l_Inside_frame,text="Attendance_Id:",font=("times new roman",12,"bold"),bg="white")
                attendance_ID.grid(row=0,column=0,padx=10,pady=5,sticky=W)

                attendance_ID=ttk.Entry(l_Inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
                attendance_ID.grid(row=0,column=1,padx=10,pady=5,sticky=W)

                # Roll
                attendance_roll=Label(l_Inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
                attendance_roll.grid(row=0,column=2,padx=10,pady=5,sticky=W)

                attendance_roll=ttk.Entry(l_Inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
                attendance_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

                # Name
                attendance_Name=Label(l_Inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
                attendance_Name.grid(row=1,column=0,padx=10,pady=5,sticky=W)

                attendance_Name=ttk.Entry(l_Inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
                attendance_Name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

                # Department
                attendance_Dep=Label(l_Inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
                attendance_Dep.grid(row=1,column=2,padx=10,pady=5,sticky=W)

                attendance_Dep=ttk.Entry(l_Inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
                attendance_Dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

                # Time
                attendance_Time=Label(l_Inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
                attendance_Time.grid(row=2,column=0,padx=10,pady=5,sticky=W)

                attendance_Time=ttk.Entry(l_Inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
                attendance_Time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

                # Date
                attendance_Date=Label(l_Inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
                attendance_Date.grid(row=2,column=2,padx=10,pady=5,sticky=W)

                attendance_Date=ttk.Entry(l_Inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
                attendance_Date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

                # Attendence
                attendanceLabel=Label(l_Inside_frame,text="Attendance_Status:",font=("times new roman",12,"bold"),bg="white")
                attendanceLabel.grid(row=3,column=0)

                self.atten_status=ttk.Combobox(l_Inside_frame,width=20,textvariable=self.var_atten_Attendance,font="comicsansns 11 bold",state="readonly")
                self.atten_status["values"]=("Status","Present","Absent")
                self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)
                self.atten_status.current(0)

                # Button Frame
                btn_frame=Frame(l_Inside_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=50,y=250,width=715,height=40)

                save_btn=Button(btn_frame,text="Import CSV",command=self.importcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="yellow")
                save_btn.grid(row=0,column=0)

                delete_btn=Button(btn_frame,text="Export CSV",command=self.exportcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="yellow")
                delete_btn.grid(row=0,column=1)

        
                update_btn=Button(btn_frame,text="Reset",width=18,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="yellow")
                update_btn.grid(row=0,column=2)


                # right frame
                right_frame=LabelFrame(mai_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
                right_frame.place(x=750,y=10,width=710,height=580)

                table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
                table_frame.place(x=5,y=5,width=690,height=445)

                #  ******************************* ScrollBar Table ****************************************** 
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.AttendaceReportTable=ttk.Treeview(table_frame,column=("Id","Roll","Name","Department","time","date","Attendance"),
                xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)

                scroll_x.config(command=self.AttendaceReportTable.xview)
                scroll_y.config(command=self.AttendaceReportTable.yview)
                # Attendance Heading

                self.AttendaceReportTable.heading("Id",text="Attendance_id")
                self.AttendaceReportTable.heading("Roll",text="Roll")
                self.AttendaceReportTable.heading("Name",text="Name")
                self.AttendaceReportTable.heading("Department",text="Department")
                self.AttendaceReportTable.heading("time",text="Time")
                self.AttendaceReportTable.heading("date",text="Date")
                self.AttendaceReportTable.heading("Attendance",text="Attendance")

                self.AttendaceReportTable["show"]="headings"
                # Width giving in the table 

                self.AttendaceReportTable.column("Id",width=100)
                self.AttendaceReportTable.column("Roll",width=100)
                self.AttendaceReportTable.column("Name",width=100)
                self.AttendaceReportTable.column("Department",width=100)
                self.AttendaceReportTable.column("time",width=100)
                self.AttendaceReportTable.column("date",width=100)
                self.AttendaceReportTable.column("Attendance",width=100)

                self.AttendaceReportTable.pack(fill=BOTH,expand=1)

                self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)


# ********************************************** Fetch Data ****************************************
        def fetchdata(self,rows):
                self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
                for i in rows:
                        self.AttendaceReportTable.insert("",END,values=i)

# ********************************* Import CSV Data ********************************************************  


        def importcsv(self):
                global mydata
                mydata.clear()
                fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
                with open(fln) as myfile:
                        csvread=csv.reader(myfile,delimiter=",")
                        for i in csvread:
                                mydata.append(i)
                        self.fetchdata(mydata)


# ************************************************** Export CSV Data *********************************************
        def exportcsv(self):
                try:
                        if len(mydata)<1:
                                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                                return False
                        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
                        with open(fln,mode="w",newline="") as myfile:
                                exp_write=csv.writer(myfile,delimiter=",")
                                for i in mydata:
                                        exp_write.writerow(i)
                                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"Successfully")
                
                except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



# *********************************** Get Cursor **********************************
        def get_cursor(self,event=""):
                cursor_row=self.AttendaceReportTable.focus()
                content=self.AttendaceReportTable.item(cursor_row)
                rows=content['values']
                self.var_atten_id.set(rows[0])
                self.var_atten_roll.set(rows[1])
                self.var_atten_name.set(rows[2])
                self.var_atten_dep.set(rows[3])
                self.var_atten_time.set(rows[4])
                self.var_atten_date.set(rows[5])
                self.var_atten_Attendance.set(rows[6])

        def reset_data(self):
                self.var_atten_id.set("")
                self.var_atten_roll.set("")
                self.var_atten_name.set("")
                self.var_atten_dep.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_Attendance.set("")






if __name__=="__main__":
        root=Tk()
        obj=Attendence(root)
        root.mainloop()

















