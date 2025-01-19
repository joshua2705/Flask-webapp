# SkyGuru: Weather Forecast Web Application

![SkyGuru Logo](image1.png)

## Project Background

SkyGuru is a weather web application designed to provide users with detailed weather forecasts for specific cities and their potential impact on users' agendas. 

### Project Motivation

The goal of the project is to help travelers plan their trips by forecasting weather conditions on specific travel dates. The application provides: 
- Weather forecasts for cities.
- Insights into weather conditions affecting scheduled events.
- Persistent event information with dynamically updated weather data.

### Key Features
- **Home Page**: Search weather information for any city in selected countries.
- **Schedule Page**: Add calendar events to check weather forecasts for event days and locations.
- **API Integration**: Uses the OpenWeather API to retrieve real-time weather data.

**Technical Note**: The free API supports weather forecasts up to five days in advance.

![Home Page UI](image2.png)

### Reasoning
The project was designed to cater to varying skill levels among team members, offering opportunities to work on API integration, UI design, and modular programming. 

---

## Collaboration and Development Framework

![Collaboration](image3.png)

- **Frameworks & Tools**: Built using Flask for backend, HTML, and Tailwind CSS for frontend.
- **Version Control**: Collaborated via GitHub for task management and code integration using a branching model.

---

## Project Versions

### V0: Foundation and Basic Features

1. **UI Design**
   - Simple, user-friendly interface with HTML and Tailwind CSS.
   - Intuitive layout for users of all technical levels.

2. **OpenWeather API Integration**
   - Modular design for API integration.
   - Environment variable setup for secure API key management.

3. **Functional Search Bar**
   - City-based search with input validation.

4. **Weather Data Display**
   - Real-time weather conditions with visual icons.

### V1: Enhancements and New Features

1. **Calendar Feature**
   - Users can schedule events.
   - Event data stored locally as JSON objects.
   - Automatic deletion of outdated events.

2. **Country Dropdown**
   - Enhanced search functionality with country selection.
   - Dictionary-based country code management.

3. **UI & Code Optimization**
   - Added radio buttons for date selection.
   - Improved maintainability and modularity.

![Weather Display](image4.png)

### V2: Final Version

1. **Event-Weather Integration**
   - Dynamically display weather conditions for scheduled events.
   - Enhanced UI with event-specific weather icons.

2. **Branding**
   - Branded as SkyGuru with a custom logo.

3. **Error Handling**
   - Improved stability with error handlers and debugging.

4. **Testing and Documentation**
   - Comments added for readability.
   - Comprehensive testing and bug fixes.

---

## Challenges and Areas for Improvement

### Challenges:
- Training team members in Python and Git.
- Time estimation and scope adjustment.
- Git branch integration.
- Balancing functionality with UI aesthetics.
- Dynamic weather rendering.
- File-based event persistence.

### Areas for Improvement:
- Add user-specific login screens.
- Support full calendar imports.
- Allow dual-location weather tracking.
- Provide hourly weather data for day-night differences.
- Optimize API calls for faster event rendering.
- Enhance error handling with informative pop-ups.

---

## Learning Contributions

![Team Contributions](image5.png)

### Mathilde:
- Focused on API integration and modularity.
- Developed country dropdown using dictionaries.
- Added comments to improve code clarity.

### George:
- Designed dynamic weather condition displays.
- Enhanced UI for better user experience.
- Developed and integrated the SkyGuru logo.

### Nate:
- Created search-input UI and calendar section.
- Improved input responsiveness with dropdown features.
- Conducted thorough testing.

### Joshua:
- Led team coordination and integration.
- Developed initial boilerplate and restructured code.
- Implemented event functionality with file persistence.
- Debugged and fine-tuned the final product.

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/joshua2705/Flask-webapp.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Flask-webapp
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   flask run
   ```
   or
   ```bash
   python -m flask run
   ```

5. Open the displayed link in your browser.

---

### Repository Link
[GitHub Repository](https://github.com/joshua2705/Flask-webapp)
