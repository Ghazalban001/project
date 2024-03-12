print("welcom to this plan")
list_=[]
def q():
    global getup,list_
    request=input(f"ok giv me your plan for {getup} {'am'if getup<12 else 'pm'}►►")
    activity=hours(1,sleep-getup)
    list_.append(f"from {getup} {'am'if getup<12 else 'pm'} to {getup+activity} {'am'if getup+activity<12 else 'pm'} = {request}")
    getup+=activity  
def hours(getup1,end,start=1,qu="how many time do you need"):   # تابع مقدار درست زمان
    s=0                      #متغییر flag
    while True:
        if s==0:
            question1=input(f"{qu}►►")
            s=1
            if question1.isdigit() and start<=int(question1)<=end and question1!="0":  #استفاده از رقم 
                return int(question1)
        if s==1:
            question1=input(f"you need enter {getup1}-{end}►►")
            if question1.isdigit() and start<=int(question1)<=end:
                return int(question1)

getup=hours(5,10,5,"what time do you get up? it need to be between 5 to 10 ")
print("*"*25)
sleep=hours(21,24,21,"what time do you sleep? it need to be between 21 to 24 ")
print("*"*25)
while getup<sleep:
    q()
print(*list_)
