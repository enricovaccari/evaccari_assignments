# import importlib
# module_names = [('sys',), ('os',)]

# def Importer(m_name):
#     module = importlib.import_module(m_name[0])
    
#     if len(m_name) > 1:
#         globals()[x[1]] = module

# print(module_names)
# for x in module_names:
#     print(len(x))
#     print(x[0])
#     Importer(x)



# # print(sys.path)
# # # x = os.getcwd()
# # # print('THIS: ' + x)










# import importlib
# import sys
# sys.path.append('C:/Users/Vaccari/Desktop/test')
# sys.path.append('C:/Users/Vaccari/Desktop/test2')

# module_names = [('script','s'), ('script','s2')]

# def Importer(m_name):
#     module = importlib.import_module(m_name[0])
    
#     if len(m_name) > 1:
#         globals()[x[1]] = module


# for x in module_names:
#     Importer(x)

# s.f()
# s2.f()


# import importlib
# import os

# command = 'cd C:/Users/Vaccari/Desktop/test.py'
# os.system(command)

# alias = 't2'
# alias = 't3'

# myVars = globals()
# print(myVars)

# myVars[alias] = importlib.import_module('C:/Users/Vaccari/Desktop/test.py')
# print(t2)


import yaml
yml_path = r"C:\Users\Vaccari\Desktop\config_test.yml"

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
    pipeline_data = yaml.safe_load(stream)