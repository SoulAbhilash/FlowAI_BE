# from app.llm.parser import FlowParser
# To run "python -m ai_tools.app.main"
from  ai_tools.app.llm.parser import FlowParser
parser = FlowParser()

text = """
1. Open cart
2. check if the cart is empty
3. if empty then show 'nothing to show'
4. else show the all the cart contents
"""

flow_name = "My Cart Flow"

print(parser.parse(text=text, flow_name=flow_name))