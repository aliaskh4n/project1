# @aliaskhan #

from flask import Flask, render_template, request

app = Flask(__name__)

def read_company_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        company_names = [line.strip() for line in file if line.strip()]
    return company_names

def read_city_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        city_names = [line.strip() for line in file if line.strip()]
    return city_names

def read_person_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        person_names = [line.strip() for line in file if line.strip()]
    return person_names

def determine_color(word, company_names, person_names, city_names):
    if word.lower() in (company.lower() for company in company_names):
        return 'orange'
    elif word.lower() in (person_name.lower() for person_name in person_names):
        return 'blue'
    elif word.lower() in (city_name.lower() for city_name in city_names):
        return 'red'
    else:
        return 'black'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')

@app.route('/update_text', methods=['POST'])
def update_text():
    file_path_city = 'city.txt'
    file_path_company = 'company.txt'
    file_path_names = 'person_names.txt'
    company_names = read_company_names(file_path_company)
    city_names = read_city_names(file_path_city)
    person_names = read_person_names(file_path_names)

    input_text = request.form['inputText']
    
    colored_text = ''
    words = input_text.split()
    for word in words:
        colored_text += f'<span style="color: {determine_color(word, company_names, person_names, city_names)};">{word}</span> '
    
    return colored_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
