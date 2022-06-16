from flask import Flask, render_template,request,redirect

from Caption_it import caption_this_image

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/',methods=['POST'])
def marks():
    
    if request.method == 'POST':
        
        f = request.files["userfile"]
        path = './static/{}'.format(f.filename)
        f.save(path)
        
        caption = caption_this_image(path)
        print(caption)
        
        result_dic = {"image" : path,
                     "caption" : caption
                     }
                          
    return render_template("index.html",your_result = result_dic)

if __name__ == "__main__":
    app.run(debug=False,threaded=False)  ## Threaded mode will load our model int he default session in which the tensorflow libraries                                            ##  are present 