from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

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
        "detailed_review": "ZenBusiness has revolutionized the LLC formation market with their $0 formation service. While you still need to pay state fees, their core formation service is completely free. They make money through their ongoing business services, which include compliance monitoring and tax filing assistance. Their business dashboard is particularly user-friendly and helps new business owners stay on top of their compliance requirements.",
        "pros": [
            "Free formation service",
            "Excellent business dashboard",
            "Good ongoing support",
            "Compliance monitoring",
            "Tax filing assistance"
        ],
        "cons": [
            "Upselling to paid services",
            "Limited free features after first year",
            "Can be confusing pricing structure"
        ],
        "best_for": "Entrepreneurs who want to minimize upfront costs and need ongoing business support services."
    },
    "Rocket Lawyer": {
        "description": "Rocket Lawyer offers a subscription-based legal service model with unlimited legal documents and attorney consultations.",
        "base_cost": "$99.99/month subscription",
        "availability": "Available in all 50 states",
        "features": [
            "Unlimited legal documents",
            "Attorney consultations",
            "Business formation included",
            "Legal document review",
            "Ongoing legal support"
        ],
        "contact": "Visit RocketLawyer.com for contact information",
        "website": "https://www.rocketlawyer.com",
        "rating": "4.4/5 stars from 1,500+ clients",
        "detailed_review": "Rocket Lawyer takes a different approach with their subscription-based model. For a monthly fee, you get access to unlimited legal documents and attorney consultations. This model works well for businesses that need ongoing legal support, but may not be cost-effective for those who only need LLC formation. Their attorney consultation feature is particularly valuable for businesses that need legal guidance.",
        "pros": [
            "Unlimited legal documents",
            "Attorney consultations included",
            "Ongoing legal support",
            "Good for complex legal needs",
            "Document review services"
        ],
        "cons": [
            "Monthly subscription required",
            "Higher long-term cost",
            "May be overkill for simple needs"
        ],
        "best_for": "Businesses that need ongoing legal support and regular attorney consultations."
    },
    "Incfile": {
        "description": "Incfile offers competitive pricing with a focus on simplicity and ease of use for LLC formation.",
        "base_cost": "Starting at $0 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Free LLC formation",
            "Free registered agent for 1 year",
            "Operating agreement",
            "Business compliance alerts",
            "Tax filing assistance"
        ],
        "contact": "Visit Incfile.com for contact information",
        "website": "https://www.incfile.com",
        "rating": "4.3/5 stars from 1,200+ clients",
        "detailed_review": "Incfile offers a straightforward approach to LLC formation with competitive pricing. Their $0 formation service includes essential features like a free registered agent and operating agreement. While their service is solid, they don't offer as many additional features as some competitors. Their platform is user-friendly and good for entrepreneurs who want a simple, no-frills formation process.",
        "pros": [
            "Free formation service",
            "Simple, user-friendly process",
            "Good customer support",
            "Competitive pricing",
            "Essential features included"
        ],
        "cons": [
            "Limited additional services",
            "Basic feature set",
            "Upselling to paid services"
        ],
        "best_for": "Entrepreneurs who want a simple, straightforward LLC formation process without unnecessary complexity."
    },
    "LegalNature": {
        "description": "LegalNature focuses on providing high-quality legal documents and forms for business formation and ongoing legal needs.",
        "base_cost": "Starting at $89 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "High-quality legal documents",
            "Attorney-reviewed forms",
            "Business formation services",
            "Ongoing legal document access",
            "Customer support"
        ],
        "contact": "Visit LegalNature.com for contact information",
        "website": "https://www.legalnature.com",
        "rating": "4.2/5 stars from 900+ clients",
        "detailed_review": "LegalNature distinguishes itself with high-quality, attorney-reviewed legal documents. While their pricing is on the higher side, they focus on providing premium legal forms and documents. Their service is particularly valuable for businesses that need ongoing access to legal documents and forms. However, their formation service is more basic compared to some competitors.",
        "pros": [
            "High-quality legal documents",
            "Attorney-reviewed forms",
            "Ongoing document access",
            "Good customer support",
            "Premium service quality"
        ],
        "cons": [
            "Higher pricing",
            "Basic formation service",
            "Limited additional features"
        ],
        "best_for": "Businesses that need high-quality legal documents and ongoing access to legal forms."
    },
    "MyCorporation": {
        "description": "MyCorporation offers comprehensive business formation services with a focus on ongoing business support and compliance.",
        "base_cost": "Starting at $99 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Comprehensive formation packages",
            "Ongoing compliance support",
            "Business credit building",
            "Tax services",
            "Business consulting"
        ],
        "contact": "Visit MyCorporation.com for contact information",
        "website": "https://www.mycorporation.com",
        "rating": "4.1/5 stars from 800+ clients",
        "detailed_review": "MyCorporation offers comprehensive business formation and ongoing support services. While their pricing is higher, they provide extensive ongoing support including business credit building and tax services. Their service is particularly valuable for businesses that need comprehensive ongoing support beyond just formation. However, their pricing may be prohibitive for budget-conscious entrepreneurs.",
        "pros": [
            "Comprehensive ongoing support",
            "Business credit building",
            "Tax services included",
            "Good customer support",
            "Extensive service offerings"
        ],
        "cons": [
            "Higher pricing",
            "Complex service offerings",
            "May be overkill for simple needs"
        ],
        "best_for": "Businesses that need comprehensive ongoing support and are willing to pay for premium services."
    },
    "BizFilings": {
        "description": "BizFilings offers advanced business formation services with sophisticated compliance monitoring and business management tools.",
        "base_cost": "Starting at $99 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Advanced business dashboard",
            "Comprehensive compliance monitoring",
            "Tax services",
            "Business consulting",
            "Document management"
        ],
        "contact": "Visit BizFilings.com for contact information",
        "website": "https://www.bizfilings.com",
        "rating": "4.0/5 stars from 700+ clients",
        "detailed_review": "BizFilings offers sophisticated business formation and management services with advanced compliance monitoring tools. Their business dashboard is particularly impressive and provides comprehensive business management capabilities. While their services are high-quality, their pricing reflects their premium positioning. Their service is best suited for established businesses that need advanced compliance and management tools.",
        "pros": [
            "Advanced business dashboard",
            "Comprehensive compliance monitoring",
            "High-quality service",
            "Good customer support",
            "Sophisticated tools"
        ],
        "cons": [
            "Higher pricing",
            "Complex interface",
            "May be overwhelming for simple needs"
        ],
        "best_for": "Established businesses that need advanced compliance monitoring and business management tools."
    },
    "CorpNet": {
        "description": "CorpNet offers personalized business formation services with a focus on customer service and ongoing support.",
        "base_cost": "Starting at $89 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Personalized service",
            "Ongoing compliance support",
            "Business consulting",
            "Document filing services",
            "Customer support"
        ],
        "contact": "Visit CorpNet.com for contact information",
        "website": "https://www.corpnet.com",
        "rating": "4.3/5 stars from 600+ clients",
        "detailed_review": "CorpNet distinguishes itself with personalized service and strong customer support. While their pricing is competitive, they focus on providing personalized attention to each client. Their service is particularly valuable for businesses that want a more personal touch and ongoing support. However, their service offerings are more basic compared to some competitors.",
        "pros": [
            "Personalized service",
            "Good customer support",
            "Competitive pricing",
            "Ongoing support",
            "Simple process"
        ],
        "cons": [
            "Limited additional services",
            "Basic feature set",
            "Less sophisticated tools"
        ],
        "best_for": "Businesses that value personalized service and ongoing support over advanced features."
    },
    "Swyft Filings": {
        "description": "Swyft Filings offers fast and efficient LLC formation services with a focus on speed and customer satisfaction.",
        "base_cost": "Starting at $49 + state fees",
        "availability": "Available in all 50 states",
        "features": [
            "Fast filing process",
            "Free name availability search",
            "Customer support",
            "Business formation services",
            "Compliance alerts"
        ],
        "contact": "Visit SwyftFilings.com for contact information",
        "website": "https://www.swyftfilings.com",
        "rating": "4.2/5 stars from 500+ clients",
        "detailed_review": "Swyft Filings lives up to their name with fast and efficient LLC formation services. Their competitive pricing and focus on speed make them a good choice for entrepreneurs who want to get their business started quickly. While their service offerings are more basic, they excel at what they do. Their customer support is responsive and helpful.",
        "pros": [
            "Fast filing process",
            "Competitive pricing",
            "Good customer support",
            "Simple process",
            "Free name search"
        ],
        "cons": [
            "Limited additional services",
            "Basic feature set",
            "Less comprehensive than competitors"
        ],
        "best_for": "Entrepreneurs who want fast, efficient LLC formation without unnecessary complexity."
    }
}

