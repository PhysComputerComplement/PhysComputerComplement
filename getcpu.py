import os, re
escape = (r"(?:\x1b[^m]*m)*")
cpu = re.compile(r"Cpu\(s\):"+escape+
    r" *([\d\.]*) "+escape+"us,"+escape+
    r" *([\d\.]*) "+escape+"sy,"+escape+
    r" *([\d\.]*) "+escape+"ni")
def get_cpu_occupy():
    topss = os.popen("top -n 1").read()
    return cpu.search(topss)