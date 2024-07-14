# creating a function called "split_delimiter" that well... splits strings :3c 
# it'll accept an argument to split strings and convert them to inline html x)


from textnode import TextNode #might need?

# okay lets do a bit of planning here
# what needs to happen is texttype nodes need to be split and checked for inline text
# if the node is not texttype then were gonna just add it to a list
# if the node is texttype we split it based on the delimiter and append textnodes 


#textnode: self, text, text_type, url

#there are so many issues present with that function

#im going to take a break from coding but the issues ive seen are as follows:

#bold (**) doesn't work because the program checks for one character delimiters.

#it checks every word, and therefore it wouldn't work for things like `block block`

#there are probably more :/ 

#couple problems that i need to address now.

# How am I going to take care of bold letters? 

# i could do something like, if the delimiter is in the string, split it by that part at that point

# then if its in the string again, take the beginning and end and make them a ___ block 


def split_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes: 
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        if delimiter in node.text:
            split_text = node.text.split(delimiter, 1)
            new_nodes.append(TextNode(split_text[0], "text", None))
            # if there is a split, then the first and last nodes would be text
            if delimiter in split_text[1]:
                appendable_node = split_text[1].split(delimiter, 1)
                new_nodes.append(TextNode(appendable_node[0], text_type, None))
                new_nodes.extend(split_delimiter([TextNode(appendable_node[1], "text", None)], delimiter, text_type))
    return(new_nodes)



                        






'''        
def split_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            # ugh this is ugly
            checkable_list = node.text.split()
            print(checkable_list)
            if len(checkable_list) == 1: # checking to see if anything was actually split based on the delimiter
                new_nodes.append(checkable_list[0])
            else:
                return_list = []
                temporary_string = ""
                for node_text in checkable_list: 
                    if node_text[0] == delimiter and node_text[len(node_text)-1] != delimiter:
                        raise Exception("Invalid markdown syntax")
                    if node_text[0] == delimiter and node_text[len(node_text)-1] == delimiter:
                        return_list.append(TextNode(temporary_string, "text", None))
                        temporary_string = ""
                        return_list.append(TextNode(f"{node_text} ", text_type, None))
                        print("it parsed right")
                    else:
                        temporary_string += f"{node_text} "
                return_list.append(TextNode(temporary_string, "text", None))
                new_nodes.extend(return_list)
    return new_nodes'''
