def main():
        
        pages = [
            {
                'filename': 'content/index.html',
                'output': 'docs/index.html',
                'title':'Bio',
            },
            {
                'filename': 'content/blog.html',
                'output': 'docs/blog.html',
                'title': 'My Blog',
            },
            {
                'filename': 'content/contact.html',
                'output': 'docs/contact.html',
                'title': 'Contact Me',
            }
        ]
    
        for page in pages:
        
            template = open('templates/base.html').read()
            
            
            filename = page['filename']
            title = page['title']
            output = page['output']
            
            content = open(filename).read()
            template = template.replace('{{content}}', content)
            template = template.replace('{{title}}', title)
            
            open(output, 'w+').write(template)
            
            

if __name__=='__main__':
main() 







phase 212

def main():


pages = [
           {
               'filename': 'content/index.html',
               'output': 'docs/index.html',
                'title':'Bio',
            },
            {
                'filename': 'content/blog.html',
                'output': 'docs/blog.html',
                'title': 'My Blog',
            },
            {
                'filename': 'content/contact.html',
                'output': 'docs/contact.html',
                'title': 'Contact Me',
            }
        ]

import glob

all_html_files = glob.glob("content/*.html")

print(all_html_files)







import os

file_path = "content/blog.html"
file_name = os.path.basename(file_path)

name_only, extension = os.path.splitext(file_name)


for page in pages:
        
            template = open('templates/base.html').read()
            
            
            filename = page['filename']
            title = page['title']
            output = page['output']
            
            content = open(filename).read()
            template = template.replace('{{content}}', content)
            template = template.replace('{{title}}', title)
            
            open(output, 'w+').write(template)
            
            

if __name__=='__main__':
main() 
