# MathTrace
Leveraging Neural Controlled Differential Equaution to predict Mathematical Expression Traces in real-time

# Preprocessing
Thanks to <a href="https://github.com/vndee/offline-crohme" target="https://github.com/vndee/offline-crohme">offline-crohme</a> and <a href="https://github.com/harvardnlp/im2markup" target ="https://github.com/harvardnlp/im2markup">im2markup</a>
 for providing some basic tools to extract inkML data into images and tokens.
  
The code for streamlining the process and parsing data is under /preprocessing
The script may require you to have access to code form the repository linked above.

### Extension of files

For convention of this project, we have the following types of files:  .token, .txt, .png (tokenized latex string, latex ground truth, image)
