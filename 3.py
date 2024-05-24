def extractfield(filename,n):
    infile=open(filename,"r")
    return [line.rstrip().split(',')[n-1] for line in infile]
c=0
infile=open("questions.csv",'r')
outfile=open("marks.csv","w")
questions=extractfield("questions.csv",1)
answers=extractfield("questions.csv",2)
for i in range(len(questions)):
    print(questions[i])
    answer=input()
    if answer==answers[i]:
        c+=1
name=input("input your name: ")
count=str(c)
print(name,count)
outfile.write(name+','+count)
outfile.close()
