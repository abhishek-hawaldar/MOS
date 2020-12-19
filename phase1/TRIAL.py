# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""

$AMJ000100030001
GD10PD10H
$DTA
HELLO
$END0001

GD-Get Data
PD-Print Data
LR-Load Register From Memory
SR-Store Register From Memory
CR-Compare Register And Memory
BT-Branch Toggle(Checks Toggle Variable)
H- Denotes end of job.
Job should start with $AMJ
There is $DTA after declaration of program cards and before data cards
Job should end with $END


0 ['G', 'D', '2', '0']
1 ['G', 'D', '3', '0']
2 ['G', 'D', '4', '0']
3 ['G', 'D', '5', '0']
4 ['P', 'D', '2', '0']
5 ['P', 'D', '3', '0']
6 ['L', 'R', '2', '0']
7 ['C', 'R', '3', '0']
8 ['B', 'T', '1', '1']
9 ['P', 'D', '5', '0']
10 ['P', 'D', '4', '0']
11 ['H', '?', '?', '?']

GD20
GD30
GD40
GD50
PD20
PD30
LR20
CR30
BT11
PD50
PD40
H


"""

SI = 0
terminate = 0


class os:
    SI = 0
    terminate = 0
    def __init__(self):

        self.mem = [['?' for x in range(4)] for y in range(100)]  # memory
        self.IR = ""  # instruction register
        self.IC = 00  # instruction counter
        self.R = ""  # general purpose register
        self.C = 0

    def reset(self):

        self.mem = [['?' for x in range(4)] for y in range(100)]  # memory
        self.IR = ""  # instruction register
        self.IC = 00  # instruction counter
        self.R = ""  # general purpose register
        self.C = 0

    def printall(self):
        print("mem:", self.mem)
        print("IR:",self.IR)  # instruction register
        print('IC',self.IC)  # instruction counter
        print("R",self.R)  # general purpose register
        print("C",self.C)

    def get_program_cards(self, job):

        k = 0
        print("again:", job)
        while (k < len(job)):
            for i in range(100):

                for j in range(4):

                    if (k < len(job)):
                        ch = job[k]
                        #print(k, ch)
                        k += 1
                        self.mem[i][j] = ch;
                        if (self.mem[i][0] == 'H'):
                            break

            print("stuck3")

    def printmem(self):

        for i in range(100):
            print(i, self.mem[i])

    def execute_user_program(self):

        global terminate

        terminate = 0
        global SI
        while (not terminate):

            print("inside execute_user_program")

            # fetched_IC = self.IC;
            self.IR = ""
            for i in range(4):
                self.IR += self.mem[self.IC][i]

            self.IC+=1
            operator = self.IR[0:2]
            operand = self.IR[2:]
            print("Current instruction:", self.IR)
            if (operator == "LR"):
                self.R=""
                print("found LR")
                pos = int(operand)
                print( "gonna load ",self.mem[pos])
                for i in range(4):
                    if(self.mem[pos][i]=="?"):
                        continue
                    self.R += self.mem[pos][i]
                print("have loaded into register: ", self.R)


            elif (operator == "SR"):

                # self.R
                print("found SR:", self.R)
                pos = int(operand)
                if self.R=="":
                    continue
                for i in range(len(self.R)):
                    self.mem[pos][i] = self.R[i]

                print("going to store in memory location",pos," :", self.R)


            elif (operator == "CR"):
                print("found CR")

                print("going to compare", )
                pos = int(operand)
                compare_string = ""
                for i in range(4):
                    if(self.mem[pos][i]=="?"):
                        break
                    compare_string += self. mem[pos][i]

                if (self.R == compare_string):
                    self.C = 1
                    print("are same")
                else:
                    self.C = 0
                    print("not same")
                print("going to compare",self.R, " and ", compare_string )

            elif (operator == "BT"):
                print("found BT", self.C)
                if (self.C):
                    pos = int(operand)
                    self.IC = pos

            elif (operator == "GD"):
                print("found gd")

                SI = 1
                self.mos()

            elif (operator == "PD"):

                print("found pd")

                SI = 2
                self.mos()



            else:
                SI = 3
                self.mos()

    def start_execution(self):
        self.IC = 00
        self.execute_user_program()

    def mos(self):
        print("mos", SI)
        if (SI == 1):
            print("inside gd")
            self.IR = self.IR[:3] + '0'
            pos = int(self.IR[2:])
            global i
            global lines
            #print("here:", i)
            s = lines[i]
            i += 1

            if (len(s) != 0 and s[-1] == '\r'):
                s = s[:len(s) - 1]

            start = 0
            s1 = ""
            j = pos
            while (start < len(s)):

                #print("stuck5")
                if ((len(s) - start) < 4):
                    s1 = s[start:len(s)]
                else:
                    s1 = s[start:start + 4]


                #print(j, s1)

                for k in range(len(s1)):
                    self.mem[j][k] = s1[k]


                start += 4
                j += 1
            #print("reached end")
            self.printmem()

        elif (SI == 2):


            print("inside pd")
            self.IR = self.IR[:3] + '0'
            print(self.IR)
            pos = int(self.IR[2:])
            flag = 0
            ans = ''
            temp = ''
            j = pos
            while (j < pos + 10):

                print("stuck6")
                print(11)
                temp = self.mem[j]
                print(temp)
                for k in range(4):
                    #print(12)
                    #print(k,temp[k])

                    if (temp[k] == '?'):
                        #print(13)
                        continue
                    print(temp[k])
                    ans += temp[k]
                    #print(14)
                if (flag):

                    print("going to print", ans)
                    break


                j += 1
            print("going to print", ans)
            with open("output.txt", "a") as myfile:
                myfile.write( ans + "\n")
            myfile.close()


        else:
            # si=3
            print("inside H")
            global terminate
            terminate = 1
            with open("output.txt", "a") as myfile:
                myfile.write("\n\nend of the previous job\n\n\n")
            myfile.close()


if __name__ == '__main__':

    '''with open("input.txt") as openfileobject:
        i=1
        for line in openfileobject:
            print(i, line)
            i+=1
['$AMJ000100030001\n', 'GD10PD10\n', 'GD90PD90\n',
 '$DTA\n', 'ABC\n', '$END0001']
     '''

    with open("output.txt", "w") as myfile:
        print("initial commit")
        myfile.write(" Going to start the stuff now\n")
    myfile.close()


    f = open('input.txt')

    lines = f.readlines()
    f.close()

    for q in  range(len(lines)):
        lines[q]= lines[q][:len(lines[q])-1]

    i = 0



    obj = os()
    print(lines)
    b=0
    while (i < len(lines) and b<20):

        print("starting line check HEEEELLL YEAHHHH\n\n\n\n\n\n\n",lines[i])
        b+=1

        if (not lines[i].find("$AMJ") == -1):
            # it is the start of a program
            print('it is the start of a program')
            print(lines[i])
            jobcount = lines[i][9:12]
            # print(jobcount)
            obj.reset()
            print(jobcount)
            i += 1

            # print("mah man:",lines[i])
            job = ""

            while (lines[i].find("$DTA") == -1):
                # print(lines[i])
                job += lines[i]
                job = job[:len(job)]
                i += 1

                print("stuck1")

            print("job:", job)

            obj.get_program_cards(job)
            #obj.printmem()

        elif (not lines[i].find("$DTA") == -1):
            i += 1
            obj.start_execution()

        elif(not lines[i].find("$END")==-1):
            obj.printmem()
            i+=2
            continue
        #i+=1
