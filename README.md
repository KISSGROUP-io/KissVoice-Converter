# KissVoice Converter

## Description

**KissVoice Converter** is a simple and efficient web tool designed to convert media files using a clean and user-friendly web interface. Built with Python's Flask framework and powered by `ffmpeg`, this application allows users to upload, process, and download files in different formats quickly and seamlessly.

### Features

- **File Upload**: Upload media files directly from your browser.
- **File Conversion**: Convert audio and video files to different formats.
- **Download Results**: Download the processed files easily.
- **Cross-Platform**: Works on any modern web browser.
- **Error Handling**: Displays user-friendly error messages when issues arise.
- **Delete**: Files are deleted after download.


## Demo

You can see the application live at: [converter.kissvoice.kissgroup.io](https://converter.kissvoice.kissgroup.io/)

## Installation

Follow these steps to run the application locally:

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)
- `ffmpeg` installed on your system ([installation guide](https://ffmpeg.org/download.html))

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/converter-web-app.git
   cd converter-web-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. Navigate to the homepage.
2. Upload a file using the provided form.
3. Select the desired output format.
4. Click the "Convert" button.
5. Download the converted file once processing is complete.

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for responsiveness)
- **Conversion Engine**: `ffmpeg`

## Folder Structure

```
converter-web-app/
|
├── static/             # Static assets (CSS, JS, images)
├── templates/          # HTML templates
├── uploads/            # Files Upload to convert
├── converted/          # Files Converted to download
├── app.py              # Main Flask application
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## Contributing

We welcome contributions to improve this project! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your branch:
   ```bash
   git commit -m "Add feature"
   git push origin feature-name
   ```
4. Create a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/your-username/converter-web-app/issues) or contact the support team at [support@kissvoice.kissgroup.io](mailto:support@kissvoice.kissgroup.io).

## Acknowledgments

- [Flask Framework](https://flask.palletsprojects.com/)
- [ffmpeg](https://ffmpeg.org/)
- Bootstrap for frontend styling.

