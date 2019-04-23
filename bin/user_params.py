 
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

        param_name1 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.tumor_radius = FloatText(
          value=250.0,
          step=10,
          style=style, layout=widget_layout)

        param_name2 = Button(description='oncoprotein_mean', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.oncoprotein_mean = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='oncoprotein_sd', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.oncoprotein_sd = FloatText(
          value=0.25,
          step=0.01,
          style=style, layout=widget_layout)

        param_name4 = Button(description='oncoprotein_min', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.oncoprotein_min = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name5 = Button(description='oncoprotein_max', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.oncoprotein_max = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='cancerous_astrocyte_non_motile_speed', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.cancerous_astrocyte_non_motile_speed = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='cancerous_astrocyte_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.cancerous_astrocyte_apoptosis_rate = FloatText(
          value=4.065e-5,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name9 = Button(description='cancerous_astrocyte_cell_cell_adhesion_strength', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.cancerous_astrocyte_cell_cell_adhesion_strength = FloatText(
          value=0.85,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='astrocyte_paracrine_secretion_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.astrocyte_paracrine_secretion_rate = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='astrocyte_paracrine_uptake_rate', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.astrocyte_paracrine_uptake_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name12 = Button(description='microglia_paracrine_uptake_rate', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.microglia_paracrine_uptake_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name13 = Button(description='astrocyte_paracrine_saturation_density', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.astrocyte_paracrine_saturation_density = FloatText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='increase_proliferation_threshold', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.increase_proliferation_threshold = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name15 = Button(description='become_migrating_threshold', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.become_migrating_threshold = FloatText(
          value=0.6,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='chemoattractant_secretion_rate', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.chemoattractant_secretion_rate = FloatText(
          value=0.7,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='microglia_motile_speed', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.microglia_motile_speed = FloatText(
          value=0.0001,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name18 = Button(description='microglia_macrophage_biasing_detection_threshold', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.microglia_macrophage_biasing_detection_threshold = FloatText(
          value=0.15,
          step=0.01,
          style=style, layout=widget_layout)

        param_name19 = Button(description='transfer_to_cancerous_threshold', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.transfer_to_cancerous_threshold = FloatText(
          value=1.1858,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='intrinsic_infection_rate', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.intrinsic_infection_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name21 = Button(description='infection_density_capacity', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.infection_density_capacity = FloatText(
          value=1000,
          step=100,
          style=style, layout=widget_layout)

        param_name22 = Button(description='viral_replication_rate', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.viral_replication_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name23 = Button(description='no_of_viruses_in_initial_injection', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.no_of_viruses_in_initial_injection = FloatText(
          value=500,
          step=10,
          style=style, layout=widget_layout)

        param_name24 = Button(description='virus_replication_minimum', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.virus_replication_minimum = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name25 = Button(description='secretion_rate_vein_wall_cell', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.secretion_rate_vein_wall_cell = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name26 = Button(description='time_of_first_injection', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.time_of_first_injection = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name27 = Button(description='time_of_second_injection', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.time_of_second_injection = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name28 = Button(description='time_of_third_injection', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.time_of_third_injection = FloatText(
          value=200,
          step=10,
          style=style, layout=widget_layout)

        param_name29 = Button(description='TRAIL_secretion_rate', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.TRAIL_secretion_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name30 = Button(description='TRAIL_killing_level', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.TRAIL_killing_level = FloatText(
          value=1e-3,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name31 = Button(description='Model_flag', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.Model_flag = IntText(
          value=3,
          step=0.1,
          style=style, layout=widget_layout)

        param_name32 = Button(description='TRAIL_generation_rate', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.TRAIL_generation_rate = FloatText(
          value=3,
          step=0.1,
          style=style, layout=widget_layout)

        param_name33 = Button(description='M', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.M = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        units_button1 = Button(description='micron', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'

        row1 = [param_name1, self.tumor_radius, units_button1, desc_button1] 
        row2 = [param_name2, self.oncoprotein_mean, units_button2, desc_button2] 
        row3 = [param_name3, self.oncoprotein_sd, units_button3, desc_button3] 
        row4 = [param_name4, self.oncoprotein_min, units_button4, desc_button4] 
        row5 = [param_name5, self.oncoprotein_max, units_button5, desc_button5] 
        row6 = [param_name6, self.random_seed, units_button6, desc_button6] 
        row7 = [param_name7, self.cancerous_astrocyte_non_motile_speed, units_button7, desc_button7] 
        row8 = [param_name8, self.cancerous_astrocyte_apoptosis_rate, units_button8, desc_button8] 
        row9 = [param_name9, self.cancerous_astrocyte_cell_cell_adhesion_strength, units_button9, desc_button9] 
        row10 = [param_name10, self.astrocyte_paracrine_secretion_rate, units_button10, desc_button10] 
        row11 = [param_name11, self.astrocyte_paracrine_uptake_rate, units_button11, desc_button11] 
        row12 = [param_name12, self.microglia_paracrine_uptake_rate, units_button12, desc_button12] 
        row13 = [param_name13, self.astrocyte_paracrine_saturation_density, units_button13, desc_button13] 
        row14 = [param_name14, self.increase_proliferation_threshold, units_button14, desc_button14] 
        row15 = [param_name15, self.become_migrating_threshold, units_button15, desc_button15] 
        row16 = [param_name16, self.chemoattractant_secretion_rate, units_button16, desc_button16] 
        row17 = [param_name17, self.microglia_motile_speed, units_button17, desc_button17] 
        row18 = [param_name18, self.microglia_macrophage_biasing_detection_threshold, units_button18, desc_button18] 
        row19 = [param_name19, self.transfer_to_cancerous_threshold, units_button19, desc_button19] 
        row20 = [param_name20, self.intrinsic_infection_rate, units_button20, desc_button20] 
        row21 = [param_name21, self.infection_density_capacity, units_button21, desc_button21] 
        row22 = [param_name22, self.viral_replication_rate, units_button22, desc_button22] 
        row23 = [param_name23, self.no_of_viruses_in_initial_injection, units_button23, desc_button23] 
        row24 = [param_name24, self.virus_replication_minimum, units_button24, desc_button24] 
        row25 = [param_name25, self.secretion_rate_vein_wall_cell, units_button25, desc_button25] 
        row26 = [param_name26, self.time_of_first_injection, units_button26, desc_button26] 
        row27 = [param_name27, self.time_of_second_injection, units_button27, desc_button27] 
        row28 = [param_name28, self.time_of_third_injection, units_button28, desc_button28] 
        row29 = [param_name29, self.TRAIL_secretion_rate, units_button29, desc_button29] 
        row30 = [param_name30, self.TRAIL_killing_level, units_button30, desc_button30] 
        row31 = [param_name31, self.Model_flag, units_button31, desc_button31] 
        row32 = [param_name32, self.TRAIL_generation_rate, units_button32, desc_button32] 
        row33 = [param_name33, self.M, units_button33, desc_button33] 

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
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)

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
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.oncoprotein_mean.value = float(uep.find('.//oncoprotein_mean').text)
        self.oncoprotein_sd.value = float(uep.find('.//oncoprotein_sd').text)
        self.oncoprotein_min.value = float(uep.find('.//oncoprotein_min').text)
        self.oncoprotein_max.value = float(uep.find('.//oncoprotein_max').text)
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.cancerous_astrocyte_non_motile_speed.value = float(uep.find('.//cancerous_astrocyte_non_motile_speed').text)
        self.cancerous_astrocyte_apoptosis_rate.value = float(uep.find('.//cancerous_astrocyte_apoptosis_rate').text)
        self.cancerous_astrocyte_cell_cell_adhesion_strength.value = float(uep.find('.//cancerous_astrocyte_cell_cell_adhesion_strength').text)
        self.astrocyte_paracrine_secretion_rate.value = float(uep.find('.//astrocyte_paracrine_secretion_rate').text)
        self.astrocyte_paracrine_uptake_rate.value = float(uep.find('.//astrocyte_paracrine_uptake_rate').text)
        self.microglia_paracrine_uptake_rate.value = float(uep.find('.//microglia_paracrine_uptake_rate').text)
        self.astrocyte_paracrine_saturation_density.value = float(uep.find('.//astrocyte_paracrine_saturation_density').text)
        self.increase_proliferation_threshold.value = float(uep.find('.//increase_proliferation_threshold').text)
        self.become_migrating_threshold.value = float(uep.find('.//become_migrating_threshold').text)
        self.chemoattractant_secretion_rate.value = float(uep.find('.//chemoattractant_secretion_rate').text)
        self.microglia_motile_speed.value = float(uep.find('.//microglia_motile_speed').text)
        self.microglia_macrophage_biasing_detection_threshold.value = float(uep.find('.//microglia_macrophage_biasing_detection_threshold').text)
        self.transfer_to_cancerous_threshold.value = float(uep.find('.//transfer_to_cancerous_threshold').text)
        self.intrinsic_infection_rate.value = float(uep.find('.//intrinsic_infection_rate').text)
        self.infection_density_capacity.value = float(uep.find('.//infection_density_capacity').text)
        self.viral_replication_rate.value = float(uep.find('.//viral_replication_rate').text)
        self.no_of_viruses_in_initial_injection.value = float(uep.find('.//no_of_viruses_in_initial_injection').text)
        self.virus_replication_minimum.value = float(uep.find('.//virus_replication_minimum').text)
        self.secretion_rate_vein_wall_cell.value = float(uep.find('.//secretion_rate_vein_wall_cell').text)
        self.time_of_first_injection.value = float(uep.find('.//time_of_first_injection').text)
        self.time_of_second_injection.value = float(uep.find('.//time_of_second_injection').text)
        self.time_of_third_injection.value = float(uep.find('.//time_of_third_injection').text)
        self.TRAIL_secretion_rate.value = float(uep.find('.//TRAIL_secretion_rate').text)
        self.TRAIL_killing_level.value = float(uep.find('.//TRAIL_killing_level').text)
        self.Model_flag.value = int(uep.find('.//Model_flag').text)
        self.TRAIL_generation_rate.value = float(uep.find('.//TRAIL_generation_rate').text)
        self.M.value = float(uep.find('.//M').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//oncoprotein_mean').text = str(self.oncoprotein_mean.value)
        uep.find('.//oncoprotein_sd').text = str(self.oncoprotein_sd.value)
        uep.find('.//oncoprotein_min').text = str(self.oncoprotein_min.value)
        uep.find('.//oncoprotein_max').text = str(self.oncoprotein_max.value)
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//cancerous_astrocyte_non_motile_speed').text = str(self.cancerous_astrocyte_non_motile_speed.value)
        uep.find('.//cancerous_astrocyte_apoptosis_rate').text = str(self.cancerous_astrocyte_apoptosis_rate.value)
        uep.find('.//cancerous_astrocyte_cell_cell_adhesion_strength').text = str(self.cancerous_astrocyte_cell_cell_adhesion_strength.value)
        uep.find('.//astrocyte_paracrine_secretion_rate').text = str(self.astrocyte_paracrine_secretion_rate.value)
        uep.find('.//astrocyte_paracrine_uptake_rate').text = str(self.astrocyte_paracrine_uptake_rate.value)
        uep.find('.//microglia_paracrine_uptake_rate').text = str(self.microglia_paracrine_uptake_rate.value)
        uep.find('.//astrocyte_paracrine_saturation_density').text = str(self.astrocyte_paracrine_saturation_density.value)
        uep.find('.//increase_proliferation_threshold').text = str(self.increase_proliferation_threshold.value)
        uep.find('.//become_migrating_threshold').text = str(self.become_migrating_threshold.value)
        uep.find('.//chemoattractant_secretion_rate').text = str(self.chemoattractant_secretion_rate.value)
        uep.find('.//microglia_motile_speed').text = str(self.microglia_motile_speed.value)
        uep.find('.//microglia_macrophage_biasing_detection_threshold').text = str(self.microglia_macrophage_biasing_detection_threshold.value)
        uep.find('.//transfer_to_cancerous_threshold').text = str(self.transfer_to_cancerous_threshold.value)
        uep.find('.//intrinsic_infection_rate').text = str(self.intrinsic_infection_rate.value)
        uep.find('.//infection_density_capacity').text = str(self.infection_density_capacity.value)
        uep.find('.//viral_replication_rate').text = str(self.viral_replication_rate.value)
        uep.find('.//no_of_viruses_in_initial_injection').text = str(self.no_of_viruses_in_initial_injection.value)
        uep.find('.//virus_replication_minimum').text = str(self.virus_replication_minimum.value)
        uep.find('.//secretion_rate_vein_wall_cell').text = str(self.secretion_rate_vein_wall_cell.value)
        uep.find('.//time_of_first_injection').text = str(self.time_of_first_injection.value)
        uep.find('.//time_of_second_injection').text = str(self.time_of_second_injection.value)
        uep.find('.//time_of_third_injection').text = str(self.time_of_third_injection.value)
        uep.find('.//TRAIL_secretion_rate').text = str(self.TRAIL_secretion_rate.value)
        uep.find('.//TRAIL_killing_level').text = str(self.TRAIL_killing_level.value)
        uep.find('.//Model_flag').text = str(self.Model_flag.value)
        uep.find('.//TRAIL_generation_rate').text = str(self.TRAIL_generation_rate.value)
        uep.find('.//M').text = str(self.M.value)
