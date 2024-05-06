# Medication Refill Calendar Generator

The Medication Refill Calendar Generator is a Python script that generates a personalized medication refill calendar for a given year. It helps users track and manage their medication schedules by displaying the start dates, refill dates, and order dates for each medication in a visually appealing calendar format.

## Features

- User-friendly input prompts for medication details
- Automatic calculation of refill dates based on dosage and total number of pills
- Visual calendar generation with highlighted medication dates
- Color-coded legend for easy identification of start dates, refill dates, and order dates
- Saving the generated calendar as a PNG image file
- Displaying the generated calendar image for immediate viewing

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command:
   ```
   pip install pillow
   ```

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the script using the following command:
   ```
   python medication_refill_calendar.py
   ```

3. Follow the prompts to enter the year for the calendar and the medication details, including:
   - Medication name
   - Dosage per day
   - Total number of pills
   - Start date (YYYY-MM-DD)

4. After entering all the medication details, the script will generate the medication refill calendar and save it as a PNG image file with a descriptive name (e.g., `medication_refill_calendar_2023.png`).

5. The generated calendar image will be displayed automatically for immediate viewing.

## Customization

- Font: The script uses the "arial.ttf" font file by default. You can replace it with any other desired font file by modifying the `font` variable in the `generate_calendar()` function.

- Colors: The script uses predefined colors for highlighting the medication dates (blue for start date, green for refill date, orange for order date). You can customize these colors by modifying the `color` variables in the `generate_calendar()` function.

- Calendar Layout: The calendar layout is generated using the `calendar` module and positioned using pixel coordinates. You can adjust the positioning and spacing of the calendar elements by modifying the coordinate values in the `generate_calendar()` function.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Acknowledgements

- The script utilizes the Pillow library for image manipulation.
- The calendar layout is generated using the built-in `calendar` module in Python.
