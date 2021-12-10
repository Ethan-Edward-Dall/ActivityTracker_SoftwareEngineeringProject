# Imports
from datetime import date
import tkinter as tk
import sqlite3 as sql
from tkinter.constants import END, HORIZONTAL, Y

import matplotlib

from Control.Sign_In import Authentication
from Control.Alter_Settings import Alter_Settings
from Control.Complete_Event import Complete_Event
from Control.Create_Activity import Create_Activity
from Control.Database import Database as DB
from Control.LineGraph import LineGraph
from Control.Sign_In import Sign_In

"""This is the Userinterface class which will handle all activity transitions
    The activities being: Log-in, Create Event, Complete Activity, Alter Settings,
    and View Line-Graph; Each will need their own subclasses and methods to occupy them"""
# This is a public class
class UserInterface(tk.Tk, Sign_In, LineGraph, DB, Create_Activity, Complete_Event, Alter_Settings):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Activity Tracker")
        self.geometry("450x350")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        SQLDatabase()
        self.Log_In()
    
    
    """Alter_Settings page is to adjust volume and/or toggle the volume
        - AdjustVolume() changes the value of the application from 1 to 100
        - toggleSound() will mute the sound of the application all together"""
    # Alter_Settings method
    def Alter_Settings(self):
        # Delete Frame
        self.deleteWidgets()

        # Labels
        self.titleLbl = tk.Label(self, text="Settings", font=('calabri', 15, "bold"))
        self.titleLbl.grid(column=1, row=0, sticky='w')

        self.notifVolLbl = tk.Label(self, text="Notification Volume", font=('calabri', 10, "bold"))
        self.notifVolLbl.grid(column=1, row=2, stick='w')

        self.notifSoundLbl = tk.Label(self, text="Notification Sound", font=('calabri', 10, "bold"))
        self.notifSoundLbl.grid(column=1, row=3, sticky='w')

        self.fileLocationLbl = tk.Label(self, text="File location and installation name", font=('calabri', 10), bd=4)
        self.fileLocationLbl.grid(column=1, row=1, sticky='w')

        # Buttons
        self.submitBtn = tk.Button(self, text="Back", command=lambda: self.Create_Activity())
        self.submitBtn.grid(column=0, row=0, sticky='nesw')

        self.onBtn = tk.Button(self, text="On", command=lambda: self.toggle(), relief="raised")
        self.onBtn.grid(column=2, row=3, sticky='nesw')

        self.offBtn = tk.Button(self, text="Off", command=lambda: self.toggle(), relief="sunken")
        self.offBtn.grid(column=3, row=3, sticky='nesw')

        # Scale
        self.volScale = tk.Scale(self, to=100, orient=HORIZONTAL)
        self.volScale.grid(column=2, row=2, columnspan=2, sticky='nesw')

    def toggle(self):
        if self.onBtn.config('relief')[-1] == "sunken":
            self.onBtn.config(relief="raised")
        else:
            self.onBtn.config(relief="sunken")
        if self.offBtn.config('relief')[-1] == "sunken":
            self.offBtn.config(relief="raised")
        else:
            self.offBtn.config(relief="sunken")


    """Complete_Event page handles events that are manually completed and overdue
        - setOverdue(events) will take all events, check the due date, and if the 
            due date is before the current time is changed to overdue
        - end(activity) will take the selected event and move the event to the completed 
            list, will no longer display the event in the activity view"""
    # Complete_Event
    def Complete_Event(self):
        # Delete Frame
        self.deleteWidgets()

        # Frames
        self.masterFrame = tk.Frame(master=self).grid(column=0, row=0, sticky='nesw')
        self.activeFrame = tk.Frame(self.masterFrame).grid(column=1, row=1, columnspan=3, sticky='nesw')

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.activeFrame)
        self.scrollbar.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='w')

        # Add to scrollList
        self.scrollList = tk.Listbox(self.activeFrame, yscrollcommand= self.scrollbar.set, height=10, width=60)
        self.activeList= self.returnActivities(Sign_In.returnUser, Sign_In.returnPass)
        self.scrollList.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='w', padx=20)
        self.scrollbar.config(command= self.scrollList.yview)

        # Labels
        self.colLabelsLbl = tk.Label(self.activeFrame, text="Event Name | Start Time | End Time | Level of Importance | Desc.",
                                 font=("calibri", 10, 'bold'))
        self.colLabelsLbl.grid(column=0, row=3, columnspan=5, sticky='w', padx=20)

        self.titleLbl = tk.Label(self, text="Completed Events", font=('calabri', 15, 'bold'))
        self.titleLbl.grid(column=1, row=0, stick='nesw')

        self.errLbl = tk.Label(self.masterFrame, text="", font=("calibri", 10, 'bold'))
        self.errLbl.grid(column=3, row=7, columnspan=2, sticky='nesw')

        # Buttons
        self.submitBtn = tk.Button(self.activeFrame, text="Back", command=lambda: self.Create_Activity())
        self.submitBtn.grid(column=0, row=0, sticky='nesw')

        # Line Graph
        self.fig = matplotlib.Figure(figsize = (5,5), dpi = 100)
        self.plot = self.fig.add_subplot(111)
        self.plot.plot(Y)

        self.canvas = matplotlib.FigureCanvasTkAgg(self.fig, master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=4, column=1)

    """Create_Activity page will ask the user to put in a value for each variable,
            which will be proceeded with a explination of an accepted value.
        - nameEvent() will change the blank value of the event name to what the user inputs
        - setStart() will change the blank value of the start time to what the user inputs
        - setEnd() will change the blank value of the end time to what the user inputs
        - setPriority() will change the blank value of the priority value to one of the 
            three predetermined values
        - AddNote() will change the blank value of the note variable if the value is not 
            blank, this is optional"""

    """LineGraph page will display the progress of the user by counting the amount of 
            completed events in every given day to display as points on the graph. The X-axis
            is the days and the Y-axis is the amount completed.
        - viewLineGraph() will display a line graph with the current total values of the 
            completed list of events and the days they were completed."""
    # Create_Activity
    def Create_Activity(self):
        # Delete Frame
        self.deleteWidgets()

        # Frames
        self.masterFrame = tk.Frame(master=self).grid(column=0, row=0, sticky='nesw')
        self.activeFrame = tk.Frame(self.masterFrame).grid(column=0, row=1, columnspan=3, sticky='nesw')
        self.createActivityFrame = tk.Frame(self.masterFrame).grid(column=0, row=2, columnspan=3, sticky='nesw')

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.activeFrame)
        self.scrollbar.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='w')

        # Add to scrollList
        self.scrollList = tk.Listbox(self.activeFrame, yscrollcommand= self.scrollbar.set, height=10, width=60)
        self.activeList= self.returnActivities(Sign_In.returnUser, Sign_In.returnPass)
        self.scrollList.insert(END, self.activeList)
        self.scrollList.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='w', padx=20)
        self.scrollbar.config(command= self.scrollList.yview)

        # Labels
        self.colLabelsLbl = tk.Label(self.activeFrame, text="Event Name | Start Time | End Time | Level of Importance | Desc.",
                                 font=("calibri", 10, 'bold'))
        self.colLabelsLbl.grid(column=0, row=3, columnspan=5, sticky='w', padx=20)

        self.titleLbl = tk.Label(self.masterFrame, text="Activity Screen", font=("calibri", 15, 'bold'))
        self.titleLbl.grid(column=2, row=0)

        today = date.today()
        currDate = today.strftime("%B %d, %Y")
        self.dateLbl = tk.Label(self.masterFrame, text=currDate, font=("calibri", 10))
        self.dateLbl.grid(column=2, row=1, sticky='nesw')

        self.actActivitiesLbl = tk.Label(self.masterFrame, text="Active Activities", font=("calibri", 10, 'bold'))
        self.actActivitiesLbl.grid(column=2, row=2, sticky='nesw')

        self.createActivityLbl = tk.Label(self.masterFrame, text="Create New Activity", font=("calibri", 10, 'bold'))
        self.createActivityLbl.grid(column=2, row=7, sticky='nesw')

        self.errLbl = tk.Label(self.masterFrame, text="", font=("calibri", 10, 'bold'))
        self.errLbl.grid(column=3, row=7, columnspan=2, sticky='nesw')

        # Text Entry
        self.eventNameTxe = tk.Entry(self.createActivityFrame, bd=2, textvariable="eventName", font=("calibri", 10))
        self.eventNameTxe.delete(0, END)
        self.eventNameTxe.insert(END, "[Event Name]")
        self.eventNameTxe.grid(column=0, row=8, sticky='nesw')

        self.startTimeTxe = tk.Entry(self.createActivityFrame, bd=2, textvariable="startTime", font=("calibri", 10))
        self.startTimeTxe.delete(0, END)
        self.startTimeTxe.insert(END, "[Start Time]")
        self.startTimeTxe.grid(column=2, row=8, sticky='nesw')

        self.endTimeTxe = tk.Entry(self.createActivityFrame, bd=2, textvariable="endTime", font=("calibri", 10))
        self.endTimeTxe.delete(0, END)
        self.endTimeTxe.insert(END, "[End Time]")
        self.endTimeTxe.grid(column=3, row=8, sticky='nesw')

        self.descTxe = tk.Entry(self.createActivityFrame, bd=2, textvariable="desc", font=("calibri", 10))
        self.descTxe.delete(0, END)
        self.descTxe.insert(END, "[Description (optional)]")
        self.descTxe.grid(column=0, row=9, columnspan=4, rowspan=2, sticky='nesw')

        # Options Menu
        options = ["Low", "Average", "High"]

        self.impLvl = tk.StringVar()
        self.impLvl.set("Low")
        self.impDrop = tk.OptionMenu(self.createActivityFrame, self.impLvl, *options)
        self.impDrop.grid(column=4, row=8, sticky='nesw')

        # Buttons
        self.overdueBtn = tk.Button(self.masterFrame, text="Overdue\n Activities", command=lambda: self.Overdue_Event(), font=("calibri", 10, 'bold'))
        self.overdueBtn.grid(column=3, row=1, rowspan=2, sticky='nesw')

        self.completeBtn = tk.Button(self.masterFrame, text="Completed\n Activities", command=lambda: self.Complete_Event(), font=("calibri", 10, 'bold'))
        self.completeBtn.grid(column=0, row=1, columnspan=2, rowspan=2, sticky='w')

        self.alterSettingsBtn = tk.Button(self.masterFrame, text="Settings", command=lambda: self.Alter_Settings(), font=("calibri", 10, 'bold'))
        self.alterSettingsBtn.grid(column=4, row=1, rowspan=2, sticky='nesw')

        self.createEvent = tk.Button(self.createActivityFrame, text="Create Event", 
                                command=lambda: self.addNewEvent(), 
                                font=("calibri", 10, 'bold'))
        self.createEvent.grid(column=4, row=9, sticky='nesw')

        self.endEvent = tk.Button(self.activeFrame, text="End Event", command=lambda: self.endSelectedEvent(), font=("calibri", 10, 'bold'))
        self.endEvent.grid(column=4, row=4, rowspan=3, sticky='nes')

    # Delete Selected Event
    def endSelectedEvent(self):
        selected_checkboxs = self.scrollList.curselection()
        start = self.scrollList.size()
        for selected_checkbox in selected_checkboxs[::-1]:
            self.scrollList.delete(selected_checkbox)
        end = self.scrollList.size()
        if(start == end):
            self.errLbl.configure(text="Error: No Event Selected", foreground='red')
        else:
            self.errLbl.configure(text="")

    # Adds the created event into Active Activities
    def addNewEvent(self):
        eventName = self.eventNameTxe.get()
        startTime = self.startTimeTxe.get()
        endTime = self.endTimeTxe.get()
        lvlImp = self.impLvl.get()
        description = self.descTxe.get()
        if(eventName != "[Event Name]" and endTime != "[End Time]"):
            if(startTime == "[Start Time]"):
                startTime = "-----"
            if(description == "[Description (optional)]"):
                description = "-----"
            newActivity = [str(eventName), str(startTime), str(endTime), str(lvlImp), str(description)]
            #SQLDatabase.addActivities(self, Sign_In.returnUser, Sign_In.returnPass, newActivity)
            self.scrollList.insert(END, ("   |   ".join(newActivity)))
        else:
            self.errLbl.configure(text="Change Event Name or End Time", foreground='red')
        
        self.eventNameTxe.delete(0, END)
        self.eventNameTxe.insert(0, "[Event Name]")
        self.startTimeTxe.delete(0, END)
        self.startTimeTxe.insert(0, "[Start Time]")
        self.endTimeTxe.delete(0, END)
        self.endTimeTxe.insert(0, "[End Time]")
        self.impLvl.set("Low")
        self.descTxe.delete(0, END)
        self.descTxe.insert(0, "[Description (optional)]")


    # Add to ListView
    def appendList(scrollList, event):
        scrollList.insert(END, event)

    # Return three lists of all the activities based on the userID
    def returnActivities(self, username, password):
        userID = SQLDatabase.returnUserID(self, username, password)
        if(userID != -1):
            active = SQLDatabase.findActivities(self, userID)
            return active
        else:
            return [], [], []

    # Overdue_Event
    def Overdue_Event(self):
        # Delete Frame
        self.deleteWidgets()

        # Frames
        self.masterFrame = tk.Frame(master=self).grid(column=0, row=0, sticky='nesw')
        self.activeFrame = tk.Frame(self.masterFrame).grid(column=0, row=1, columnspan=3, sticky='nesw')

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.activeFrame)
        self.scrollbar.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='w')

        # Add to scrollList
        self.scrollList = tk.Listbox(self.activeFrame, yscrollcommand= self.scrollbar.set, height=10, width=60)
        self.activeList= self.returnActivities(Sign_In.returnUser, Sign_In.returnPass)
        self.scrollList.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='w', padx=20)
        self.scrollbar.config(command= self.scrollList.yview)

        # Labels
        self.colLabelsLbl = tk.Label(self.activeFrame, text="Event Name | Start Time | End Time | Level of Importance | Desc.",
                                 font=("calibri", 10, 'bold'))
        self.colLabelsLbl.grid(column=0, row=3, columnspan=5, sticky='w', padx=20)

        self.titleLbl = tk.Label(self.activeFrame, text="Overdue Activities", font=("calibri", 15, 'bold'))
        self.titleLbl.grid(column=1, row=0, sticky='w')

        self.errLbl = tk.Label(self.masterFrame, text="", font=("calibri", 10, 'bold'))
        self.errLbl.grid(column=3, row=7, columnspan=2, sticky='nesw')

        # Buttons
        self.submitBtn = tk.Button(self.activeFrame, text="Back", command=lambda: self.Create_Activity())
        self.submitBtn.grid(column=0, row=0, sticky='nesw')

        self.endEvent = tk.Button(self.activeFrame, text="End Event", command=lambda: self.endSelectedEvent(), font=("calibri", 10, 'bold'))
        self.endEvent.grid(column=4, row=4, rowspan=3, sticky='nes')


    """Log_In page is the first page to be displayed when the application opens, and will 
            confirm the log-in information the user provides. It also has the option to 
            add new users with their given information.
        - login(username, password) will take the username and password inputed 
            by the user and assign them variables for future methods
        - signup(username, password) will take the information given by the user and put 
            a new addition to the database table
        - check(username, password) will authenticate the information that was put in 
            from the saved values and will result in one of two ways:
            i. All information has been found and confirmed == access granted to the activity 
                page of that user
            ii. Some/None of the informaiton can be confirmed == Display error message 'invalid 
                password or username try again or create a new account' and return to the 
                default state of the log_in page"""
    # Log_In
    def Log_In(self):
        # Delete Frame
        self.deleteWidgets()

        # Labels
        self.userLbl = tk.Label(self, text="Username ", font=("calibri", 10, 'bold'))
        self.userLbl.grid(column=0, row=0, sticky='nesw')
        self.passLbl = tk.Label(self, text="Password ", font=("calibri", 10, 'bold'))
        self.passLbl.grid(column=0, row=2, sticky='nesw')
        self.qLbl = tk.Label(self, text="New User? ")
        self.qLbl.grid(column=0, row=5, sticky='nesw')
        self.errLbl = tk.Label(self, text="Error: ", font=("calibri", 10, 'bold'), foreground='white')
        self.errLbl.grid(column=0, row=6, rowspan=3, sticky='nesw')

        # Text Entry
        username = ""
        password = ""

        self.userTxe = tk.Entry(self, bd=2, textvariable=username)
        self.userTxe.insert(0, "Ex: John Doe")
        self.userTxe.grid(column=0, row=1, columnspan=3, pady=5)
        self.passTxe = tk.Entry(self, bd=2, textvariable=password, show='*')
        self.passTxe.grid(column=0, row=3, columnspan=3, pady=5)

        # Buttons
        self.submitBtn = tk.Button(self, text="Sign In", command= lambda: self.checkUserInfo(),
                                 width=16, font=("calibri", 10, 'bold'), foreground='white', background='black')
        self.submitBtn.grid(column=0, row=4, columnspan=2, sticky='n')
        self.newUserBtn = tk.Button(self, text="Sign Up", command=lambda: self.Create_User(), 
                                bd=0, font=("calibri", 10, 'bold', 'underline'), pady=10)
        self.newUserBtn.grid(column=1, row=5, sticky='nw')

    def checkUserInfo(self):
        username = self.userTxe.get()
        password = self.passTxe.get()
        if(Sign_In.login(username,password) and DB.findUser(username, password)):
            self.deleteWidgets()
            self.Create_Activity()
        else:
            self.errLbl.configure(text="Unknown Username/Password | New?", foreground='red')



    # Create_User
    def Create_User(self):
        # Delete Frame
        self.deleteWidgets()


        # Labels
        self.userLbl = tk.Label(self, text="Username ", font=("calibri", 10, 'bold'))
        self.userLbl.grid(column=0, row=1, sticky='w')
        self.passLbl = tk.Label(self, text="Password ", font=("calibri", 10, 'bold'))
        self.passLbl.grid(column=0, row=3, sticky='w')
        self.confirmLbl = tk.Label(self, text="Confirm Password ", font=("calibri", 10, 'bold'))
        self.confirmLbl.grid(column=0, row= 5, sticky='w')
        self.errLbl = tk.Label(self, text="", font=("calibri", 10, 'bold'))
        self.errLbl.grid(column=0, row=7, sticky='nesw')

        # Text Entry
        username = ""
        password = ""

        self.userTxe = tk.Entry(self, bd=2, textvariable=username)
        self.userTxe.grid(column=0, row=2, columnspan=2, pady=5)
        self.passTxe = tk.Entry(self, bd=2, textvariable=password)
        self.passTxe.insert(0, "Up to 30 Characters")
        self.passTxe.grid(column=0, row=4, columnspan=2, pady=5)
        self.confirmPassTxe = tk.Entry(self, bd=2)
        self.confirmPassTxe.grid(column=0, row=6, columnspan=2, pady=5)
        self.confirmPassTxe.insert(0, "Up to 30 Characters")

        # Buttons
        self.createBtn = tk.Button(self, text="Create", command=lambda: 
                                 self.checkNewUserInfo(self.userTxe.get(), self.passTxe.get(), self.confirmPassTxe.get()),
                                 width=16, font=("calibri", 10, 'bold'), foreground='white', background='black')
        self.createBtn.grid(column=0, row=7)
        self.backBtn = tk.Button(self, text="Back", command=lambda: self.Log_In(),
                                 width=16, font=("calibri", 10, 'bold'))
        self.backBtn.grid(column=0, row=0)
        
    def checkNewUserInfo(self, username, passOne, passTwo):
        if(passOne == passTwo and len(passOne) < 30):
            DB.addUser(self, username, passOne)
            self.Create_Activity()
        else:
            self.errLbl.configure(text="Passwords do not match", foreground='red')

    # Deletes all the widgets currently in Frame
    def deleteWidgets(self):
        for widgets in tk.Frame.winfo_children(self):
                widgets.destroy()


    # Create SQL Database
