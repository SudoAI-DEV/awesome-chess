# Awesome Chess [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of resources for chess players, coaches, developers and researchers.

[English](README.md) | [简体中文](README.zh-CN.md)

Chess is a two-player strategy board game played on an 8×8 board. This list covers everything around it: where to play and learn, the best books and videos, and the open-source engines, libraries, datasets and research that power modern chess software.

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## Contents

- [Play Online](#play-online)
- [Training](#training)
  - [Tactics](#tactics)
  - [Openings](#openings)
  - [Endgames](#endgames)
  - [Courses and Coaching](#courses-and-coaching)
- [Kids and Beginners](#kids-and-beginners)
- [Books](#books)
  - [Beginner](#beginner)
  - [Intermediate](#intermediate)
  - [Advanced and Classics](#advanced-and-classics)
  - [Free Public-Domain Books](#free-public-domain-books)
- [Videos](#videos)
  - [YouTube Channels](#youtube-channels)
  - [Talks](#talks)
- [Podcasts](#podcasts)
- [Films and Documentaries](#films-and-documentaries)
- [News, Databases and Ratings](#news-databases-and-ratings)
- [Organizations](#organizations)
- [Tournaments and Events](#tournaments-and-events)
- [Communities](#communities)
- [Variants](#variants)
- [Composition and Problems](#composition-and-problems)
- [Correspondence Chess](#correspondence-chess)
- [Accessibility](#accessibility)
- [Chinese-Language Resources](#chinese-language-resources)
- [Tools](#tools)
  - [Analysis and Statistics](#analysis-and-statistics)
  - [Diagrams and Images](#diagrams-and-images)
  - [Clocks](#clocks)
- [Software](#software)
  - [Desktop GUIs](#desktop-guis)
  - [Mobile](#mobile)
  - [Terminal](#terminal)
- [Engines](#engines)
  - [Top Engines](#top-engines)
  - [Neural and Human-Like](#neural-and-human-like)
  - [Variant Engines](#variant-engines)
  - [Classic and Educational](#classic-and-educational)
  - [Commercial](#commercial)
- [Libraries](#libraries)
  - [Python](#python)
  - [JavaScript and TypeScript](#javascript-and-typescript)
  - [Board Components](#board-components)
  - [Rust](#rust)
  - [Go](#go)
  - [JVM](#jvm)
  - [C and C++](#c-and-c)
  - [Other Languages](#other-languages)
- [Engine Development](#engine-development)
  - [Testing](#testing)
  - [Neural Network Training](#neural-network-training)
  - [Tuning and Debugging](#tuning-and-debugging)
  - [Opening Books and PGN](#opening-books-and-pgn)
- [Platforms and Servers](#platforms-and-servers)
- [Bots and APIs](#bots-and-apis)
- [Tablebases](#tablebases)
- [Datasets](#datasets)
- [AI and Research](#ai-and-research)
  - [Papers](#papers)
  - [Projects](#projects)
  - [LLM Benchmarks](#llm-benchmarks)
- [Computer Vision](#computer-vision)
- [Hardware](#hardware)
- [Rating Lists and Competitions](#rating-lists-and-competitions)
- [Formats and Protocols](#formats-and-protocols)
- [Learning Chess Programming](#learning-chess-programming)

## Play Online

*Servers and apps for playing against people.*

- [Lichess](https://lichess.org) - Free, open-source and ad-free server with every time control, variants, studies and analysis.
- [Chess.com](https://www.chess.com) - The largest chess platform, with play, puzzles, lessons, news and live events.
- [World Chess](https://worldchess.com) - FIDE's official online platform, where you can earn FIDE online ratings and titles.
- [Internet Chess Club](https://www.chessclub.com) - One of the oldest commercial chess servers, running since 1995.
- [Free Internet Chess Server](https://www.freechess.org) - Long-running free server (FICS) that works with many classic desktop clients.
- [PlayOK](https://www.playok.com/en/chess/) - Simple browser play with no registration required.
- [Take Take Take](https://taketaketake.com) - App co-founded by Magnus Carlsen for playing, following events and reviewing games.

## Training

*Sites and apps for getting better.*

### Tactics

- [Lichess Puzzles](https://lichess.org/training) - Unlimited free rated puzzles with themes, [Puzzle Storm](https://lichess.org/storm), [Racer](https://lichess.org/racer) and [Streak](https://lichess.org/streak).
- [Chess.com Puzzles](https://www.chess.com/puzzles) - Rated puzzles plus Puzzle Rush and Puzzle Battle.
- [ChessTempo](https://chesstempo.com) - Tactics trainer with spaced repetition, endgame and opening training and a game database.
- [Blitz Tactics](https://blitztactics.com) - Fast pattern-recognition drills against the clock.
- [Listudy](https://listudy.org) - Free spaced-repetition training for openings, tactics and blindfold tactics.
- [Lichess Coordinate Trainer](https://lichess.org/training/coordinate) - Drill board-square recognition.

### Openings

- [Lichess Opening Explorer](https://lichess.org/analysis) - Analysis board with master, Lichess and personal game statistics for any position.
- [Lichess Openings](https://lichess.org/opening) - Free opening encyclopedia with statistics and model games.
- [OpeningTree](https://www.openingtree.com) - Build an opening tree from any Lichess or Chess.com player's games ([source](https://github.com/openingtree/openingtree)).
- [Chessbook](https://www.chessbook.com) - Repertoire builder and trainer focused on the moves you will actually face.
- [Chess Opening Theory](https://en.wikibooks.org/wiki/Chess_Opening_Theory) - Free, community-written opening theory on Wikibooks.
- [ChessGames.com ECO Index](https://www.chessgames.com/chessecohelp.html) - Games organized by ECO opening code.

### Endgames

- [Lichess Practice](https://lichess.org/practice) - Interactive lessons on checkmates, key endgames and more.
- [Chess.com Endgames](https://www.chess.com/endgames) - Endgame theory drills sorted by difficulty.
- [Endgame Trainer](https://endgametrainer.com) - More than 6,000 theoretical endgame exercises.
- [Chess Endgame Training](https://chess-endgame-trainer.web.app) - Free web app for playing out endgames against tablebases and Stockfish.

### Courses and Coaching

- [Chess.com Lessons](https://www.chess.com/lessons) - Structured video lessons from beginner to master.
- [Chessable](https://www.chessable.com) - Interactive courses built on spaced repetition; many courses are paid.
- [ChessMood](https://chessmood.com) - Grandmaster-led video courses and a training community (paid).
- [ChessDojo](https://www.chessdojo.club) - Rating-based training program with a supportive community.
- [Aimchess](https://aimchess.com) - Analyzes your online games and builds personalized training.
- [Noctie](https://noctie.ai) - Human-like AI sparring partner that coaches as you play.
- [DecodeChess](https://decodechess.com) - AI that explains engine moves in plain language.
- [Chess Steps](https://www.chess-steps.com) - The Dutch six-step curriculum used by coaches worldwide.
- [Chess Strategy Online](https://www.chessstrategyonline.com) - Free tutorials on strategy for improving players.

## Kids and Beginners

*Gentle ways to learn the game.*

- [Lichess Learn](https://lichess.org/learn) - Free interactive course on the rules and basic tactics.
- [ChessKid](https://www.chesskid.com) - Safe, moderated site for children with play, lessons and puzzles.
- [ChessWorld](https://www.chessworld.io) - Gamified app for kids (formerly ChessMatec) based on GM Boris Alterman's method.
- [Story Time Chess](https://storytimechess.com) - Story-based board game that teaches chess to children aged three and up.
- [Chessily](https://chessily.com) - Beginner-friendly interactive learning platform.

## Books

*Classic and modern books, grouped by level. Links go to [Open Library](https://openlibrary.org) or free copies.*

### Beginner

- [Bobby Fischer Teaches Chess](https://openlibrary.org/works/OL6572297W) - Bobby Fischer, Stuart Margulies and Don Mosenfelder - programmed-learning primer on checkmating patterns.
- [Logical Chess: Move by Move](https://openlibrary.org/works/OL16043919W) - Irving Chernev - every move of 33 master games explained.
- [Chess Fundamentals](https://www.gutenberg.org/ebooks/33870) - José Raúl Capablanca - timeless 1921 classic, free on Project Gutenberg.
- [1001 Chess Exercises for Beginners](https://openlibrary.org/works/OL28215716W) - Franco Masetti and Roberto Messa - graded tactical exercises.
- [Chess: 5334 Problems, Combinations and Games](https://openlibrary.org/works/OL19641960W) - László Polgár - huge workbook of mates in one, two and three.

### Intermediate

- [The Amateur's Mind](https://openlibrary.org/works/OL1806209W) - Jeremy Silman - common thinking errors of club players.
- [How to Reassess Your Chess](https://openlibrary.org/works/OL1806212W) - Jeremy Silman - evaluating positions through imbalances.
- [Silman's Complete Endgame Course](https://openlibrary.org/works/OL1806211W) - Jeremy Silman - endgames organized by rating level.
- [The Woodpecker Method](https://openlibrary.org/works/OL26456631W) - Axel Smith and Hans Tikkanen - tactics training through repetition.
- [Pawn Structure Chess](https://openlibrary.org/works/OL3297355W) - Andrew Soltis - plans that follow from common pawn structures.
- [Chess Structures: A Grandmaster Guide](https://openlibrary.org/works/OL21568498W) - Mauricio Flores Rios - modern guide to pawn structures.
- [The Art of Attack in Chess](https://openlibrary.org/works/OL4069104W) - Vladimir Vuković - classic on attacking the king.
- [Simple Chess](https://openlibrary.org/works/OL6473115W) - Michael Stean - positional ideas explained clearly.

### Advanced and Classics

- [My System](https://openlibrary.org/works/OL4918564W) - Aron Nimzowitsch - foundational 1925 treatise on positional play.
- [Think Like a Grandmaster](https://openlibrary.org/works/OL7983003W) - Alexander Kotov - the classic on calculation and the tree of variations.
- [Zurich International Chess Tournament 1953](https://openlibrary.org/works/OL27997817W) - David Bronstein - legendary tournament book.
- [My 60 Memorable Games](https://openlibrary.org/works/OL2714658W) - Bobby Fischer - annotated games by the 11th world champion.
- [Dvoretsky's Endgame Manual](https://openlibrary.org/works/OL265702W) - Mark Dvoretsky - the reference work on endgame theory.
- [Fundamental Chess Endings](https://openlibrary.org/works/OL16972394W) - Karsten Müller and Frank Lamprecht - comprehensive endgame encyclopedia.
- [Endgame Strategy](https://openlibrary.org/works/OL9047079W) - Mikhail Shereshevsky - strategic principles of the endgame.
- [Garry Kasparov on My Great Predecessors](https://openlibrary.org/works/OL3006223W) - Garry Kasparov - multi-volume history of the world champions.
- [Grandmaster Preparation: Calculation](https://openlibrary.org/works/OL21179548W) - Jacob Aagaard - demanding calculation training.
- [Game Changer](https://openlibrary.org/works/OL21643546W) - Matthew Sadler and Natasha Regan - AlphaZero's style and what humans can learn from it.

### Free Public-Domain Books

- [Project Gutenberg Chess Shelf](https://www.gutenberg.org/ebooks/subject/1677) - All public-domain chess books on Project Gutenberg.
- [Chess Strategy](https://www.gutenberg.org/ebooks/5614) - Edward Lasker - classic introduction to strategy.
- [Chess and Checkers: The Way to Mastership](https://www.gutenberg.org/ebooks/4913) - Edward Lasker - practical guide for improving players.
- [The Blue Book of Chess](https://www.gutenberg.org/ebooks/16377) - Howard Staunton - 19th-century manual of the game.
- [The Exploits and Triumphs in Europe of Paul Morphy](https://www.gutenberg.org/ebooks/34180) - Frederick Milnes Edge - contemporary account of Morphy's European tour.
- [Chess Generalship](https://www.gutenberg.org/ebooks/55278) - Franklin K. Young - military-inspired theory of chess.

## Videos

*Channels and talks worth watching.*

### YouTube Channels

- [GothamChess](https://www.youtube.com/@GothamChess) - IM Levy Rozman's lessons, recaps and entertainment.
- [agadmator's Chess Channel](https://www.youtube.com/@agadmator) - Analysis of classic and modern games.
- [GMHikaru](https://www.youtube.com/@GMHikaru) - Hikaru Nakamura's streams and recaps.
- [Daniel Naroditsky](https://www.youtube.com/@DanielNaroditskyGM) - Instructive speedrun series and lectures by the late GM Daniel Naroditsky (1995-2025).
- [Eric Rosen](https://www.youtube.com/@eric-rosen) - IM Eric Rosen's instructive and fun games.
- [Chess Vibes](https://www.youtube.com/@ChessVibesOfficial) - Clear, concept-driven lessons by GM Nelson Lopez.
- [Hanging Pawns](https://www.youtube.com/@HangingPawns) - In-depth opening explainers.
- [John Bartholomew](https://www.youtube.com/@JohnBartholomewChess) - The long-running instructional series Climbing the Rating Ladder.
- [Saint Louis Chess Club](https://www.youtube.com/@STLChessClub) - Lectures and elite event broadcasts.
- [ChessNetwork](https://www.youtube.com/@ChessNetwork) - Classic instructive commentary.
- [ChessBase India](https://www.youtube.com/@ChessBaseIndia) - Large Indian chess media channel with event coverage.
- [Anna Cramling](https://www.youtube.com/@AnnaCramling) - Entertaining games and vlogs.
- [FIDE](https://www.youtube.com/@FIDE_chess) - Official broadcasts of FIDE events.

### Talks

- [Understanding Chess Mastery](https://www.youtube.com/watch?v=fPopQaY7Og4) - Jennifer Shahade at TEDxBaltimore.
- [How Chess Can Revolutionize Learning](https://www.youtube.com/watch?v=A3yDvM8aplY) - Cody Pomeranz at TEDxYale.
- [Working Backward to Solve Problems](https://www.youtube.com/watch?v=v34NqCbAA1c) - Maurice Ashley on problem-solving lessons from chess.
- [Don't Fear Intelligent Machines. Work with Them](https://www.ted.com/talks/garry_kasparov_don_t_fear_intelligent_machines_work_with_them) - Garry Kasparov on Deep Blue and human-machine collaboration.

## Podcasts

*Chess to listen to.*

- [Perpetual Chess Podcast](https://www.perpetualchesspod.com) - Weekly interviews with top players, coaches and authors.
- [C-Squared Podcast](https://c2pod.com) - Weekly discussion of the chess world with GMs Fabiano Caruana and Cristian Chirila.
- [The Chess Pit](https://www.chesspitpod.com) - Light-hearted weekly UK podcast about chess and chess culture.

## Films and Documentaries

*Movies and series about chess and its players.*

- [The Queen's Gambit](https://en.wikipedia.org/wiki/The_Queen%27s_Gambit_(miniseries)) - Netflix miniseries (2020) about a fictional prodigy, Beth Harmon.
- [Searching for Bobby Fischer](https://en.wikipedia.org/wiki/Searching_for_Bobby_Fischer) - Film (1993) based on the childhood of Josh Waitzkin.
- [Pawn Sacrifice](https://en.wikipedia.org/wiki/Pawn_Sacrifice) - Film (2014) about the 1972 Fischer-Spassky match.
- [Queen of Katwe](https://en.wikipedia.org/wiki/Queen_of_Katwe) - Film (2016) about Ugandan player Phiona Mutesi.
- [Magnus](https://en.wikipedia.org/wiki/Magnus_(2016_film)) - Documentary (2016) on Magnus Carlsen's rise to world champion.
- [Bobby Fischer Against the World](https://en.wikipedia.org/wiki/Bobby_Fischer_Against_the_World) - HBO documentary (2011) on Bobby Fischer.
- [Game Over: Kasparov and the Machine](https://en.wikipedia.org/wiki/Game_Over:_Kasparov_and_the_Machine) - Documentary (2003) on Kasparov versus Deep Blue.
- [Closing Gambit](https://vimeo.com/ondemand/closinggambit) - Documentary (2018) on the 1978 Korchnoi-Karpov world championship match.
- [Brooklyn Castle](https://en.wikipedia.org/wiki/Brooklyn_Castle) - Documentary (2012) about an inner-city school chess team.
- [The Dark Horse](https://en.wikipedia.org/wiki/The_Dark_Horse_(2014_film)) - Film (2014) about New Zealand chess coach Genesis Potini.
- [The Luzhin Defence](https://en.wikipedia.org/wiki/The_Luzhin_Defence) - Film (2000) adapted from Vladimir Nabokov's novel.

## News, Databases and Ratings

*Follow the chess world and look up games and players.*

- [Lichess Broadcasts](https://lichess.org/broadcast) - Free live relays of major events with engine analysis.
- [Chess.com Events](https://www.chess.com/events) - Live coverage and event hubs (successor to chess24 and ChessBomb).
- [ChessBase News](https://en.chessbase.com) - Long-running chess news and analysis.
- [The Week in Chess](https://theweekinchess.com) - Weekly news and free PGN downloads, published since 1994.
- [ChessGames.com](https://www.chessgames.com) - Huge annotated game database with an active community.
- [365Chess](https://www.365chess.com) - Game database with players, tournaments and an opening explorer.
- [Chessdom](https://www.chessdom.com) - Chess news and live games.
- [New in Chess](https://www.newinchess.com/magazine) - Premier chess magazine written with top grandmasters.
- [FIDE Ratings](https://ratings.fide.com) - Official FIDE rating lists and player profiles.
- [2700chess](https://www.2700chess.com) - Live ratings of the world's top players.
- [Chess-Results](https://chess-results.com) - Pairings and results for thousands of over-the-board tournaments.

## Organizations

*Governing bodies and federations.*

- [FIDE](https://www.fide.com) - International Chess Federation, the world governing body; see also the [FIDE Handbook](https://handbook.fide.com) for the Laws of Chess.
- [Chinese Chess Association](https://cca.mindsports.org.cn) - China's national chess federation (中国国际象棋协会).
- [US Chess](https://new.uschess.org) - National federation of the United States.
- [English Chess Federation](https://www.englishchess.org.uk) - National federation of England.
- [Chess Federation of Canada](https://www.chess.ca) - National federation of Canada.
- [European Chess Union](https://www.europechess.org) - Continental governing body for Europe.
- [Saint Louis Chess Club](https://www.saintlouischessclub.org) - Leading US club and host of the Sinquefield Cup and US Championships.

## Tournaments and Events

*Major recurring competitions.*

- [FIDE World Championship](https://worldchampionship.fide.com) - Official site of the World Chess Championship match.
- [Candidates Tournament](https://en.wikipedia.org/wiki/Candidates_Tournament) - Eight-player event that decides the world championship challenger.
- [Chess Olympiad](https://en.wikipedia.org/wiki/Chess_Olympiad) - Biennial team championship between national teams.
- [Norway Chess](https://norwaychess.no) - Elite annual super-tournament in Stavanger.
- [Tata Steel Chess](https://tatasteelchess.com/en) - The "Wimbledon of chess", held every January in Wijk aan Zee.
- [Grand Chess Tour](https://grandchesstour.org) - Elite circuit that includes the Sinquefield Cup.
- [Freestyle Chess](https://www.freestyle-chess.com) - Elite Chess960 events co-founded by Magnus Carlsen.
- [Esports World Cup Chess](https://www.esportsworldcup.com/en/competitions/chess) - Online chess event of the Esports World Cup.

## Communities

*Places to talk chess.*

- [r/chess](https://www.reddit.com/r/chess/) - The largest chess subreddit.
- [r/chessbeginners](https://www.reddit.com/r/chessbeginners/) - Friendly place for beginner questions.
- [Lichess Forum](https://lichess.org/forum) - Discussion forum, plus [teams](https://lichess.org/team) for clubs.
- [Chess.com Forums](https://www.chess.com/forum) - Large general-purpose chess forum.
- [Chess Stack Exchange](https://chess.stackexchange.com) - Question-and-answer site for rules, history and strategy.
- [Lichess Discord](https://discord.gg/lichess) - Official Lichess Discord server.

## Variants

*Beyond standard chess.*

- [Lichess Variants](https://lichess.org/variant) - Chess960, Crazyhouse, Atomic, Antichess, King of the Hill, Three-check, Horde and Racing Kings.
- [PyChess](https://www.pychess.org) - Free server for dozens of variants, including Xiangqi, Shogi, Makruk and Janggi.
- [Chess.com Variants](https://www.chess.com/variants) - Variants including 4-player chess and Bughouse.
- [The Chess Variant Pages](https://www.chessvariants.com) - Encyclopedic catalog of fairy chess variants.
- [Chess960](https://en.wikipedia.org/wiki/Chess960) - Fischer Random: randomized back-rank starting positions.

## Composition and Problems

*The art of chess composition.*

- [YACPDB](https://www.yacpdb.org) - Yet Another Chess Problem Database, a large open problem collection.
- [Meson](http://www.bstephen.me.uk/meson/) - Database of about 150,000 chess problems.
- [World Federation for Chess Composition](https://www.wfcc.ch) - Governing body for composition and solving championships.
- [The Problemist](https://www.theproblemist.org) - British Chess Problem Society and its magazine.

## Correspondence Chess

*Slow chess, one move at a time.*

- [ICCF](https://www.iccf.com) - International Correspondence Chess Federation.
- [SchemingMind](https://www.schemingmind.com) - Correspondence chess club and server with variants.
- [Chess.com Daily](https://www.chess.com/play/online/daily) - Turn-based games with days per move.

## Accessibility

*Chess for blind and visually impaired players.*

- [Lichess Blind Mode](https://lichess.org/page/blind-mode-guide) - Guide to Lichess's screen reader support.
- [IBCA](https://ibca-info.org) - International Braille Chess Association.

## Chinese-Language Resources

*Resources in Chinese.*

- [国象联盟](https://www.chessease.net) - Major Chinese chess platform with play, tactics, a game database and events.
- [弈战](https://www.ixiaqi.com) - Online grading exams and competitions for chess, Go and Xiangqi.
- [国象充电站](https://www.hellochess.cn) - Chinese chess learning site with articles and book recommendations.
- [国家体育总局棋牌运动管理中心](https://www.sport.gov.cn/qpzx/) - Government body overseeing chess, Go and Xiangqi in China.
- [国际象棋 - 维基百科](https://zh.wikipedia.org/wiki/%E5%9B%BD%E9%99%85%E8%B1%A1%E6%A3%8B) - Chinese Wikipedia article on chess.
- [Chess in China](https://en.wikipedia.org/wiki/Chess_in_China) - History of chess in China, including the [China Chess League](https://en.wikipedia.org/wiki/China_Chess_League).

## Tools

*Handy utilities for players.*

### Analysis and Statistics

- [Lichess Board Editor](https://lichess.org/editor) - Set up any position, then analyze it or [import PGN](https://lichess.org/paste).
- [Chess.com Analysis](https://www.chess.com/analysis) - Analysis board, game review and PGN editor.
- [Chesskit](https://chesskit.org) - Free open-source game review with Stockfish ([source](https://github.com/GuillaumeSD/Chesskit)).
- [WintrChess](https://wintrchess.com) - Free open-source game review with move classifications ([source](https://github.com/WintrCat/wintrchess)).
- [ChessMonitor](https://www.chessmonitor.com) - Analytics dashboard for your Lichess and Chess.com games.
- [Lumichess](https://lumichess.com) - Free game review and statistics for Chess.com and Lichess.

### Diagrams and Images

- [Apronus Diagram Editor](https://www.apronus.com/chess/diagram/editor/) - Create board diagrams and animated GIFs.
- [Jin Chess Diagram Composer](https://www.jinchess.com/chessboard/composer/) - Classic diagram image generator.
- [ChessboardImage](https://chessboardimage.com) - Generate chessboard images from FEN.
- [Chessvision.ai](https://chessvision.ai) - Recognize positions from screenshots, books and videos.
- [Chess Symbols in Unicode](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) - Unicode code points for chess pieces.
- [Wikimedia Commons Chess Pieces](https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent) - Freely licensed piece images.
- [Lichess Piece Sets](https://github.com/lichess-org/lila/tree/master/public/piece) - Dozens of SVG piece sets under open licenses.
- [Spiral Chess Set](https://www.thingiverse.com/thing:470700) - 3D-printable chess pieces.

### Clocks

- [ChessClock.org](https://chessclock.org) - Free online chess clock.

## Software

*Programs for playing, analyzing and managing games.*

### Desktop GUIs

- [En Croissant](https://github.com/franciscoBSalgueiro/en-croissant) - Modern cross-platform analysis and database toolkit ([website](https://encroissant.org)).
- [Nibbler](https://github.com/rooklift/nibbler) - Analysis GUI for UCI engines with Leela-specific features.
- [Cute Chess](https://github.com/cutechess/cutechess) - GUI, command-line tool and library for engine matches.
- [BanksiaGUI](https://www.banksiagui.com) - Free GUI for engine tournaments and analysis.
- [Arena](http://www.playwitharena.de) - Long-standing free GUI for UCI and WinBoard engines.
- [Scid vs. PC](https://scidvspc.sourceforge.net) - Database and analysis toolkit.
- [ChessX](https://github.com/Isarhamster/chessx) - Cross-platform database and PGN tool.
- [Lucas Chess](https://github.com/lukasmonk/lucaschessR6) - Training-focused GUI with dozens of exercises and engines.
- [PyChess](https://github.com/pychess/pychess) - GTK desktop client with FICS and Lichess support.
- [XBoard](https://www.gnu.org/software/xboard/) - Classic GNU GUI and reference implementation of CECP.
- [Stockfish for Mac](https://github.com/daylen/stockfish-mac) - Native macOS app for analysis with Stockfish.
- [ChessBase](https://www.chessbase.com) - Industry-standard commercial database software.

### Mobile

- [Lichess Mobile](https://github.com/lichess-org/mobile) - Official open-source Lichess app built with Flutter.
- [DroidFish](https://github.com/peterosterlund2/droidfish) - Android app with engine analysis.

### Terminal

- [chess-tui](https://github.com/thomas-mauran/chess-tui) - Terminal chess in Rust with Stockfish and Lichess support.
- [cli-chess](https://github.com/trevorbayless/cli-chess) - Terminal client for Lichess and offline play.
- [Gambit](https://github.com/maaslalani/gambit) - Play chess in your terminal.

## Engines

*Programs that play chess.*

### Top Engines

- [Stockfish](https://github.com/official-stockfish/Stockfish) - The strongest open-source engine, with NNUE evaluation ([website](https://stockfishchess.org)).
- [Leela Chess Zero](https://github.com/LeelaChessZero/lc0) - Neural-network engine in the style of AlphaZero ([website](https://lczero.org)).
- [Reckless](https://github.com/codedeliveryservice/Reckless) - Top NNUE engine written in Rust.
- [PlentyChess](https://github.com/Yoshie2000/PlentyChess) - Top engine with neural-network evaluation.
- [Viridithas](https://github.com/cosmobobak/viridithas) - Superhuman NNUE engine written in Rust.
- [Obsidian](https://github.com/gab8192/Obsidian) - Strong NNUE engine written in C++.
- [Stormphrax](https://github.com/Ciekce/Stormphrax) - Engine whose network is trained from zero knowledge.
- [Integral](https://github.com/aronpetko/integral) - Strong neural-network engine written in C++.
- [Alexandria](https://github.com/PGG106/Alexandria) - Strong NNUE bitboard engine.
- [Berserk](https://github.com/jhonnold/berserk) - Top-tier engine written in C.
- [Ethereal](https://github.com/AndyGrant/Ethereal) - Well-documented engine by the author of OpenBench.
- [Koivisto](https://github.com/Luecx/Koivisto) - Strong NNUE engine.
- [Caissa](https://github.com/Witek902/Caissa) - Strong NNUE engine written in C++.
- [Arasan](https://github.com/jdart1/arasan-chess) - Veteran engine in active development since the 1990s.

### Neural and Human-Like

- [Maia Chess](https://github.com/CSSLab/maia-chess) - Human-like neural networks trained on Lichess games ([website](https://www.maiachess.com)).
- [Maia-2](https://github.com/CSSLab/maia2) - Unified human-like model across skill levels.
- [Patricia](https://github.com/Adam-Kulju/Patricia) - Deliberately aggressive engine that loves sacrifices.
- [ChessCoach](https://github.com/chrisbutner/ChessCoach) - Neural-network engine that also produces natural-language commentary.

### Variant Engines

- [Fairy-Stockfish](https://github.com/fairy-stockfish/Fairy-Stockfish) - Stockfish derivative for Xiangqi, Shogi, Crazyhouse and many other variants.
- [CrazyAra](https://github.com/QueensGambit/CrazyAra) - Deep-learning MCTS engine for Crazyhouse and other variants.

### Classic and Educational

- [Sunfish](https://github.com/thomasahle/sunfish) - Minimal engine in about 111 lines of Python.
- [GNU Chess](https://www.gnu.org/software/chess/) - The Free Software Foundation's chess engine.
- [Crafty](https://github.com/MichaelB7/Crafty) - Robert Hyatt's classic bitboard engine (mirror).
- [Fruit](https://github.com/Warpten/Fruit-2.1) - Hugely influential open-source engine by Fabien Letouzey (mirror).
- [Weiss](https://github.com/TerjeKir/weiss) - Clean, readable engine written in C.
- [Andoma](https://github.com/healeycodes/andoma) - Small, readable Python engine for learning alpha-beta search.
- [latrunculorum](https://github.com/benwr/latrunculorum) - Simple chess bot in Python.

### Commercial

- [Komodo Dragon](https://www.chessprogramming.org/Komodo) - Multiple TCEC champion; sales ended in 2026.
- [HIARCS](https://www.hiarcs.com) - Commercial engine and HIARCS Chess Explorer GUI.
- [Shredder](https://www.shredderchess.com) - Commercial engine and GUI by Stefan Meyer-Kahlen.
- [Fritz](https://shop.chessbase.com/en/categories/fritz) - ChessBase's playing and analysis program.

## Libraries

*Move generation, parsing and board rendering.*

### Python

- [python-chess](https://github.com/niklasf/python-chess) - The standard library for move generation, PGN, Polyglot, tablebases and UCI/XBoard engines.
- [stockfish](https://github.com/zhelyabuzhsky/stockfish) - Simple wrapper for driving Stockfish.
- [Chessnut](https://github.com/cgearhart/Chessnut) - Simple board model with FEN parsing and legal move generation.
- [fenparser](https://github.com/tlehman/fenparser) - Small parser for Forsyth-Edwards Notation.

### JavaScript and TypeScript

- [chess.js](https://github.com/jhlywa/chess.js) - Move generation and validation, FEN/PGN and game-end detection.
- [chessops](https://github.com/niklasf/chessops) - Chess and variant rules in TypeScript, used by Lichess.
- [kokopu](https://github.com/yo35/kokopu) - Chess rules plus FEN and PGN reading and writing.
- [pgn-parser](https://github.com/mliebelt/pgn-parser) - Parses PGN into JSON.
- [stockfish.js](https://github.com/nmrugg/stockfish.js) - Stockfish compiled to WebAssembly for browsers and Node.js.
- [chess](https://www.npmjs.com/package/chess) - Algebraic-notation-driven engine that validates positions and lists legal moves.

### Board Components

- [chessground](https://github.com/lichess-org/chessground) - Lichess's board UI for web and mobile.
- [cm-chessboard](https://github.com/shaack/cm-chessboard) - Dependency-free ES6 SVG chessboard.
- [react-chessboard](https://github.com/Clariity/react-chessboard) - Responsive chessboard component for React.
- [vue3-chessboard](https://github.com/qwerty084/vue3-chessboard) - Vue 3 chessboard built on chessground and chess.js.
- [chessboard.js](https://github.com/oakmac/chessboardjs) - Classic standalone JavaScript chessboard.
- [Lichess PGN Viewer](https://github.com/lichess-org/pgn-viewer) - Embeddable PGN viewer from Lichess.
- [chess-board](https://github.com/laat/chess-board) - Web component that renders a position from FEN.
- [flutter-chessground](https://github.com/lichess-org/flutter-chessground) - Chessboard widget for Flutter from Lichess.

### Rust

- [shakmaty](https://github.com/niklasf/shakmaty) - Chess and variant rules library powering Lichess's Rust services.
- [cozy-chess](https://github.com/analog-hors/cozy-chess) - Fast chess and Chess960 move generation.
- [chess](https://github.com/jordanbray/chess) - Fast move generation crate.
- [Pleco](https://github.com/pleco-rs/Pleco) - Rust rewrite of Stockfish usable as a library and an engine.
- [fen](https://github.com/ucarion/fen) - Parser for FEN with proper error handling.

### Go

- [CorentinGS/chess](https://github.com/CorentinGS/chess) - Maintained fork of notnil/chess with bitboards, PGN/FEN, UCI and opening books.

### JVM

- [chesslib](https://github.com/bhlangonijr/chesslib) - Java library for legal move generation and FEN/PGN parsing.
- [scalachess](https://github.com/lichess-org/scalachess) - Lichess's immutable chess model in Scala.

### C and C++

- [chess-library](https://github.com/Disservin/chess-library) - Fast single-header C++ chess library.
- [Fathom](https://github.com/jdart1/Fathom) - Standalone library for probing Syzygy tablebases.
- [Gaviota Tablebases](https://github.com/michiguel/Gaviota-Tablebases) - Probing code for Gaviota endgame tablebases.

### Other Languages

- [Rudzoft ChessLib](https://github.com/rudzen/ChessLib) - C# data structures and move generation.
- [dartchess](https://github.com/lichess-org/dartchess) - Dart chess library from Lichess.
- [chesskit-swift](https://github.com/chesskit-app/chesskit-swift) - Swift package for chess logic.
- [Chess.jl](https://github.com/romstad/Chess.jl) - Julia library by Stockfish co-author Tord Romstad.
- [chessIO](https://github.com/mlang/chessIO) - Fast Haskell move generator with a UCI frontend.
- [chess](https://github.com/pioz/chess) - Fast bitboard chess library for Ruby.

## Engine Development

*Tools for building, testing and tuning engines.*

### Testing

- [OpenBench](https://github.com/AndyGrant/OpenBench) - Distributed SPRT testing framework used by many top engines.
- [Fishtest](https://github.com/official-stockfish/fishtest) - Stockfish's distributed testing framework ([live instance](https://tests.stockfishchess.org)).
- [fastchess](https://github.com/Disservin/fastchess) - Fast command-line tool for engine matches and SPRT.
- [c-chess-cli](https://github.com/lucasart/c-chess-cli) - Lightweight command-line match runner written in C.
- [Stockfish Books](https://github.com/official-stockfish/books) - Opening books used for engine testing.

### Neural Network Training

- [bullet](https://github.com/jw1912/bullet) - Rust ML library that trains the NNUE networks of many modern engines.
- [nnue-pytorch](https://github.com/official-stockfish/nnue-pytorch) - Stockfish's NNUE trainer in PyTorch.
- [Grapheus](https://github.com/Luecx/Grapheus) - GPU framework for training NNUE networks.
- [lczero-training](https://github.com/LeelaChessZero/lczero-training) - Leela Chess Zero's network training code.

### Tuning and Debugging

- [texel-tuner](https://github.com/GediminasMasaitis/texel-tuner) - Generic Texel tuner for evaluation parameters.
- [chess-tuning-tools](https://github.com/kiudee/chess-tuning-tools) - Bayesian optimization of engine parameters.
- [perftree](https://github.com/agausmann/perftree) - Perft debugger that compares your move generator with Stockfish.
- [Stockfish WDL Model](https://github.com/official-stockfish/WDL_model) - Fits win/draw/loss models to normalize evaluations.

### Opening Books and PGN

- [PolyGlot](https://github.com/ddugovic/polyglot) - Opening book tool and UCI-to-XBoard adapter.
- [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) - Command-line tool for searching, filtering and converting PGN.

## Platforms and Servers

*Open-source infrastructure behind online chess.*

- [lila](https://github.com/lichess-org/lila) - The Lichess server, written in Scala.
- [lila-ws](https://github.com/lichess-org/lila-ws) - Lichess's WebSocket server.
- [fishnet](https://github.com/lichess-org/fishnet) - Distributed volunteer Stockfish analysis for Lichess.
- [lila-openingexplorer](https://github.com/lichess-org/lila-openingexplorer) - Lichess's opening explorer backend.
- [lila-tablebase](https://github.com/lichess-org/lila-tablebase) - Lichess's tablebase server.
- [lila-gif](https://github.com/lichess-org/lila-gif) - Renders positions and games as images and GIFs.
- [irwin](https://github.com/clarkerubber/irwin) - Machine-learning cheat detection for Lichess.
- [pychess-variants](https://github.com/gbtami/pychess-variants) - Server behind the PyChess variants site.
- [Listudy](https://github.com/ArneVogel/listudy) - Spaced-repetition training server in Elixir.
- [Infinite Chess](https://github.com/Infinite-Chess/infinitechess.org) - Server for chess on an infinite board.

## Bots and APIs

*Connect programs to online chess.*

- [Lichess API](https://lichess.org/api) - Official REST and streaming API with Bot, Board, Tablebase and Explorer endpoints.
- [lichess-bot](https://github.com/lichess-bot-devs/lichess-bot) - Official bridge between Lichess bot accounts and UCI/XBoard engines.
- [BotLi](https://github.com/Torom/BotLi) - Configurable alternative bridge between the Lichess bot API and UCI engines.
- [berserk](https://github.com/lichess-org/berserk) - Official Python client for the Lichess API.
- [chariot](https://github.com/tors42/chariot) - Java client for the Lichess API.
- [Chess.com Published-Data API](https://www.chess.com/news/view/published-data-api) - Read-only public API for player, game and club data.
- [chess.com](https://github.com/sarartur/chess.com) - Python client for the Chess.com Published-Data API.
- [chess-web-api](https://github.com/andyruwruw/chess-web-api) - JavaScript wrapper for the Chess.com public API.
- [Chess Challenge](https://github.com/SebLague/Chess-Challenge) - Sebastian Lague's C# framework for writing a tiny chess bot.

## Tablebases

*Perfect play for positions with few pieces.*

- [Syzygy Tables](https://syzygy-tables.info) - Web interface and API for probing 7-piece Syzygy tablebases.
- [Lichess Tablebase](https://tablebase.lichess.ovh) - Public tablebase server and download mirror.
- [Syzygy Generator](https://github.com/syzygy1/tb) - Ronald de Man's generator for Syzygy tablebases.
- [Syzygy Bases](https://www.chessprogramming.org/Syzygy_Bases) - Overview of the standard WDL/DTZ tablebases.
- [Gaviota Tablebases Overview](https://www.chessprogramming.org/Gaviota_Tablebases) - Compressed DTM tablebases for up to five pieces.
- [Lomonosov Tablebases](https://www.chessprogramming.org/Lomonosov_Tablebases) - The first complete 7-piece DTM tablebases.

## Datasets

*Games, puzzles and evaluations for analysis and machine learning.*

- [Lichess Open Database](https://database.lichess.org) - Every rated Lichess game as monthly PGN dumps, plus puzzles and evaluations.
- [Lichess on Hugging Face](https://huggingface.co/Lichess) - Lichess games, puzzles and position evaluations in Parquet.
- [lichess-org/chess-openings](https://github.com/lichess-org/chess-openings) - Opening names, ECO codes and moves as TSV.
- [Lichess Elite Database](https://database.nikonoel.fr) - Lichess games filtered to highly rated players.
- [Lumbra's GigaBase](https://lumbrasgigabase.com) - Very large free database of over-the-board and online games.
- [FICS Games Database](https://www.ficsgames.org) - Downloadable archive of FICS games.
- [TCEC Games](https://github.com/TCEC-Chess/tcecgames) - Games from every TCEC season.
- [Leela Training Data](https://storage.lczero.org/files/training_data/) - Public self-play training data from Leela Chess Zero.
- [Chess Game Dataset](https://www.kaggle.com/datasets/datasnaek/chess) - Popular Kaggle dataset of about 20,000 Lichess games.

## AI and Research

*Papers and projects at the intersection of chess and machine learning.*

### Papers

- [AlphaZero](https://arxiv.org/abs/1712.01815) - Mastering chess and shogi by self-play with a general reinforcement learning algorithm.
- [MuZero](https://arxiv.org/abs/1911.08265) - Planning with a learned model across Atari, Go, chess and shogi.
- [Acquisition of Chess Knowledge in AlphaZero](https://arxiv.org/abs/2111.09259) - Interpretability study of the concepts AlphaZero learns.
- [Aligning Superhuman AI with Human Behavior](https://arxiv.org/abs/2006.01855) - The Maia paper on predicting human moves.
- [Grandmaster-Level Chess Without Search](https://arxiv.org/abs/2402.04494) - Transformer reaching grandmaster strength without explicit search.
- [Evidence of Learned Look-Ahead in a Chess-Playing Neural Network](https://arxiv.org/abs/2406.00877) - Interpretability study of Leela's policy network.
- [ChessGPT](https://arxiv.org/abs/2306.09200) - Bridging policy learning and language modeling.

### Projects

- [searchless_chess](https://github.com/google-deepmind/searchless_chess) - DeepMind's code and ChessBench dataset for searchless chess.
- [Allie](https://github.com/ippolito-cmu/allie) - Human-aligned chess transformer with adaptive search.
- [chess-transformers](https://github.com/sgrvinod/chess-transformers) - Training transformers to play chess.
- [chess_llm_interpretability](https://github.com/adamkarvonen/chess_llm_interpretability) - Probing the world model inside chess-playing GPTs.
- [Neural Networks for Chess](https://github.com/asdfjkl/neural_network_chess) - Free book covering AlphaZero, Leela and NNUE.
- [pgx](https://github.com/sotetsuk/pgx) - Vectorized JAX game environments, including chess, for reinforcement learning.

### LLM Benchmarks

- [Kaggle Game Arena](https://www.kaggle.com/game-arena) - Benchmark that pits large language models against each other in games, including chess.
- [llm_chess](https://github.com/maxim-saplin/llm_chess) - Benchmark of LLMs playing chess against a random player and each other.
- [llm-chess-puzzles](https://github.com/kagisearch/llm-chess-puzzles) - Benchmark testing LLMs on Lichess puzzles.
- [chess_gpt_eval](https://github.com/adamkarvonen/chess_gpt_eval) - Evaluates GPT-style models against Stockfish.

## Computer Vision

*Recognize boards and positions from images and video.*

- [tensorflow_chessbot](https://github.com/Elucidation/tensorflow_chessbot) - Predicts FEN from chessboard screenshots.
- [chesscog](https://github.com/georg-wolflein/chesscog) - Recognizes positions from photos of physical boards.
- [LiveChess2FEN](https://github.com/davidmallasen/LiveChess2FEN) - Converts live photos of physical boards into FEN.
- [fenify-3D](https://github.com/notnil/fenify-3D) - FEN from real-world photos of chessboards.
- [CameraChessWeb](https://github.com/Pbatch/CameraChessWeb) - Records over-the-board games with a camera and uploads the PGN to Lichess.

## Hardware

*Electronic boards, robots and DIY projects.*

- [DGT](https://www.dgtprojects.com) - Maker of the standard tournament e-boards and clocks.
- [Chessnut](https://www.chessnutech.com) - Maker of the Air and Evo electronic boards.
- [Certabo](https://www.certabo.com) - RFID electronic chessboards.
- [Square Off](https://squareoffnow.com) - Self-moving robotic chessboards.
- [PicoChess](https://github.com/jromang/picochess) - Turns a Raspberry Pi and a DGT board into a standalone chess computer.
- [DGTCentaurMods](https://github.com/DGTCentaurMods/DGTCentaurMods) - Custom firmware and protocols for the DGT Centaur.
- [Play Online Chess with a Real Chess Board](https://github.com/karayaman/Play-online-chess-with-real-chess-board) - Uses a webcam to play online games on a physical board.
- [Chess-Robot](https://github.com/EDGE-tronics/Chess-Robot) - Chess robot built with a robotic arm, a Raspberry Pi and OpenCV.

## Rating Lists and Competitions

*How engines compare.*

- [CCRL](https://computerchess.org.uk/ccrl/4040/) - Computer Chess Rating Lists for many time controls.
- [CEGT](http://www.cegt.net) - Chess Engines Grand Tournament rating lists.
- [TCEC](https://tcec-chess.com) - Top Chess Engine Championship, the most prestigious engine competition.
- [Computer Chess Championship](https://www.chess.com/computer-chess-championship) - Continuous engine tournaments run by Chess.com.
- [SPCC](https://www.sp-cc.de) - Stefan Pohl's rating lists and UHO opening books.

## Formats and Protocols

*Standards for describing games and talking to engines.*

- [UCI](https://backscattering.de/chess/uci/) - Universal Chess Interface, the standard engine protocol.
- [CECP](https://www.gnu.org/software/xboard/engine-intf.html) - Chess Engine Communication Protocol used by XBoard and WinBoard.
- [PGN](https://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm) - Portable Game Notation standard for recording games.
- [FEN](https://www.chessprogramming.org/Forsyth-Edwards_Notation) - Forsyth-Edwards Notation for describing a position in one line.
- [EPD](https://www.chessprogramming.org/Extended_Position_Description) - Extended Position Description, used for test suites.
- [Polyglot Book Format](http://hgm.nubati.net/book_format.html) - Specification of Polyglot opening books.
- [Algebraic Notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) - The standard notation for recording moves.
- [ICCF Numeric Notation](https://en.wikipedia.org/wiki/ICCF_numeric_notation) - Language-neutral notation used in correspondence chess.
- [Descriptive Notation](https://en.wikipedia.org/wiki/Descriptive_notation) - Historical English and Spanish notation.
- [Perft Results](https://www.chessprogramming.org/Perft_Results) - Reference node counts for validating move generators.

## Learning Chess Programming

*Guides, tutorials and communities for engine authors.*

- [Chess Programming Wiki](https://www.chessprogramming.org) - The encyclopedia of computer chess; start with [Getting Started](https://www.chessprogramming.org/Getting_Started).
- [TalkChess](https://talkchess.com) - The main forum for engine developers.
- [Coding Adventure: Chess](https://www.youtube.com/watch?v=U4ogK0MIzqk) - Sebastian Lague builds a chess engine in C# ([follow-up](https://www.youtube.com/watch?v=_vqlIPDR2TU)).
- [Bitboard Chess Engine in C](https://www.youtube.com/watch?v=QUNP-UjujBM) - Code Monkey King's video series building the BBC engine ([code](https://github.com/maksimKorzh/bbc)).
- [VICE](https://github.com/bluefeversoft/vice) - Code for the classic VICE video tutorial series.
- [Rustic](https://rustic-chess.org) - Online book documenting how the Rustic engine was built.
- [CPW-Engine](https://github.com/nescitus/cpw-engine) - Teaching engine written for the Chess Programming Wiki.
- [TSCP](https://tckerrigan.com/Chess/TSCP/) - Tom Kerrigan's Simple Chess Program, a classic for learning.
- [Stockfish Docs](https://official-stockfish.github.io/docs/stockfish-wiki/Home.html) - Official Stockfish documentation on options, building and development.
- [NNUE Explained](https://official-stockfish.github.io/docs/nnue-pytorch-wiki/docs/nnue.html) - In-depth explanation of the NNUE architecture and training.

## Related Lists

*Other curated lists you might enjoy.*

- [Awesome](https://github.com/sindresorhus/awesome#readme) - The list of awesome lists.
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning#readme) - Machine learning frameworks, libraries and software.
