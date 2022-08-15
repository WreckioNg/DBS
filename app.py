#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request


# In[2]:


app = Flask(__name__)


# In[3]:


# dir(Flask)


# In[4]:


import joblib

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates=float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load('LR_DBS')
        r1 = model1.predict([[rates]])
        model2 = joblib.load("Tree")
        r2 = model2.predict([[rates]])
        return (render_template("index.html",result1=r1,result2=r2))
    else:
        return (render_template("index.html",result1="waiting",result2="waiting"))


# In[5]:


# render_template?


# In[ ]:


if __name__ == "__main__":
    app.run(port=8080)


# In[ ]:




