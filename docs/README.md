# docs 

A place for other project-related documentation. 

## Generating Diagrams 

### Prerequisites

-[PlantUML](https://plantuml.com/)

### Folder Structure

- `graph/`: Put all your UML diagram source here. 
- `img/`: Generated image will go here automatically. 

### Run

Once installed, run the `generate_graphs.sh` script. 

If a diagram already has a corresponding image (e.g. `graph/my_diagram.uml` and `img/my_diagram.png` both exist), then the script skips that diagram. You can either delete the image before running the script or invoke PlantUML manually: 

```
$ plantuml graph/my_diagram.uml -o img/
```
where `-o` option denotes the output destination folder. The above command will result in `img/my_diagram.png` being generated forcibly even if it exists already. 

You can also use an online tool (https://www.planttext.com/) for quick diagramming. 
