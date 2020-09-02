### lecture notes/ progress journal : 

### video 1,2 : 
1. created main app
2. directed it through the main/url.py and mysite/urls.py file to homepage, which is default "", basically got rid of the default python page
3. Displayed content on the home page on main/views.py
4. added a tutorial model to add tutorials for the website and added it to main/admin.py where the orientation is decided

### video 3 : 
1. now we have the TextField, but we need editing tools, so added a preexisting app TinyMCE in mysite/settings, also added its settings (copy pasted) 
2. then in  main.admin.py added the widget TinyMCE by importing and overriding the form field->textfield and set widget->TinyMCE; and viola we now have a fully functional text editor to wite paragraphs!!!

### video 4 :
1. in view this is how you link a html page :
    return render(request=request, template_name="main/home.html", context = {"tutorials": Tutorial.objects.all})
2. {{ variable }} & {% logic %}
3. putting "|safe" to render the variable into code. EG:{{variable|safe}}
4. javascript is put where needed, CSS is always put at the beginning.

### video 5 : 
1. added CSS "MaterialisticCSS" & navbar [copy-pasted HTML lol]
2. learnt how to use blocks {%block content%} {%endblock%}
3. how to include a html block in another... like import in python, at the top do {%extends "file path"%}
4. changed css by [ downloading scss source -> editing scss -> converting to css ->copying to "mysite/main/static/main/css" ->linking it in header.css  ]

### video 6 : 
1. making register.html page
2. {% csrf_token %} : cross site request forgery token -> security reasons-- so that noone tricks users to get info(for every form do it)
3. just build the form in django and catch it as a variable : {{form}}
4. add register in views, create the form variable in the function itself and return, also add in urls
5. add submit button 
6. {{form}} has attributes EG : as_table, as_p, etc ->its for styling so F 
7. In register function in views add the actual user creation code->adding to admin database.

### video 7 : 
1. added pop up messages while registering warning, success, info, etc
2. simplified the html code by making includes folder 

### video 8 : 
1. added logout,login functionality in views.py
2. made login.html
3. customised the default registertin for to accept emails too by making forms.py

### video 9 : 
1. created models for series and category in models.py
2. registered them in amin.py
3. viola!

### video 10 : 
1. used the foreign keys to fetch urls and display them using category.html.... major changes in views.py, added a single slug function to return the required url!

### Random notes : 
1. to comment multiple lines in python press (CTRL + '/') 
2.  1. UNDO local file changes and KEEP your last commit
    git reset --hard

    2. UNDO local file changes and REMOVE your last commit
    git reset --hard HEAD^
    
    3. KEEP local file changes and REMOVE your last commit
    git reset --soft HEAD^

