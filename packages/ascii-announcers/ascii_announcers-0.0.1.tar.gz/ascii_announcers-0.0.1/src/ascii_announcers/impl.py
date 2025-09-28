import os

raw = {
"cow":"""
            ^__^
            (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
""",
"tux":"""
        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/
""",
"cat":"""
     |\\_/|
     |o o|__
     --*--__\\
     C_C_(___)
""",
"owl":"""
           ___
          (o o)
         (  V  )
        /--m-m-
""",
"horse":"""

        (\\w/)
        (..  \\
       _/  )  \\______
      (oo /'\\        )`,
       `--' (v  __( / ||
             |||  ||| ||
            //_| //_|    
""",
"dog":"""
^..^      /
/_/\\_____/
   /\\   /\\
  /  \\ /  \\
""",
"elephant":"""
    _    _
   /=\\""/=\\
  (=(0_0 |=)__
   \\_\\ _/_/   )
     /_/   _  /\\
    |/ |\\ || |
""",
"monkey":"""
          __
     w  c(..)o   (
      \\__(-)    __)
          /\\   (
         /(_)___)
         w /|
          | \\
         m  m
"""}

def trim(text):
    min_spaces = min(
        len(line) - len(line.lstrip(" "))
        for line in text.splitlines()
        if line.strip()
    )
    text = os.linesep.join([s[min_spaces:] for s in text.splitlines() if s.strip()])
    return text

announcers = {k: trim(v) for k, v in raw.items()}
