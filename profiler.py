from datetime import datetime

SPACER = "====="
DOUBLE_SPACE = "  "
CLASSES = ["rookie", "amateur", "advanced", "semi-pro", "pro", "super-pro", "clockwork"]


def log(level, msg):
    now = datetime.now().strftime("%H:%M:%S:%f")
    print("[ " + level.upper() + " : " + now + " ] " + msg, end="")


def header(title):
    return SPACER + " " + title + " " + SPACER


def render_menu():
    print("")
    print(header("RVGL Cars Profiler"))
    print("1. csv -> yml")
    print("2. Exit")
    print("")


def render_classes_menu():
    print(header("Car Classes"))
    print("1. Rookie")
    print("2. Amateur")
    print("3. Advanced")
    print("4. Semi-Pro")
    print("5. Pro")
    print("6. Super-Pro")
    print("7. Clockwork")
    print()


def eval_option(number):
    if number == 1:
        profile()
    elif number == 2:
        exit(0)
    else:
        print("Invalid option!")


def profile():
    while True:
        render_classes_menu()
        try:
            clazz = int(input("Option number: "))

            if option < 1 or option > 7:
                continue

            break
        except:
            print("Invalid option!")

    class_name = CLASSES[clazz - 1]
    print("")
    print("Profiling " + class_name + " class (csv -> yml)...")

    with open("csv/" + class_name + ".csv", "r", encoding="utf-8-sig") as data:
        file = open("yml/" + class_name + ".yml", "w")
        file.write(class_name + ":\n")

        for raw_entry in data.readlines()[1:]:
            entry = raw_entry.strip().split(",")

            slug = entry[0].lower().replace(" ", "_")

            line0 = DOUBLE_SPACE + slug + ":\n"
            line1 = DOUBLE_SPACE + DOUBLE_SPACE + "name: " + entry[0] + "\n"
            line2 = DOUBLE_SPACE + DOUBLE_SPACE + "slug: " + slug + "\n"
            line3 = DOUBLE_SPACE + DOUBLE_SPACE + "speed: " + entry[1] + "\n"
            line4 = DOUBLE_SPACE + DOUBLE_SPACE + "acc: " + entry[2] + "\n"
            line5 = DOUBLE_SPACE + DOUBLE_SPACE + "weight: " + entry[3] + "\n"
            line6 = DOUBLE_SPACE + DOUBLE_SPACE + "multiplier: " + entry[4] + "\n"

            file.write(line0)
            log("info", line0)
            file.write(line1)
            log("info", line1)
            file.write(line2)
            log("info", line2)
            file.write(line3)
            log("info", line3)
            file.write(line4)
            log("info", line4)
            file.write(line5)
            log("info", line5)
            file.write(line6)
            log("info", line6)

        log("info", "Done. Closing " + class_name + ".yml...")
        file.close()


while True:
    while True:
        render_menu()

        try:
            option = int(input("Option number: "))
            break
        except:
            print("Invalid option!")

    eval_option(option)
