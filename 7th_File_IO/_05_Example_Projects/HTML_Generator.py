# artistic_log_generator.py

import file_toolkit  # Import the shared toolkit

def generate_html_log(log_file, output_file, title):
    """
    Reads log entries from the log file and writes them into an HTML file
    with a nice lookin' format.
    """
    # Read the log entries as a list of lines
    entries = file_toolkit.read_list(log_file)
    
    # Begin building the HTML content with a doctype, head, and style definitions.
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> 
    """ + title + """
    </title>
    <style>
        body {
            background: linear-gradient(135deg, #2a2a72, #009ffd);
            color: #fff;
            font-family: 'Courier New', Courier, monospace;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }
        h1 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
        }
        .entry {
            border-bottom: 1px solid #fff;
            padding: 10px 0;
            margin-bottom: 10px;
        }
        .timestamp {
            font-weight: bold;
            color: #ffcc00;
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>""" + title + """</h1>
"""
    # Process each log entry
    for entry in entries:
        # Skip empty lines
        if entry.strip() == "":
            continue
        # Attempt to split the entry into a timestamp and the message.
        if entry.startswith('['):
            try:
                timestamp, message = entry.split(']', 1)
                timestamp += ']'  # Add the closing bracket back
            except ValueError:
                timestamp = ""
                message = entry
        else:
            timestamp = ""
            message = entry
        # Add the entry in HTML format
        html_content += f'        <div class="entry"><span class="timestamp">{timestamp}</span>{message.strip()}</div>\n'
    
    # Close the container and HTML tags
    html_content += """    </div>
</body>
</html>"""

    # Write the styled HTML content to the output file
    with open(output_file, "w") as f:
        f.write(html_content)
    
    print(f"Artistic log HTML file has been generated: {output_file}")

def main():
    """
    Main function to prompt the user for the log file and output file names,
    then generate the beautiful HTML log.
    """
    log_file = input("Enter the name of the log file to turn into a clean looking HTML file: ")
    output_file = input("Enter the name for the output HTML file (e.g., log.html): ")
    title = input("Enter the title for the HTML file: ")
    generate_html_log(log_file, output_file, title)

if __name__ == "__main__":
    main()
