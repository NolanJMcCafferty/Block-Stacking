# import libraries
import operator
import sys

# read command line arguments in as file names
infile = sys.argv[1]
outfile = sys.argv[2]

# read in infile and construct initial box types
with open(infile, 'r') as infile:
    num_types = int(infile.readline())
    box_types = []
    for line in infile:
        #get the box dimensions from the given line
        dims = [int(x) for x in line.split()]
        #store dimensiobs for box object
        box = {'width': dims[0], 'height': dims[1], 'depth': dims[2]} 
        box_types.append(box)

# make all 3 rotations of each box type
rotations = []
for box_type in box_types:
    rotations.append({'height': box_type['height'], 'width': max(box_type['width'], box_type['depth']), 'depth': 
                      min(box_type['width'], box_type['depth']), 'area': box_type['width']*box_type['depth']})
    rotations.append({'height': box_type['width'], 'width': max(box_type['height'], box_type['depth']), 'depth': 
                      min(box_type['height'], box_type['depth']), 'area': box_type['height']*box_type['depth']})
    rotations.append({'height': box_type['depth'], 'width': max(box_type['width'], box_type['height']), 'depth': 
                      min(box_type['width'], box_type['height']), 'area': box_type['width']*box_type['height']})
rotations.sort(key=operator.itemgetter('area'), reverse=True)

def get_max_height(rotations):
  # initialize max height for each box
  max_heights = []
  num_blocks = []
  num_boxes = len(rotations)
  blocks_used = []
    
  for i in range(num_boxes):
      num_blocks.append(0)
      max_heights.append(rotations[i]['height'])
    
    # calculate max stack heights from the bottom up 
def get_max_height(rotations):
  # initialize max height for each box
  max_heights = []
  num_blocks = []
  num_boxes = len(rotations)
  blocks_used = []
    
  for i in range(num_boxes):
      num_blocks.append(0)
      max_heights.append(rotations[i]['height'])
    
  # calculate max stack heights from the bottom up 
  for i in range(num_boxes):
    max_heights[i] = 0
    height_rest = 0
    block_num = 0
    box = rotations[i]
    blocks_used.append([])
    blocks = []
        
    for j in range(i):
      previous_box = rotations[j]
      if box['width'] < previous_box['width'] and box['depth'] < previous_box['depth'] and height_rest < max_heights[j]:
        height_rest = max_heights[j]
        block_num = num_blocks[j]
        blocks = blocks_used[j]
    blocks_used[i] = blocks + [box]
    max_heights[i] = height_rest + box['height']
    num_blocks[i] = block_num + 1
  max_height = max(max_heights)
  index = max_heights.index(max_height);
  print('The tallest tower has', num_blocks[index], 'blocks and a height of', max_height)
  return max_height, num_blocks[index], blocks_used[index]

max_height, num_blocks, blocks_used = get_max_height(rotations)

with open(outfile, 'w') as outfile:
  outfile.write(str(num_blocks) + '\n')
  for block in blocks_used:
    outfile.write(str(block['depth']) + ' ' + str(block['width']) + ' ' + str(block['height']) + '\n')
