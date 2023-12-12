## flask --app app run --debug

from flask import Flask, render_template      
import json

app = Flask(__name__)

@app.route("/")
def home():
    # Đọc dữ liệu từ tệp JSON
    with open("data.json", "r") as file:
        data = json.load(file)
        
    print(data)

    # Truyền dữ liệu vào template
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)