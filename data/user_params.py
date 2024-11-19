 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.cell_cell_adhesion_strength = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.cell_cell_repulsion_strength = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.relative_maximum_adhesion_distance = FloatText(
          value=1.25,
          step=0.1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='use_function_to_set_relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.use_function_to_set_relative_maximum_adhesion_distance = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name5 = Button(description='set_relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.set_relative_maximum_adhesion_distance = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='use_function_to_set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.use_function_to_set_relative_equilibrium_distance = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name7 = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.set_relative_equilibrium_distance = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='use_function_to_set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.use_function_to_set_absolute_equilibrium_distance = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name9 = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.set_absolute_equilibrium_distance = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='relative multiplier', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='relative multiplier', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='relative multiplier', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'

        desc_button1 = Button(description='Cell-cell Adhesion Strength', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='Cell-cell Repulsion Strength', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='Maximum adhesion strength between cells', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='True, if you would like to use relative adhesion distance', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='Relative adhesion distance to cell radius', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='True, if you would like to set relative equilibrium distance', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='Relative equilibrium distance to cell radius', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='True, if you would like to set absolute equilibrium distance', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='Absolute equilibrium distance. ', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'

        row1 = [param_name1, self.cell_cell_adhesion_strength, units_button1, desc_button1] 
        row2 = [param_name2, self.cell_cell_repulsion_strength, units_button2, desc_button2] 
        row3 = [param_name3, self.relative_maximum_adhesion_distance, units_button3, desc_button3] 
        row4 = [param_name4, self.use_function_to_set_relative_maximum_adhesion_distance, units_button4, desc_button4] 
        row5 = [param_name5, self.set_relative_maximum_adhesion_distance, units_button5, desc_button5] 
        row6 = [param_name6, self.use_function_to_set_relative_equilibrium_distance, units_button6, desc_button6] 
        row7 = [param_name7, self.set_relative_equilibrium_distance, units_button7, desc_button7] 
        row8 = [param_name8, self.use_function_to_set_absolute_equilibrium_distance, units_button8, desc_button8] 
        row9 = [param_name9, self.set_absolute_equilibrium_distance, units_button9, desc_button9] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.cell_cell_adhesion_strength.value = float(uep.find('.//cell_cell_adhesion_strength').text)
        self.cell_cell_repulsion_strength.value = float(uep.find('.//cell_cell_repulsion_strength').text)
        self.relative_maximum_adhesion_distance.value = float(uep.find('.//relative_maximum_adhesion_distance').text)
        self.use_function_to_set_relative_maximum_adhesion_distance.value = ('true' == (uep.find('.//use_function_to_set_relative_maximum_adhesion_distance').text.lower()) )
        self.set_relative_maximum_adhesion_distance.value = float(uep.find('.//set_relative_maximum_adhesion_distance').text)
        self.use_function_to_set_relative_equilibrium_distance.value = ('true' == (uep.find('.//use_function_to_set_relative_equilibrium_distance').text.lower()) )
        self.set_relative_equilibrium_distance.value = float(uep.find('.//set_relative_equilibrium_distance').text)
        self.use_function_to_set_absolute_equilibrium_distance.value = ('true' == (uep.find('.//use_function_to_set_absolute_equilibrium_distance').text.lower()) )
        self.set_absolute_equilibrium_distance.value = float(uep.find('.//set_absolute_equilibrium_distance').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//cell_cell_adhesion_strength').text = str(self.cell_cell_adhesion_strength.value)
        uep.find('.//cell_cell_repulsion_strength').text = str(self.cell_cell_repulsion_strength.value)
        uep.find('.//relative_maximum_adhesion_distance').text = str(self.relative_maximum_adhesion_distance.value)
        uep.find('.//use_function_to_set_relative_maximum_adhesion_distance').text = str(self.use_function_to_set_relative_maximum_adhesion_distance.value)
        uep.find('.//set_relative_maximum_adhesion_distance').text = str(self.set_relative_maximum_adhesion_distance.value)
        uep.find('.//use_function_to_set_relative_equilibrium_distance').text = str(self.use_function_to_set_relative_equilibrium_distance.value)
        uep.find('.//set_relative_equilibrium_distance').text = str(self.set_relative_equilibrium_distance.value)
        uep.find('.//use_function_to_set_absolute_equilibrium_distance').text = str(self.use_function_to_set_absolute_equilibrium_distance.value)
        uep.find('.//set_absolute_equilibrium_distance').text = str(self.set_absolute_equilibrium_distance.value)
