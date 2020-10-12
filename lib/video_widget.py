import ipywidgets as widgets
from IPython.display import display
from IPython.display import clear_output

def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Riktig." + '\x1b[0m' +"\n" +"\n"  "Correct! PYNQ is a framework developed by Xilinx to integrate Python and Python based applications within an FPGA architecture. 'PYNQ' comes from Python + ZYNQ--Zynq referring to a specific FPGA architecture developed by Xilinx."
        else:
            s = '\x1b[5;30;41m' + "Feil. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

Q1 = create_multipleChoice_widget('What is PYNQ?',['A development board','An operating system','An open-source project and framework','A Python-based game'], 'An open-source project and framework')
Q2 = create_multipleChoice_widget('lalalalal',['cat','dog','mouse'],'dog')
Q3 = create_multipleChoice_widget('jajajajaj',['blue','white','red'],'white')


def good_luck_with_the_quiz():
    print()
    for i in range(1,4):
        eval(f'display(Q{i})')
        print("\n" * 2)
        