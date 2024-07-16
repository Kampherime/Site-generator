import unittest
from linksntwinks import extract_markdown_links, extract_markdown_images
from blocks import markdown_to_blocks


class test_the_guys(unittest.TestCase):
    def test_most_cases(self):
        image_test = "We're going to try a random image I found off of google. The image is ![here](https://static.zerochan.net/Satanick.full.2589552.jpg)"
        try:
            images = extract_markdown_images(image_test)
            print(images)
        except Exception as e:
            print(f"failed to extract image because {e}")

        link_test = "We're going to try a link with the example url as [follows](https://www.example.com/)"

        try:
            links = extract_markdown_links(link_test)
            print(links)
        except Exception as e:
            print(f"Failed to extract link because {e}")

        paragraph = "Now we have to do something a little bit annoying. I'm going to write a paragraph where I include links to ![images](https://static.zerochan.net/Satanick.full.2589552.jpg) and links to [links](https://www.example.com/), then I have to include another example of an ![image](https://pm1.narvii.com/7464/ae3f1a47480bb1abe8fe81b8ba31ef6cd272b82dr1-720-719v2_hq.jpg) and another example of a [link :3](https://www.google.com/) to make sure everything works right. I'll test both before anything else"
        
        try: 
            links_from_paragraph = extract_markdown_links(paragraph)
            images_from_paragraph = extract_markdown_images(paragraph)
            print("LOOKING HERE ---------------------------------------------- LOOKING HERE")
            print(links_from_paragraph)
            print(images_from_paragraph)
        except Exception as e:
            print(f"Failed to do both because {e}")


    def test_blocks(self):
        paragraph = '''
        Paragraphs are separated by a blank line.

        2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
        look like:

          * this one
          * that one
          * the other one

        Note that --- not considering the asterisk --- the actual text
        content starts at 4-columns in.

        > Block quotes are
        > written like so.
        >
        > They can span multiple paragraphs,
        > if you like.

        Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
        in chapters 12--14"). Three dots ... will be converted to an ellipsis.
        Unicode is supported. ''' 
        print (paragraph)
        try:
            blocks = markdown_to_blocks(paragraph)
            for i in range(0, len(blocks)):
                print(f"Block number {i}: {blocks[i]}")
            print(blocks)
        except Exception as e:
            print(f"HEY LOOK HERE GOOBER GOOGUS JOKADSHJFOAUIJPHFGIOUPASDFASHUPJOAHVJPUSCJOKPASDNHGUIOJPHD {e}")

        blocks2 = ""
        print(markdown_to_blocks(blocks2))
