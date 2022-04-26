filepath = 'hr_base10.txt'
f_read = open("hr_hex.txt", "r")
f_write = open("hr_base10.txt", "w")

for line in f_read:
    line = line.strip()
    if line:
        val = str(int(line,16)) + "\n"
        f_write.write(val)

f_read.close()
f_write.close()
