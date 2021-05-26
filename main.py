from wsgiref import simple_server
from flask import Flask
from flask import Response
from flask_cors import CORS,cross_origin

app=Flask(__name__)
CORS(app)

@app.route('/training',methods=['POST'])
@cross_origin()

def training_route_client():
    try:
        return Response("Training Successfull!")
    except ValueError:
        return  Response("Error occurred - %s" % ValueError)
    except KeyError:
        return Response("Error occurred - %s" % KeyError)
    except Exception as e:
        return Response("Error occurred - %s" % e)

if __name__=="__main__":
    app.run()