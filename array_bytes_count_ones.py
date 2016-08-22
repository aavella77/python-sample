#!/usr/bin/python
print "Array of bytes 10101100, count the number of ones"

array = ["11001100", "11110010", "00001010", "10000000"]

count = 0
for byte in array:
	print "Byte is: " + byte
	for bit in range(0,8):
		bit_x = byte[bit]
		print " bit is: " + str(bit_x)
		if (bit_x == str(1)):
			count = count + 1

print "The number of ones is " + str(count)
