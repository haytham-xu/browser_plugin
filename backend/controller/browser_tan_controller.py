
from flask import request
from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/tabs', methods=['POST'])
def tabs():
    tabs = request.json['tabs']
    for tab in tabs:
        print(tab)
        existing_tab = Tab.query.filter_by(tab_url=tab).first()
        print( existing_tab is None, existing_tab)
        if existing_tab is None:
            new_tab = Tab(tab_url=tab)
            db.session.add(new_tab)
    db.session.commit()
    return jsonify({'message': 'Tabs received and stored.'}), 200
