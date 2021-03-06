## 📌 Demo site
Deploying a Flask app Demo on AWS Lambda with Zappa  

🔗 [Demo site link](https://rgb3xxlq7l.execute-api.ap-northeast-2.amazonaws.com/dev)

## 📌 Testing
![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/82564045/154107881-1042b196-1251-4df7-9014-594e06f4316e.gif)

## 📌 Structure
```
.
├── app
│   ├── configs.py
│   ├── constants.py
│   ├── __init__.py
│   ├── introduction
│   │   ├── case.py
│   │   └── product.py
│   │
│   ├── model.py
│   ├── static
│   ├── templates
│   └── test.py
├── env
├── run.py
└── zappa_settings.json
```

## 📌 Usage
```python
$ git clone https://github.com/GeunYeongii/Flask-web-inolock.git
$ cd Flask-web-inolock  # changing to project directory
$ pip install virtualenv
```

- Linux/macOS
```
$ source env/bin/activate
$ (env) python run.py
```

- Windows
```
C:\[Path\to\project]> env\Scripts\activate.bat
(env) C:\[Path\to\project]> python run.py
```

> deactivate virtualenv : commant to ```deactivate```

## 📌 stack
<p>
  <!-- Your languages and tools. Be careful with the alignment. 
  You can use this sites to get logos: https://www.vectorlogo.zone or https://simpleicons.org/
  -->
  <code><a href="https://docs.python.org/3.8/whatsnew/3.8.html"><img width="10%" src="https://www.vectorlogo.zone/logos/python/python-ar21.svg"></code></a>
  <code><a href="https://flask.palletsprojects.com/en/2.0.x/"><img width="10%" src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg"></a></code>
  <code><a href="https://jinja.palletsprojects.com/en/3.0.x/"><img width="10%" src="https://www.vectorlogo.zone/logos/pocoo_jinja/pocoo_jinja-ar21.svg"></a></code>
  <br />
  <code><a href="https://releases.ubuntu.com/20.04/"><img width="10%" src="https://www.vectorlogo.zone/logos/ubuntu/ubuntu-ar21.svg"></a></code>
  <code><a href="https://aws.amazon.com/ko/lambda/"><img width="10%" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-ar21.svg"></a></code>
  <code><a href="https://github.com/zappa/Zappa"><img width="10%" src="https://img.shields.io/badge/Zappa-white.svg"></a></code>
  <br />
</p>


## 📌 Deploy update
```
(env) $ zappa update
```
