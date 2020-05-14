from Modules import * 

class Vm:
    def __init__(this, defLocation, progLocation):
        this.addresses = []
        this.loadDef(defLocation)

        this.prog = []
        this.loadProg(progLocation)
                
        this.fileLocation = progLocation
        

    def loadDef(this, location):
        with open(location) as f:
            line = f.readline()
            this.addresses = [moduleList["module"]() for i in range(int(line) + 1)]
            line = f.readline()
            while line:
                com = line.replace("\n", "").split("//")[0].split(",")
                line = f.readline()
                if len(com) < 2:
                    continue
                
                this.addresses[int(com[0])] = moduleList[com[1]]()
                

    def loadProg(this, location):
        with open(location) as f:
            for line in f:
                this.prog.append(line.replace("\n", "").split("//")[0])
                #Add cleaned line to prog


    def runTape(this):
        while(True):
            command = this.getDat(this.addresses[0].value)
            this.addresses[0].value += 1
            
            if this.runCommand(command) == False:
                return


    def getDat(this, line):        
        command = this.prog[line].split(" ")
        while command.count(""):
            command.remove("")
        return command


    def runCommand(this, command):
        if len(command) == 0:
            return True #Skip Empty lines

        com = command[0].lower()

        if com == "done":
            return False #Done on done

        if len(command) < 3:
            this.errOut("Tried to execute an invalid command : " + str(command))
            return False

        try:
            to = int(command[1])
            if to >= len(this.addresses):
                this.errout("Target module address out of bounds : " + str(command))
            to = this.addresses[to]
        except:
            this.errOut("Invalid target module address : " + str(command))

        try:
            by = int(command[2])
        except:
            this.errout("Invalid origin module address : " + str(command))


        if com == "set":
            to.setValue(by)
            return True

        if by >= len(this.addresses):
                this.errOut("Origin module address out of bounds : " + str(command))
        by = this.addresses[by]
                
        if com == "rst":
            to.reset(by.getValue())
        elif com == "mov":
            to.setValue(by.getValue())            
        else:
            this.errOut("Tried to execute an invalid command : " + com)
            return False

        return True
    

    def errOut(this, text):
        print(">> ERR:", text, ":", this.fileLocation)
        #print(str(this.addresses)) #Good for debug
        exit(1)

#######
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print(">> ERR: No program provided")
        if len(sys.argv) < 2:
            print(">> ERR: No Computer definition provided")
        exit(1)
    
    a = Vm(sys.argv[1], sys.argv[2])
    
    a.runTape()
