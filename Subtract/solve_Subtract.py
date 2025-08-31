from PIL import Image

#Create arrays to check for duplicates
counts = [[0 for _ in range(500)] for _ in range(500)]
duplicate_coordinates = []

#Open the file
with open('coordinates.txt', 'r') as file:
    for line in file:
	#Get the x, y coords from each line
        line = line.strip().replace('(', '').replace(')', '')
        x_coord, y_coord = line.split(',')
        x = int(x_coord)
        y = int(y_coord)

    #Check for duplicates
    for x in range(500):
    	for y in range(500):
            if counts[x][y] > 1:
                duplicate_coordinates.append((x, y))

# Create a new image
image = Image.new('RGB', (500, 500), 'white')
pixels = image.load()

#Set the duplicate coords to be black
for x, y in duplicate_coordinates:
    pixels[x, y] = (0, 0, 0)

#Save the image
image.save('flag.png')