import re

# Sample HTML string
html_string = '''<p>This is a paragraph.</p>
<div class="example">Example Div</div>
<img src="image.jpg" alt="description">
<p>Another paragraph.</p>
<div class="example">Another Example</div>
<img src="image2.jpg" alt="another description">'''

# Extract content inside <p> tags
p_tags = re.findall(r'<p>(.*?)<\/p>', html_string, re.DOTALL)

# Extract content inside <div class="example"> tags
div_tags = re.findall(r'<div class="example">(.*?)<\/div>', html_string, re.DOTALL)

# Extract src and alt attributes from <img> tags
img_tags = re.findall(r'<img\s+src="([^"]+)"\s+alt="([^"]*)">', html_string)

# Print extracted data
print("Paragraphs:", p_tags)
print("Divs with class 'example':", div_tags)
print("Image tags (src and alt):", img_tags)
