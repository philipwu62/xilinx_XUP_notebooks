import ipywidgets
from ipywidgets import *
from IPython.display import display, Markdown

all_options=[]
all_answers=[]
all_feedback=[]

options1=['ASIC, SoC, FPGA, MPSoC', 'FPGA, SoC, ASIC, MPSoC', 'SoC, ASIC, FPGA, MPSoC', 'ASIC, MPSoC, FPGA, SoC']
ans1='ASIC, SoC, FPGA, MPSoC'
fb1_a='Correct! We know ASICs are application specific. The other three descriptions can apply to an FPGA, but you can determine the correct answer from the mention of other components and multiple processors.'
fb1_b='Incorrect! Go back to the beginning of this notebook to review info on these four terms.'
fb1=[fb1_a, fb1_b, fb1_b, fb1_b]

all_options.append(options1); all_answers.append(ans1); all_feedback.append(fb1)

options2=['A','B','C']
ans2='B'
fb2_a='Incorrect; take a closer look at the diagram, and review to the gates discussed above.'
fb2_b='Correct! If B is changed to 1, the AND gate receives a 0 from the inverted B value. Because the AND gate is receiving to low inputs, its output is also low, and because A is also low, the OR gate will also be receiving two low inputs, making its output 0. On the flip side, switching either A or C to high, leaving the other two low, will result in D being high as well.'
fb2=[fb2_a, fb2_b, fb2_a]

all_options.append(options2); all_answers.append(ans2); all_feedback.append(fb2)

options3=['Verilog','JHDL','Ruby','VHDL']
ans3='Ruby'
fb3_a='Incorrect; look at the examples given in the notebook. Don\'t be afraid to look up a language that looks unfamiliar to you.'
fb3_b='Correct! Ruby is a high-level programming language that isn\'t used in designing hardware.'
fb3=[fb3_a, fb3_a, fb3_b, fb3_a]

all_options.append(options3); all_answers.append(ans3); all_feedback.append(fb3)

options4=['The size of the FPGA','The size of a feature on an FPGA','The maximum routing distance between IP','The physical size of a processor on an SoC']
ans4='The size of a feature on an FPGA'
fb4=['Incorrect; remember that an FPGA is a silicon component.',
'Correct! An FPGA \'feature\' refers to the elements on an FPGA, like a transistor, and smaller features means more can be fit in the same space, which is why you hear the number growing smaller as newer devices are developed. A higher number of features can imply (though not always) higher performance and power.',
'Incorrect; routing is not often measured and monitored in this way.', 
'Incorrect; not all FPGA devices are SoCs.']

all_options.append(options4); all_answers.append(ans4); all_feedback.append(fb4)

options5=['A .tcl script','An HDL file', 'An IP', 'A bitstream']
ans5='A bitstream'
fb5_1='Incorrect; a tcl script is used to rebuild your design, as it includes commands for Vivado to use.'
fb5_2='Incorrect; HDL is used when developing the hardware, but is not loaded into the device.'
fb5_3='Incorrect; IP are building blocks in your hardware design.'
fb5_4='Correct! A bitstream is created based on your design, which is what is loaded onto the device in order for it to function as the designer intends. '
fb5=[fb5_1, fb5_2, fb5_3, fb5_4]

all_options.append(options5); all_answers.append(ans5); all_feedback.append(fb5)

def populate_questions():
    questions=[]
    for i in range(len(all_options)):
        questions.append(show_buttons(all_options[i], all_answers[i], all_feedback[i]))
    return questions


def show_buttons(options, answer, feedback):
    radios=RadioButtons(
        description=' ',
        options=options,
        disabled=False,
        layout={'width': 'max-content'}
    )
    interactive_q=interactive(mc_interact,mc_val=radios, options=fixed(options), feedback=fixed(feedback))
    return interactive_q
        
# interactive function, changing value: mc_val
def mc_interact(mc_val, options, feedback):
    fb_text=feedback[options.index(mc_val)]
    display(Markdown(fb_text))