import ipywidgets
from ipywidgets import *
from IPython.display import display, Markdown
import random

flow_options=[('PS',0),('PL',1),('ARM',2),('DRAM',3),('AXI Interconnects',4),('Resize IP',5),('Datawidth Converter IP',6),('DMA',7)]
flow_description='Flow Components: '
flow_default=0
ps='The <em>PS</em> or processing system is the device\'s software interface that allows the user to interact with the device logic.'
arm='<em>ARM</em> refers to the core of the processing system, an integral part of the "system" in "system on chip". The PYNQ PS is built around the ARM Cortex-A9 processor.'
dram='<em>DRAM</em> stands for Dynamic Random Access Memory, and is the device\'s read and write memory. It contains data used by Python, which is copied for use in the programmable logic.' 
axi='The PS and PL interface with each other through <em>AXI Interconnects</em>, which facilitate the movement of data between the two. \n em>Note:</em> "GP" refers to general purpose interconnects, while "HP" refers to high performance interconnects.'
pl='The <em>PL</em> or programmable logic refers to the logic that is configured to match your design. We think of the PS being built around the processing core, and the PL being built around the FPGA.'
resize='The <em>Resize IP</em> contains all the logic required for the actual resizing application. Our original data streams through as an input, an the resized images are its outputs. As you can see--a lot more than logic design goes into using hardware for this application.'
dma='The <em>DMA IP</em> (Direct Memory Access), in this context, allows for the quick movement of data between the PS and PL, bypassing the processor.'
dwc='The <em>datawidth converter IP</em> IP converts data of a certain width to data of another certain width, in accordance with what\'s required within the design. As you can see, the Resize IP takes a stream with a 24-bit width, and the DMA IP takes a 32-bit width stream.'
desc_list=[ps,pl,arm,dram,axi,resize,dwc,dma]

def flowdd():
    dropdown(flow_options, flow_default, flow_description, desc_list)

def dropdown(options, default, desc, desc_list):

    def platform_dropdown(dd_option, desc_list):
        desc=desc_list[dd_option]
        print('\n')
        display(Markdown(desc))
    
    dd=Dropdown(
        options=options,
        value=default,
        description=' ',
        disabled=False,
    )
    dd_int=interactive(platform_dropdown, dd_option=dd, desc_list=fixed(desc_list))
    display(Markdown(desc),dd_int)
    

    
    
        