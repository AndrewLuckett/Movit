from Modules import * 

class Vm:
    def __init__(this, location):
        this.tape = []
        with open(location) as f:
            for line in f:
                this.tape.append(line.replace("\n",""))
                
        this.fileLocation = location
        this.addresses = {"pc":Module(),"lder":LoaderModule()}

    def runTape(this):
        while(True):
            command = this.getDat(this.addresses["pc"].value)
            
            this.addresses["pc"].value += 1
            if this.runCommand(command) == False:
                return

    def getDat(this,line):        
        command = this.tape[line].split("//")[0].split(" ")
        while command.count(""):
            command.remove("")
        return command

    def runCommand(this,command): #Ugly needs rework
        if len(command) == 0:
            return True #Skip Empty lines

        com = command[0].lower()

        if com == "done":
            return False #Done on done

        if len(command) < 2:
            this.errOut("Tried to execute an invalid command : " + str(command))
            return False

        to = command[1]
        try:
            to = int(command[1]) #make int if you can
        except:
            pass

        if com == "rst":
            this.addresses[to].reset()
            return True

        if len(command) < 3:
            this.errOut("Tried to execute an invalid command : " + str(command))
            return False
                    
        by = command[2]
        try:
            by = int(command[2]) #make int if you can
        except:
            pass

        if not this.addresses.get(to):
            this.addresses[to] = Module()
          
        if com == "mov":
            val = this.addresses[by].getValue()
            if type(val) == type(Module): #if we're addressing a module
                this.addresses[to] = val() #instance it
            else:
                this.addresses[to].setValue(val) #Otherwise just move value
        elif com == "set":
            if type(by) != int:
                this.errOut("Tried to set non int value : " + by)
                return False
            this.addresses[to].setValue(by) #Set address to value
        else:
            this.errOut("Tried to execute an invalid command : " + com)
            return False

        return True

    def errOut(this,text):
        print(">> ERR:",text,":",this.fileLocation)
        #print(str(this.addresses)) #Good for debug
        exit(1)

#######
if __name__ == "__main__":
    import sys
    
    try:
        a = Vm(sys.argv[1])
    except:
        print(">> ERR: Unable to load program")
        exit()

    a.runTape()
