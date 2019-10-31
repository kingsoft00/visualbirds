import webbrowser

f = open('upload.html','w')
message = """<html>
<head>
    <meta charset="utf-8">
	<title>Birds Identifier Web App</title>
	<link rel = "icon" href = "https://usercontent2.hubstatic.com/7923939_f520.jpg" type = "image/x-icon"> 
	<style>
	    html {
	        background-image: url("images/giphy.gif");
	        background-size: cover;
	    }
		body form {
		    font-family: Arial, Helvetica, sans-serif;
	        background-color: #7BB5FF;
	        width: 300px;
	        height: 100px;
	        border: 1px solid;
	        margin: auto;
		}
		body h1:first-letter { 
	        font-size: 240%;
        }
        h1, p {
            text-align: center;
        }
	</style>
</head>
<body>
    <h1>welcome to NC birds identification!!!</h1>
    <form action="/action_page.php"> <input type="file" name="pic" accept="image/*"> <input type="submit">
    <p><strong>Note:</strong> Upload an NC bird image <p>
    </form>
</body>
</html>"""

f.write(message)
f.close()
webbrowser.open_new_tab('upload.html')
