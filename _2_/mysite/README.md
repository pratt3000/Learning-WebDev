### lecture notes/ progress journal : 

### video 1,2 : 
1. created main app
2. directed it through the main/url.py and mysite/urls.py file to homepage, which is default "", basically got rid of the default python page
3. Displayed content on the home page on main/views.py
4. added a tutorial model to add tutorials for the website and added it to main/admin.py where the orientation is decided

### video 3 : 
1. now we have the TextField, but we need editing tools, so added a preexisting app TinyMCE in mysite/settings, also added its settings (copy pasted) 
2. then in  main.admin.py added the widget TinyMCE by importing and overriding the form field->textfield and set widget->TinyMCE; and viola we now have a fully functional text editor to wite paragraphs!!!

### Random notes : 
1. to comment multiple lines in python press (CTRL + '/') 
