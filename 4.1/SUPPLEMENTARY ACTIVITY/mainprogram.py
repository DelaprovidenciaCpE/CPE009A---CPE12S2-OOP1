from projectilemotion import projectilemotion_solver

velocity = 11.0  
angle = 20.0     

distance, height = projectilemotion_solver(velocity, angle)

print(f"Horizontal Distance: {distance:.2f} meters")
print(f"Maximum Height: {height:.2f} meters")


