import requests
import re
import IPython

def wsd(code):
    response = requests.post("http://www.websequencediagrams.com/index.php", data={
            'message': code,
            'apiVersion': 1,
        })
    expr = re.compile("(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")
    m = expr.search(response.text)
    if m == None:
        print("Invalid response from server.")
        return False
                            
    image=requests.get("http://www.websequencediagrams.com/" + m.group(0))
    return IPython.core.display.Image(image.content)