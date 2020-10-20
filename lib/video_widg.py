import ipywidgets
from ipywidgets import *
from IPython.display import display, Markdown

all_options=[]
all_answers=[]
all_feedback=[]

options1=['A development board','An operating system','An open-source project and framework','A Python-based game']
ans1='An open-source project and framework'
fb1=['Not quite--a PYNQ board can be referred to as a development board, but this doesn\'t emcompass all of what PYNQ is.','Incorrect--operating systems take care of a computer\'s basic functions. Examples include various versions of Linux and Windows systems, and don\'t include PYNQ.','Correct! PYNQ is a framework developed by Xilinx to integrate Python and Python based applications within an FPGA architecture. \'PYNQ\' comes from Python + ZYNQ--Zynq referring to a specific FPGA architecture developed by Xilinx.','Incorrect--PYNQ is not a game, but you can certainly create one with the help of PYNQ.']

all_options.append(options1); all_answers.append(ans1); all_feedback.append(fb1)

options2=['PyCharm','Jupyter Notebooks','Visual Studio Code','BlueJ']
ans2='Jupyter Notebooks'
fb2=['Incorrect! Python is a Python IDE (integrated development environment), but not the one that is readily installed with PYNQ.','Correct! Jupyter Notebooks is already installed and usable on the PYNQ right out of the box. It\'s a cell-based coding environment that uses kernels to help you compile and run your (in this case, Python) code. With Jupyter Notebooks you can create .ipynb files or regular .py files. This quiz was built using Jupyter!','Visual Studio Code is a popular code editor, but isn\'t as well suited for our purposes as another answer.','BlueJ is a coding environment for the Java programming language, written in Java. Cool, but not appropriate for those coding in Python.']

all_options.append(options2); all_answers.append(ans2); all_feedback.append(fb2)

options3=['Plug the board into your computer for power, set the boot jumper to SD, and turn it on.','Power the board, connect your computer to the board, turn it on, and load the PYNQ image onto the MicroSD with the OS on the device.','Load PYNQ image onto MicroSD card, set the boot jumper, connect the board to power, connect computer to device, and turn it on.','Set the boot jumper to SD, place the MicroSD with a pre-loaded PYNQ image in the device, and connect the board with Ethernet.']
ans3='Load PYNQ image onto MicroSD card, set the boot jumper, connect the board to power, connect computer to device, and turn it on.'
fb3=['Incorrect; recall what is needed to start the board properly outside of the hardware setup.','Incorrect; recall the order of the setup steps.','Correct! Have the board setup instructions on hand so you don\'t forget any necessary steps.','Incorrect; recall that you have to interact with the device through a computer.']

all_options.append(options3); all_answers.append(ans3); all_feedback.append(fb3)

options4=['APIs','Layers','Notebooks','Overlays']
ans4='Overlays'
fb4=['An API (or "Application Programming Interface") is the software link between the user and the application. While this is the incorrect answer, and API is what allows you to interact with the correct answer.','A "layer" may refer to a "layer" in an application software stack, among other things, but in this case, this is the incorrect answer.','You may have first been exposed to Python or PYNQ through the use of iPython notebooks (like the one you\'re currently using), which provides an easy to use, cell-based coding environment.','Correct! An PYNQ overlay is essentially a hardware design that is used to configure the architecture of your device as an FPGA.']

all_options.append(options4); all_answers.append(ans4); all_feedback.append(fb4)

options5=['Bitstream (*.bit),  Jupyter Notebook (*.ipynb)','Bitstream (*.bit), Hardware Handoff (*.hwh)','Hardware Handoff (*.hwh), Jupyter Notebook (*ipynb)',' Java Archive (*.jar), Text (.txt)']
ans5='Bitstream (*.bit), Hardware Handoff (*.hwh)'
fb5=['Close-- but you don\'t necessarily need a Jupyter notebook to deploy a PYNQ system, though those notebooks are used to interact with the device.','Correct! The bitstream is what is loaded onto the device to configure its architecture. The hardware hand-off file contains a lot of information about the system on which your application is running--including info on clocks, IPs, and various system settings, among other things. Tip: You can also save the .tcl file created from Vivado to rebuild the hardware block diagram if necessary.','Close-- but you don\'t necessarily need a Jupyter notebook to deploy a PYNQ system, though those notebooks are used to interact with the device.','Not quite--recall what files are created in Vivado to work with the PYNQ framework.']

