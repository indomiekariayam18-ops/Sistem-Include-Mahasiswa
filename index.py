import os
from flask import Flask, render_template, request, redirect, url_for, flash, session

# Konfigurasi template folder (mengacu ke folder templates di luar direktori saat ini)
current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_dir, '../templates')

app = Flask(__name__, template_folder=template_folder)
app.secret_key = 'kunci_rahasia_sim_2026'

# Simulasi Database Akun di Memory
users_db = {"admin": "admin123"}

# --- DATA INTERNAL TEKNIK INFORMATIKA ---
MATA_KULIAH = [
    {"kode": "IF101", "nama": "Algoritma dan Pemrograman", "sks": 3, "semester": 3},
    {"kode": "IF102", "nama": "Sistem Informasi", "sks": 3, "semester": 3},
    {"kode": "IF103", "nama": "Matematika Diskrit", "sks": 3, "semester": 3},
    {"kode": "IF104", "nama": "Kalkulus", "sks": 3, "semester": 3},
    {"kode": "IF105", "nama": "Struktur Data", "sks": 3, "semester": 3},
    {"kode": "IF106", "nama": "Sistem Berkas", "sks": 2, "semester": 3},
    {"kode": "IF107", "nama": "Sistem Operasi", "sks": 3, "semester": 3},
    {"kode": "IF108", "nama": "Pemrograman Orientasi Objek", "sks": 3, "semester": 3},
    {"kode": "IF109", "nama": "Basis Data", "sks": 3, "semester": 3},
    {"kode": "IF110", "nama": "Jaringan Komputer", "sks": 3, "semester": 3},
    {"kode": "IF111", "nama": "Komputer Grafik", "sks": 3, "semester": 3},
    {"kode": "IF112", "nama": "Fisika Dasar", "sks": 3, "semester": 3},
    {"kode": "IF113", "nama": "Komunikasi Data", "sks": 3, "semester": 3},
    {"kode": "IF114", "nama": "Pengantar Aplikasi Komputer", "sks": 3, "semester": 3},
    {"kode": "IF115", "nama": "Statistika dan Probabilitas", "sks": 3, "semester": 3},
    {"kode": "IF116", "nama": "Graph Terapan", "sks": 2, "semester": 3}
]

DOSEN = [
    {"nama": "Prof. Haikal Maulana Rayhan, M.Kom.", "lulusan": "Ilmu Komputer", "matkul": "Sistem Informasi"},
    {"nama": "Eka Sri Rahayu S.Kom., M.Kom.", "lulusan": "Teknik Informatika", "matkul": "Algoritma dan Pemrograman"},
    {"nama": "Siti Aminah, M.T.", "lulusan": "Sistem Informasi", "matkul": "Matematika Diskrit"},
    {"nama": "Irwan Kurniawan, Ph.D", "lulusan": "Teknik Informatika", "matkul": "Kalkulus"},
    {"nama": "Rina Wijaya, M.Cs.", "lulusan": "Ilmu Komputer", "matkul": "Struktur Data"},
    {"nama": "Agus Setiawan, M.Kom.", "lulusan": "Teknik Informatika", "matkul": "Sistem Berkas"},
    {"nama": "Dewi Lestari, M.T.", "lulusan": "Teknik Informatika", "matkul": "Sistem Operasi"},
    {"nama": "Eko Prasetyo, M.Kom.", "lulusan": "Ilmu Komputer", "matkul": "Pemrograman Orientasi Objek"},
    {"nama": "Fahmi Idris, M.T.", "lulusan": "Sistem Informasi", "matkul": "Basis Data"},
    {"nama": "Gita Permata, M.Sc.", "lulusan": "Teknik Elektro", "matkul": "Jaringan Komputer"},
    {"nama": "Nabila Azzahra Pratama, S.Kom.", "lulusan": "Sistem Informasi", "matkul": "Graph Terapan"},
    {"nama": "Dinda Maharani Saputri, S.Kom.", "lulusan": "Ilmu Komputer", "matkul": "Statistika dan Probabilitas"},
    {"nama": "Nadira Khairunnisa Putri, S.Kom.", "lulusan": "Teknologi Informasi", "matkul": "Komputer Grafik"},
    {"nama": "Salsabila Nur Aini, S.Kom.", "lulusan": "Teknik Informatika", "matkul": "Komunikasi Data"},
    {"nama": "Muhammad Rizky Pratama, S.Kom.", "lulusan": "Teknik Informatika", "matkul": "Pengantar Aplikasi Komputer"},
    {"nama": "Dimas Saputra Wijaya, S.Kom.", "lulusan": "Ilmu Komputer", "matkul": "Fisika Dasar"}
]

