# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

# Function to check if user is logged in
def is_logged_in():
    print("Checking login status:", 'user_id' in session)  # Debug line
    return 'user_id' in session

# Function to get database connection
def get_db_connection():
    db_path = 'database.db'
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

today_date=(date.today() + timedelta(days=1)).isoformat()
# put this with the is_logged_in part in the functions