# PyTokenCounter/_utils.py

"""
Utilities for file operations, including reading text files with UTF-8 encoding.
Provides a custom exception for unsupported encodings.

Key Classes
-----------
- ``UnsupportedEncodingError`` : Custom exception for unsupported file encodings.

Key Functions
-------------
- ``ReadTextFile`` : Reads a text file using its detected encoding.
"""


from pathlib import Path

import chardet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


# Custom exception for unsupported file encodings
class UnsupportedEncodingError(Exception):
    """
    Exception raised when a file's encoding is not UTF-8 or ASCII.
    """

    def __init__(
        self,
        encoding: str | None,
        filePath: Path | str,
        message: str = "File encoding is not supported",
    ):
        self.encoding = encoding
        self.filePath = filePath

        # Build a rich formatted error message
        errorText = Text()
        errorText.append(f"{message}", style="bold red")
        errorText.append("\n\n")
        errorText.append("Detected encoding: ", style="green")
        errorText.append(f"{encoding}", style="bold")
        errorText.append("\n")
        # Intentionally do not include file path inside the panel to avoid line wrapping issues

        panel = Panel(
            errorText, title="Encoding Error", title_align="left", border_style="red"
        )

        console = Console(color_system="truecolor", record=True)

        with console.capture() as capture:

            console.print("")  # Add a new line before the panel
            console.print(panel)
            console.print("")

            # Print the file path outside the panel and prevent wrapping so it remains clickable
            pathText = Text()
            pathText.append("File path: ", style="green")
            pathText.append(f"{filePath}", style="bold blue")
            pathText.no_wrap = True
            console.print(pathText)
        captured = capture.get()

        # Store the formatted panel; pass a plain message to the base Exception
        self.message = captured
        super().__init__(message)

        # Flag to ensure the rich panel is output only once
        self._printed = False

    def __str__(self) -> str:
        # Return the rich formatted error message only the first time __str__ is called

        if not self._printed:

            self._printed = True

            return self.message

        return ""


# Set module for correct traceback display
UnsupportedEncodingError.__module__ = "PyTokenCounter"


def ReadTextFile(filePath: Path | str) -> str:
    """
    Reads a text file using its detected encoding.
    """

    if not isinstance(filePath, str) and not isinstance(filePath, Path):

        raise TypeError(
            f'Unexpected type for parameter "filePath". Expected type: str or pathlib.Path. Given type: {type(filePath)}'
        )

    file = Path(filePath).resolve()

    if not file.exists():

        raise FileNotFoundError(f"File not found: {file}")

    fileSize = file.stat().st_size

    if fileSize == 0:

        return ""

    rawBytes = file.read_bytes()
    detection = chardet.detect(rawBytes)
    detectedEncoding = detection.get("encoding")
    confidence = detection.get("confidence", 0)

    encodingsToTry: list[str] = []
    if detectedEncoding:
        encodingsToTry.append(detectedEncoding)

    if confidence < 0.8:
        for fallback in ["windows-1252", "utf-8", "latin-1"]:
            if fallback not in encodingsToTry:
                encodingsToTry.append(fallback)

    for enc in encodingsToTry:
        try:
            text = rawBytes.decode(enc)
            if enc != "utf-8":
                text = text.encode("utf-8").decode("utf-8")
            return text
        except UnicodeDecodeError:
            continue

    raise UnsupportedEncodingError(
        encoding=detectedEncoding,
        filePath=filePath,
        message=f"Failed to decode using encodings: {', '.join(encodingsToTry)}",
    )
