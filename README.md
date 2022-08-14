it is a project creating my personal blog 
https://startbootstrap.com/previews/clean-blog I used this form and changed a bit with python flask framework

1. I divided header and footer section for multiple uses with {% include %} tag of jinja template.
2. I replace blog's posts into post-data.txt by using npoint.io. and render it by using {% for %} tag in html file.
3. I made 'contact' page work with contact_page/send_email func/smtplib module
- when request.method is 'POST'(when you pess 'send' button), context written in contact page will be sent
- contact page will be show 'Successfully Sent you message!'
- witho send_email function, message will be sent to my gmail address (Currently not working because of changed Gmail policy)                                                      
