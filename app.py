from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Configure for Vercel
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Helper function to safely convert values to strings
def safe_str(value):
    """Safely convert any value to string"""
    if pd.isna(value) or value is None:
        return ''
    return str(value)

# Top 10 LLC services (based on common ones)
TOP_LLC_SERVICES = [
    "Northwestern", # Moved to first position
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

# Service information including costs and availability
SERVICE_INFO = {
    "Northwestern": {
        "description": "Northwest Registered Agent offers the most cost-effective LLC formation service at just $39, with comprehensive business formation packages including registered agent service, business address, email, domain name, custom website, and mail forwarding.",
        "base_cost": "$39 formation service",
        "availability": "Available in all 50 states",
        "features": [
            "Free registered agent service",
            "Business address & email included",
            "Custom website & domain name",
            "Mail forwarding service",
            "Privacy by Default® protection",
            "Corporate Guide® Service"
        ],
        "contact": "Visit their website for direct contact information",
        "website": "https://consumer-champion.org/LLCwebsite", # Updated link
        "rating": "4.7/5 stars from 1,645+ clients", # Added rating
        "detailed_review": "Northwest Registered Agent stands out as the most cost-effective option in the LLC formation market. With their $39 formation service, they provide exceptional value while maintaining high-quality service standards. Their comprehensive package includes essential services like registered agent service, business address, and even a custom website with domain name. The company's Privacy by Default® protection ensures your personal information stays secure, while their Corporate Guide® Service provides ongoing support for your business needs. Customer reviews consistently praise their responsive customer service and transparent pricing structure.",
        "pros": [
            "Lowest cost at $39",
            "Comprehensive package included",
            "Excellent customer service",
            "Privacy protection features",
            "Custom website included",
            "Free registered agent service"
        ],
        "cons": [
            "Limited additional services",
            "Basic website templates"
        ],
        "best_for": "Budget-conscious entrepreneurs and small business owners looking for comprehensive LLC formation at the lowest cost."
    },
    "LegalZoom": {
        "description": "LegalZoom is a well-established legal services company offering comprehensive LLC formation packages with additional legal document services.",
        "base_cost": "Starting at $79 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Operating agreement included",
            "EIN application assistance",
            "Business compliance alerts",
            "Legal document library",
            "Attorney consultations available"
        ],
        "contact": "Visit LegalZoom.com for contact information",
        "website": "https://www.legalzoom.com",
        "rating": "4.5/5 stars from 2,000+ clients",
        "detailed_review": "LegalZoom is one of the most recognized names in online legal services, with over 20 years of experience helping businesses get started. Their comprehensive LLC formation packages include essential legal documents and ongoing compliance support. While their pricing is higher than some competitors, their extensive legal document library and attorney consultation options provide significant value for businesses that need ongoing legal support.",
        "pros": [
            "Well-established brand",
            "Comprehensive legal services",
            "Attorney consultations available",
            "Extensive document library",
            "Good customer support"
        ],
        "cons": [
            "Higher pricing",
            "Upselling during process",
            "Can be overwhelming for simple needs"
        ],
        "best_for": "Businesses that need ongoing legal support and comprehensive legal services beyond just LLC formation."
    },
    "ZenBusiness": {
        "description": "ZenBusiness offers a unique $0 LLC formation service with ongoing business support and compliance monitoring.",
        "base_cost": "Starting at $0 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Free LLC formation",
            "Free registered agent for 1 year",
            "Compliance monitoring",
            "Business dashboard",
            "Tax filing assistance"
        ],
        "contact": "Visit ZenBusiness.com for contact information",
        "website": "https://www.zenbusiness.com",
        "rating": "4.6/5 stars from 1,800+ clients",
        "detailed_review": "ZenBusiness stands out with their unique $0 LLC formation offer, making them an attractive option for budget-conscious entrepreneurs. Their platform provides comprehensive business support beyond just formation, including compliance monitoring and tax filing assistance. The free registered agent service for the first year adds significant value to their offering.",
        "pros": [
            "Free LLC formation",
            "Free registered agent for 1 year",
            "Comprehensive business support",
            "Good customer service",
            "Compliance monitoring"
        ],
        "cons": [
            "Limited free features",
            "Upselling to paid plans",
            "Basic website templates"
        ],
        "best_for": "Entrepreneurs looking for free LLC formation with ongoing business support and compliance monitoring."
    },
    "Rocket Lawyer": {
        "description": "Rocket Lawyer provides legal document services with attorney consultations and ongoing legal support.",
        "base_cost": "Starting at $99 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Legal document library",
            "Attorney consultations",
            "Business formation services",
            "Ongoing legal support",
            "Document review services"
        ],
        "contact": "Visit RocketLawyer.com for contact information",
        "website": "https://www.rocketlawyer.com",
        "rating": "4.4/5 stars from 1,500+ clients",
        "detailed_review": "Rocket Lawyer focuses on providing comprehensive legal services beyond just business formation. Their platform offers access to a vast library of legal documents and attorney consultations, making them ideal for businesses that need ongoing legal support. While their pricing is higher, the value comes from their extensive legal resources and professional consultations.",
        "pros": [
            "Extensive legal document library",
            "Attorney consultations available",
            "Ongoing legal support",
            "Professional legal services",
            "Document review included"
        ],
        "cons": [
            "Higher pricing",
            "Complex for simple needs",
            "Requires subscription for full access"
        ],
        "best_for": "Businesses that need ongoing legal support and access to legal documents and attorney consultations."
    },
    "Incfile": {
        "description": "Incfile offers free LLC formation with registered agent service and business compliance tools.",
        "base_cost": "Free LLC formation + $0/year registered agent",
        "availability": "Available in all 50 states",
        "features": [
            "Free LLC formation",
            "Free registered agent service",
            "Business compliance alerts",
            "Tax filing assistance",
            "Business dashboard"
        ],
        "contact": "Visit Incfile.com for contact information",
        "website": "https://www.incfile.com",
        "rating": "4.3/5 stars from 1,200+ clients",
        "detailed_review": "Incfile offers a compelling free LLC formation service with ongoing registered agent service included. Their platform provides essential business tools and compliance monitoring, making them a good choice for entrepreneurs who want to minimize upfront costs while still getting quality service.",
        "pros": [
            "Free LLC formation",
            "Free registered agent service",
            "Good customer support",
            "Compliance monitoring",
            "Business tools included"
        ],
        "cons": [
            "Limited additional services",
            "Basic website templates",
            "Upselling to paid features"
        ],
        "best_for": "Entrepreneurs looking for free LLC formation with ongoing registered agent service and basic business tools."
    },
    "LegalNature": {
        "description": "LegalNature provides affordable legal document services with a focus on business formation and compliance.",
        "base_cost": "Starting at $49 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Affordable pricing",
            "Legal document library",
            "Business formation services",
            "Compliance monitoring",
            "Customer support"
        ],
        "contact": "Visit LegalNature.com for contact information",
        "website": "https://www.legalnature.com",
        "rating": "4.2/5 stars from 800+ clients",
        "detailed_review": "LegalNature offers competitive pricing for LLC formation and legal document services. Their platform is straightforward and user-friendly, making it a good choice for entrepreneurs who want quality service without the complexity of larger platforms.",
        "pros": [
            "Affordable pricing",
            "Simple and straightforward",
            "Good customer support",
            "Legal document access",
            "Compliance tools"
        ],
        "cons": [
            "Limited additional services",
            "Basic features compared to competitors",
            "Less brand recognition"
        ],
        "best_for": "Entrepreneurs looking for affordable, straightforward LLC formation without unnecessary complexity."
    },
    "MyCorporation": {
        "description": "MyCorporation offers business formation services with additional business tools and compliance support.",
        "base_cost": "Starting at $79 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Business formation services",
            "Compliance monitoring",
            "Business tools and resources",
            "Customer support",
            "Document filing services"
        ],
        "contact": "Visit MyCorporation.com for contact information",
        "website": "https://www.mycorporation.com",
        "rating": "4.1/5 stars from 600+ clients",
        "detailed_review": "MyCorporation provides solid business formation services with additional tools and resources for ongoing business management. Their platform is user-friendly and offers good customer support, making it suitable for entrepreneurs who want comprehensive business support.",
        "pros": [
            "Comprehensive business tools",
            "Good customer support",
            "User-friendly platform",
            "Compliance monitoring",
            "Additional business resources"
        ],
        "cons": [
            "Higher pricing",
            "Limited free features",
            "Less brand recognition"
        ],
        "best_for": "Entrepreneurs who want comprehensive business formation and ongoing business management tools."
    },
    "BizFilings": {
        "description": "BizFilings offers professional business formation services with compliance and tax support.",
        "base_cost": "Starting at $99 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Professional business formation",
            "Compliance monitoring",
            "Tax filing assistance",
            "Business dashboard",
            "Customer support"
        ],
        "contact": "Visit BizFilings.com for contact information",
        "website": "https://www.bizfilings.com",
        "rating": "4.0/5 stars from 500+ clients",
        "detailed_review": "BizFilings offers professional business formation services with a focus on compliance and ongoing business support. Their platform provides comprehensive tools for business management and tax filing assistance.",
        "pros": [
            "Professional services",
            "Compliance monitoring",
            "Tax filing assistance",
            "Business dashboard",
            "Good customer support"
        ],
        "cons": [
            "Higher pricing",
            "Limited free features",
            "Complex for simple needs"
        ],
        "best_for": "Businesses that need professional formation services with ongoing compliance and tax support."
    },
    "CorpNet": {
        "description": "CorpNet provides business formation and compliance services with personalized support.",
        "base_cost": "Starting at $89 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Business formation services",
            "Compliance monitoring",
            "Personalized support",
            "Document filing",
            "Business tools"
        ],
        "contact": "Visit CorpNet.com for contact information",
        "website": "https://www.corpnet.com",
        "rating": "4.0/5 stars from 400+ clients",
        "detailed_review": "CorpNet offers personalized business formation services with a focus on customer support and compliance monitoring. Their platform is suitable for entrepreneurs who want more hands-on support during the formation process.",
        "pros": [
            "Personalized support",
            "Compliance monitoring",
            "Good customer service",
            "Business tools included",
            "Document filing services"
        ],
        "cons": [
            "Higher pricing",
            "Limited online features",
            "Less automation"
        ],
        "best_for": "Entrepreneurs who prefer personalized support and hands-on assistance during business formation."
    },
    "Swyft Filings": {
        "description": "Swyft Filings offers fast and efficient business formation services with ongoing support.",
        "base_cost": "Starting at $49 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Fast filing process",
            "Business formation services",
            "Compliance monitoring",
            "Customer support",
            "Business tools"
        ],
        "contact": "Visit SwyftFilings.com for contact information",
        "website": "https://www.swyftfilings.com",
        "rating": "3.9/5 stars from 300+ clients",
        "detailed_review": "Swyft Filings focuses on providing fast and efficient business formation services. Their platform is straightforward and offers good customer support, making it suitable for entrepreneurs who want quick and simple formation.",
        "pros": [
            "Fast filing process",
            "Simple and straightforward",
            "Good customer support",
            "Affordable pricing",
            "Business tools included"
        ],
        "cons": [
            "Limited additional services",
            "Basic features",
            "Less brand recognition"
        ],
        "best_for": "Entrepreneurs who want fast, simple, and affordable LLC formation without unnecessary complexity."
    }
}

