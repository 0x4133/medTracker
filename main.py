import calendar
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont


def get_medication_details():
    medications = []
    while True:
        name = input("Enter medication name (or press Enter to finish): ")
        if name == "":
            break
        dosage = int(input("Enter dosage per day: "))
        total_pills = int(input("Enter total number of pills: "))
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        medications.append((name, dosage, total_pills, start_date))
    return medications


def calculate_refill_dates(medications):
    refill_dates = {}
    for name, dosage, total_pills, start_date in medications:
        days_supply = total_pills // dosage
        refill_date = start_date + timedelta(days=days_supply)
        order_date = refill_date - timedelta(days=7)  # Order 1 week before refill
        refill_dates[name] = (start_date, refill_date, order_date)
    return refill_dates


def generate_calendar(year, refill_dates):
    img = Image.new("RGB", (1200, 1600), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)

    # Draw calendar grid
    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]
        draw.text((50, (month - 1) * 120 + 25), month_name, fill="black", font=font)

        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day != 0:
                    date = datetime(year, month, day)
                    day_str = str(day)
                    draw.text(
                        (day_idx * 150 + 100, week_idx * 20 + (month - 1) * 120 + 50),
                        day_str,
                        fill="black",
                        font=font,
                    )

                    # Highlight medication dates
                    for name, dates in refill_dates.items():
                        if date in dates:
                            if date == dates[0]:
                                color = "blue"
                                label = name
                            elif date == dates[1]:
                                color = "green"
                                label = name
                            else:
                                color = "orange"
                                label = "Order Date"

                            draw.rectangle(
                                (
                                    day_idx * 150 + 90,
                                    week_idx * 20 + (month - 1) * 120 + 50,
                                    day_idx * 150 + 160,
                                    week_idx * 20 + (month - 1) * 120 + 70,
                                ),
                                fill=color,
                            )
                            draw.text(
                                (
                                    day_idx * 150 + 100,
                                    week_idx * 20 + (month - 1) * 120 + 50,
                                ),
                                day_str,
                                fill="white",
                                font=font,
                            )
                            draw.text(
                                (
                                    day_idx * 150 + 170,
                                    week_idx * 20 + (month - 1) * 120 + 50,
                                ),
                                label,
                                fill=color,
                                font=font,
                            )

    # Add legend
    draw.text((50, 1520), "Legend:", fill="black", font=font)
    draw.rectangle((50, 1560, 70, 1580), fill="blue")
    draw.text((80, 1560), "Start Date", fill="black", font=font)
    draw.rectangle((250, 1560, 270, 1580), fill="green")
    draw.text((280, 1560), "Refill Date", fill="black", font=font)
    draw.rectangle((450, 1560, 470, 1580), fill="orange")
    draw.text((480, 1560), "Order Date", fill="black", font=font)

    return img


def main():
    print("Medication Refill Calendar Generator")
    print("------------------------------------")

    year = int(input("Enter the year for the calendar: "))
    medications = get_medication_details()
    refill_dates = calculate_refill_dates(medications)

    calendar_img = generate_calendar(year, refill_dates)
    filename = f"medication_refill_calendar_{year}.png"
    calendar_img.save(filename)
    print(f"Medication refill calendar generated: {filename}")
    calendar_img.show()


if __name__ == "__main__":
    main()
