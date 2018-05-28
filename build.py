

def main(run_page):
    top = open('templates/top.html').read()
    bottom = open('templates.bottom.html').read()
    content = open('contents/index.html').read ()
    index_html = top_template + content + bottom_template
    open('contents/index.html','w+').write(index_html)

    content = open('contents/contact.html').read()
    contact_html = top_template + content + bottom_template
    open('contents/contact.html', 'w+').write(contact_html)

    content = open('contents/blog.html').read()
    blog_html = top_template + content + bottom_template
    open ('contents/blog.html','w+').write(blog_html)

    
    



if __name__='__main__':
    main(run_page)    
