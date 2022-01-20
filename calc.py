#Just a script that helps me
import math

num_dbm1 = 40 #dbm
num_dbm2 = 20 #dbm

#mW -> Convert to dBm
def mw_to_dbm(value):
    return 10 * math.log10(value)

#dBm -> Convert to mW
def  dbm_to_mw(value):
    return math.pow(10, value/10)
  
num_mw = dbm_to_mw(num_dbm1) + dbm_to_mw(num_dbm2)
var = str(mw_to_dbm(num_mw))
print(str(num_mw)+" mW = " + var + " dbm")
  
# print(dbm_to_mw(20.0))
# print(mw_to_dbm(100.0))
