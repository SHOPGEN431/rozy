# LLC Directory Flask Website

A comprehensive Flask web application that provides a directory of LLC formation services across the United States. The application organizes data from a CSV file and presents it in an easy-to-navigate format.

## Features

- **Top 10 LLC Services**: Features the most popular LLC formation services
- **State-by-State Coverage**: Each service has dedicated pages for every state they operate in
- **Detailed Information**: Contact details, ratings, reviews, and service descriptions
- **Modern UI**: Beautiful, responsive design with Bootstrap 5
- **API Endpoints**: RESTful API for programmatic access to data

## Services Included

1. LegalZoom
2. Northwestern
3. Rocket Lawyer
4. Incfile
5. ZenBusiness
6. LegalNature
7. MyCorporation
8. BizFilings
9. CorpNet
10. Swyft Filings

## 🚀 Deployment

### Vercel Deployment (Recommended)

This project is configured for easy deployment on Vercel:

1. **Fork/Clone** this repository to your GitHub account
2. **Connect to Vercel**:  
   * Go to [vercel.com](https://vercel.com)  
   * Sign up/Login with your GitHub account  
   * Click "New Project"  
   * Import your GitHub repository  
   * Vercel will automatically detect the Flask configuration
3. **Deploy**:  
   * Vercel will automatically build and deploy your site  
   * You'll get a live URL (e.g., `https://your-project.vercel.app`)

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Local Development

#### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

#### Installation

1. **Clone or download the project files to your local machine**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure your CSV file is in the correct location**:
   - The application expects the CSV file at: `C:\rozy\LLC Data.csv`
   - Make sure the file contains the required columns: name, state, city, phone, full_address, rating, reviews, site, category, type, description, working_hours, logo

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the website**:
   - Open your web browser and go to: `http://localhost:5000`

## Usage

### Home Page (`/`)
- Displays all 10 top LLC services
- Click on any service to view states where they operate

### Service Page (`/service/<service_name>`)
- Shows all states where a specific service operates
- Displays summary information for each state
- Click on a state to view detailed services

### State-Specific Page (`/service/<service_name>/<state>`)
- Lists all LLC services for a specific service in a specific state
- Shows detailed contact information, ratings, and reviews
- Provides direct links to websites, phone numbers, and directions

### API Endpoints
- `/api/services` - Get list of all services
- `/api/service/<service_name>/states` - Get states for a specific service

## File Structure

```
C:\rozy\
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── DEPLOYMENT.md         # Deployment guide
├── README.md             # This file
├── LLC Data.csv          # Your CSV data file
├── templates/            # HTML templates
│   ├── base.html         # Base template with styling
│   ├── index.html        # Home page
│   ├── service.html      # Service overview page
│   ├── service_state.html # State-specific service page
│   ├── top10_llc_services.html # Top 10 services page
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
│   ├── privacy_policy.html # Privacy policy
│   └── terms_and_conditions.html # Terms and conditions
└── static/               # Static assets (if any)
```

## Customization

### Adding New Services
Edit the `TOP_LLC_SERVICES` list in `app.py` to add or modify services.

### Styling
Modify the CSS in `templates/base.html` to change the appearance.

### Data Source
Update the `csv_path` variable in the `load_llc_data()` function to point to your CSV file location.

## Troubleshooting

### Common Issues

1. **CSV file not found**:
   - Ensure the CSV file is located at `C:\rozy\LLC Data.csv`
   - Check file permissions

2. **Missing dependencies**:
   - Run `pip install -r requirements.txt`

3. **Port already in use**:
   - Change the port in `app.py` line: `app.run(debug=True, host='0.0.0.0', port=5001)`

4. **Data not displaying**:
   - Check that your CSV file has the required columns
   - Verify the service names in your data match the `TOP_LLC_SERVICES` list

## Support

For issues or questions, please check:
1. The CSV file format and location
2. Python version compatibility
3. Network connectivity for external resources (Bootstrap, Font Awesome)

## License

This project is open source and available under the MIT License.
