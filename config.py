import sorts

sort_options = (
    ("bubble", sorts.BubbleSort),
    ("insertion", sorts.InsertionSort),
    ("selection", sorts.SelectionSort),
    ("merge", sorts.MergeSort),
    ("inplacemerge", sorts.InPlaceMergeSort),
    ("quick", sorts.Quicksort),
    ("bogo", sorts.Bogosort)
)

with open("config.txt") as f:
    data = f.read().replace(" ", "").split("\n")

config_data = {}
for line in data:
    if not "=" in line:continue
    var, value = line.split("=")
    name, type_ = var.split(":")
    if type_ == "int":config_data[name] = int(value)
    elif type_.startswith("tuple"):
        if "int" in type_:config_data[name] = tuple([int(i) for i in value.split(",")])
        elif "float" in type_:config_data[name] = tuple([float(i) for i in value.split(",")])
    elif type_ == "sort":
        for sort_name, sort_class in sort_options:
            if sort_name == value:config_data[name] = sort_class

ELEMENTS = config_data["ELEMENTS"] # Number of elements in Sortable
WINDOW_SIZE = config_data["WINDOW_SIZE"] # Window size
FILL_COLOR = config_data["FILL_COLOR"] # Background color
CANVAS_WIDTH = config_data["CANVAS_WIDTH"]
CANVAS_HEIGHT = config_data["CANVAS_HEIGHT"] # Area for the sorting bars (Values from 0 to 1, minimum to maximum)

SORTING_AREA_WIDTH = (CANVAS_WIDTH[1] - CANVAS_WIDTH[0]) * WINDOW_SIZE[0]
SORTING_AREA_HEIGHT = (CANVAS_HEIGHT[1] - CANVAS_HEIGHT[0]) * WINDOW_SIZE[1]

bar_width = SORTING_AREA_WIDTH / ELEMENTS # Average width per bar
filled_height = SORTING_AREA_HEIGHT / ELEMENTS # Height within the sorting area

SORT = config_data["SORT"]
SPEED = config_data["SPEED"]