# Load CSV data
def load_csv_data():
    """Load and return CSV data"""
    # Try multiple possible paths for different environments
    possible_paths = [
        "LLC Data.csv",  # For Vercel deployment
        r"C:\rozy\LLC Data.csv",  # For local development
        "./LLC Data.csv",  # Alternative local path
    ]
    
    for csv_path in possible_paths:
        if os.path.exists(csv_path):
            try:
                df = pd.read_csv(csv_path)
                print(f"Successfully loaded CSV from: {csv_path}")
                return df
            except Exception as e:
                print(f"Error loading CSV from {csv_path}: {e}")
                continue
    
    print("CSV file not found in any of the expected locations")
    return pd.DataFrame()

@app.route('/')
def index():
    """Home page showing top LLC services"""
    return render_template('index.html', 
                         top_services=TOP_LLC_SERVICES,
                         service_info=SERVICE_INFO)

@app.route('/service/<service_name>')
def service_page(service_name):
    """Individual service page showing states with available services"""
    df = load_csv_data()
    
    if df.empty:
        return render_template('service.html', 
                             service_name=service_name,
                             states=[],
                             service_info=SERVICE_INFO.get(service_name, {}))
    
    # Get all unique states from the CSV
    states = df['state'].dropna().unique().tolist()
    states.sort()
    
    # For each state, get the first 50 services to display
    state_services = {}
    for state in states:
        state_data = df[df['state'].astype(str).str.contains(state, case=False, na=False)]
        state_services[state] = state_data.head(50).to_dict('records')
    
    return render_template('service.html', 
                         service_name=service_name,
                         states=states,
                         state_services=state_services,
                         service_info=SERVICE_INFO.get(service_name, {}))

