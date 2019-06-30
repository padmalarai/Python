class system:
    def __init__(self,name,ip,port):
        self.name=name
        self.ip=ip
        self.port=port
        
    def sysinfo(self):
        print("System name:{}".format(self.name))
        print("System ip:{}".format(self.ip))
        print("System port:{}".format(self.port))

    @staticmethod
    def test_static():
        print("staticc syntax")
        print("test static")

    def __del__(self):
        print("ssystem has been removed")

sys1=system('vm101','10.101.10.1',22)
sys1.sysinfo()

sys2=system('vm102','10.101.10.2',80)
sys2.sysinfo()

system.test_static()
sys1.test_static() # or optional way to invoke static

del sys1
del sys2
