import re

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

def block_to_block_type(block):
    if re.match(r'(^|\n)#{1,6} ', block) != None:
        return "heading"
    if re.match(r'(^|\n)`{3}(.*?)`{3}(\n|$)', block, re.DOTALL) != None:
        return "code"
    if re.match(r'> ', block) != None:
        return "quote"
    if re.match(r'\* ', block) != None or re.match(r'- (.*?)', block) != None:
        return "unordered list"
    if re.match(r'[0-9]. ', block) != None:
        return "ordered list"
    return "text"


