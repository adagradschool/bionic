# Convert to Bionic

Convert to Bionic is a simple Python script that converts EPUB files to use Bionic Reading, a technique that can improve reading speed and comprehension.

## What is Bionic Reading?

Bionic Reading is a technique developed by German computer scientist and neurobiologist Dr. Thomas Feibel. It involves using a specific pattern of eye movements to improve reading speed and comprehension. Instead of reading word by word from left to right, Bionic Reading involves scanning the text in short, rapid movements called saccades, followed by brief stops called fixations.

To learn more about Bionic Reading, you can check out the following resources:

- [Bionic Reading: How Humans Learn to Read in the Digital Age](https://www.dw.com/en/bionic-reading-how-humans-learn-to-read-in-the-digital-age/a-57481837) - an article from Deutsche Welle
- [Bionic Reading: The Next Revolution in Education?](https://www.youtube.com/watch?v=qMUm3tVyDfM) - a TEDx talk by Dr. Thomas Feibel

## Usage

To use Convert to Bionic, you can run the script from the command line with the following command:

```
python convert.py --book_path <path to book>
```

Replace `<path to book>` with the path to your EPUB file. The converted file will be saved in the same directory with the prefix `converted-` added to the file name.

## Future Tasks

- **Support more formats than EPUB**: We plan to add support for other formats like PDF, HTML, and more.
- **A web app to support upload**: We plan to create a web app that allows users to upload their files and convert them to Bionic Reading.
- **Bug Fixes in parsing DOM trees**: We plan to improve the parsing of DOM trees to fix any issues that may arise during the conversion process.