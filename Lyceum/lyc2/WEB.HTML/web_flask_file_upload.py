from flask import Flask, request, url_for

app = Flask(__name__)

script = '''<script type="text/javascript">
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#profile-img-tag').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#profile-img").change(function(){
        readURL(this);
    });
</script>'''

@csrf.exempt
@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/load_photo', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet"
                                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                                    crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_mars_anketa.css')}"/>
     <title>Отбор астронавтов</title>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.js"></script>
</head>
<body>
<h1 align="center">Загрузка фотографии</h1>
                                   <h4 align="center">для участия в миссии</h4>
<div>
                                        <form class="mars_form" method="post" enctype="multipart/form-data">

                                            <div class="form-group">
                                                <label for="photo">Приложите фотографию</label></br>
                                                <input type="file" class="form-control-file" id="profile-img" name="file">
        <img src="" id="profile-img-tag" width="200px" />
        {script}
                                            </div>
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                    </div>

</body>
</html>'''

    elif request.method == 'POST':

        return f'''<!doctype html>
                        <html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet"
                                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                                    crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_mars_anketa.css')}"/>
     <title>Отбор астронавтов</title>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.js"></script>
</head>
<body>
<h1 align="center">Форма отправлена</h1>
                                  

</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
