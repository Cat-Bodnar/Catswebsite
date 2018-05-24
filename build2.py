top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

content = open('contents/bio.html').read ()
bio_html = top_template + content + bottom_template
open('contents/bio.html','w+').write(bio_html)

content = open('contents/contact.html').read()
contact_html = top_template + content + bottom_template
open('contents/contact.html', 'w+').write(contact_html)

content = open('contents/blog.html').read()
blog_html = top_template + content + bottom_template
open ('contents/blog.html','w+').write(blog_html)


