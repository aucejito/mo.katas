# mo.katas Python + Flask

## Requisitos
pip install Flask

## He asumido que
- Cuando se despliega el rover en una posición donde hay un obstáculo, te avisa y se corta la ejecución.
- Sobre el grid (o planeta) por donde viaja el rover se ha puesto, por comodidad, que por defecto no tenga obstáculos.
- En caso de no reconocer un comando lo ignora y para la ejecución, aborta la secuencia.

## Body for sample API request
- POST - http://127.0.0.1:5000/grid - {"size":[3,3],"name":"Mars","obstacles":[[1,1]] } - Crea un planeta
- POST - http://127.0.0.1:5000/rover - {"init_pos":[0,0],"init_orient":"N"} - Lanza un rover
- POST - http://127.0.0.1:5000/move - {"moves":["f", "b", "r", "f","l","f"]} - Mueve el rover
