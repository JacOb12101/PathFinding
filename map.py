import json
import random

class Map:
    def __init__(self, data_path):
        self.sector_list = self.getzones(data_path)['zones']

    def getzones(self, path):
        contents = ''
        with open(path, 'r') as file:
            contents = file.read()
        return json.loads(contents)

    def __str__(self):
        return str(self.sector_list)
    
    def create_path(self, starting_sector_name):

        current_sector = starting_sector_name
        pathed_sectors = [starting_sector_name]
        impossible_paths = {}
        
        while True:
            if len(pathed_sectors) == len(self.sector_list.keys()):
                break

            unpathed_sectors = []                    # unpathed for current sector
            for sector in self.sector_list[current_sector]['borders']:
                if sector not in pathed_sectors:
                    unpathed_sectors.append(sector)
            seq = ''.join(pathed_sectors)
            if seq in impossible_paths:
                for item in impossible_paths[seq]:
                    if item in unpathed_sectors:
                        unpathed_sectors.remove(item)
        

            if unpathed_sectors:
                while True:
                    current_sector = random.choice(unpathed_sectors)
                    seq = ''.join(pathed_sectors)
                    print(seq)
                    if seq in impossible_paths:
                        if current_sector not in impossible_paths[seq]:
                            break
                    else:
                        break
                pathed_sectors.append(current_sector)

            else:
                seq = ''.join(pathed_sectors[:-1])
                if seq in impossible_paths:
                    impossible_paths[seq].append(pathed_sectors[-1])
                else:
                    impossible_paths[seq] = [pathed_sectors[-1]]
                
                pathed_sectors.pop()
                current_sector = pathed_sectors[-1]

        return pathed_sectors



if __name__ == "__main__":
    path = "/Users/jzeld/Documents/hackathon/sector_data.json"
    map = Map(path)
    my_path = map.create_path("A")
    print(''.join(my_path))
