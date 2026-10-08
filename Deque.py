from collections import deque

#Function check whether a block is clear
def is_clear(state, block):
  for b, position in state:
    if position == block:
      return False
  #Generate possible moves
  def generate_moves(state, blocks):
    moves = []
    for block in blocks:
      # Block must be clear
      for b, position in state:
        if not is_clear(state, block):
          continue
      #find current possition
      current_position = None
      for b, position in state:
        if b == block:
          current_position = position
          break
      #New block to table
      if current_position !="Table":
        new_state = set(state)
        new_state.remove((block,current_position))
        new_state.add((block,"Table"))
        moves.append((frozenset(new_state),
                     f"Move {block} from {current_position} to Table"))
      # Move block onto another block
      for destination in blocks:
        if block==destination:
          continue
        #Destination must be claer
        if not is_clear(state, destination):
          continue
        #Don't move to the same position
        if current_position == destination:
          continue
        new_state = set(state)
        new_state.remove((block,current_position))
        new_state.add((block,destination))
        moves.append((frozenset(new_state),
                     f"Move {block} from {current_position} to {destination}"))
    return moves
#BSF function
def block_world(initial_state, goal_state,blocks):
  queue = deque()
  queue.append((initial_state, []))
  visited = set()
  while queue:
    state, path = queue.popleft()
    if state in visited:
      continue