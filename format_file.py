import argparse

def main(filename, new_filename=None):

    if new_filename == None:
        new_filename = filename

    with open(filename, "r") as f:
        data = f.read()
    
    #data = data.replace(",{\"number\"", "\n{\"number\"")
    lines = data.split("\n")

    new_lines = []
    template = "{{\"index\": {{\"_index\": \"extract_articles\", \"_id\": \"{}\"}}}}"
    for i in range(len(lines)):
        new_lines.append(template.format(i+1))
        new_lines.append(lines[i])

    new_data = "\n".join(new_lines)        

    with open(new_filename, "w") as f:
        f.write(new_data)

if __name__ == "__main__":
    # execute only if run as a script

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Path to the args json file", type=str)
    parser.add_argument("-n", "--new_filename", help="Path to the args json file", type=str, default=None)
    args = parser.parse_args()

    main(args.filename, args.new_filename)