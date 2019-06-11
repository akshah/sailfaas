from flask import make_response
def handle(request):
    """handle a request to the function
    Args:
        request (str): request body
    """
    val1 = float(request.args.get('val1'))
    val2 = float(request.args.get('val2'))
    val3 = float(request.args.get('val3'))
    val4 = float(request.args.get('val4'))
    val5 = float(request.args.get('val5'))
    val6 = float(request.args.get('val6'))
    
    res1 = str(val1*val2/val3)
    res2 = str(val4*val5/val6) 
    response = make_response(res1+"|"+res2,200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
