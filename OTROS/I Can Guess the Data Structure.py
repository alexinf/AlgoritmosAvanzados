#!/usr/bin/python3
# coding: utf-8 


while True:
    try :
        stack=[]
        queue=[]
        priority_queue=[]
        n = int(input())
        m=n
        f=-1
        c=0
        s=0 
        p=0 
        q=0 
        while(n):
            n=n-1
            i,j=input().split()
            i=int(i)
            j=int(j)
            if i==1:
                queue.append(j)
                stack.append(j)
                priority_queue.append(j)
                priority_queue.sort(reverse=True)
            else:
                c=c+1 
                if len(stack)>0 and j==stack[len(stack)-1] and s==0:
                    stack.pop(len(stack)-1)
                else:
                    s=1
                if len(queue)>0 and j==queue[0] and q==0:
                    queue.pop(0)
                else:
                    q=1
                if len(priority_queue)>0 and j==priority_queue[0] and p==0:
                    priority_queue.pop(0)
                else:
                    p=1
                if s==1 and p==1 and q==1:
                    f=0
        
        if(c>m-c):
            f=0
        
        if f!=0:
            if (s==0 and p==0 and q==0) or (s==0 and q==0) or (p==0 and q==0) or (s==0 and p==0 ): 
                print("not sure")
            elif m-2*c==len(stack):
                print("stack")
            elif m-2*c==len(queue):
                print("queue")
            elif m-2*c==len(priority_queue):
                print("priority queue")
            else:
                print("impossible")
        else:        
            print("impossible")
        
        
    except EOFError:
        break