# Load CSV data
def load_csv_data():
    """Load and return CSV data"""
    try:
        csv_path = os.path.join(os.path.dirname(__file__), 'LLC Data.csv')
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            return df
        else:
            # Return empty DataFrame if file doesn't exist
            return pd.DataFrame()
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return pd.DataFrame()

# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', top_services=TOP_LLC_SERVICES, service_info=SERVICE_INFO)

@app.route('/service/<service_name>')
def service_page(service_name):
    """Individual service page"""
    df = load_csv_data()
    
    if df.empty:
        return render_template('service.html', service_name=service_name, state_services=[], service_info=SERVICE_INFO.get(service_name, {}))
    
    # Filter data for the specific service
    service_data = df[df['name'].astype(str).str.contains(service_name, case=False, na=False)]
    
    # Group by state
    state_services = {}
    for _, row in service_data.iterrows():
        state = safe_str(row.get('state', ''))
        if state:
            if state not in state_services:
                state_services[state] = []
            state_services[state].append(row)
    
    return render_template('service.html', service_name=service_name, state_services=state_services, service_info=SERVICE_INFO.get(service_name, {}))

@app.route('/service/<service_name>/<state>')
def service_state_page(service_name, state):
    """State-specific service page"""
    df = load_csv_data()
    
    if df.empty:
        return render_template('service_state.html', service_name=service_name, state=state, services=[], service_info=SERVICE_INFO.get(service_name, {}))
    
    # Filter data for the specific service and state
    service_data = df[
        (df['name'].astype(str).str.contains(service_name, case=False, na=False)) &
        (df['state'].astype(str).str.contains(state, case=False, na=False))
    ]
    
    # Limit to 50 services
    services = service_data.head(50).to_dict('records')
    
    return render_template('service_state.html', service_name=service_name, state=state, services=services, service_info=SERVICE_INFO.get(service_name, {}))

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

