s=input("Expression: ").split()
evaluation=[]
for x in s:
    if x.isdigit():
        evaluation.append(float(x))
    else:
        if x=="/":
            evaluation.append(evaluation.pop()/evaluation.pop())
        if x=="*":
            evaluation.append(evaluation.pop()*evaluation.pop())
        if x=="+":
            evaluation.append(evaluation.pop()+evaluation.pop())
        if x=="-":
            evaluation.append(evaluation.pop()-evaluation.pop())
print(evaluation.pop())
