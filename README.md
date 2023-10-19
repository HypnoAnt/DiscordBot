ReadMe for HypnoAnt's Discord Bot

.env Varibles
- TOKEN : Users Bot token for server
- Mark : Used for Automatic Play of OhhHiMark clip

Pip Packages
- discord
- asyncio
- chess
- os
- cairosvg
- dotenv

Commands (Use prefix .)
- .Hello : "I am the Server Manager"
- .gavgav : Posts gavgav.png (File Not provided in github Repo)
- .join : Plays OhhHiMarkCut.mp3 in users voice channel (File not provided in Github Repo)
- .leave : removes bot from users voice channel
- .chess 
    - move : Provide extra argument to specify piece movement in chess notation and responds with svg of updated board position. If a draw or checkmate has been reached will respond with Draw or Checkmate. Does not affect board if in Checkmate or Draw.
    - reset : resets the board and responds with initial board position


Automatic
- On user MARK joining a voice channel plays OhhHiMarkCut.mp3 in voice channel (File Not Provided in Github Repo)