# API endpoints
@app.route('/api/services')
def api_services():
    """API endpoint to get all services"""
    return jsonify(TOP_LLC_SERVICES)

@app.route('/api/service/<service_name>/states')
def api_service_states(service_name):
    """API endpoint to get states for a specific service"""
    df = load_csv_data()
    
    if df.empty:
        return jsonify([])
    
    # Filter data for the specific service
    service_data = df[df['name'].astype(str).str.contains(service_name, case=False, na=False)]
    
    # Get unique states
    states = service_data['state'].astype(str).unique().tolist()
    states = [state for state in states if state and state != 'nan']
    
    return jsonify(states)

@app.route('/api/states')
def api_states():
    """API endpoint to get all states"""
    df = load_csv_data()
    
    if df.empty:
        return jsonify([])
    
    states = df['state'].astype(str).unique().tolist()
    states = [state for state in states if state and state != 'nan']
    
    return jsonify(states)

@app.route('/api/data-summary')
def api_data_summary():
    """API endpoint to get data summary"""
    df = load_csv_data()
    
    if df.empty:
        return jsonify({
            'total_services': 0,
            'total_states': 0,
            'total_cities': 0
        })
    
    summary = {
        'total_services': len(df),
        'total_states': df['state'].nunique(),
        'total_cities': df['city'].nunique()
    }
    
    return jsonify(summary)

# For Vercel deployment
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
