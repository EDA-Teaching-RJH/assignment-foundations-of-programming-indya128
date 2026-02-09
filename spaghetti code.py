n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    #bug fix 1 - added 'loading' increment to prevent infinite loop
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        loading +=1 
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        opt = input("Select option: ")
    #bug fix 2 - changed '=' to '==' for comparison
        
        if opt == "1":  
            print("Current Crew List:")
    #bug fix 3 - changed range(10) to range(len(n)) to prevent index out of range error 
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
    #bug fix 4- missing colon sytax error             
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
#bug fix 5- added appending to rank and division lists when adding crew member  
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
     #bug fix 6- unprotected indexing. added an 'if' check to ensure the name exists before calling. index()to avoid crashing.  
            if rem in n:
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
            else:
                print("Crew member not found.")

        elif opt == "4":
            print("Analyzing...")
            count = 0
            for rank in r:
        #bug fix 7- logic. changed to 'rank == "Captain" or rank == "Commander"'so the second halve of or isnt always true. 
                if rank == "Captain" or  rank == "Commander": 
                    count += 1 
        #bug fix 8- type error. added str() to convert count to string for concatenation.
            print("High ranking officers: " + str(count)) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        #bug fix 9- change if to else for better performance and logical flow. 
        else: 
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")
        #bug fix 10- added parentheses to properly call the function.
run_system_monolith ()