

def main():
    
    top = open('templates/top.html').read()
    bottom = open('templates/bottom.html').read()
    content = open('content/index.html').read ()
    
    index_html = top + content + bottom
    open('content/index.html','w+').write(index_html)

    content = open('content/contact.html').read()
    contact_html = top + content + bottom
    open('content/contact.html', 'w+').write(contact_html)

    content = open('content/blog.html').read()
    blog_html = top + content + bottom
    open ('content/blog.html','w+').write(blog_html)

    
    



if __name__=='__main__':
    main()    
