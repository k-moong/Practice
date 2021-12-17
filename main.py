import pymcprotocol

#If you use Q series PLC
pymc3e = pymcprotocol.Type3E()

#If you use ascii byte communication, (Default is "binary")
pymc3e.setaccessopt(commtype="binary")
pymc3e.connect("192.168.3.39", 1026)

#write 1(ON) to "X0", 0(OFF) to "X10"
pymc3e.randomwrite_bitunits(bit_devices=["X00", "X05"], values=[1, 1])

#read from X10 to X20
bitunits_values = pymc3e.batchread_bitunits(headdevice="X0", readsize=32)

print(bitunits_values)

#read from M2000 to M2032
Mbitunits_values = pymc3e.batchread_bitunits(headdevice="M2000", readsize=32)
print(Mbitunits_values)
