


"""This is the Userinterface class which will handle all activity transitions
    The activities being: Log-in, Create Event, Complete Activity, Alter Settings,
    and View Line-Graph; Each will need their own subclasses and methods to occupy them"""
# This is a public class
class UserInterface:

    """Alter_Settings page is to adjust volume and/or toggle the volume
        - AdjustVolume() changes the value of the application from 1 to 100
        - toggleSound() will mute the sound of the application all together"""
    # Alter_Settings method
    pass

    """Complete_Activity page handles events that are manually completed and overdue
        - setOverdue(events) will take all events, check the due date, and if the 
            due date is before the current time is changed to overdue
        - end(activity) will take the selected event and move the event to the completed 
            list, will no longer display the event in the activity view"""
    # Complete_Activity
    pass

    """Create_Activity page will ask the user to put in a value for each variable,
            which will be proceeded with a explination of an accepted value.
        - nameEvent() will change the blank value of the event name to what the user inputs
        - setStart() will change the blank value of the start time to what the user inputs
        - setEnd() will change the blank value of the end time to what the user inputs
        - setPriority() will change the blank value of the priority value to one of the 
            three predetermined values
        - AddNote() will change the blank value of the note variable if the value is not 
            blank, this is optional"""
    # Create_Activity
    pass

    """LineGraph page will display the progress of the user by counting the amount of 
            completed events in every given day to display as points on the graph. The X-axis
            is the days and the Y-axis is the amount completed.
        - viewLineGraph() will display a line graph with the current total values of the 
            completed list of events and the days they were completed."""
    # LineGraph
    pass

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
    pass

