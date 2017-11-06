from flask import Flask, redirect, url_for
from flask import render_template
from flask import request

app = Flask(__name__)

dict = {"订单": ["order", "order1"], "职位": ["position", "position1", "position2"], "产品": ['product']}


@app.route('/')
def index():
    return render_template('index.html', result=[])


@app.route('/naming', methods=['GET', 'POST'])
def naming():
    if request.method == 'GET':
        chinese_name = request.args.get('chinese_name', '')
        return render_template('index.html', result=dict.get(chinese_name, []), chinese_name=chinese_name)
    else:
        chinese_name = request.form['chinese_name']
        english_name = request.form['english_name']
        result = dict.get(chinese_name, [])
        result.insert(0, english_name)
        if (len(result) == 1):
            dict[chinese_name] = result
        return redirect(url_for('naming', chinese_name=chinese_name))


if __name__ == '__main__':
    app.run(debug=True)
