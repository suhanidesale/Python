from os import write


# with open('file2.txt' , 'w') as f:
#     # f_cont = f.readline()
#     f.write('Text')
#     f.seek(0)

    # size_read = 100

    # f_contents = f.write('file')
    # print(f_contents , end = '')

    # for f_cont in f:
    #  print(f_cont , end = '')

    # f_cont = f.readline()
    # print(f_cont , end = '')

with open('file.txt','r') as rf:
    with open('file_copy1.txt' , 'w') as wf:
        for line in rf:
            wf.write(line)
