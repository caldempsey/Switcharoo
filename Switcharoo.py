print("Switcharoo!")
print("*" * 35)
print("")
print("")
print("Initializing engine.")
print("")

# Write Globs#

while True:
    try:
        print("Writing global arguments")
        switch_model = []
        switch_ports = []
        switch_type = []
        switch_uplink = []
        uplink_type = []
        bad_switch_model = []
        bad_switch_ports = []
        bad_switch_type = []
        bad_uplink_type = []
        bad_switch_uplink = []
        engine_error = 0
        stackname = ("")
        flag = True
        switchcount = 0

        def flagchange():
            global flagchange
            global flag
            flag = not flag

        def setglobalvar():
            global switch_model
            global file
            global switch_uplink
            global switch_type
            global uplink_type
            global switchcount
            global stackname
            global bad_switch_model
            global bad_switch_ports
            global bad_switch_type
            global bad_switch_uplink
            global bad_uplink_type
            global bad_switchcount
            global stackname

        setglobalvar()
        flagchange()
        print("Success")
        break
    except:
        print(
            "Error writing global arguments. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1
        break

    #Import modules required for the program to initialize#
    ##Also creates clearscreen() function##

    #SYS MODULE#

while True:
    try:
        print("")
        print("Attempting import sys.py")
        import sys

        print("System module successfully imported")
        break
    except ImportError:
        print(
            "Cannot open system module. Please ensure 'sys' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/sys.html")
        engine_error = 1
        break
    #COLORCONS

    #LINECACHE MODULE#
while True:
    try:
        print("")
        print("Attempting import linecache.py")
        import linecache

        print("Linecache module successfully imported")
        break
    except ImportError:
        print(
            "Cannot open linecache module. Please ensure 'linecache' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/linecache.html")
        engine_error = 1
        break


        #OS MODULE#

while True:
    try:
        print("")
        print("Attempting import os.py")
        import os

        print("OS module successfully imported")
        print("Writing clear-screen")

        #CLEARSCREEN FUNCTION#

        def clearscreen():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        break
    except:
        print(
            "Cannot open OS module or write clearscreen from OS module. Please ensure 'os' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/os.html")
        engine_error = 1
        break

while True:
    try:
        print("")
        print("Attempting import shutil.py")
        import shutil
        break

    except:
        print("Cannot open shutil module. Please ensure 'shutil' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/shutil.html")
        engine_error = 1
        break

        #REGEX MODULE#

while True:
    try:
        print("Attempting import re.py")
        import re

        print("Regular expression module successfully imported")
        break
    except ImportError:
        print(
            "Cannot import re.py(regular expression module). Please ensure 're' module is correctly installed on your system. For more information about this module please visit http://docs.python.org/2/library/re.html")
        engine_error = 1
        break










#System#

#SYS_MOUNT#

while True:
    try:
        print("")
        print("Developing sys_mount sub-module")

        def sys_mount():
            while True:
                try:
                    clearscreen()
                    print("Switcharoo!: Mount Menu")
                    print()
                    print("Enter switch-name to mount i.e. 'stack1.txt' in stacks directory")
                    print("No input will return you to the main menu")
                    print("")
                    global switchname
                    global switchcount
                    filename = input("> ")
                    if filename == (""):
                        ui()
                    regexp = re.compile(r"^(.+)\s*((24)|(48))+\s*((A)|(B)|(C)|(D)|]+)\s*([0-9]+)+\s*((A)|(B)|(C)|(D)|]+)$", re.M)
                    global file
                    file = open(os.path.join('./Stacks/', filename))
                    fail = False
                    switchcount = 0
                    failed_switches = 0
                    linepos = 0
                    goodswitch_position = []
                    badswitch_position = []

                    for line in file.readlines():
                        result = regexp.search(line)

                        if result == None:
                            if "##" in line:
                                linepos += 1 #int linepos
                                pass
                            else:
                                fail = True
                                badswitch_position.append(linepos)
                                split_line = line.split()
                                bad_switch_model.append(split_line[0])
                                bad_switch_ports.append(split_line[1])
                                bad_switch_type.append(split_line[2])
                                bad_switch_uplink.append(split_line[3])
                                bad_uplink_type.append(split_line[4])
                                failed_switches = (failed_switches + 1)
                                linepos += 1

                        else:
                            goodswitch_position.append(linepos)
                            split_line = line.split()
                            switch_model.append(split_line[0])
                            switch_ports.append(split_line[1])
                            switch_type.append(split_line[2])
                            switch_uplink.append(split_line[3])
                            uplink_type.append(split_line[4])
                            switchcount += 1 #For valid switches only
                            linepos += 1 #Switch-count was creating false index's i.e. bad switch on 1 and not 2

                    clearscreen()
                    print("Switcharoo!: Mount Menu")
                    print()
                    print()

                    if switchcount == 0:
                        print("Error. This files formatting is incompatible with this system.")
                        print("")
                        print("Please ensure all of your data is formatted in the correct syntax")
                        print("")
                        print("Pressing enter will terminate the program.")
                        input()
                        sys.exit()

                    #PARSE
                    global switch_type
                    parsed_switch_type = []
                    global uplink_type
                    parsed_uplink_type = []


                    for parse_switch_type in switch_type:
                        parse_switch_type = re.sub(r"(A)", "GigabitEthernet", parse_switch_type)
                        parse_switch_type = re.sub(r"(B)", "Ten-GigabitEthernet", parse_switch_type)
                        parse_switch_type = re.sub(r"(C)", "40-GigabitEthernet", parse_switch_type)
                        parse_switch_type = re.sub(r"(D)", "100-GigabitEthernet", parse_switch_type)
                        parsed_switch_type.append(parse_switch_type)
                    switch_type = parsed_switch_type

                    for parse_uplink_type in uplink_type:
                        parse_uplink_type = re.sub(r"(A)", "GigabitEthernet", parse_uplink_type)
                        parse_uplink_type = re.sub(r"(B)", "Ten-GigabitEthernet", parse_uplink_type)
                        parse_uplink_type = re.sub(r"(C)", "40-GigabitEthernet", parse_uplink_type)
                        parse_uplink_type = re.sub(r"(D)", "100-GigabitEthernet", parse_uplink_type)
                        parsed_uplink_type.append(parse_uplink_type)
                    uplink_type = parsed_uplink_type


                    print("VALID?" + " " + "MODEL" + "  " + "PORTS" + "  " + "TYPE({#}GigaBits)" + "  " + "UPLINK"+ "  " + "UPLINK TYPE")
                    print("")
                    for i in range(len((goodswitch_position))):
                        print("VALID" + "  " + switch_model[i] + "  " + switch_ports[i] + "  " + switch_type[i] + "  " +
                              switch_uplink[i]+"  "+uplink_type[i])
                    for i in range(len((badswitch_position))):
                        print("INVALID" + "  " + bad_switch_model[i] + "  " + bad_switch_ports[i] + "  " +
                              bad_switch_type[i] + "  " + bad_switch_uplink[i] + bad_uplink_type[i])

                    stackname = os.path.splitext(filename)[0]
                    print("")
                    if fail == False:
                        print(
                            "Detected " + str(switchcount) + " valid switches in stack '" + stackname + "' (see data)")
                    if fail == True:
                        print("Detected " + str(switchcount) + " valid switches and " + str(
                            failed_switches) + " invalid switches in stack '" + stackname + "' detailed above.")
                        print("Please validate all of the information stored in '" + filename + "' and try again")
                        print("")
                        print("Pressing enter will terminate the program.")
                        input()
                        sys.exit()

                    while True:
                        try:
                            print("")
                            prompt = input("Confirm information is correct, (Y)es or (N)o ? ")
                            if prompt == "Yes" or prompt == "Y" or prompt == "y":
                                global stackname
                                flagchange()
                                ui()
                            elif prompt == "No" or prompt == "N" or prompt == "n":
                                sys_unmount()
                            else:
                                print("")
                                print("Please enter a valid selection")
                                continue
                        except:
                            raise SystemExit

                except IOError:
                    clearscreen()
                    print("Switcharoo! Warning!")
                    print("")
                    print("Error. The file you entered does not exist.")
                    print("")
                    print("Please enter a different file name.")
                    print("Press enter to continue.")
                    input("")

        print("Success")
        break
    except:
        print(
            "Error writing 'parsing' protocol. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        print(
            "If you are still encountering this error proceeding that action it is possible the 're' module found within the default installation package no longer supports any of the commands issued in this program or they have been tampered with.")
        engine_error = 1
        break




#SYS UNMOUNT#

while True:
    try:
        print("Developing un-mounter sub-module")

        def sys_unmount():
            clearscreen()
            print("Switcharoo!: Un-mount")
            print("*" * 35)
            print("")
            print("Un-mounting current database: clearing arrays:")
            print("")
            global switch_model
            global switch_ports
            global switch_type
            global switch_uplink
            global stackname
            switch_model = []
            switch_ports = []
            switch_type = []
            switch_uplink = []
            switchcount = 0
            failed_switches = 0
            linepos = 0
            goodswitch_position = []
            badswitch_position = []
            if flag == True:
                flagchange()
            elif flag == False:
                pass
            file.close()
            print(stackname + " has been successfully unmounted")
            stackname = ""
            print("")
            print("Press enter to return to the main menu.")
            ui()

        print("Success")
        break
    except:
        print(
            "Error writing un-mount protocol. Please visit www.python.org and ensure that your version of Python is correctly installed and version of Python 3 or higher.")
        engine_error = 1
        break







#SYS OPERATION (Output config)#

while True:
    try:
        print("Defining database parser")

        def sys_operation():


            #HEADER
            OutfileNAME1 = "./sys/temp/" + stackname + "_header.txt" #Check dir exists
            if not os.path.exists(os.path.dirname(OutfileNAME1)):
                os.makedirs(os.path.dirname(OutfileNAME1))

            with open(OutfileNAME1, "wt") as Outfile:
                with open("./sys/BaseHeader.txt", "rt") as Infile:
                    for line in Infile:
                        Outfile.write(line.replace("<SwitchName>", stackname))

            #GENERATED
            OutfileNAME2 = "./sys/temp/" + stackname + "_generated.txt" #Check dir exists
            if not os.path.exists(os.path.dirname(OutfileNAME2)):
                os.makedirs(os.path.dirname(OutfileNAME2))

            with open("./sys/BaseGenerated.txt", "rt") as Infile:
                with open(OutfileNAME2, "wt") as Outfile:
                    copy = False
                    for line in Infile:
                        if line.strip() == "=<STATICTEXT>=":
                            copy = True
                        elif line.strip() == "=<ENDSTATICTEXT>=":
                            copy = False
                        elif copy:
                            Outfile.write(line)

                    li_config = []
                    li_uplink_config = []
                    li_int_total_ports = []  #Find total number of ports for switch_ports and uplink so can range ports TO uplink


                    int_switch_ports = [int(x) for x in (switch_ports)] #Ad-hoc fix str bug (all lists mounted as strings)#
                    int_switch_uplink = [int(x) for x in (switch_uplink)]


                    for i in range(switchcount):
                        x = (i + 1)
                        for a in range(int_switch_ports[i]):
                        #                 print (x) DEBUG
                        #                print (a+1) DEBUG
                        #               print ("") DEBUG
                            xstr = str(x) #Convert ints back into strings
                            astr = str(a + 1)
                            li_config.append(switch_type[i] + (xstr) + "/0/" + (astr)) # NOTE APPEND TYPE TO THIS



                        li_int_total_ports.append(int_switch_ports[i] + int_switch_uplink[i])
                        switch_ports_to_uplink_ports_at_i = ([int_switch_ports[i], li_int_total_ports[i]])
                        switch_ports_to_uplink_ports_at_i.sort()
                        range_a = (switch_ports_to_uplink_ports_at_i[0])
                        range_b = (switch_ports_to_uplink_ports_at_i[1])

                        for a in range (range_a, range_b):

                        #                 print (x) DEBUG
                        #                print (a+1) DEBUG
                        #               print ("") DEBUG
                            xstr = str(x) #Convert ints back into strings
                            astr = str(a + 1)
                            li_config.append(uplink_type[i] + (xstr) + "/0/" + (astr)) # NOTE APPEND TYPE TO THIS


                    for i in range(len(li_config)):
                        Outputstring = ("interface " + (li_config[
                                                            i]) + "\n port link-mode bridge\n port access vlan 999\n shutdown\n stp edged-port enable\n#\n")
                        Outfile.write(Outputstring)

            #FOOTER
            #BASEFOOTER.TXT
            OutfileNAME3 = "./sys/temp/" + stackname + "_footer.txt" #Check dir exists
            if not os.path.exists(os.path.dirname(OutfileNAME3)):
                os.makedirs(os.path.dirname(OutfileNAME3))

            with open(OutfileNAME3, "wt") as Outfile:
                with open("./sys/BaseFooter.txt", "rt") as Infile:
                    for line in Infile:
                        Outfile.write(line)
                #/FOOTER#

            # Compile files
            OutfileNAME4 = "./Output/" + stackname + "/" + stackname + "_config.txt" #Check dir exists
            if not os.path.exists(os.path.dirname(OutfileNAME4)):
                os.makedirs(os.path.dirname(OutfileNAME4))

            compile_files = [OutfileNAME1, OutfileNAME2, OutfileNAME3]
            with open(OutfileNAME4, 'w') as outfile:
                for fname in compile_files:
                    with open(fname) as infile:
                        for line in infile:
                            outfile.write(line)
            print("")
            print("Successfully wrote config file at './Output/" + stackname + "_config.txt'")
            print("")
            print ("Cleaning up temporary directory...")
            try:
                shutil.rmtree("./sys/temp")
                print ("")
                print ("Success")
                print ("")
                input ("Press enter to return to the main menu")
            except:
                print ("Unable to delete temporary directory. Please manually remove "+os.getcwd()+"/sys/temp")

        print ("Success")
        break

    except:
        print(
            "Error writing parsing protocol. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        print(
            "If you are still encountering this error proceeding that action it is possible the 're' module found within the default installation package no longer supports any of the commands issued in this program or they have been tampered with.") #Line 205
        engine_error = 1
        break

#About


while True:
    try:
        print("Defining database parser")

        def about():
            clearscreen()
            print("Switcharoo v.1.0")
            print("")
            print("Switcharoo was developed as an exercise by Callum Dempsey Leach (a Philosophy student studying in Leeds University) who hopes to join the software\ndevelopment industry post graduation.")
            print("")
            print("You can contact the author as follows...\n\nEmail, callum.leach@hotmail.co.uk.\n\nTweet at, www.twitter.com/mmacheerpuppy.")
            print("")
            print("Whilst I hope you enjoy the application, this work is licensed under a\nGNU GPL v3.0 License (see DOCS for full license).")
            print ("The license broadly entails...")
            print("\n<Users can>\n Legally distribute and create adaptations of Switcharoo only if the source code and license is disclosed with the content and stated significant changes are made to the content.\nSwitcharoo or its distributions (inclusively) may be modified.\nUse and modify Switcharoo without distributing it.\n<Users cannot>\nHold the author liable for any damages caused by Switcharoo (the software is provided without warrenty)\nGrant a sublicense to modify and distribute Switcharoo not included in the license.")
            print("")
            print("")
            input("Press enter to return to the main menu")
            ui()
        break


    except:
        print(
            "Error writing About. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1
        break

#UserInterface

while True:
    try:
        print("Writing UI")

        def ui():
            while True:
                try:
                    clearscreen()
                    print("Switcharoo v.1.0")
                    print("")
                    print("Welcome to the main menu.")
                    print("")
                    print("Please select from among the following options:")

                    if flag == False:
                        print("1. Mount a stack of switches from switch name")
                        print("2. About")
                        print("3. Quit the program")

                    elif flag == True:
                        print("1. Unmount stack " + stackname)
                        print("2. Output switch config")
                        print("3. Quit the program")

                    menuinput = int(input("> "))

                    if menuinput == (1) and flag == False:
                        sys_mount()

                    elif menuinput == (1) and flag == True:
                        sys_unmount()

                    if menuinput == (2) and flag == False:
                        about()
                        break

                    elif menuinput == (2) and flag == True:
                        sys_operation()

                    elif menuinput == (3):
                        print("")
                        print("Goodbye.")
                        if flag == 1:
                            file.close()
                            sys.exit()
                        else:
                            sys.exit()

                    elif menuinput != ((1) or (2) or (3)):
                        print("")
                        print("Please enter a valid selection.")
                        print ("Pressing enter will return you to the selection screen")
                        continue

                except ValueError:
                    print("")
                    print("Please enter a valid selection.")
                    print("Pressing enter will return you to selection screen.")
                    input()
                    continue

        print("Success")
        break
    except:
        print(
            "Error writing UI. Please visit www.python.org and ensure that your version of Python is correctly and fully installed and that you are running a version of Python 3 or higher.")
        engine_error = 1

if engine_error == 1:
    print("")
    print("An error occurred initializing the application. See the above log for more details.")
    print("Terminating.")
    raise SystemExit
else:
    print("")
    print("Initialization successful.")
    clearscreen()
    print("")
    print("")

ui()
