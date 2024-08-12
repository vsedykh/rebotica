str = "Жил был у мамы серенький козлик"
print(str)
index = str.find("к")
index2 = str.rfind("к")
print(index)
print(index2)
s1 = str[0:3]
s2 = str[4:7]
s3 = str[8]
s4 = str[10:15]
s5 = str[15:24]
s6 = str[25:31]
print(s1,s2,s3,s4,s5,s6)

result = "%s %s %s %s %s %s" % (s6,s5,s4,s3,s2,s1)
print(result)