all_options.append(options5); all_answers.append(ans5); all_feedback.append(fb5)

options6=['FPGA, RPi, Arduino', 'FPGA, Arduino, RPi', 'Arduino, RPi, FPGA', 'RPi, FPGA, Arduino']
ans6='Arduino, RPi, FPGA'
fb6_a='Try again! Refer to the "What is an FPGA?" notebook, the dropdown widget above, or try to recall what best differentiates these devices from each other.'
fb6_b='Correct! As we know, an FPGA\'s architecture is user defined through configuration, while you can differentiate the RPi and Arduino microcontrollers through, for example, their proximity to peripherals, or specifying which is running an operating system.'
fb6=[fb6_a, fb6_a, fb6_b, fb6_a]

all_options.append(options6); all_answers.append(ans6); all_feedback.append(fb6)

options7 = ['Load/program the logic ciruit','Load/program the arm microprocessor','Load/program the configuration memory layer in the FPGA','Load/program the ZYNQ 7020 chip']
ans7 = 'Load/program the configuration memory layer in the FPGA'
fb7_a = 'Incorrect'
fb7_b = 'Incorrect'
fb7_c = 'Correct'
fb7_d = 'Incorrect'
fb7 = [fb7_a,fb7_b,fb7_c,fb7_d]

all_options.append(options7); all_answers.append(ans7); all_feedback.append(fb7)

options8 = ['Arm Application microprocessor, real-time microcontroller','integrated programmable logic, Linux','Arm Application microprocessor, real-time microcontroller, integrated programmable logic, Linux','None of these features']
ans8 = 'Arm Application microprocessor, real-time microcontroller, integrated programmable logic, Linux'
fb8_a = 'Incorrect'
fb8_b = 'Incorrect'
fb8_c = 'Correct'
fb8_d = 'Incorrect'
fb8 = [fb8_a,fb8_b,fb8_c,fb8_d]

all_options.append(options8); all_answers.append(ans8); all_feedback.append(fb8)

options9 = ['ZYNQ 7020','XADC','The ARM microprocessor','Not on the board']
ans9 = 'ZYNQ 7020'
fb9_a = 'Correct'
fb9_b = 'Incorrect'
fb9_c = 'Incorrect'
fb9_d = 'Incorrect'
fb9 = [fb9_a,fb9_b,fb9_c,fb9_d]

all_options.append(options9); all_answers.append(ans9); all_feedback.append(fb9)

options10 = ['TRUE','FALSE']
ans10 = 'TRUE'
fb10_a = 'Correct'
fb10_b = 'Incorrect'
fb10 = [fb10_a,fb10_b]

all_options.append(options10); all_answers.append(ans10); all_feedback.append(fb10)


options11 = ['Conda install','PIP install','APT-get install','Easy-install']
ans11 = 'PIP install'
fb11_a = 'Try again. install conda sets up the environment, not a specific package'
fb11_b = 'Correct! Pip can be used to install Python packages outside of a virtual environment like conda. '
fb11_c = 'Incorrect, this command is used in Linux terminals, and is not used for PYNQ installs. '
fb11_d = 'Incorrect'

all_options.append(options11); all_answers.append(ans11); all_feedback.append(fb11)

options12 = ['ASIC, SoC, FPGA, MPSoC','FPGA, SoC, ASIC, MPSoC','SoC, ASIC, FPGA, MPSoC','ASIC, MPSoC, FPGA, SoC']
ans12 = 'ASIC, SoC, FPGA, MPSoC'
fb12_a = 'Correct! We know ASICs are application specific. The other three descriptions can apply to an FPGA, but you can determine the correct answer from the mention of other components and multiple processors.'
fb12_b = 'Incorrect! Go back to the beginning of this notebook to review info on these four terms.'
fb12_c = 'Incorrect! Go back to the beginning of this notebook to review info on these four terms.'
fb12_d = 'Incorrect! Go back to the beginning of this notebook to review info on these four terms.'

all_options.append(options12); all_answers.append(ans12); all_feedback.append(fb12)

