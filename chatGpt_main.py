from patterns import Persona_Pattern,Templete_Pattern,Cognitive_Verifier,Refinement_Pattern,normal_Pattern
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.GREEN +"1 - Persona Pattern \n2 - Templete Pattern \n3 - Cognitive Verifier Pattern\n4 - Refinement_Pattern\nQ - To Stop Using Pattern\n")
print("\n\n\n\t\t\t\t1 ~ Before Moving Further You must Understand What is (LLM) Large Language Model and Prompt Engineering ~")
print(Fore.LIGHTYELLOW_EX + "\n\n"+ normal_Pattern("Act as a AI Expert and tell me what are Large Language  Models also Describe what is prompt Engineering Consider me as a 10 yrs old make it simple."))
message = input(Fore.BLUE + "Enter Which Pattern You Want to Use: ")

while True:
    print(Fore.LIGHTCYAN_EX+"\n\n \t\t\t~ IF YOU WANT TO QUIT PRESS Q \n\n")

    #PERSONA PATTERN : AFTER SAW AN EXAMPLE JUST WRITE THE QUESTION TO CHATGPT AND SEE HOW IT WORKS
    if message == '1':
        print(Fore.RED + "\t\t\t The Example Of Person Pattern also What are Large Language Model and what is Prompting ~".upper())
        print(Fore.CYAN + normal_Pattern("\n\n Write about what is PERSONA PATTERN in Prompt Engineering Give me some kind of Example!!") .upper())
        prompt = input(Fore.GREEN + "what you want to ask  from ChatGPT: ")
        if prompt == 'Q':
            break
        else:
            pattern_output = Persona_Pattern(prompt)
            print(pattern_output)
            

    # Templete PAttern
    elif message == '2':
        print(Fore.RED + "\t\t\t The Example Of Templete Pattern".upper())
        print(Fore.CYAN + normal_Pattern("\n\nAct as a Prompt Engineerer Write about what is Templete Pattern in Prompt Engineering and Show us Few Example also make it Simple TO Understand use some templete like where <placeholder> is the place holder") .upper())
        print(Fore.MAGENTA + "\n\n\n -- Please Provide the Templete After writing you Message Also Use <placeholder> for templete Placeholder and ***Bold*** for bold something  For Example: -- ")
        print( Fore.LIGHTYELLOW_EX + """\n***SHort_text_Bold***: <PlaceHolder> templete can be any type!\n\nFor Example: message_for_GPT -> Generate some 3 Random Names.\nTemplete is: <firstName> and Last name is <Lastname>\n\nOutput is: <harry> and last name is <potter> => Harry and Last name is Potter""")
        print(Fore.RED + "\n\n\n --- ALERT!! DON'T WRITE TEMPLETE OVER HERE WE'WILL LET YOU KNOW WHEN TO WRITE TEMPALTE BUT FOR KNOW WRITE YOUR MESSAGE ---")
        
        prompt = input(Fore.GREEN + "\n what you want to ask  from ChatGPT: ")
        if prompt == 'Q':
            break
        else:
            print( Fore.RED+ "\n\n * Please Provide Some Templete NOW * If you Want to give new line use '\+n = Add them' ")
            temp_late = input(Fore.CYAN+"Write Your Templete: ")
            temp_pattern = Templete_Pattern(prompt,temp_late)
            print("\n\n",temp_pattern)
    

    # COgnitive Verifier Pattern
    elif message == '3':
        print(Fore.RED + "\t\t\t The Example Of Cognitive Verifier Pattern".upper())
        print(Fore.CYAN + normal_Pattern("Act as a Prompt Engineer and Tell me what is Cognitive Verifier Pattern in Prompt Engineering also generate me Some Exaples keep it simple."))
        print(Fore.LIGHTCYAN_EX + "\n\n\t\t Cognitive Verifier Pattern Answer ")
        prompt = input(Fore.GREEN + "\n Write Your Message To ChatGPT: ")
        if prompt == 'Q':
            break
        else:
            cognitive = Cognitive_Verifier(prompt)
            print("\n\n",cognitive)
    
    # Refinement Pattern
    elif message == '4':
        print(Fore.RED + "\t\t\t The Example Of Refinement Pattern".upper())
        print(Fore.CYAN + normal_Pattern("Act as a Prompt Engineer and Tell me what is Refinement Pattern in Prompt Engineering also generate me Some Examples keep it simple."))
        print(Fore.BLUE + "\n\n\t\t Refinement Pattern Answer ")
        prompt = input(Fore.GREEN + "\n Write Your Message To ChatGPT: ")
        if prompt == 'Q':
            break
        else:
            refinement = Refinement_Pattern(prompt)
            print("\n\n",refinement)
    
    elif message == 'Q':
        break
