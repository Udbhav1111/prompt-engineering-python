import os
from dotenv import load_dotenv
import openai
from colorama import init
from colorama import Fore, Back, Style
init()

load_dotenv()
key = os.getenv("KEY")



def normal_Pattern(message):
    
    """
    Help TO Connect ChatGpt to Python With an APi KEY

    Args:
        str: message

    Returns:
        str: response
    """

    openai.api_key = key
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": message},
    ])
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return (result)



def Persona_Pattern(message):
    persona = f"Act as a Person or as a professor or as a developer having good experience throught the industry and answer my question talk me like a person and answer my question which is {message}"
    normal_ouput = normal_Pattern(message)
    persona_result = normal_Pattern(message=persona)
    return (Fore.LIGHTBLUE_EX +'\033[1m'+' Normal Output:'+ '\033[0m'+normal_ouput+ Fore.LIGHTMAGENTA_EX+"\n\n\n"+'\033[1m' +"Persona Pattern "+ '\033[0m' +":"+persona_result)



def Templete_Pattern(message,templete=False):
    if templete == False or templete == '':
        templete = "< NewsHeading >: < News >"
    if message == False or message == '':
        message = "Generate 3 Randoms News for me in IT industry"
    
    templete_prompt = f"""{message} I will Provide you a templete and for This templete <placeholder> is my placeholder for content which i used in templete 
                        try to fill the output in one or more placeholder Please preserve the formatting and overall templete that i provided also make sure for <placeholder> and how it is written what content should come inside place holder is also given by me
                        My Templete is: {templete}"""
    template_result = normal_Pattern(templete_prompt)
    return (Fore.LIGHTBLUE_EX +'\033[1m'+' Normal Output:'+ '\033[0m'+normal_Pattern(message) + Fore.LIGHTMAGENTA_EX+"\n\n\n"+'\033[1m' +"Template Pattern "+ '\033[0m' +":"+template_result)



def Cognitive_Verifier(message):
    
    cognitive_verifier = f"""Whenever i asked a question to you follow these rules generate a number of addtional questional that would
                            help you more accurately answer the question Combine the answer to the individual question to produce the final answer
                            to the overall Question!! Now My questin is {message}"""
    output_verifier = normal_Pattern(cognitive_verifier)
    return (Fore.LIGHTBLUE_EX +'\033[1m'+' Normal Output:'+ '\033[0m'+normal_Pattern(message) + Fore.LIGHTMAGENTA_EX+"\n\n\n"+'\033[1m' +"Cognitive Verifier Pattern "+ '\033[0m' +":"+output_verifier)


def Refinement_Pattern(message):
    pattern_prompt = f"""From Now On If i ask Any Question first answer my question and in the end Suggest a better Version of that question and Ask me if I want to use that Instead. Now My question is : {message}"""
    output_refinement = normal_Pattern(pattern_prompt)
    return (Fore.LIGHTBLUE_EX +'\033[1m'+' Normal Output:'+ '\033[0m'+normal_Pattern(message) + Fore.LIGHTMAGENTA_EX+"\n\n\n"+'\033[1m' +"Refinement Pattern "+ '\033[0m' +":"+output_refinement)



    
    