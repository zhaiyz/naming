from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from model import Naming

app = Flask(__name__)

dict = {"订单": ["order", "order1"], "职位": ["position", "position1", "position2"], "产品": ['product']}


@app.route('/')
def index():
    return render_template('index.html', result=[])


@app.route('/naming', methods=['GET', 'POST'])
def naming():
    if request.method == 'GET':
        chinese_name = request.args.get('chinese_name', '')
        namings = Naming.query.filter_by(chinese_name=chinese_name)
        result = map(lambda x: x.english_name, namings)
        return render_template('index.html', result=result, chinese_name=chinese_name)
    else:
        chinese_name = request.form['chinese_name']
        english_name = request.form['english_name']
        Naming(chinese_name, english_name).save()
        return redirect(url_for('naming', chinese_name=chinese_name))


if __name__ == '__main__':
    app.run(debug=True)
