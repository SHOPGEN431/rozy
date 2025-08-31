# FileYourLLC.online - LLC Formation Services Directory

A comprehensive directory website for LLC formation services, providing detailed information about top service providers, local business resources, and state-specific guidance.

## 🌟 Features

- **Top 10 LLC Services Directory** - Detailed reviews and comparisons
- **State-Specific Pages** - Service availability by state
- **Local Business Integration** - Connect with local CPAs and accountants
- **Comprehensive Reviews** - Detailed analysis of each service provider
- **Mobile-Responsive Design** - Works perfectly on all devices
- **Modern UI/UX** - Clean, professional design with smooth animations

## 🚀 Live Demo

Visit the live website: [FileYourLLC.online](https://fileyourllc.online)

## 📋 Pages

- **Home** - Overview of top LLC services
- **Service Pages** - Individual service provider information
- **State Pages** - State-specific service availability
- **Top 10 Reviews** - Detailed comparison of top services
- **About Us** - Information about the directory
- **Contact** - Contact form and information
- **Privacy Policy** - Privacy and data collection policies
- **Terms & Conditions** - Legal terms and affiliate disclosures

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5.3.0, Custom CSS
- **Icons**: Font Awesome 6.4.0
- **Data**: Pandas for CSV processing
- **Deployment**: Vercel

## 📁 Project Structure

```
rozy/
├── app.py                 # Main Flask application
├── vercel.json           # Vercel deployment configuration
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── templates/           # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Home page
│   ├── service.html     # Service provider pages
│   ├── service_state.html # State-specific pages
│   ├── top10_llc_services.html # Top 10 reviews
│   ├── about.html       # About page
│   ├── contact.html     # Contact page
│   ├── privacy_policy.html # Privacy policy
│   └── terms_and_conditions.html # Terms and conditions
└── LLC Data.csv         # Local business data (not included in repo)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SHOPGEN431/rozy.git
   cd rozy
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🌐 Deployment

### Vercel Deployment

This project is configured for easy deployment on Vercel:

1. **Connect to Vercel**
   - Fork this repository
   - Connect your GitHub account to Vercel
   - Import the repository

2. **Automatic Deployment**
   - Vercel will automatically detect the Flask app
   - The `vercel.json` file handles routing configuration
   - Deployments happen automatically on git push

3. **Environment Variables**
   - No additional environment variables required
   - The app works out of the box

### Manual Deployment

If you prefer manual deployment:

1. **Build the application**
   ```bash
   pip install -r requirements.txt
   ```

2. **Deploy to your preferred platform**
   - The app is compatible with most Python hosting platforms
   - Ensure your platform supports Flask applications

## 📊 Data Management

The application uses a CSV file (`LLC Data.csv`) containing local business information. This file is not included in the repository for privacy reasons.

### CSV Structure
- `name` - Business name
- `site` - Website URL
- `state` - State location
- `city` - City location
- `category` - Business category
- `type` - Business type
- `phone` - Contact phone
- `full_address` - Complete address
- `rating` - Business rating
- `reviews` - Number of reviews
- `description` - Business description
- `working_hours` - Operating hours
- `logo` - Logo URL

## 🔧 Configuration

### Customization

1. **Service Information**: Edit the `SERVICE_INFO` dictionary in `app.py`
2. **Styling**: Modify CSS in `templates/base.html`
3. **Content**: Update HTML templates in the `templates/` directory

### Adding New Services

To add a new LLC service:

1. Add the service name to `TOP_LLC_SERVICES` list
2. Add service information to `SERVICE_INFO` dictionary
3. Update navigation in `templates/base.html`

## 📱 Mobile Responsiveness

The website is fully responsive and optimized for:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🔒 Privacy & Legal

- **Privacy Policy**: No personal data collection
- **Terms & Conditions**: Educational information only
- **Affiliate Disclosure**: Transparent affiliate relationships
- **Legal Disclaimer**: Not legal advice

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- Visit the [Contact Page](https://fileyourllc.online/contact)
- Check the [About Page](https://fileyourllc.online/about) for more information

## 🙏 Acknowledgments

- Bootstrap for the responsive framework
- Font Awesome for the icons
- Flask community for the web framework
- All the LLC service providers listed in the directory

---

**Note**: This directory is for educational purposes only. Always consult with qualified legal, tax, and financial professionals before making business decisions.
