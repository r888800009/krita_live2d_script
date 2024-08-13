from krita import *

"""
backup first!
"""

doc = Krita.instance().activeDocument()
flat_keyword = "_MergeDown"
LR_keyword = "_LR"
Draft_keyword = "_Draft"

def split_layer(root_node, node):

    # Get the layer's size and position
    width, height = doc.width(), doc.height()

    # Calculate the midpoint
    mid_x = width // 2

    # Duplicate the layer
    left_layer = node.duplicate()
    right_layer = node.duplicate()

    # Rename the duplicated layers
    left_layer.setName(node.name()[:-len(LR_keyword)] + "_L")
    right_layer.setName(node.name()[:-len(LR_keyword)] + "_R")

    # Add them to the document
    root_node.addChildNode(left_layer, node)
    root_node.addChildNode(right_layer, node)

    # Crop the left layer to the right half
    right_layer.cropNode(0, 0, mid_x, height)

    # Crop the right layer to the left half
    left_layer.cropNode(mid_x, 0, width - mid_x, height)

    # Hide or delete the original layer if necessary
    print(f"splited: {node.name()}")
    node.remove()

def process_layers(node):
    for child in node.childNodes():
        process_layers(child)

        if not (isinstance(child, Node)): # and child.childNodes()):
            continue

        if child.name().endswith(Draft_keyword):
            print(f"clean: {child.name()}")
            child.remove()

        if child.name().endswith(flat_keyword):
            print(f"Flattening: {child.name()}")
            child.mergeDown()

        if child.name().endswith(LR_keyword):
            split_layer(node, child)

root = doc.rootNode()
process_layers(root)

doc.refreshProjection()
Krita.instance().action('file_save_as').trigger()
