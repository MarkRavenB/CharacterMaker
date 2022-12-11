race = []
name = []
skills = []
role = []
item = []
personality = []

def menu():
    print("\n========================")
    print("=====Welcome User!======")
    print("========================")
    print("1. Create Character")
    print("2. View Character")
    print("3. Delete Character")
    print("4. Update Character")
    print("5. Exit")

def create():
    
    print("\n==============================")
    print("=====Please Enter Genre!======")
    print("==============================\n")
    print("1 - An Anime Character")
    print("2 - An Movie Character")
    print("3 - An Game Character")
    
    secoption = int(input("\nEnter choice: "))

    while secoption != 5:
     if secoption == 1:
      animecreate()
      break
  
     elif secoption == 2:
      moviecreate()   
      break
  
     elif secoption == 3:
      gamecreate()
      break   
      
      
def animecreate():
    a_race = input("\nWhat is your Anime Race? : ")
    a_name = input("What is your Anime Name? : ")
    a_skills = input("What Skill do you like from your Character? : ")
    a_role = input("What is your Role in your World? : ")
    a_item = input("What is your main Item for your Journey? : ")
    a_personality = input("What is the Personality of your Character? : ")
    
    race.append(a_race)
    name.append(a_name)
    skills.append(a_skills)
    role.append(a_role)
    item.append(a_item)
    personality.append(a_personality)
    print("\nInput SuccessFully!")
    
    
def moviecreate():
   print()
   m_race = input("\nWhat is your Being in the Movie? : ")
   m_name = input("What is your Movie Name? : ")
   m_skills = input("What is the Ability of your Movie Character? ")
   m_role = input("What is your Role in your Movie? : ")
   m_item = input("What is the personal Item for your Role? : ")
   m_personality = input("What is your Personality for your Role? : ")
    
   race.append(m_race)
   name.append(m_name)
   skills.append(m_skills)
   role.append(m_role)
   item.append(m_item)
   personality.append(m_personality)
   print("\nInput SuccessFully!")     
    
def gamecreate():
   print()
   g_race = input("\nWhat is your Race in your Game? : ")
   g_name = input("What is your Name in your Game? : ")
   g_skills = input("What is the Skill of your Character? : ")
   g_role = input("What is the Role of your Character in your Game? : ")
   g_item = input("What will be your main Item for your Adventure? : ")
   g_personality = input("What is your Character's Personality in the Game? : ")
    
   race.append(g_race)
   name.append(g_name)
   skills.append(g_skills)
   role.append(g_role)
   item.append(g_item)
   personality.append(g_personality)
   print("\nInput SuccessFully!")        

def view():
    if len(race) == 0:
        print("\nNo Data To View!")
    else:
     for i in range(len(race)):       
        print("\n",[i],"\nRace: ",race[i], "\nName: ",name[i], "\nSkills: ",skills[i], "\nRole: ", role[i], "\nItem: ", item[i], "\nPersonality: ", personality[i])
