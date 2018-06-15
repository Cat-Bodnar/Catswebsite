

pages = []

def main():
    #generate_pages()
    #print('we are indeed here')
    import glob
    import os
        
    all_html_files = glob.glob('content/*.html')
    for filename in all_html_files:
        
        file_path = filename
        file_name = os.path.basename(file_path)
        
        output = os.path.join('docs', file_name)
        
        pages.append({
        'filename': filename,
        'output': output,
        })
       
    #print(pages)   f 

    #generate_pages()
    #for page in pages:
    
import markdown
md = markdown.Markdown(extensions=["markdown.extensions.meta"])
data = """
index.html
"""
html = md.convert(data)
title = md.Meta["title"][0]
#print(title, "by", author)
print(html)

        
from jinja2 import Template
index_html = open('content/index.html').read()
template_html = open('templates/base.html').read()
template = Template(template_html)
result = template.render(
        title = 'This is the Title Page!',
        content = index_html
)
open('docs/index.html', 'w+').write(result)
      
blog_html = open('content/blog.html').read()
template_html = open('templates/base.html').read()
template = Template(template_html)
result = template.render(
        title = 'This is a Something Page!',
        content = blog_html
)
open('docs/blog.html', 'w+'). write(result) 

contact_html = open('content/contact.html').read()
template_html = open('templates/base.html').read()
template = Template(template_html)
result = template.render(
        title = 'I am Here!',
        content = contact_html
)
open('docs/contact.html', 'w+').write(result)  

     
        


        
        
        
        
        
        #filename = page['filename']
        #title = page['title']
        #output = page['output']
        
        #content = open(filename).read()
        #template = template.replace('{{content}}', content)
        #template = template.replace('{{title}}', title)
        
    #open(output, 'w+').write(template)
print('success!')
        
            

if __name__=='__main__':
    main() 


