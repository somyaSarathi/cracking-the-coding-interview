class vertex:
  def __init__(self, val, *edges):
    if val == None:
      raise TypeError
    
    self.data = val
    self.edges = []
    
    if edges:
      for edge in edges:
        self.edges.append(edge)
        
    return
  
  
  def __str__(self):
    return self.val.__str__()
