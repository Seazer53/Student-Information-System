from flask import Flask,render_template,url_for,request,redirect
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    user="Mert Sezer Ardal",
    password="abc123",
    database="ogrencibilgisistemi",
    host="localhost"
)


ogrencibilgi = []
cursor = db.cursor()
cursor.execute("SELECT ogrenciid,sifre FROM ogrenciler")
sonuc = cursor.fetchall()
for x in sonuc:
    ogrencibilgi.append(x)


idler = [a[0] for a in sonuc]
sifreler = [b[1] for b in sonuc]


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        for x in range(4):
            if str(request.form['username']) == str(idler[x]) and str(request.form['password']) == str(sifreler[x]):
                return redirect(url_for('home'))
            else:
                error = 'Kullanıcı adı veya şifre ya da ikisi hatalı. Lütfen bilgilerinizin doğruluğunu kontrol ediniz!'

    return render_template('girisekrani.html', error=error)



@app.route("/anasayfa", methods=["GET","POST"])
def home():
    return render_template("bilgiler.html")



@app.route("/anasayfa/yardim",methods=["POST","GET"])
def yardim():
    return render_template("yardim.html")



@app.route("/anasayfa/sinavsonuclari",methods=["POST","GET"])
def sinavsonuc():
    return render_template("sinav.html")



@app.route("/anasayfa/iletisim",methods=["POST","GET"])
def iletisim():
    return render_template("iletisim.html")



@app.route("/giris",methods=["POST","GET"])
def giris():
    return "Üniversitenin size vermiş olduğu şifre ve öğrenci numaranızla giriş yapabilirsiniz. Hala sorun yaşıyorsanız öğrenci işlerine başvurunuz."



@app.route("/anasayfa/hakkinda",methods=["POST","GET"])
def hakkinda():
    return "Bu web sitesinin tasarımı Mert Sezer Ardal'a aittir. Tüm hakları saklıdır. Öğrenci Bilgi Sistemi 2019©"



@app.route("/anasayfa/derssecimi",methods=["POST","GET"])
def derssecimi():
    return render_template("derssecimi.html")


if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True)