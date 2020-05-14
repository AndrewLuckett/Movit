class Module:
    def __init__(this):
        this.reset(0)

        
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
        this.value = value


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
    def setValue(this, value):
        this.value = int(value > this.comp)

    def reset(this, value):
        this.value = 0
        this.comp = value


class JumpIfModule(Module):
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
