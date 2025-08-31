from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Top 10 LLC services
TOP_LLC_SERVICES = [
    "Northwestern",
    "LegalZoom", 
    "Rocket Lawyer",
    "Incfile",
    "ZenBusiness",
    "LegalNature",
    "MyCorporation",
    "BizFilings",
    "CorpNet",
    "Swyft Filings"
]

# Service information
SERVICE_INFO = {
    "Northwestern": {
        "description": "Northwest Registered Agent offers the most cost-effective LLC formation service at just $39.",
        "base_cost": "$39 formation service",
        "website": "https://consumer-champion.org/LLCwebsite",
        "rating": "4.7/5 stars"
    },
    "LegalZoom": {
        "description": "LegalZoom is a well-established legal services company offering comprehensive LLC formation packages.",
        "base_cost": "Starting at $79 + state fees",
        "website": "https://www.legalzoom.com",
        "rating": "4.5/5 stars"
    },
    "ZenBusiness": {
        "description": "ZenBusiness offers a unique $0 LLC formation service with ongoing business support.",
        "base_cost": "Starting at $0 + state fees",
        "website": "https://www.zenbusiness.com",
        "rating": "4.6/5 stars"
    },
    "Rocket Lawyer": {
        "description": "Rocket Lawyer provides legal document services with attorney consultations.",
        "base_cost": "Starting at $99 + state fees",
        "website": "https://www.rocketlawyer.com",
        "rating": "4.4/5 stars"
    },
    "Incfile": {
        "description": "Incfile offers free LLC formation with registered agent service.",
        "base_cost": "Free LLC formation + $0/year registered agent",
        "website": "https://www.incfile.com",
        "rating": "4.3/5 stars"
    },
    "LegalNature": {
        "description": "LegalNature provides affordable legal document services.",
        "base_cost": "Starting at $49 + state fees",
        "website": "https://www.legalnature.com",
        "rating": "4.2/5 stars"
    },
    "MyCorporation": {
        "description": "MyCorporation offers business formation services with additional business tools.",
        "base_cost": "Starting at $79 + state fees",
        "website": "https://www.mycorporation.com",
        "rating": "4.1/5 stars"
    },
    "BizFilings": {
        "description": "BizFilings offers professional business formation services.",
        "base_cost": "Starting at $99 + state fees",
        "website": "https://www.bizfilings.com",
        "rating": "4.0/5 stars"
    },
    "CorpNet": {
        "description": "CorpNet provides business formation and compliance services.",
        "base_cost": "Starting at $89 + state fees",
        "website": "https://www.corpnet.com",
        "rating": "4.0/5 stars"
    },
    "Swyft Filings": {
        "description": "Swyft Filings offers fast and efficient business formation services.",
        "base_cost": "Starting at $49 + state fees",
        "website": "https://www.swyftfilings.com",
        "rating": "3.9/5 stars"
    }
}

# Sample data for demonstration (in production, this would come from CSV)
SAMPLE_DATA = {
    "California": [
        {"name": "ABC Business Services", "phone": "(555) 123-4567", "address": "123 Main St, Los Angeles, CA"},
        {"name": "XYZ Consulting", "phone": "(555) 987-6543", "address": "456 Oak Ave, San Francisco, CA"}
    ],
    "Texas": [
        {"name": "Lone Star Business", "phone": "(555) 111-2222", "address": "789 Pine St, Austin, TX"},
        {"name": "Texas Solutions", "phone": "(555) 333-4444", "address": "321 Elm St, Houston, TX"}
    ],
    "Florida": [
        {"name": "Sunshine Services", "phone": "(555) 555-6666", "address": "654 Beach Blvd, Miami, FL"},
        {"name": "Florida Business", "phone": "(555) 777-8888", "address": "987 Palm St, Orlando, FL"}
    ]
}

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', top_services=TOP_LLC_SERVICES, service_info=SERVICE_INFO)

@app.route('/service/<service_name>')
def service_page(service_name):
    """Individual service page"""
    return render_template('service.html', service_name=service_name, service_info=SERVICE_INFO.get(service_name, {}))

@app.route('/service/<service_name>/<state>')
def service_state_page(service_name, state):
    """State-specific service page"""
    state_data = SAMPLE_DATA.get(state, [])
    return render_template('service_state.html', service_name=service_name, state=state, services=state_data, service_info=SERVICE_INFO.get(service_name, {}))

@app.route('/top10-llc-services')
def top10_llc_services():
    """Top 10 LLC Services page"""
    return render_template('top10_llc_services.html', services=TOP_LLC_SERVICES, service_info=SERVICE_INFO)

@app.route('/about')
def about():
    """About Us page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact Us page"""
    return render_template('contact.html')

@app.route('/privacy-policy')
def privacy_policy():
    """Privacy Policy page"""
    return render_template('privacy_policy.html')

@app.route('/terms-and-conditions')
def terms_and_conditions():
    """Terms and Conditions page"""
    return render_template('terms_and_conditions.html')

@app.route('/api/services')
def api_services():
    """API endpoint to get all services"""
    return jsonify(TOP_LLC_SERVICES)

@app.route('/api/states')
def api_states():
    """API endpoint to get all states"""
    return jsonify(list(SAMPLE_DATA.keys()))

@app.route('/api/service/<service_name>/states')
def api_service_states(service_name):
    """API endpoint to get states for a specific service"""
    return jsonify(list(SAMPLE_DATA.keys()))

@app.route('/api/data-summary')
def api_data_summary():
    """API endpoint to get data summary"""
    total_services = sum(len(services) for services in SAMPLE_DATA.values())
    return jsonify({
        'total_services': total_services,
        'total_states': len(SAMPLE_DATA),
        'total_cities': total_services
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
