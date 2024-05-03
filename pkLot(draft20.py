pkslot={}
for i in range(1,21):
    pkslot[i]=0


while True:
    op=int(input("Please Enter Your Choice of Action:\n1.Park\n2.Checkout"))#get i/p from user
    
    if op==1:#user chooses to park
        space_lot=[]#an empty list to show the space available
        for i in range(1,21):
            if pkslot[i]==0:#checking if the key has no value
                space_lot.append(i)#append the value when true
        if space_lot==[]:#check if slot is available
            print("The spaces are currently occupied")
            break
        else:#show slots available
            print("Spaces currently available\n",space_lot)
        while True:
            ch=int(input("Enter your preferred slot"))
            if ch in space_lot:#if preferred slot choice is available
                
                break
            else:
                print("Space currently occupied")#if not
        vhno=input("Enter your vehicle number")
        pkslot[ch]=vhno #in that slot enter the vhno
        print("Vehicle parked")#show its parked
    elif op==2:#users chooses to checkout their vehicle from the pklot
        while True:
            vhno=input("Enter the Vehicle\'s no:\n")#ask user for their vhno
            if vhno in pkslot.values():#if vhno is in the pklot
                for slot, vh in pkslot.items():
                    if vh==vhno:
                        pkslot[slot]=0
                    print("Your Vehicle has been retrived succesfully")
                    break
            else:#vhno not in pklot
                print("There is no vehicle in the parking lot with your entered number.")

    else:
        break

            