@app.route('/service/<service_name>/<state>')
def service_state_page(service_name, state):
    """State-specific service page showing local business services"""
    df = load_csv_data()
    
    if df.empty:
        return render_template('service_state.html', 
                             service_name=service_name,
                             state=state,
                             llc_services=[],
                             service_info=SERVICE_INFO.get(service_name, {}))
    
    # Filter by state (case-insensitive)
    state_data = df[df['state'].astype(str).str.contains(state, case=False, na=False)]
    
    # Limit to 50 services per state
    llc_services = state_data.head(50).to_dict('records')
    
    # Convert all values to strings safely
    for service in llc_services:
        for key, value in service.items():
            service[key] = safe_str(value)
    
    return render_template('service_state.html', 
                         service_name=service_name,
                         state=state,
                         llc_services=llc_services,
                         service_info=SERVICE_INFO.get(service_name, {}))

@app.route('/top10-llc-services')
def top10_llc_services():
    """Top 10 LLC Services page with detailed reviews"""
    return render_template('top10_llc_services.html', 
                         service_info=SERVICE_INFO,
                         top_services=TOP_LLC_SERVICES)

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
    
    # Get all unique states from the entire DataFrame
    states = df['state'].dropna().unique().tolist()
    states.sort()
    
    return jsonify(states)

@app.route('/api/states')
def api_states():
    """API endpoint to get all states with service counts"""
    df = load_csv_data()
    
    if df.empty:
        return jsonify([])
    
    # Get state counts
    state_counts = df['state'].value_counts().to_dict()
    
    # Format response
    states_data = []
    for state, count in state_counts.items():
        if pd.notna(state):
            states_data.append({
                'state': state,
                'service_count': int(count)
            })
    
    # Sort by state name
    states_data.sort(key=lambda x: x['state'])
    
    return jsonify(states_data)

@app.route('/api/data-summary')
def api_data_summary():
    """API endpoint to get data summary"""
    df = load_csv_data()
    
    if df.empty:
        return jsonify({
            'total_records': 0,
            'unique_states': 0,
            'unique_cities': 0,
            'top_states': [],
            'top_cities': []
        })
    
    # Calculate summary statistics
    total_records = len(df)
    unique_states = df['state'].nunique()
    unique_cities = df['city'].nunique() if 'city' in df.columns else 0
    
    # Top states by service count
    top_states = df['state'].value_counts().head(10).to_dict()
    
    # Top cities by service count (if city column exists)
    top_cities = []
    if 'city' in df.columns:
        top_cities = df['city'].value_counts().head(10).to_dict()
    
    return jsonify({
        'total_records': total_records,
        'unique_states': unique_states,
        'unique_cities': unique_cities,
        'top_states': top_states,
        'top_cities': top_cities
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
