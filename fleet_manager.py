def init_database():
    names = ["picard", "riker", "data", "Troi", "worf"]
    ranks = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Lieutenant"]
    divisions = ["Command", "Command", "Operations", "sciences", "Security"]
    ids = [101,102,103,104,105]
    return names, ranks, divisions

def display_menu(student_name)
    print(f"\nLogged in as {student_name}")
    print("--- FLEET MANAGEMENT SYSTEM ---")
    print("display roster\n2. add crew member\n3. remove crew member\n4. update rank")
    print("5. search crew member\n6.filter by divison\n7. calculate payroll\n8. count officers\n9 exit")
    