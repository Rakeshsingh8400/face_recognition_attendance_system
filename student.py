from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x730+0+0")
        self.root.title("Student Details")

        # ********************************Variables************************

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_Id = StringVar()
        self.var_std_Name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mobile = StringVar()
        self.var_add = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(
            "C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak7.jfif")
        img = img.resize((550, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        flbl = Label(self.root, image=self.photoimg)
        flbl.place(x=0, y=0, width=550, height=130)

        img1 = Image.open(
            "C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak5.jfif")
        img1 = img1.resize((550, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        flbl = Label(self.root, image=self.photoimg1)
        flbl.place(x=500, y=0, width=550, height=130)

        img2 = Image.open(
            "C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak1.jfif")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        flbl = Label(self.root, image=self.photoimg2)
        flbl.place(x=1000, y=0, width=550, height=130)

        img3 = Image.open(
            "C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak12.jfif")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=800)

# label creating for the system
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Frame creation
        mai_frame = Frame(bg_img, bd=2)
        mai_frame.place(x=10, y=60, width=1500, height=650)

        # left frame
        left_frame = LabelFrame(mai_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=40, y=10, width=710, height=580)
        img_left = Image.open(
            "C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak10.jfif")
        img_left = img_left.resize((710, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        flbl = Label(left_frame, image=self.photoimg_left)
        flbl.place(x=20, y=0, width=710, height=130)

        # current course
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=20, y=140, width=700, height=135)

        # department
        dep_lbl = Label(current_course_frame, text="Department",
                        font=("times new roman", 12, "bold"), bg="white")
        dep_lbl.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science and Enginerring", "Mechanical Engineering",
                               "Civil Engineering", "Electrical Engineering", "Elctronics Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_lbl = Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")
        course_lbl.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_lbl = Label(current_course_frame, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_lbl.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select year", "2019-20",
                                "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        sem_lbl = Label(current_course_frame, text="Semester",
                        font=("times new roman", 12, "bold"), bg="white")
        sem_lbl.grid(row=1, column=2, padx=10, sticky=W)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "1st",
                               "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=20, y=270, width=700, height=400)

        # Student Id
        Sid_lbl = Label(class_student_frame, text="Student_Id:",
                        font=("times new roman", 12, "bold"), bg="white")
        Sid_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Sid_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_Id, width=20, font=(
            "times new roman", 12, "bold"))
        Sid_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        Sname_lbl = Label(class_student_frame, text="Student_Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        Sname_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Sname_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_Name, width=20, font=(
            "times new roman", 12, "bold"))
        Sname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division
        classDiv_lbl = Label(class_student_frame, text="Class_division:", font=(
            "times new roman", 12, "bold"), bg="white")
        classDiv_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        classDiv_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), state="readonly")
        classDiv_combo["values"] = ("G1", "G2", "G3")
        classDiv_combo.current(0)
        classDiv_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Student rollno
        rollNo_lbl = Label(class_student_frame, text="Roll_No:", font=(
            "times new roman", 12, "bold"), bg="white")
        rollNo_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Student gender
        gender_lbl = Label(class_student_frame, text="Gender:", font=(
            "times new roman", 12, "bold"), bg="white")
        gender_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # Student DOB
        dOb_lbl = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 12, "bold"), bg="white")
        dOb_lbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dOb_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        dOb_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Student Email
        email_lbl = Label(class_student_frame, text="email:", font=(
            "times new roman", 12, "bold"), bg="white")
        email_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Student phone
        phone_lbl = Label(class_student_frame, text="Mobile_No:", font=(
            "times new roman", 12, "bold"), bg="white")
        phone_lbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_mobile, width=20, font=(
            "times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Student Address
        add_lbl = Label(class_student_frame, text="Address:",
                        font=("times new roman", 12, "bold"), bg="white")
        add_lbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        add_entry = ttk.Entry(class_student_frame, textvariable=self.var_add, width=20, font=(
            "times new roman", 12, "bold"))
        add_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Student Teacher name
        teacher_lbl = Label(class_student_frame, text="Teacher_Name:", font=(
            "times new roman", 12, "bold"), bg="white")
        teacher_lbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

        # Button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=715, height=68)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=25, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        save_btn.grid(row=0, column=0)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=25, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        delete_btn.grid(row=0, column=1)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=25, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        reset_btn.grid(row=1, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.updaet_data, width=25, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        update_btn.grid(row=1, column=1)

        update_photo_btn = Button(btn_frame, text="Update Photo", width=25, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        update_photo_btn.grid(row=0, column=3)

        take_Photo_btn = Button(btn_frame, text="Photo Sample", command=self.generate_dataset, width=25, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        take_Photo_btn.grid(row=1, column=3)

        # right frame
        right_frame = LabelFrame(mai_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=710, height=580)
        img_right = Image.open(
            "C:\\Users\\rakes\\OneDrive\\Documents\\Face recognition of students in python\\rak8.jfif")
        img_right = img_right.resize((710, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        flbl = Label(right_frame, image=self.photoimg_right)
        flbl.place(x=20, y=0, width=710, height=130)

        """********************************* Search System***********************************"""
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=20, y=140, width=710, height=70)

        search_lbl = Label(search_frame, text="Search By:", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        search_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll_No", "Mobile_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=14, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        search_btn.grid(row=0, column=3, padx=4)

        sall_btn = Button(search_frame, text="Show All", width=12, font=(
            "times new roman", 12, "bold"), bg="blue", fg="yellow")
        sall_btn.grid(row=0, column=4, padx=4)

        # ***********************Table Frame*******************************

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=20, y=210, width=690, height=350)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "dev", "roll",
                                          "gender", "dob", "email", "mobile","add","teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_Id")
        self.student_table.heading("name", text="Student_Name")
        self.student_table.heading("dev", text="Class_Division")
        self.student_table.heading("roll", text="Roll_No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="email")
        self.student_table.heading("mobile", text="Mobile_No")
        self.student_table.heading("add", text="Address")
        self.student_table.heading("teacher", text="Teacher_Name")
        self.student_table.heading("photo", text="Photo")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("dev", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("mobile", width=100)
        self.student_table.column("add", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        # ***********************************Function  declaration *****************************

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_Name.get() == "" or self.var_std_Id.get() == "":
            messagebox.showerror(
                "Error", "All feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s, %s,%s,%s,%s,%s ,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),

                    self.var_std_Id.get(),
                    self.var_std_Name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),

                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_mobile.get(),
                    self.var_add.get(),

                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Successful", "\nStudent details has been added Successfully\n", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to :{str(es)}", parent=self.root)

        # **************************** Fetch Data ****************************************

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # **************************** Get Cursor **************************************
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_Id.set(data[4]),
        self.var_std_Name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_mobile.set(data[11]),
        self.var_add.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # ********************************* Update Function ********************************
    def updaet_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_Name.get() == "" or self.var_std_Id.get() == "":
            messagebox.showerror(
                "Error", "All feilds are required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to Update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="root", database="mydata")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,division=%s,Roll_no=%s,Gender=%s,DOB=%s,email=%s,mobile=%s,addressl=%s,teacher=%s,photosample=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),

                        self.var_semester.get(),
                        self.var_std_Id.get(),
                        self.var_std_Name.get(),

                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),

                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_mobile.get(),
                        
                        self.var_add.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                    ))

                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "success", "Student destails successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

        # ***************************** Delete *************************************

    def delete_data(self):
        if self.var_std_Id.get() == "":
            messagebox.showerror("Error", "Student Id Must Be Required")
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="root", database="mydata")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_std_Id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted deatials", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # ******************************** Reset Data ************************************

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select year"),
        self.var_semester.set("Select Semester"),
        self.var_std_Id.set(""),
        self.var_std_Name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_mobile.set(""),
        self.var_add.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


# ************************************Generate data set take photoimage Sample************************

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_Name.get() == "" or self.var_std_Id.get() == "":
            messagebox.showerror(
                "Error", "All feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,student_id=%s,Name=%s,division=%s,Roll_no=%s,Gender=%s,DOB=%s,email=%s,mobile=%s,addressl=%s,teacher=%s,photosample=%s where student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),

                    self.var_semester.get(),
                    self.var_std_Name.get(),
                    self.var_div.get(),

                    self.var_roll.get(),
                    self.var_gender.get(),

                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_mobile.get(),

                    self.var_add.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_Id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

# ***************************** Load Predefined data on face frontals from openCV *****************************************
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # Minimum Neighbor =5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, myframe = cap.read()
                    if face_cropped(myframe) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(myframe), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data sets complex!!!")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
