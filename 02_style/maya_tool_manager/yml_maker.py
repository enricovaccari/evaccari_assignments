from tkinter import PIESLICE
import yaml

yml_path = r'C:\Users\Vaccari\Desktop\maya_tool_manager\python.yml'



# write yaml file
user_data = [{'1. Why' : "Set your goals"},
             {'2. Coding Style' : ['Zen of Python',
              'Start with Style', 'Meta', 'Extras', 'References',
              'France', 'Spain']},
              {'3. Advanced Python' : ['Script Editor', 'Classes',
              'Decorator', 'Try and Except', '...']},
              {'4. UI scripts and design' : ['Script', 'Design',
              'Extras', 'Reference']}, ]

with open(yml_path, 'w') as outfile:
    yaml.dump(user_data, outfile, default_flow_style=False,
              allow_unicode=True)
# read yaml file
with open(yml_path, 'r') as stream:
    pipeline_data = yaml.load(stream)
    print(pipeline)
