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
            
            #index_content = open('content.index.html').read()
            #finished_index_page = template.replace('{{content}}', index_content)
            #open('docs/index.html', 'w+').write(finished_index_page)
            
            filename = page['filename']
            title = page['title']
            output = page['output']
            
            content = open(filename).read()
            template = template.replace('{{content}}', content)
            template = template.replace('{{title}}', title)
            
            open(output, 'w+').write(template)
            #print(blog_content)
            
            
#           contact_content = open('content/contact.html').read()
#           finished_contact_page = template.replace('{{content}}', contact_content)
#           open('docs/contact.html', 'w+').write(finished_contact_page)
            

if __name__=='__main__':
    main()    