options13 = ['Verilog','JHDL','Ruby','VHDL']
ans13 = 'Ruby'
fb13_a = 'Incorrect; look at the examples given in the notebook. Don\'t be afraid to look up a language that looks unfamiliar to you.'
fb13_b = 'Incorrect; look at the examples given in the notebook. Don\'t be afraid to look up a language that looks unfamiliar to you.'
fb13_c = 'Correct! Ruby is a high-level programming language that isn\'t used in designing hardware.'
fb13_d = 'Incorrect; look at the examples given in the notebook. Don\'t be afraid to look up a language that looks unfamiliar to you.'

all_options.append(options13); all_answers.append(ans13); all_feedback.append(fb13)

options14 = ['The size of the FPGA','The size of a feature on an FPGA','The maximum routing distance between IP','The physical size of a processor on an SoC']
ans14 = 'The size of a feature on an FPGA'
fb14_a = 'Incorrect; remember that an FPGA is a silicon component.'
fb14_b = 'Correct! An FPGA 'feature' refers to the elements on an FPGA, like a transistor, and smaller features means more can be fit in the same space, which is why you hear the number growing smaller as newer devices are developed. A higher number of features can imply (though not always) higher performance and power.'
fb14_c = 'Incorrect; routing is not often measured and monitored in this way.'
fb14_d = 'Incorrect; not all FPGA devices are SoCs.'

all_options.append(options14); all_answers.append(ans14); all_feedback.append(fb14)

options15 = ['A .tcl script','An HDL file','An IP block','A bitstream']
ans15 = 'A bitstream'
fb15_a = 'Incorrect; a tcl script is used to rebuild your design, as it includes commands for Vivado to use.'
fb15_b = 'Incorrect; HDL is used when developing the hardware, but is not loaded into the device.'
fb15_c = 'Incorrect; IP are building blocks in your hardware design.'
fb15_d = 'Correct! A bitstream is created based on your design, which is what is loaded onto the device in order for it to function as the designer intends.'

all_options.append(options15); all_answers.append(ans15); all_feedback.append(fb15)



###

ardesc='An Arduino comes with a microcontroller. Unlike a Raspberry Pi, it does not have an operating system and can only run programs that were created and compiled specifically for Arduino boards, mostly written in C++. They\'re good for low-power applications and driving hardware, and are relatively easy to use, which has made them popular for robotics projects and teaching.'
rpi_desc='Raspberry Pis come with a microprocessor. They\'re pretty powerful, and have a variety of I/O options--with an RPi, you can use an SD cards, USB devices, HDMI displays, etc. You\'re also free to run it with almost any programming language.'
fpga_desc='FPGA stands for Field Programmable Gate Array. As you saw from the presentation, they are usable only after they\'ve been configured, creating a device whose architecture is customized for your task. This makes them efficient, adaptable, and useful for plenty of applications--medical devices, spacecrafts, self-driving cars, etc. Shown below is an evaluation board, with a Spartan-6 FPGA.'

platform_options=[('Arduino', 0), ('Raspberry Pi', 1), ('FPGA', 2)]
p_val=0
p_desc='Platform'
platform_img_paths=['images/arduino_uno.jpg','images/rpi.jpg','images/fpga.jpg']
plat_imgs=[];
for i in platform_img_paths:
    file=open(i, "rb")
    image=file.read()

    plat_imgs.append(image)
    
platform_descs=[ardesc,rpi_desc,fpga_desc]
platforms=widgets.Dropdown(
    options=platform_options,
    value=p_val,
    description=p_desc,
    disabled=False,
)

#Use with an interact widget to create a drowndown menu that displays an image and description based on dropdown selection. 
#dd_option: Dropdown input; img_paths: list of image paths corresponding with index of dropdown selection;
#desc_list: list of description strings corresponding with index of dropdown selection

def platform_dropdown(dd_option, img_wgs, desc_list):
    image=img_wgs[dd_option];
    desc=desc_list[dd_option]
    img = widgets.Image(
        value=image,
        format='png',
        width=300,
        align='center'
    )
    display(Markdown('\n'+desc))
    display(img)
    return

def pop_platforms():
    t=widgets.interactive(platform_dropdown, desc_list=fixed(platform_descs), img_wgs=fixed(plat_imgs), dd_option=platforms)
    return t

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
