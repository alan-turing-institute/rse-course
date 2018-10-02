from unittest.mock import Mock, MagicMock
class CompMock(Mock):
    def __sub__(self, b):
        return CompMock()
    def __lt__(self,b):
        return True
array=[]
agt=[]
ws=[]
agents=[]
counter=0
x=MagicMock()
y=None
agent=MagicMock()
value=0
bird_types=["Starling", "Hawk"]
import numpy as np
average=np.mean
hawk=CompMock()
starling=CompMock()
sInput="2.0"
input ="2.0"
iOffset=1
offset =1
anothervariable=1
flag1=True
variable=1
flag2=False
def do_something(): pass
chromosome=None
start_codon=None
subsequence=MagicMock()
transcribe=MagicMock()
ribe=MagicMock()
find=MagicMock()
can_see=MagicMock()
my_name=""
your_name=""
flag1=False
flag2=False
start=0.0
end=1.0
step=0.1
birds=[MagicMock()]*2
resolution=100
pi=3.141
result= [0]*resolution
import numpy as np
import math
data= [math.sin(y) for y in np.arange(0,pi,pi/resolution)]
import yaml
import os
