import random

def talk(str, template):
    idx = int(random.uniform(0, len(template)))
    return template[idx]["forward"] + str + template[idx]["back"]