@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # Collecting form data
            full_name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            age = request.form.get('age')  # Using get() instead of direct access

            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Checking if email is already registered
            cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                flash('Email already registered. Please use a different email or log in.', 'danger')
                conn.close()
                return redirect(url_for('register'))

            # Hashing password and inserting user data into database
            hashed_password = generate_password_hash(password)
            cursor.execute('INSERT INTO users (full_name, email, password, age) VALUES (?, ?, ?, ?)',
                         (full_name, email, hashed_password, age))
            conn.commit()
            conn.close()
            
            flash('You are now registered and can log in', 'success')
            return redirect(url_for('login'))
        
        except sqlite3.Error as e:
            flash(f'Database error: {str(e)}', 'danger')
            return redirect(url_for('register'))
    
    return render_template('register.html', is_logged_in=is_logged_in)