class Module:
    def __init__(this):
        this.reset(0)


    def handleCommand(this, com, dat):
        #set and mov already seperated
        if com == "rst":
            this.reset(dat)
        else:
            this.setValue(dat)
        return True

        
    def setValue(this, value):
        this.value = value

        
    def getValue(this):
        return this.value

    
    def reset(this, value):
        this.value = value
        

class LoaderModule(Module):
    def setValue(this, value):
        this.value = moduleList[value]


class AdderModule(Module):
    def setValue(this, value):
        this.value += value


class SubtractorModule(Module):
    def setValue(this, value):
        this.value -= value


class MultiplierModule(Module):
    def setValue(this, value):
        this.value *= value



class DivisorModule(Module):
    def setValue(this, value):
        this.value //= value


class ModuloModule(Module):
    def setValue(this, value):
        this.value %= value


class GreaterThanModule(Module):
    '''
    value == second value > first value
    '''
    def setValue(this, value):
        this.value = int(value > this.comp)

    def reset(this, value):
        this.value = 0
        this.comp = value


class JumpIfModule(Module):
    '''
    Reset with jumpa address
    Set or move in jumpb addres
    set or move in value
    if value != 0 then jumpa is used, otherwise jumpb
    '''
    def setValue(this, value):
        if this.jumpb == None:
            this.jumpb = value
        else:
            this.value = this.jumpa if value else this.jumpb

    def reset(this, value):
        this.value = value
        this.jumpa = value
        this.jumpb = None


class VPrintModule(Module):
    def setValue(this, value):
        this.value = value
        print(value, end="")


class APrintModule(Module):
    def setValue(this, value):
        this.value = value
        print(chr(value), end="")


moduleList = {"module" : Module,
              "adder" : AdderModule,
              "subtractor" : SubtractorModule,
              "multiplier" : MultiplierModule,
              "divisor" : DivisorModule,
              "modulo" : ModuloModule,
              "greaterthan" : GreaterThanModule,
              "jumpaddressif" : JumpIfModule,
              "vprint" : VPrintModule,
              "aprint" : APrintModule}
