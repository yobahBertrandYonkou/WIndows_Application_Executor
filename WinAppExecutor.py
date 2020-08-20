import os

os.system("cls")

#main menu
menu = '''
--------------------------------------------------------------------------
\t\tWINDOWS APPLICATION EXECUTOR
--------------------------------------------------------------------------
WORD EDITORS\t\t MEDIA PLAYERS\t\t\t BROWSERS
- Notepad\t\t - Windows Media Player\t\t - Microsoft Edge
- WordPad\t\t - Gom Player\t\t\t - Google Chrome

\nMS APPLICATIONS\t\t COMMAND PROMPTS\t\t OTHERS
- Word\t\t\t - PowerShell\t\t\t - Camera
- Excel\t\t\t - Command Prompt\t\t - Mail
- PowerPoint\t\t - Git Bash\t\t\t - MS Store
- Access\t\t - MySQL\t\t\t - Python

\nACCESSORIES\t\t IDEs\t\t\t\t DISTRIBUTORS
- Calendar\t\t - Jupyther Notebook\t\t - Anaconda CLI
- Narrator\t\t - Visual Studio Code

\nVIDEO CONFERENCE APPs
- Zoom
- Skype
--------------------------------------------------------------------------
help or assist -> help text | menu -> main menu |  clear -> clear screen
--------------------------------------------------------------------------
'''
print(menu)
while True:
    print("[USER@WIN-APP-EX - ]$ ", end='')
    #gets query from user
    query = input()
    run_status = ('start' in query) or ('run' in query) or ('select' in query) or ('execute' in query) or ('pick' in query) or ('goto' in query) or ('go for' in query) or ('take' in query) or ('open' in query) or ('launch' in query)
#execution decisions based on query
    if query == '':
        continue
    elif('do not' in query or 'not ' in query or 'dont' in query or 'don\'t' in query):
        print("Ok")
#word editors
    elif(run_status and ('notepad' in query) or query == 'notepad'): 
        os.system('notepad')
    elif(run_status and ('wordpad' in query) or query == 'wordpad'):
        os.system('start wordpad')
#media players
    elif(run_status and ('windows media player' in query or 'wmplayer' in query) or query in ['wmplayer','windows media player']):
        os.system('start wmplayer')
    elif(run_status and ('gom player' in query) or query == 'gom player'):
        os.system('start gom')
#browsers
    elif(run_status and ('chrome' in query)  or query == 'chrome'):
        os.system('chrome')
    elif(run_status and ('microsoft edge' in query or 'msedge' in query) or query in ['edge', 'msedge', 'microsoft edge']):
        os.system('start msedge')
#command lines
    elif(run_status and ('cmd' in query or 'command prompt' in query) or query in ['cmd', 'command prompt']):
        os.system('start')    
    elif(run_status and ('powershell' in query)  or query == 'powershell'):
        os.system('start powershell')
    elif(run_status and ('gitbash' in query or 'git bash' in query)  or query in ['git bash', 'gitbash']):
        os.system('start gitbash')
    elif(run_status and ('mysql' in query) or query == 'mysql'):
        os.system('start mysqlcli')

#others
    elif(run_status and ('windows camera' in query or 'camera' in query) or query in ['windows camera', 'camera']):
        os.system('start wincamera')
    elif(run_status and ('windows mail' in query or 'mail' in query) or query in ['mail', 'windows mail']):
        os.system('start winmail')
    elif(run_status and ('python' in query) or query == 'python'):
        os.system('start python')
    elif(run_status and ('msstore' in query or 'ms store' in query or 'microsoft store' in query) or query in ['msstore', 'ms store', 'microsoft store']):
        os.system('start msstore')

#ms applications
    elif(run_status and ('msword' in query or 'ms word' in query  or 'microsoft word' in query) or query in ['word', 'msword', 'ms word', 'microsoft word']):
        os.system('start msword')
    elif(run_status and ('msexcel' in query or 'ms excel' in query  or 'microsoft excel' in query) or query in ['excel', 'msexcel', 'ms excel', 'microsoft excel']):
        os.system('start msexcel')
    elif(run_status and ('mspowerpoint' in query or 'ms powerpoint' in query  or 'microsoft powerpoint' in query) or query in ['powerpoint', 'ms powerpoint', 'ms powerpoint', 'microsoft powerpoint']):
        os.system('start mspowerpoint')
    elif(run_status and ('msaccess' in query or 'ms access' in query  or 'microsoft access' in query) or query in ['access', 'msaccess', 'ms access', 'microsoft access']):
        os.system('start msaccess')

#accessories
    elif(run_status and ('windows calendar' in query or 'calendar' in query) or query in ['windows calendar','calendar']):
        os.system('start wincalendar')
    elif(run_status and ('windows narrator' in query or 'narrator' in query) or query in ['windows narrator','narrator']):
        os.system('start winnarrator')

#ides
    elif(run_status and ('vscode' in query or 'code' in query or 'vsc' in query or 'visual studio code' in query) or query in ['vsc', 'vscode', 'code', 'visual studio code']):
        os.system('code')
    elif(run_status and ('jupyter notebook' in query) or query == 'jupyter notebook'):
        os.system('start jupyter notebook')

#distributors
    elif(run_status and ('anaconda cli' in query) or query in ['anaconda', 'anaconda cli']):
        os.system('start anacondacli')
    
    
#video conference
    elif(run_status and ('skype' in query) or query == 'skype'):
        os.system('skype')    
    elif(run_status and ('zoom' in query) or query == 'zoom'):
        os.system('start zoom')


#program enhancements
    elif query == 'clear' or query == 'cls' or 'clear' in query:
        os.system('cls')
    
    elif query == 'menu' or 'menu' in query:
        os.system("cls")
        print(menu)    
    elif 'help' in query or 'assist' in query:
        os.system("cls")
        print("\t\tHELP TEXT")
        print("\nExecute program:\nSELECT, GOTO, PICK, CHOOSE, TAKE, GO FOR, RUN, EXECUTE, OPEN")
        print("Followed by program name")
        print("\nUser can enter only program name to launch program\nFor exameple:\n\"notepad\" launches notepad")
        print("\nFor example: \n\"please SELECT windows media player\" executes Windows Media Player\n\"can you RUN calendar\" executes calendar")
        print("\nExit from Win-App-Ex:\nSTOP, EXIT, TERMINATE, GET OUT, CLOSE, END, FINISH\n")
        print('help or assist -> help text | menu -> supported apps |  clear -> clear screen\n')

    elif('exit' in query or 'stop' in query or 'terminate' in query or 'finish' in query or 'end ' in query or 'close' in query):
        print("Thank you. Bye!!! :)")
        break

    else:
        print("{}: command not found".format(query))
