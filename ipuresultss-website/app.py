from flask import Flask, request, render_template
import json, requests
import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb+srv://xxx:xxx@cluster0-gclx4.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return render_template("home.html")
    else :

        inp = request.form.get('search_string').strip()

        subjects = json.loads(requests.get('https://xxx/subjects.json').text)
        df = pd.DataFrame(list(db.test.find({}))).set_index('en_no')

        try:
            inp_batch = df.loc[inp,'batch']
            inp_college = df.loc[inp,'college']
            inp_class = df.loc[inp,'class']
        except KeyError:
            return render_template("home.html", err = "Valid roll no not found. Try another.")
        else:
            df = df[(df['batch']==inp_batch) & (df['college']==inp_college) & (df['class']==inp_class)]
            df = df.fillna(0)
            df['tot0'] = df['tot1'] + df['tot2'] + df['tot3'] + df['tot4'] + df['tot5'] + df['tot6'] + df['tot7'] + df['tot8']
            df['ns0'] = df['ns1'] + df['ns2'] + df['ns3'] + df['ns4'] + df['ns5'] + df['ns6'] + df['ns7'] + df['ns8']

            for i in range(9):
                df['per'+str(i)] = df['tot'+str(i)] / df['ns'+str(i)]
                df['rank'+str(i)] = df['per'+str(i)].rank(method='min', ascending=False)

            df = df.fillna(0)
            ret = df.loc[inp]
            rankdicts = df.loc[:,['name','per0','per1','per2','per3','per4','per5','per6','per7','per8']].reset_index().to_dict('records')

            return render_template("display.html", inp = inp, data=dict(ret), subjects = subjects, rankdicts=rankdicts)

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)