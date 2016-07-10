def html(title, body):
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <title>
            %s
        </title>
    </head>

    <body>
        %s
    </body>

    </html>
    """ % (title, body)
