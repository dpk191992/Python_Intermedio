DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
        all_python_devs = [worker ["name"] for worker in DATA if worker ["language"] == "python" ]
        all_platzi_devs = [trabajador ["name"] for trabajador in DATA if trabajador ["organization"] == "Platzi"]
        adultos = list(filter(lambda worker: worker ["age"] > 18, DATA))
        adultos = list(map(lambda worker: worker ["name"], adultos))

        python_devs = list(filter(lambda worker: worker ["language"]== "python", DATA))
        python_devs = list(map(lambda worker: worker ["name"], python_devs))
        for worker in python_devs:
            print(worker)




        ######mayores = list(map(lambda worker: worker | {"old": worker ["age"]> 70}, DATA))
        ###mayores = list(map(lambda worker: worker ["name"and "old"], mayores) )
        ###for worker in mayores:
           ### print(worker)
        
       ### for trabajador in all_platzi_devs:
          ###  print(trabajador)
        
        #for worker in all_python_devs:
         ###   print(worker)

if __name__ == "__main__":
    run()
