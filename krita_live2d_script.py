from krita import *

"""
backup first!
"""

doc = Krita.instance().activeDocument()
merge_down_keyword = "_MergeDown"
flatten_keyword = "_Flatten"
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

        if child.name().endswith(merge_down_keyword):
            print(f"MergeDown: {child.name()}")
            child.mergeDown()
            
        if child.name().endswith(flatten_keyword):
            print(f"Flatten: {child.name()}")
            target_name = child.name()[:-len(flatten_keyword)]

            # create a empty layer below
            empty_layer = doc.createNode(target_name, "paintLayer")
            duplicate = child.duplicate()
            
            # add empty layer and duplicate layer
            node.addChildNode(duplicate, child)
            node.addChildNode(empty_layer, child)
            
            # if layer is inheritAlpha, disable it, if not, layer will be nothing
            inherit_alpha = duplicate.inheritAlpha()
            if inherit_alpha:
                duplicate.setInheritAlpha(False)
            
            # using mergeDown to flatten
            duplicate.mergeDown()
            
            # if layer was inheritAlpha, enable it
            duplicate.setInheritAlpha(inherit_alpha)
            
            # remove original layer
            child.remove()

        if child.name().endswith(LR_keyword):
            split_layer(node, child)

root = doc.rootNode()
process_layers(root)

doc.refreshProjection()
Krita.instance().action('file_save_as').trigger()
