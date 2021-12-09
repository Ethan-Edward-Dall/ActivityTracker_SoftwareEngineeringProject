# Imports
from datetime import date
import tkinter as tk
import sqlite3 as sql
from tkinter.constants import END
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
        self.geometry("425x450")
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

        titleLbl = tk.Label(self, text="Settings")
        titleLbl.grid(column=1, row=0)

        submitBtn = tk.Button(self, text="Back", command=lambda: self.Create_Activity())
        submitBtn.grid(column=0, row=0)


    """Complete_Event page handles events that are manually completed and overdue
        - setOverdue(events) will take all events, check the due date, and if the 
            due date is before the current time is changed to overdue
        - end(activity) will take the selected event and move the event to the completed 
            list, will no longer display the event in the activity view"""
    # Complete_Event
    def Complete_Event(self):
        # Delete Frame
        self.deleteWidgets()

        titleLbl = tk.Label(self, text="Completed Events")
        titleLbl.grid(column=1, row=0)

        submitBtn = tk.Button(self, text="Back", command=lambda: self.Create_Activity())
        submitBtn.grid(column=0, row=0)

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
        masterFrame = tk.Frame(master=self).grid(column=0, row=0, sticky='nesw')
        activeFrame = tk.Frame(masterFrame).grid(column=0, row=1, columnspan=3, sticky='nesw')
        createActivityFrame = tk.Frame(masterFrame).grid(column=0, row=2, columnspan=3, sticky='nesw')

        # Scrollbar
        scrollbar = tk.Scrollbar(activeFrame)
        scrollbar.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='w')

        # Add to scrollList
        scrollList = tk.Listbox(activeFrame, yscrollcommand= scrollbar.set, height=10, width=70, )
        activeList= self.returnActivities(Sign_In.returnUser, Sign_In.returnPass)
        scrollList.insert(END, activeList)
        scrollList.grid(column=0, row=4, columnspan=5, rowspan=3, sticky='n')
        scrollbar.config(command= scrollList.yview)

        # Labels
        colLabelsLbl = tk.Label(activeFrame, text="Event Name | Start Time | End Time | Level of Importance | Desc.",
                                 font=("calibri", 10, 'bold'))
        colLabelsLbl.grid(column=0, row=3, columnspan=4, sticky='nesw')

        titleLbl = tk.Label(masterFrame, text="Activity Screen", font=("calibri", 10, 'bold'))
        titleLbl.grid(column=2, row=0)

        today = date.today()
        currDate = today.strftime("%B %d, %Y")
        dateLbl = tk.Label(masterFrame, text=currDate, font=("calibri", 10))
        dateLbl.grid(column=2, row=1, sticky='nesw')

        actActivitiesLbl = tk.Label(masterFrame, text="Active Activities", font=("calibri", 10, 'bold'))
        actActivitiesLbl.grid(column=2, row=2, sticky='nesw')

        createActivityLbl = tk.Label(masterFrame, text="Create New Activity", font=("calibri", 10, 'bold'))
        createActivityLbl.grid(column=2, row=7, sticky='nesw')

        # Buttons
        overdueBtn = tk.Button(masterFrame, text="Overdue\n Activities", command=lambda: self.Overdue_Event(), font=("calibri", 10, 'bold'))
        overdueBtn.grid(column=3, row=1, rowspan=2, sticky='nesw')

        completeBtn = tk.Button(masterFrame, text="Completed\n Activities", command=lambda: self.Complete_Event(), font=("calibri", 10, 'bold'))
        completeBtn.grid(column=0, row=1, columnspan=2, rowspan=2, sticky='w')

        alterSettingsBtn = tk.Button(masterFrame, text="Settings", command=lambda: self.Alter_Settings(), font=("calibri", 10, 'bold'))
        alterSettingsBtn.grid(column=4, row=1, rowspan=2, sticky='nesw')

        # Text Entry


        # Dropbox

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

        titleLbl = tk.Label(self, text="Overdue Activities")
        titleLbl.grid(column=1, row=0)

        submitBtn = tk.Button(self, text="Back", command=lambda: self.Create_Activity())
        submitBtn.grid(column=0, row=0)


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
class SQLDatabase:

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
            con = sql.connect("ActivityTracker.db")
            if(DB.checkTable(con, "UserInfo.db")):
                cur = con.cursor()
                try:
                    cur.execute('''SELECT UserID
                                FROM UserInfo
                                WHERE username = (?) AND password = (?)''', (username, password,))
                    ID = cur.fetchall[0]
                    con.commit()
                    con.close()
                    return ID
                except sql.OperationalError:
                    return -1
            else:
                return -1
        except sql.OperationalError:
            print("ERR: UserInfo database not found...")
            con.commit()
            con.close()
        

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
        


frm = UserInterface()
frm.mainloop()


