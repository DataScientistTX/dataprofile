# DataProfile: No-Code Exploratory Data Analysis Tool

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dataprofile.streamlit.app/)

DataProfile is a powerful, user-friendly tool for performing exploratory data analysis without writing a single line of code. It leverages the capabilities of pandas-profiling to provide in-depth insights into your data, all within a sleek Streamlit interface.

![DataProfile Demo](https://github.com/DataScientistTX/dataprofile/blob/main/gif.gif)

## Features

- Upload CSV files for instant analysis
- Generate comprehensive data profiles with a single click
- Choose between Minimal, Explorative, and Default profiling modes
- Interactive web interface powered by Streamlit
- Detailed visualizations and statistics for each variable in your dataset

## Installation

Follow these steps to set up DataProfile on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/DataScientistTX/dataprofile.git
   ```

2. Navigate to the project directory:
   ```bash
   cd dataprofile
   ```

3. (Optional) Ensure you have the latest version:
   ```bash
   git pull origin main
   ```

4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you're in the project directory:
   ```bash
   cd dataprofile
   ```

2. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

4. Upload your CSV file and select a profiling mode to start analyzing your data.

Alternatively, you can use the deployed version of DataProfile at [https://dataprofile.streamlit.app/](https://dataprofile.streamlit.app/).

## Contributing

We welcome contributions to DataProfile! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling) for the excellent profiling tool
- [Streamlit](https://streamlit.io/) for making it easy to create data apps

## Contact

Your Name - [@DataScientistTX](https://x.com/DataScientistTX) - sercan.gul@gmail.com

Project Link: [https://github.com/DataScientistTX/dataprofile](https://github.com/DataScientistTX/dataprofile)