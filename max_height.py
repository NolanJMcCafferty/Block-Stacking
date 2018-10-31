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
        # get the box dimensions from the given line
        dims = [int(x) for x in line.split()]
        # store dimensiobs for box object
        box = {'width': dims[0], 'height': dims[1], 'depth': dims[2]} 
        box_types.append(box)

# make all 3 rotations of each box type
rotations = []
for box_type in box_types:
    # for simplicity always make depth smaller than or equal to width
    rotations.append({'height': box_type['height'], 'width': max(box_type['width'], box_type['depth']), 'depth': 
                      min(box_type['width'], box_type['depth']), 'area': box_type['width']*box_type['depth']})
    rotations.append({'height': box_type['width'], 'width': max(box_type['height'], box_type['depth']), 'depth': 
                      min(box_type['height'], box_type['depth']), 'area': box_type['height']*box_type['depth']})
    rotations.append({'height': box_type['depth'], 'width': max(box_type['width'], box_type['height']), 'depth': 
                      min(box_type['width'], box_type['height']), 'area': box_type['width']*box_type['height']})
   # sort the rotations in decreasing order by area
rotations.sort(key=operator.itemgetter('area'), reverse=True)
    
# function to compute max stack heights from the bottom up 
def get_max_height(rotations):
  # initialize the arrays
  max_heights = []
  num_blocks = []
  blocks_used = []
    
  # number of boxes
  num_boxes = len(rotations)

  # initialize the number of blocks and max height
  for i in range(num_boxes):
      num_blocks.append(0)
      max_heights.append(rotations[i]['height'])
    
  # loop through the boxes
  for i in range(num_boxes):
    max_heights[i] = 0
    height_rest = 0
    block_num = 0
    box = rotations[i]
    blocks_used.append([])
    blocks = []
       
    # loop through all the blocks with larger area
    for j in range(i):
      previous_box = rotations[j]
    
      # check if box can be stacked and the height of that stack is larger than our current height
      if box['width'] < previous_box['width'] and box['depth'] < previous_box['depth'] and height_rest < max_heights[j]:
        # update the max height, number of blocks used, and the blocks used
        height_rest = max_heights[j]
        block_num = num_blocks[j]
        blocks = blocks_used[j]
        
    # add variables from best possible stack with box i on top
    blocks_used[i] = blocks + [box]
    max_heights[i] = height_rest + box['height']
    num_blocks[i] = block_num + 1
    
  # find max height of all the possible top blocks
  max_height = max(max_heights)
  index = max_heights.index(max_height);

  # print out and return the results
  print('The tallest tower has', num_blocks[index], 'blocks and a height of', max_height)
  return max_height, num_blocks[index], blocks_used[index]

# run function on block types
max_height, num_blocks, blocks_used = get_max_height(rotations)

# write out results to outfile
with open(outfile, 'w') as outfile:
  outfile.write(str(num_blocks) + '\n')
  for block in blocks_used:
    outfile.write(str(block['depth']) + ' ' + str(block['width']) + ' ' + str(block['height']) + '\n')
