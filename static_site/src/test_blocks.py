from blocks import block_to_block_type, markdown_to_blocks
import re
import unittest


def debugging(string):
    print(re.match(r'(^|\n)#{1,6} ', string))
    print(re.match(r'(^|\n)`{3}(.*?)`{3}(\n|$)', string, re.DOTALL))
    print(re.match(r'>', string))
    print(re.match(r'\* ', string))
    print(re.match(r'[0-9]. ', string))


class TestBlocks(unittest.TestCase):


    # NEED TO UPDATE THE BLOCK TO BLOCK TYPE FUNCTION TO ACCOUNT FOR MULTIPLE TYPES OF HEADERS (h1 -> h6)
    def test_block_to_block_type(self):

        paragraph = '''# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.             

        * This is the first list item in a list block
        * This is a list item   
        * This is another list item               


        > quote
        > blocks
        > .jpg


        ```code
        block :)```

        1. line
        2. line
        3. line
        
        '''
        



        list_of_blocks = markdown_to_blocks(paragraph)
        print(list_of_blocks)
        for block in list_of_blocks:
            print(block)
            debugging(block)
            print(block_to_block_type(block))