MAHASISWA = [
    {"nim": 241011450240, "nama": "Haikal Anugrah Ramadhan", "prodi": "Teknik Informatika"},
    {"nim": 241011452511, "nama": "Arkan Mahendra Putra", "prodi": "Teknik Informatika"},
    {"nim": 241011459076, "nama": "Aisha Humaira Zahra", "prodi": "Teknik Informatika"},
    {"nim": 241011454025, "nama": "Elvano Akbar Pratama", "prodi": "Teknik Informatika"},
    {"nim": 241011453698, "nama": "Aria Celestine", "prodi": "Teknik Informatika"},
    {"nim": 241011450357, "nama": "Chloe Anindya", "prodi": "Teknik Informatika"},
    {"nim": 241011451024, "nama": "Axel Mahardika Putra", "prodi": "Teknik Informatika"},
    {"nim": 241011456975, "nama": "Alessa Nayla", "prodi": "Teknik Informatika"},
    {"nim": 241011453252, "nama": "Nathan Akbar Saputra", "prodi": "Teknik Informatika"},
    {"nim": 241011453963, "nama": "Alya Safira Putri", "prodi": "Teknik Informatika"},
    {"nim": 241011452045, "nama": "Yusuf Alfarel Akbar", "prodi": "Teknik Informatika"},
    {"nim": 241011451248, "nama": "Elina Grace", "prodi": "Teknik Informatika"},
    {"nim": 241011450560, "nama": "Arshaka Wijaya", "prodi": "Teknik Informatika"},
    {"nim": 241011457984, "nama": "Olivia Kirana", "prodi": "Teknik Informatika"},
    {"nim": 241011452566, "nama": "Alina Safira Putri", "prodi": "Teknik Informatika"},
    {"nim": 241011454982, "nama": "Syifa Nabila Putri", "prodi": "Teknik Informatika"},
    {"nim": 241011457234, "nama": "Luna Valerie", "prodi": "Teknik Informatika"},
    {"nim": 241011452241, "nama": "Yuna Aveline", "prodi": "Teknik Informatika"},
    {"nim": 241011452150, "nama": "Nathaniel Pratama", "prodi": "Teknik Informatika"},
    {"nim": 241011454157, "nama": "Bianca Azzahra", "prodi": "Teknik Informatika"}
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users_db and users_db[username] == password:
            session['user'] = username
            flash("show_welcome_toast", "welcome")
            return redirect(url_for('dashboard'))
        else:
            flash("Username atau Password Salah!", "error")
            
    return render_template('login.html', form_type="login")

@app.route('/registrasi', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if username in users_db:
            flash("Username sudah terdaftar!", "error")
        elif password != confirm_password:
            flash("Password dan Ulangi Password tidak cocok!", "error")
        elif not username or not password:
            flash("Semua kolom input wajib diisi!", "error")
        else:
            users_db[username] = password
            flash("Registrasi Berhasil! Silakan Masuk.", "success")
            return redirect(url_for('login'))

    return render_template('login.html', form_type="registrasi")

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html', page="dashboard", mhs_count=len(MAHASISWA), dsn_count=len(DOSEN), mk_count=len(MATA_KULIAH))

@app.route('/mahasiswa')
def mahasiswa_page():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html', page="mahasiswa", data_list=MAHASISWA)

@app.route('/dosen')
def dosen_page():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html', page="dosen", data_list=DOSEN)

@app.route('/matkul')
def matkul_page():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html', page="matkul", data_list=MATA_KULIAH)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
