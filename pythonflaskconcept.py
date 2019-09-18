from flask import Flask,render_template,Request
app_guvi=Flask(__name__)
@app_guvi.route('/getName/<name>', methods=['GET','POST'])
def index_guvi(name):
    return render_template('myweb.html',name=name)
if __name__=="__main__":
    app_guvi.run()
    
    
    
    
    #html file:
   
   <html>
    <head>
        <title>my web page</title>
    </head>
    <body>
        <h1>welcome</h1>                                    //must stored in templates
        <h1>welcome to india {{name}}</h1>
    </body>
</html>
    
