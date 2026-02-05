def init_database():
    names = ["picard", "riker", "data", "Troi", "worf"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Lieutenant"]
    divisions = ["Command", "Command", "Operations", "sciences", "Security"]
    ids = [101,102,103,104,105]
    return names, ranks, divisions

def display_menu(student_name):
    print(f"\nLogged in as {student_name}")
    print("--- FLEET MANAGEMENT SYSTEM ---")
    print("display roster\n2. add crew member\n3. remove crew member\n4. update rank")
    print("5. search crew member\n6.filter by divison\n7. calculate payroll\n8. count officers\n9 exit")

def add_member(names, ranks, divisions,id):
    new_id = int(input("Enter ID: "))
    if new_id in id:
        print("Error: ID must be unique.")
        return
    new_rank = input("Enter TNG rank: ")
    valid_ranks= ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Ensign"]
    if new_rank not in valid_ranks:
        print("Error: Invalid TNG rank.")
        return
    names.append(input("Enter name: "))
    ranks.append(new_rank)
    divisions.append(input("Enter division: "))
    id.append(new_id)
    print("Crew member added successfully.")

def remove_member(names, ranks, divisions, id):
    target_id = int(input("Enter ID of crew member to remove: "))
    if target_id in id:
        idx = id.index( target_id)
        names.pop(idx)
        ranks.pop(idx)
        divisions.pop(idx)
        id.pop(idx)
        print("member removed.")
    else:
        print("ID not found.")

def update_rank(names, ranks, id):
    target_id = int(input("Enter ID to update: "))
    if target_id in id:
        idx = id.index(target_id)
        ranks[idx] = input(f"Enter newrank for {names[idx]}: ")
        print("Rank updated.")
    else:
        print("ID not found.")

def display_roster(names, ranks, divisions, id):
    print(f"{'ID':<5} {'Name':<15} {'Rank':<15} {'Division':<15}")
    for i in range(len(names)):
        print(f"{id[i]:<5} {names[i]:<15} {ranks[i]:<15} {divisions[i]:<15}")
