# Pymail

Pymail is a Python library for sending gmail in python program.

## Installation

Clone the repo and exec  `pip install .`

```bash
git clone git@github.com:shuyaeer/pymail.git
cd pymail
pip install .
```

## Configulation

You must enable Google-2-factor-authentication.  
<https://myaccount.google.com/signinoptions/two-step-verification>  
Generate app password  
<https://myaccount.google.com/apppasswords>  
set the gmail address and password you ealier generate as environment variable.

```bash
echo 'export GMAIL="hogehoge@gmail.com"' >> ~/.bashrdc
echo 'export GMAIL_PASSWORD="password"' >> ~/.bashrc
source ~/.bashrc
```

## Usage

```python
from pymail inmport send_mail

# simple useage
send_mail('destination@hogehoge.com', 'subject', 'body_test')

# you cat attach images
send_mail('destination@hogehoge.com', 'subject', 'body_test', image_path="images/sample.png")
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
