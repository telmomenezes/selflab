def css():
    return """
    body {
        background-color: #FFF;
    }
    input {
        width: 100%;
        font-family:"Arial Black", Gadget, sans-serif;
        font-size:x-large;
    }
    input[type=submit] {
        margin-top:2em;
    }
    h3 {
        font-family:"Arial Black", Gadget, sans-serif;
        font-size:x-large;
        color: #555;
        margin-bottom:0px;
    }
    .last-event {
        font-family:"Arial Black", Gadget, sans-serif;
        font-size:large;
        color: #33A;
        margin-top:2em;
    }
    """


def html(title, body):
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <title>
            %s
        </title>
        <style TYPE="text/css">
        <!--
        %s
        -->
        </style>
    </head>

    <body>
        %s
    </body>

    </html>
    """ % (title, css(), body)
