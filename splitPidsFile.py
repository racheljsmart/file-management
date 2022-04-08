#!/usr/bin/env python

#change the filename to the file you are running. Remember to pass it as an argument in the shell or create a path in the code.
with open('test_pid_count.txt', 'r') as org_pids:
    num_lines = 0
    cntr = 1
    for line in org_pids:
        pid = line.strip()
        print(pid)

        if pid != '':
            num_lines += 1

        if num_lines < 20:
            with open(str(cntr) + '.txt', 'w') as new_file:
                new_file.write(pid + '\r\n')
                cntr += 1
        else:
            num_lines = 0
            new_file.close()

print (num_lines)
