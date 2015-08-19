fh = open("mbox-short.txt")
count =0
val =0
for line in fh:

    if not line.startswith("X-DSPAM-Confidence:") : continue
    val = val+float(line[len("X-DSPAM-Confidence:"):])
    count =count+1

average = val/count
print(average)