class SQLDatabase(tk.Tk):

    def __init__(self):
        self.con = sql.connect('ActivityTracker.db')
        self.checkTablesExists(self.con)

    def checkTablesExists(self, con):    
        # Check/Create Tables
        try:
            if(DB.checkTable(con,"UserInfo.db")):
                self.loginUser(con, Authentication.getUser, Authentication.getPassword)
            else:
                return False
        except sql.OperationalError:
            cur = con.cursor()
            try:
                cur.execute('''CREATE TABLE UserInfo
                            (userID int, username text, password text)''')
            except sql.OperationalError:
                pass

    def returnUserID(self, username, password):
        try:
            if(DB.checkTable(DB.getConnection(self), "UserInfo.db")):
                cur = DB.getConnection(self).cursor()
                try:
                    cur.execute("""SELECT UserID
                                FROM UserInfo
                                WHERE username = (?) AND password = (?)""", (str(username), str(password),))
                    ID = cur.fetchall[0]
                    DB.getConnection(self).commit()
                    DB.getConnection(self).close()
                    return ID
                except sql.OperationalError:
                    return -1
            else:
                return -1
        except sql.OperationalError:
            print("ERR: UserInfo database not found...")
            cur = DB.getConnection(self).cursor()
            try:
                    cur.execute("""SELECT UserID
                                FROM UserInfo
                                WHERE username = (?) AND password = (?)""", (str(username), str(password),))
                    ID = cur.fetchall
                    DB.getConnection(self).commit()
                    DB.getConnection(self).close()
                    return ID
            except sql.OperationalError:
                print("ERR: No ID")
                DB.getConnection(self).commit()
                DB.getConnection(self).close()
                return -1
        

    def loginUser(self, con, user, passW):
        if(DB.checkUserLogin(con, user, passW)):
            return True
        else:
            return False

    def findActivities(self, userID):
        # Check/Create Tables
        con = sql.connect("ActivityTracker.db")
        try:
            if(DB.checkTable(con,"UserActivities.db")):
                return DB.usersActivities(userID)
            else:
                return [-1]
        except sql.OperationalError:
            cur = con.cursor()
            try:
                cur.execute('''CREATE TABLE UserActivities
                            (userID int, ActivityName text, StartTime text, EndTime text, Importance text, Desc text, status text)''')
            except sql.OperationalError:
                pass

    def addActivities(self, username, password, list):
        userID = self.returnUserID(username, password)

        # Check/Create Tables
        con = sql.connect("ActivityTracker.db")
        try:
            if(DB.checkTable(con,"UserActivities.db")):
                name = list[0]
                start = list[1]
                end = list[2]
                importance = list[3]
                description = list[4]
                status = DB.getStatus(end)
                cur = con.cursor()
                try:
                    cur.execute("""
                                INSERT INTO UserActivities
                                VALUES (?, ?, ?, ?, ?, ?, ?)""", (userID, name, start, end, importance, description, status))
                except sql.OperationalError:
                    print("ERROR: Values incompatable")
            else:
                return [-1]
        except sql.OperationalError:
            cur = con.cursor()
            try:
                cur.execute('''CREATE TABLE UserActivities
                            (userID int, ActivityName text, StartTime text, EndTime text, Importance text, Desc text, status text)''')
            except sql.OperationalError:
                pass
        


frm = UserInterface()
frm.mainloop()


