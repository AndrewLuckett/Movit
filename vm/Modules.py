class Module:
    def __init__(this):
        this.reset()
    def setValue(this,value):
        this.value = value
        this.init = True
    def getValue(this):
        return this.value
    def reset(this):
        this.value = 0
        this.init = False

class LoaderModule(Module):
    def setValue(this,value):
        this.value = moduleList[value]

class AdderModule(Module):
    def setValue(this,value):
        this.value += value

class SubtractorModule(Module):
    def setValue(this,value):
        if this.init:
            this.value -= value
        else:
            this.value = value
            this.init = True

class MultiplierModule(Module):
    def setValue(this,value):
        if this.init:
            this.value *= value
        else:
            this.value = value
            this.init = True

class DivisorModule(Module):
    def setValue(this,value):
        if this.init:
            this.value //= value
        else:
            this.value = value
            this.init = True

class ModuloModule(Module):
    def setValue(this,value):
        if this.init:
            this.value %= value
        else:
            this.value = value
            this.init = True

class PositiveComparitorModule(Module):
    def setValue(this,value):
        if value > 0:
            this.value = 1
        else:
            this.value = 0

class NegativeComparitorModule(Module):
    def setValue(this,value):
        if value < 0:
            this.value = 1
        else:
            this.value = 0

class ZeroComparitorModule(Module):
    def setValue(this,value):
        if value == 0:
            this.value = 1
        else:
            this.value = 0

class VPrintModule(Module):
    def setValue(this,value):
        this.value = value
        print(value,end="")

class APrintModule(Module):
    def setValue(this,value):
        this.value = value
        print(chr(value),end="")


moduleList = {0:Module, #0-9 core modules
              1:LoaderModule,
              10:AdderModule, #10-19 math modules
              11:SubtractorModule,
              12:MultiplierModule,
              13:DivisorModule,
              14:ModuloModule,
              20:PositiveComparitorModule, #20-29 comparitor assist modules
              21:NegativeComparitorModule,
              22:ZeroComparitorModule,
              30:VPrintModule, #30-39 io modules
              31:APrintModule}
