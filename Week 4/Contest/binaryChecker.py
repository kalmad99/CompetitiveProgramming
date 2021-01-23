class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


def check_binary_search_tree_(root):
    res = []
    res = inordered(root)
    for i in range(len(res)-1):
        if res[i] >= res[i+1]:
            return False
    return True


def inordered(node):
    output = []
    if node:
        output = inordered(node.left)
        output.append(node.data)
        output += inordered(node.right)
    return output
    # return (inordered(node.left) + [node.data] + inordered(node.right)) if node else []
