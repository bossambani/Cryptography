from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            text = request.form["ceasar"]
            shift = int(request.form["key"])
            result = ""
            for char in text:
                if char.isalpha():
                    shift_amount = shift % 26
                    new_char = chr(((ord(char.lower()) - ord('a') - shift_amount) % 26) + ord('a'))
                    result += new_char.upper() if char.isupper() else new_char
                elif char.isdigit():
                    result += chr(((ord(char) - ord('0') - shift) % 10 + 10) % 10 + ord('0'))

                else:
                    result += char
            return render_template("index1.html", result=result)
    return render_template("index1.html")
    


if __name__ == '__main__':
    app.run(debug=True, port=8000)