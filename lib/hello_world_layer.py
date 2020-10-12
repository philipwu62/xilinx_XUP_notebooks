from __future__ import unicode_literals, print_function
import ipywidgets
from ipywidgets import *
from IPython.display import display, Markdown
import random
from prompt_toolkit import print_formatted_text, HTML
import markdown

hw_desc = markdown.markdown('<h3> Hardware Layer </h3>  Pynq utilizes overlays to build its system. <br> <br> **Overlays** are hardware libraries, similar to software libraries, and are used to configure for different applications. In PYNQ, overlays are the hardware system designs. Overlays extend the applications from the Processing System (PS) to the PL, and has the IP needed for accelerating designs. Some examples include image processing, edge detection, thresholding, filtering. The base overlay includes Pynq packages. <br> <br> Overlays contains the following: <ul> <li> Bitstream </li> <li> Tcl file to expose IP </li> <li> API to expose IP </li> </ul> <p>To enable overlays in a Jupyter Notebook, the follow code can be inserted:</p> <code> from pynq </code> <br> <code> import Ovelay overlay = Overlay(''/[path to bit file]/base.bit'') </code>')

sw_desc = markdown.markdown('<h3> Software Layer </h3> Running on PCs and embedded systems, the Linux kernel is an open source platform that offers customization for designs and applications. Linux accesses the following peripherals (or hardware ports) on the PYNQ boards: <ul> <li> SD/MicroSD cards </li><li> Ethernet </li> <li> UART</li> <li> USB </li> </ul> <p> Programmers utilize Python with PYNQ, which is a high level programming language used to program PYNQ board. There is API available so the board can interact with the Linux Kernel </p>')

app_desc = markdown.markdown ('<h3> Application Layer </h3> Integrated with Python, programmers can utilize the following Python libraries: <ul> <li> **OpenCV**: contains functions used for real-time computer vision </li> <li>**Sci-Kit Learn**: includes various classification, regression, clustering algorithms </li> <li>**Numpy**: supports large, multi-dimensional arrays and matrices, with high-level mathematical functions </li> <li>**Matplotlib**: utilizes Python for plotting and graphing data </li> <br> <p> For Pynq environment, programmers use Jupyter Notebook. This platform utilizes Python softtware language to create applications. This program makes code appear neat and interactive. </p> ')


platform_options=[('Hardware', 0), ('Software', 1), ('Application', 2)]
p_val=0
p_desc='Layer'
platform_img_paths=['imgs/Hardward_Layer.JPG','imgs/Software_layer.JPG','imgs/Application_layer.JPG'] 
platform_descs=[hw_desc,sw_desc,app_desc]
platforms=widgets.Dropdown(
    options=platform_options,
    value=p_val,
    description=p_desc,
    disabled=False,
)


def platform_dropdown(dd_option, img_paths, desc_list):
    img_path=img_paths[dd_option];
    desc=desc_list[dd_option]
    
    file=open(img_path, "rb")
    image=file.read()
    display(Markdown('\n'+desc))
    img = widgets.Image(
        value=image,
        format='png',
        width=1000,
        height=700,
        align='center'
    )
    display(img)
    return


question_text=[];
options=[];
answers=[];

#q1
question_text.append('What is PYNQ?')
options.append(['A development board','An operating system','An open-source project and framework','A Python-based game'])
answers.append('An open-source project and framework')
#q2
question_text.append('Which of the following environments is used with PYNQ?')
options.append(['PyCharm','Jupyter Notebooks','Visual Studio','BlueJ'])
answers.append('Jupyter Notebooks')
#q3
question_text.append('What is the standard way to create a PYNQ image for a custom board?')
options.append(['Via Petalinux HDF file','Via Petalinux BOOT.BIN file','Via Petalinux BSP file','Via Petalinux image.ub'])
answers.append('Via Petalinux BOOT.BIN file')
#q5
question_text.append('With PYNQ, hardware system designs are referred to as:')
options.append(['APIs','Layers','Notebooks','Overlays'])
answers.append('Overlays')

def questions_list():
    questions=[];
    for i in range(len(question_text)):
        questions.append(show_buttons(options[i],question_text[i],answers[i],func=None, args=None))
    random.shuffle(questions)
    return questions

#Display interactive radio buttons with a given HTML description
def show_buttons(options, description, answer, func=None, args=None):
    radios=RadioButtons(
        description=' ',
        options=options,
        disabled=False,
        layout={'width': 'max-content'}
    )
    text=ipywidgets.HTML(
        value='<h2>'+ description+'</h2>')
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