# Shivmani_Echo
Installing First, make sure you have all the requirements listed in the “Requirements” section.  The easiest way to install this is using pip install SpeechRecognition.  Otherwise, download the source distribution from PyPI, and extract the archive.  In the folder, run python setup.py install.  Requirements To use all of the functionality of the library, you should have:  Python 2.6, 2.7, or 3.3+ (required) PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone) PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx) Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud) FLAC encoder (required only if the system is not x86-based Windows/Linux/OS X) The following requirements are optional, but can improve or extend functionality in some situations:  On Python 2, and only on Python 2, some functions (like recognizer_instance.recognize_bing) will run slower if you do not have Monotonic for Python 2 installed. If using CMU Sphinx, you may want to install additional language packs to support languages like International French or Mandarin Chinese. The following sections go over the details of each requirement.  Python The first software requirement is Python 2.6, 2.7, or Python 3.3+. This is required to use the library.
