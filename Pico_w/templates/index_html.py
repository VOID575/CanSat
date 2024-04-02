from csv_module import dernieres_valeurs

def render(*a, **d):
    if float(dernieres_valeurs()[1][:-1]) < -10 or float(dernieres_valeurs()[1][:-1]) > 50:

        temperature_check = '❌'
    
    else : temperature_check = '✔'

    try :
        if float(dernieres_valeurs()[2][:-2]) > 102000 or float(dernieres_valeurs()[2][:-2]) < 98000:

            pressure_check = '❌'
            
        else : pressure_check = '✔'
        
    except ValueError:
        
        pass

    if float(dernieres_valeurs()[3][:-1]) > 80 or float(dernieres_valeurs()[3][:-1]) < 40:

        humidity_check = '❌'
        
    else : humidity_check = '✔'

    if float(dernieres_valeurs()[4][:-4]) > 100000:

        airquality_check = '❌'
        
    else : airquality_check = '✔'

    val = dernieres_valeurs()
    yield """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>CanStellar - Rapport</title>
    <style>
    
    body """
    yield """{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #232937;
        color: #ffffff;
    }
    
    .container """
    yield """{
        max-width: 800px;
        margin: 50px auto;
        text-align: center;
    }
    
    h1 """
    yield """{
        font-size: 2em;
        color: #3498db;
    }
    
    #data-container """
    yield """{
        background-color: #2c3e50;
        border: 1px solid #34495e;
        border-radius: 5px;
        padding: 20px;
        margin-top: 20px;
    }
    
    p """
    yield """{
        font-size: 1.2em;
        margin: 0;
        padding: 10px;
        border-bottom: 1px solid #34495e;
    }
    
    /* Ajoute une ombre légère pour un effet de profondeur */
    #data-container """
    yield """{
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    </style>
</head>
<body>
    <div class=\"container\">
        <h1>CanStellar - Rapport</h1>
        <div id=\"data-container\">
            <!-- Les données seront affichées ici -->
            """
    yield f"""
        <h2>Le {val[0]}</h2>
        <p>Température : {val[1]} : {temperature_check}</p>
        <p>Humidité : {val[3]} : {humidity_check}</p>
        <p>Pression : {val[2]} : {pressure_check}</p>
        <p>Qualité de l'air : {val[4]} : {airquality_check}</p>
        </div>
    </div>
    <script>
        setInterval(function () {{location.reload()}}, 5000);
    </script>
</body>
</html>
"""
