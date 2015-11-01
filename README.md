# keatsbot
A light-winged Dryad of the trees; tweeting. All explained at http://blog.arrayofbytes.co.uk/?p=127

## Prerequisites
- Python 2
- virtualenv
- pip

## Getting started
- Clone the repo
- Create a virtual env as you wish e.g. `virtualenv env` then enter it e.g. `source env/bin/activate`
- Restore packages `pip install -r requirements.txt`
- Create a file `settings.txt` containing your Twitter credentials, (token; token key; consumer secret; consumer secret key) separated by line breaks
- replace `corpus/all.txt` with the writings of your muse
- `python keatsbot.py` and you're away!

