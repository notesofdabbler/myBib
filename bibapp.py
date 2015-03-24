from flask import Flask, render_template, request, redirect, url_for, g
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from makedb import Base, Articles

global srchtitle,srchauthors,srchjournal,srchyearlo,srchyearhi

srchtitle = ''
srchauthors = ''
srchjournal = ''
srchyearlo = ''
srchyearhi = ''

engine = create_engine('sqlite:///mybib.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/article/new/', methods=['GET','POST'])
def newArticle():
  if request.method == 'POST':
      article1 = Articles(title = request.form['title'],
                    authors = request.form['authors'],
                    journal = request.form['journal'],
                    volume = request.form['volume'],
                    pages = request.form['pages'],
                    year = request.form['year'],
                    weburl = request.form['weburl'],
                    localurl = request.form['localurl'],
                    keywords = request.form['keywords']
                    )
      session.add(article1)
      session.commit()
      return redirect(url_for('newArticle')) 
  else:
      return render_template('newarticle.html')

@app.route('/article/search', methods = ['GET','POST'])      
def searchArticle():
 
    global srchtitle,srchauthors,srchjournal,srchyearlo,srchyearhi

    if request.method == 'POST':
 
        srchtitle = request.form['title']
        srchauthors = request.form['authors']
        srchjournal = request.form['journal']
        srchyearlo = request.form['yearlo']
        srchyearhi = request.form['yearhi']
        
        print "Hello, I am in POST"
#        srchtitle = "%Approximation%"
        print srchtitle
        
        return redirect(url_for('searchArticlesList'))
        
    else:
        return render_template('searchArticles.html')

@app.route('/articles/searchlist/', methods = ['GET','POST'])        
def searchArticlesList():

    qry = session.query(Articles)
 
    if srchtitle != "":
        qry = qry.filter(Articles.title.like(srchtitle))
    
    if srchauthors != "":
        qry = qry.filter(Articles.authors.like(srchauthors))
    
    if srchjournal != "":
        qry = qry.filter(Articles.journal.like(srchjournal))
    
    if srchyearlo != "":
        qry = qry.filter(Articles.year >= int(srchyearlo))

    if srchyearhi != "":
        qry = qry.filter(Articles.year <= int(srchyearhi))    
    
    items = qry.all()
    
    print 'srchtitle = ' + srchtitle
    
    for x in items:
        print x.authors

    return render_template('searchArticlesList.html',items = items) 
    
@app.route('/article/edit/<id>', methods = ['GET','POST'])      
def editArticle(id):

    item = session.query(Articles).filter(Articles.id == id).first()
    print item.id, item.title
 
    if request.method == 'POST':
        if request.form['title']:
            item.title = request.form['title']
            
        if request.form['authors']:
            item.authors = request.form['authors']

        if request.form['journal']:
            item.journal = request.form['journal']

        if request.form['volume']:
            item.volume = request.form['volume']

        if request.form['pages']:
            item.pages = request.form['pages']

        if request.form['year']:
            item.year = request.form['year']

        if request.form['weburl']:
            item.weburl = request.form['weburl']

        if request.form['localurl']:
            item.localurl = request.form['localurl']
            
        if request.form['keywords']:
            item.keywords = request.form['keywords']

        session.add(item)
        session.commit()
        
        return render_template('showArticle.html',item = item)
    
    else:
 
        return render_template('editArticle.html',item = item)
         
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)