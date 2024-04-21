from app import app, ADMIN_LOGIN, ADMIN_PASSWORD
from flask import render_template, redirect, request
import requests


@app.route('/admin', methods=['GET', 'POST'])
def sites():

    login = request.args.get('login', None)
    password = request.args.get('password', None)

    if login != ADMIN_LOGIN or password != ADMIN_PASSWORD:
        return 'Page not found', 404

    with open('app/sites.txt', 'r', encoding='utf-8') as inp:
        sites_arr = inp.read().split()

    return render_template(
        'sites_page.html',
        sites = sites_arr
    )
@app.route('/block')
def block():
    with open('app/sites.txt', 'r', encoding='utf-8') as inp:
        req_sites = []
        sites = inp.read().split()
        for site in sites:
            if 'www' not in site:
                req_sites.append(site)
                req_sites.append('www.' + site)
            else:
                req_sites.append(site[4:])
                req_sites.append(site)

        req = '\n'.join(req_sites)
        print(req)
        response = requests.post('http://localhost:8080/', data=req)

    print(response.status_code)
    if response.status_code == 200 or response.status_code == 502:
        return 'POST запрос успешно отправлен на прокси сервер.'
    else:
        return 'Ошибка при отправке POST запроса на прокси сервер.'

@app.route('/')
def default():

    return render_template(
        'blocked_page.html'
    )


@app.route('/change', methods=['POST'])
def change():
    text = request.form.get('text', None)

    if text is None:
        return redirect('/admin')
    
    if 'add' in text:
        text = text.replace('add', '')
        arr = text.split()

       
        with open('app/sites.txt', 'r', encoding='utf-8') as inp:
            cur_sites = inp.read()
        with open('app/sites.txt', 'a', encoding='utf-8') as inp:
            for site in arr:
                if site not in cur_sites:
                    inp.write(site + '\n')

        return redirect('/block')
    
    elif 'delete' in text:
        text = text.replace('delete', '')
        arr = text.split()

        with open('app/sites.txt', 'r', encoding='utf-8') as inp:
            sites = inp.read()
   
  
        for site in arr:
          
            sites = sites.replace(site + '\n', '')

            # на случай, если после тек сайта нет переноса строки (стоит последним)
            sites = sites.replace(site, '')
            

        with open('app/sites.txt', 'w', encoding='utf-8') as inp:
            inp.write(sites)
        return redirect('/block')
    else:

        return redirect('/admin')


            


            


