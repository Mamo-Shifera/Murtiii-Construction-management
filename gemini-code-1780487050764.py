# app.py
from flask import Flask, render_template, request # Added 'request' for potential form handling

# Initialize the Flask application
app = Flask(__name__)

# --- Routes for Different Pages ---

@app.route('/')
def home():
    """Renders the homepage."""
    # You can pass dynamic data to your template here if needed
    # page_data = {"title": "Welcome"}
    return render_template('index.html') # Renders templates/index.html

@app.route('/placement')
def placement():
    # For now, let's reuse index.html or create placement.html
    # Replace with render_template('placement.html') when created
    return render_template('index.html', page_title="Placement")

@app.route('/about')
def about():
    # Replace with render_template('about.html') when created
    return render_template('index.html', page_title="About Us")

@app.route('/services')
def services():
    # Replace with render_template('services.html') when created
    return render_template('index.html', page_title="Our Services")

@app.route('/projects')
def projects():
    # Replace with render_template('projects.html') when created
    return render_template('index.html', page_title="Projects")

@app.route('/clients')
def clients():
     # Replace with render_template('clients.html') when created
    return render_template('index.html', page_title="Our Clients")

@app.route('/safety')
def safety():
     # Replace with render_template('safety.html') when created
    return render_template('index.html', page_title="Safety First")

@app.route('/careers')
def careers():
     # Replace with render_template('careers.html') when created
    return render_template('index.html', page_title="Careers")

@app.route('/contact', methods=['GET', 'POST']) # Allow POST for form submission
def contact():
    if request.method == 'POST':
        # --- Form Handling Logic (Basic Example) ---
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # TODO: Process the form data (e.g., send email, save to database)
        print(f"Received message from {name} ({email}): {message}")
        # Redirect or show a success message
        return render_template('index.html', page_title="Contact Us", message_sent=True)

    # Replace with render_template('contact.html') when created
    return render_template('index.html', page_title="Contact Us")


# --- Run the Application ---
if __name__ == '__main__':
    # debug=True is helpful during development for auto-reloading and error details
    # Turn off debug mode in production!
    app.run(debug=True)