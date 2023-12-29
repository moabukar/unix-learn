import os

def merge_markdown_files(directory, output_file, line_to_remove):
    """
    Merges all markdown files in a given directory into a single markdown file,
    removing a specific line from each file and adding thematic breaks between files.

    Parameters:
    directory (str): The directory containing markdown files.
    output_file (str): The path of the output merged file.
    line_to_remove (str): The line to be removed from each markdown file.
    """
    # List all markdown files in the directory
    markdown_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    
    # Sort files in alphabetical order (or any other desired order)
    markdown_files.sort()

    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate through each markdown file
        for md_file in markdown_files:
            with open(os.path.join(directory, md_file), 'r') as infile:
                # Read the file content and remove the specified line
                file_content = infile.readlines()
                cleaned_content = [line for line in file_content if line.strip() != line_to_remove]

                # Write the cleaned content to the output file
                outfile.writelines(cleaned_content)
                outfile.write('\n\n---\n\n')  # Add a thematic break for spacing between files

# Example usage
merge_markdown_files('./unix-book/unix-learn/docs/text-manipulation/', 'merged_output.md', "Click the right arrow to view the answers")