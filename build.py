pages = []

def generate_pages():
    #print('we are indeed here')
    import glob
    import os
        
    all_html_files = glob.glob('content/*.html')
    for filename in all_html_files:
        
        file_path = filename
        file_name = os.path.basename(file_path)
        
        output = os.path.join('docs', file_name)
        print(output)
        pages.append({
        'filename': filename,
        'output': output,
        })
       
    print(pages)    

    
    
    

def main():
    generate_pages()
    for page in pages:
    
        template = open('templates/base.html').read()
        
        
        filename = page['filename']
        #title = page['title']
        output = page['output']
        
        content = open(filename).read()
        template = template.replace('{{content}}', content)
        #template = template.replace('{{title}}', title)
        
        open(output, 'w+').write(template)
    print('success!')
        
            

if __name__=='__main__':
    main() 


