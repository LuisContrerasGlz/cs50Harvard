import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    rows=db.execute("SELECT symbol,sum(shares) as totalShares from movement WHERE user_id=:id group by (symbol) having totalShares>0 ",id=session["user_id"])
    holdings=[]
    grand_total=0
    for row in rows:
        stock=lookup(row["symbol"])
        holdings.append({
            "symbol":stock["symbol"],
            "name":stock["name"],
            "totalShares":row["totalShares"],
            "price":usd(stock["price"]),
            "total":usd(stock["price"]*row["totalShares"])
        })
        grand_total += stock["price"]*row["totalShares"]
    rows=db.execute("SELECT cash from users WHERE id=:id",id=session["user_id"])    
    cash=rows[0]["cash"]
    return render_template("index.html", holdings = holdings, cash=usd(cash), grand_total=usd(grand_total))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    #"""Buy shares of stock"""
    #return apology("TODO")
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    rows=db.execute("SELECT mov_type,symbol,shares,price,date from movement WHERE user_id=:id ",id=session["user_id"])
    movements=[]
    grand_total=0
    for row in rows:
        stock=lookup(row["symbol"])
        movements.append({
            "mov_type":row["mov_type"],
            "symbol":row["symbol"],
            "name":stock["name"],
            "shares":row["shares"],
            "price":usd(row["price"]),
            "total":usd(row["price"]*row["shares"]),
            "date":row["date"]
        })
        grand_total += row["price"]*row["shares"]
    rows=db.execute("SELECT cash from users WHERE id=:id",id=session["user_id"])    
    cash=rows[0]["cash"]
    return render_template("history.html", movements = movements, cash=usd(cash), grand_total=usd(grand_total))

    
    
    
    
    
    
    
    #"""Show history of transactions"""
    #return apology("TODO")
    return render_template("history.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    #"""Get stock quote."""
    #return apology("TODO")
    return render_template("quote.html")

@app.route("/quoted", methods=["GET", "POST"])
@login_required
def quoted():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        symbol=request.form.get("symbol").upper()
        stock= lookup(symbol)
        if stock==None:
            return apology("invalid symbol", 400)
        return render_template("quoted.html", stock=stock)
    else:
        # quoted
        return render_template("quoted.html")
        
@app.route("/buyed", methods=["GET", "POST"])
@login_required
def buyed():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        
        if not request.form.get("shares"):
            return apology("must provide shares", 400)
        else:
            try:
                shares = int(request.form.get("shares"))
            except ValueError:
                return apology("must provide a valid number", 400)
            
        # Ensure username was submitted
        symbol=request.form.get("symbol").upper()
        stock= lookup(symbol)
        if stock==None:
            return apology("invalid symbol", 400)
        
        if shares<=0:
            return apology("must provide a number greater than zero", 400)
        rows = db.execute("SELECT cash FROM users WHERE id = :id",id=session["user_id"])
        cash=rows[0]["cash"]
        updated_cash = cash - shares * stock['price']
        if updated_cash < 0:
            return apology("insufficient funds", 400)
        db.execute("UPDATE users set cash=:updated_cash WHERE id=:id",updated_cash=updated_cash,id=session["user_id"])
        rows=db.execute("INSERT INTO movement (mov_type,user_id,symbol,shares,price) VALUES (%s,%s,%s,%s,%s)",("B",session["user_id"],request.form.get("symbol").upper(),request.form.get("shares"),stock['price']))
        return redirect("/")
    else:
        # quoted
        return render_template("quoted.html")

@app.route("/sold", methods=["GET", "POST"])
@login_required
def sold():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        
        if not request.form.get("shares"):
            return apology("must provide shares", 400)
        else:
            try:
                shares = int(request.form.get("shares"))
            except ValueError:
                return apology("must provide a valid number", 400)
            
        # Ensure username was submitted
        symbol=request.form.get("symbol").upper()
        stock= lookup(symbol)
        if stock==None:
            return apology("invalid symbol", 400)
        
        if shares<=0:
            return apology("must provide a number greater than zero", 400)
            
        rows=db.execute("SELECT sum(shares) as cuantity from movement WHERE user_id=:id and symbol=:sym ",id=session["user_id"],sym=request.form.get("symbol").upper())
        cuantity=rows[0]["cuantity"]
        if cuantity<shares:
            return apology("insufficient shares", 400)
        rows = db.execute("SELECT cash FROM users WHERE id = :id",id=session["user_id"])
        cash=rows[0]["cash"]
        updated_cash = cash + shares * stock['price']
        shares=shares*(-1)
        db.execute("UPDATE users set cash=:updated_cash WHERE id=:id",updated_cash=updated_cash,id=session["user_id"])
        rows=db.execute("INSERT INTO movement (mov_type,user_id,symbol,shares,price) VALUES (%s,%s,%s,%s,%s)",("S",session["user_id"],request.form.get("symbol").upper(),shares,stock['price']))
        return redirect("/")
    else:
        # quoted
        return render_template("quoted.html")




@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@app.route("/ins_reg", methods=["GET", "POST"])
def ins_reg():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 403)
        elif not request.form.get("password")==request.form.get("confirmation"):
            return apology("confirmation must match to password", 403)

        # Query database for username
        aux_pass=generate_password_hash(request.form.get("password"))
        rows = db.execute("INSERT INTO users (username,hash) VALUES (%s,%s)",
                          (request.form.get("username"),aux_pass))


        # Redirect user to home page
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
