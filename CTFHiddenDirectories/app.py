from flask import Flask, render_template, abort, send_from_directory
import os

app = Flask(__name__)

# Main flag parts
FLAG_PARTS = {
    'part1': 'CTF{1m_',
    'part2': 'p4rt_',
    'part3': '0f_th3_fl4g}'
}

@app.route('/')
def index():
    return render_template('index.html')

# First part - easy to find (as template)
@app.route('/secret')
def part1():
    return render_template('part1.html', flag_part=FLAG_PARTS['part1'])

# Second part - serve actual file from /secret directory
@app.route('/backup')
def part2():
    return send_from_directory('secret', 'hidden-part2.html')

# Third part - serve actual file from /admin directory
@app.route('/admin/config')
def part3():
    return send_from_directory('admin', 'config-part3.html')


# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('secret', exist_ok=True)
    os.makedirs('admin', exist_ok=True)
    app.run(debug=True)