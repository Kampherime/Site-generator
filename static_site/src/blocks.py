
paragraph = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.             

* This is the first list item in a list block
* This is a list item   
* This is another list item               







'''


def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split("\n\n")
    return_list = []    
    # this is really stupid
    for block in list_of_blocks:
        checkable_block = block.strip()
        if checkable_block == "":
            continue
        return_list.append(checkable_block)
    return return_list

print(markdown_to_blocks(paragraph))


