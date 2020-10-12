import ipywidgets
from ipywidgets import *
from IPython.display import display, Markdown
import random

question_text=[];
options=[];
answers=[];
correct=[]

question_text.append('What does our image data need to go through before being resized?')
options.append(['DRAM, DMA, Resize IP','PIL Image conversion, DRAM, AXI interconnect, DMA, data width conversion, resize IP','DRAM, PIL image conversion, DMA, AXI interconnect, data width conversion, resize IP'])
answers.append('PIL Image conversion, DRAM, AXI interconnect, DMA, data width conversion, resize IP')
correct.append('PIL Image conversion is basic data processing that is required for use within an application--be it an machine learning algorithm or a resizer. C is also incorrect as we know the AXI interconnect does not interface directly with the data width conversion IP.')

question_text.append('True or False: The DRAM connects directly to the DMA to share data between the PS and PL.')
options.append(['True','False'])
answers.append('False')
correct.append('The DMA is used so that the resizer can access data from the PS DRAM, but the DMA and the DRAM communicate through the AXI interconnects.')


def questions_list():
    questions=[];
    for i in range(len(question_text)):
        questions.append(show_buttons(options[i],question_text[i],answers[i],func=show_correct_text, args=[correct,i]))
    #random.shuffle(questions)
    return questions

def show_correct_text(text_list,index):
    display(HTML('Correct! '+text_list[index]))
    

#Display interactive radio buttons with a given HTML description
def show_buttons(options, description, answer, func=None, args=None):
    radios=RadioButtons(
        description=' ',
        options=options,
        disabled=False,
        layout={'width': 'max-content'}
    )
    text=ipywidgets.HTML(
        value='<h2>'+ description)
    interactive_q=interactive(mc_interact,mc_val=radios, answer=fixed(answer), func=fixed(func), args=fixed(args))
    return VBox([text, interactive_q])
        
# interactive function, changing value: mc_val
def mc_interact(mc_val, answer, func=None, args=None):
    if mc_val == answer:
        if func:
            if args:
                func(*args)
            else:
                func()
        else: 
            display(Markdown('Correct!'))
    else:
        display(Markdown('  '))