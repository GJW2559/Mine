
from flask import Flask, request, render_template, redirect, url_for, flash, session
import os

app = Flask(__name__)
# 设置密钥，用于会话管理和Flash消息
app.secret_key = os.urandom(24)

# 模拟用户数据库 (实际项目中应使用数据库)
USERS = {
    "admin": "123456",
    "user": "password"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # 简单验证逻辑
        if username in USERS and USERS[username] == password:
            session['username'] = username
            flash('登录成功！欢迎回来, ' + username, 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('用户名或密码错误，请重试。', 'error')
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('请先登录', 'warning')
        return redirect(url_for('login'))
    return f"<h1>欢迎, {session['username']}!</h1><p>这是受保护的仪表盘页面。</p><a href='/logout'>退出登录</a>"

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('已安全退出', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1900, debug=True)
