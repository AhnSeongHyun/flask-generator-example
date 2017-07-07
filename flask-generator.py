from flask import Flask
from flask import request, make_response
app = Flask(__name__)

generator_store = dict()


@app.route('/')
def hello_world():
    global  generator_store
    key = request.cookies.get('key', None)
    flag = request.args.get('flag', None)
    print 'key : %s' % key
    print generator_store
    if key in generator_store:
        x = generator_store[key]
        if flag == 'exit':
            del generator_store[key]
            x.close()
            return "%s is exit" %  key
        else:
            return return_value(str(x.next()()), key)
    else:
        x = generator()
        import random
        key = 'test' + str(random.randrange(1000,9999))
        generator_store[key] = x

        return return_value(str(next(x)()), key)


def return_value(msg, key):
    resp = make_response(msg)
    resp.set_cookie("key", key)
    return resp


def printf():
    from datetime import datetime
    return "test"  + str(datetime.now())


def generator():
    while True:
        try:
            yield printf
        except GeneratorExit:
            break


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8765)
