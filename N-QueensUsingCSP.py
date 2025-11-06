import tkinter as tk
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk  # make sure Pillow is installed: pip install pillow
class N_Queen:
    def __init__(self, N):
        self.domains = {i: list(range(1, N+1)) for i in range(1, N+1)}
        self.constraints = dict()
        self.assignments = dict()
        self.build_constraints()
        # GUI setup
        self.N = N
        self.cell_size = 50
        self.window_size = N * self.cell_size
        self.root = tk.Tk()
        self.root.title(f"{N}-Queens Visualization")
        self.canvas = tk.Canvas(self.root, width=self.window_size, height=self.window_size)
        self.canvas.pack()

    def forward_check(self, variable, value):
        assigned_variable_neighbours = self.constraints[variable]
        pruned_values = dict()

        for neighbour in assigned_variable_neighbours:
            pruned_domains = []
            if neighbour in self.assignments:
                continue
            for neighbour_domain in self.domains[neighbour]:
                if not self.is_consistent(variable, value, neighbour, neighbour_domain):
                    pruned_domains.append(neighbour_domain)

            for pruned_domain in pruned_domains:
                self.domains[neighbour].remove(pruned_domain)

            if len(pruned_domains) != 0:
                pruned_values[neighbour] = pruned_domains

            if len(self.domains[neighbour]) == 0: #if failure occurs(all the domains are pruned)
                return False, pruned_values
        return True, pruned_values    

    def restore_domains(self, pruned_values):
        for variable, pruned_domain in pruned_values.items():
            self.domains[variable].extend(pruned_domain)
        

        
    def build_constraints(self):
        for variable in self.domains:
            self.constraints[variable] = [neighbour for neighbour in self.domains if neighbour != variable]

    def is_consistent(self, selected_variable, selected_variable_value, neighbor, neighbor_value):
        # variable = column, value = row
        return (selected_variable_value != neighbor_value) and (abs(selected_variable_value - neighbor_value) != abs(selected_variable - neighbor))
          
    def get_MRV(self):
            MRV = [] #key = smallest domain length, value = list of variables with smallest domain length
            smallest_domain_length = None
            for variable, domain in self.domains.items():
                if variable in self.assignments:
                    continue
                if MRV == [] or smallest_domain_length > len(domain):
                    MRV = [variable]
                    smallest_domain_length = len(domain)
                elif smallest_domain_length == len(domain):
                    MRV.append(variable)

            #check degree heuristics
            if len(MRV) > 1:
                MRV_degree = [None, -1]
                for variable in MRV:
                    constraint_size = len(self.constraints[variable])
                    if constraint_size > MRV_degree[1]:
                        MRV_degree = [variable, constraint_size]
                return MRV_degree[0]
            
            elif len(MRV) == 0:
                return None
            else:
                return MRV[0]
  
               
    
    def get_LCV(self, selected_variable):
        variable, domain = selected_variable, self.domains[selected_variable]
        variable_neighbors = [neighbor for neighbor in self.constraints[variable] if neighbor not in self.assignments]
        LCV = dict()
        for domain_value in domain:
            eliminations = 0
            for neighbor in variable_neighbors:
                for neighbor_value in self.domains[neighbor]:
                    if not self.is_consistent(variable, domain_value, neighbor, neighbor_value):
                        eliminations += 1
            
            LCV[domain_value] =  eliminations

        LCV = sorted(LCV, key=LCV.get)
        return LCV
       
    def backtrack(self):
        #base case if all the variables are assigned all the values return True
        if len(self.assignments) == len(self.domains):
            return True
        
        variable = self.get_MRV()
        LCV_list = self.get_LCV(variable)

        for LCV in LCV_list:
            self.assignments[variable] = LCV
            self.draw_board(active_variable=variable)
            no_failure, pruned_values = self.forward_check(variable, LCV)
            if no_failure:
                if self.backtrack() == True:
                    return True
            #restore when there is a failure currently or there is a failure ahead
            self.restore_domains(pruned_values)
            del self.assignments[variable]
        return False
                
    def forward_checking_algo(self):
        if self.backtrack():
            print('solution found')
        else:
            print('no solution exists')
    
    

    def draw_board(self, active_variable=None):
        """Draws the N-Queens board with an optional active highlight."""
        self.canvas.delete("all")

        # --- Lazy-load and cache queen image ---
        if not hasattr(self, "_queen_image"):
            from urllib.request import urlopen
            from io import BytesIO
            from PIL import Image, ImageTk

            image_url = (
                "https://static.wikia.nocookie.net/chess/images/4/42/"
                "LightQueen.png/revision/latest/scale-to-width/360?cb=20230320152643"
            )
            with urlopen(image_url) as response:
                img_data = response.read()

            img = Image.open(BytesIO(img_data))
            size = self.cell_size - 12  # padding for neat fit
            img = img.resize((size, size), Image.Resampling.LANCZOS)
            self._queen_image = ImageTk.PhotoImage(img)

        # --- Draw board cells ---
        for col in range(1, self.N + 1):
            for row in range(1, self.N + 1):
                x1, y1 = (col - 1) * self.cell_size, (row - 1) * self.cell_size
                x2, y2 = col * self.cell_size, row * self.cell_size

                # Modern chessboard color palette
                base_color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"
                color = "#F6F668" if active_variable == col else base_color

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

                # --- Draw queen image if assigned ---
                if col in self.assignments and self.assignments[col] == row:
                    cx, cy = x1 + self.cell_size // 2, y1 + self.cell_size // 2
                    self.canvas.create_image(cx, cy, image=self._queen_image)

        self.root.update()
        self.root.after(500)


queen = N_Queen(8)

queen.forward_checking_algo()