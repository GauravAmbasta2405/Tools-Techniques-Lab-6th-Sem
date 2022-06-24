with open('xyz.txt', 'r') as firstfile, open('xyz2.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)