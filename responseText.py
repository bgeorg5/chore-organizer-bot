def no_user():
    return "This user is not participating in our chore game :("


def mark_chore_a():
    return "@ the chore-bot with the the phrase 'mark' and the number of the chore you would like to mark (ex. 'mark 1' will mark the chore listed as 1 on the list as complete)."

def mark_err():
    return "You're missing something. \nTry 'mark chore' or 'mark #' where # is the number of the chore on your list. \nType 'mark chore' if you're not sure which one it is."


def unmark_chore_a():
    return "@ the chore-bot with the the phrase 'unmark' and the number of the chore you would like to unmark (ex. 'unmark 1' will unmark the chore listed as 1 on the list to show that it is incomplete)."

def unmark_err():
    return "You're missing something. \nTry 'unmark chore' or 'unmark #' where # is the number of the chore on your list. \nType 'unmark chore' if you're not sure which one it is."



def trade_err_a():
    return "You're missing something. \n type 'trade <#> with <discord name>' where # is the number of the task and <discord name> is the username of the person you would like to trade with.  \nType 'trade my task' if you're not sure which tasks are available."


def trade_err_b():
    return "Are you trying to trade with a chore?\n  type 'trade <#> with <discord name>' where # is the number of the task and <discord name> is the username of the person you would like to trade with. \nType 'trade my task' if you're not sure which tasks are available."


def steal_a():
    "Who would you like to steal from? \n @ chore bot with the phrase: \n'steal <victim's task number> from <victim's first name>' \n where <victim's task number> and <their task number> is the number of the task and <victim's first name> is the First name of the person you would like to steal from. (ex. 'steal 1 from Jamal')\n"




def help_msg():
    return " The following are command options: (case insensitive)  \n - 'my stats' \n - 'group stats' \n - 'unmark chore' \n - 'mark chore' (these marks your chore as either incomplete or complete) \n - 'my tasks' \n - 'group tasks' (shows you everyone's tasks) \n - 'trade' (Allows you to view Incoming/outgoing trade request and initiate a trade your task with another member of the group) \n -  'steal' (allows you to Steal someone else's task to obtain more points) \n -  'forfeit' (Allows you to forfeit your task to a given member of the group)"     

def laundry_schedule():
    return " The Laundry day schedule is as follows: \n - "

