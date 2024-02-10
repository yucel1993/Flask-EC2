from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_word():
    return "<p> Hello Word </p>"



if __name__ == '__main__':  # We added this to run python hello.py
    # app.run(debug=True)
    # app.run(debug=True,port=3003)
    app.run(host='0.0.0.0',port=80)
