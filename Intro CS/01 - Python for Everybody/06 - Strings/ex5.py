str = 'X-DSPAM-Confidence:0.8475'

pos = str.find(":")
print(float(str[pos+1: ]))