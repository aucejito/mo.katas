from flask import Flask, jsonify, request, render_template
from sympy import content
from grid import Grid
from rover import Rover

app = Flask(__name__)

grid = None
rover = None

@app.route('/grid', methods=['GET', 'POST'])
def get_set_grid():
    global grid
    if(request.method=="GET"):
        if(grid is None):
            return "Initialize a planet / grid!"
        else:
            return jsonify({'name':grid.name,'size':(grid.size_x, grid.size_y), 'obstacles': grid.obstacles})
    elif(request.method=="POST"):
        content=request.json
        size = content["size"]
        name = content["name"]
        obstacles = content["obstacles"]
        obstacles_tuples = []
        for obs in obstacles:
            obstacles_tuples.append((obs[0],obs[1]))
        grid = Grid(size[0], size[1],name,obstacles_tuples)
        return "Planet created correctly"

@app.route('/rover', methods=['GET', 'POST'])
def get_set_rover():
    global rover, grid
    if(request.method=="GET"):
        if(rover is None):
            return "Initialize a rover!"
        if(grid is None):
            return "Initialize a grid!"
        else:
            return jsonify({'pos':(rover.x, rover.y), 'orientation': rover.orientation, 'planet':grid.name})
    elif(request.method=="POST"):
        content=request.json
        init_pos = content["init_pos"]
        init_orient = content["init_orient"]
        rover = Rover(init_pos[0],init_pos[1],init_orient,grid)
        return "Rover launched correctly"

@app.post('/move')
def move_rover():
    if(rover is None):
        return "Initialize a rover first!"
    elif(grid is None):
        return "Initialize a planet first!"

    content = request.json
    if 'moves' in content:
        rover.move(content["moves"])
    return jsonify({'pos':(rover.x, rover.y), 'orientation': rover.orientation})
    
if __name__ == '__main__':
  
    app.run(debug = True)