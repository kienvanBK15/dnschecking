from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from dnstwist import *


app = Flask(__name__)
api = Api(app)

@app.route('/dnstwist', methods = ['GET'])
#generating domain names similar with seed domain
def get():
    domain = request.args.get("domain")
    print(domain)
    dfuzz = DomainFuzz(domain)
    dfuzz.generate()
    domains = dfuzz.domains
    domains_registered = []
    for d in domains:
        if 'dns-ns' in d or 'dns-a' in d:
            domains_registered.append(d)
	
    domains = domains_registered
    del domains_registered
    return json.dumps(domains)

if __name__ == '__main__':
    app.run()
