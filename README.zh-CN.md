# Awesome Chess [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精选的国际象棋资源清单，面向棋手、教练、开发者和研究者。

[English](README.md) | [简体中文](README.zh-CN.md)

国际象棋是在 8×8 棋盘上进行的双人策略棋类游戏。本清单收录了与之相关的方方面面：在哪里下棋和学棋、优秀的书籍与视频，以及支撑现代国际象棋软件的开源引擎、开发库、数据集和前沿研究。

欢迎贡献！提交前请先阅读[贡献指南](CONTRIBUTING.zh-CN.md)。

## 目录

- [在线对弈](#在线对弈)
- [训练与提高](#训练与提高)
  - [战术](#战术)
  - [开局](#开局)
  - [残局](#残局)
  - [课程与教学](#课程与教学)
- [少儿与入门](#少儿与入门)
- [书籍](#书籍)
  - [入门](#入门)
  - [进阶](#进阶)
  - [高级与经典](#高级与经典)
  - [免费公版书籍](#免费公版书籍)
- [视频](#视频)
  - [YouTube 频道](#youtube-频道)
  - [演讲](#演讲)
- [播客](#播客)
- [影视作品](#影视作品)
- [新闻、棋谱与等级分](#新闻棋谱与等级分)
- [组织机构](#组织机构)
- [赛事](#赛事)
- [社区](#社区)
- [变体](#变体)
- [排局与问题](#排局与问题)
- [通讯棋](#通讯棋)
- [无障碍](#无障碍)
- [中文资源](#中文资源)
- [工具](#工具)
  - [分析与统计](#分析与统计)
  - [棋图与图片](#棋图与图片)
  - [棋钟](#棋钟)
- [软件](#软件)
  - [桌面图形界面](#桌面图形界面)
  - [移动端](#移动端)
  - [终端](#终端)
- [引擎](#引擎)
  - [顶级引擎](#顶级引擎)
  - [神经网络与拟人引擎](#神经网络与拟人引擎)
  - [变体引擎](#变体引擎)
  - [经典与教学引擎](#经典与教学引擎)
  - [商业引擎](#商业引擎)
- [开发库](#开发库)
  - [Python](#python)
  - [JavaScript 与 TypeScript](#javascript-与-typescript)
  - [棋盘组件](#棋盘组件)
  - [Rust](#rust)
  - [Go](#go)
  - [JVM](#jvm)
  - [C 与 C++](#c-与-c)
  - [其他语言](#其他语言)
- [引擎开发](#引擎开发)
  - [测试](#测试)
  - [神经网络训练](#神经网络训练)
  - [调参与调试](#调参与调试)
  - [开局库与 PGN](#开局库与-pgn)
- [开源平台与服务](#开源平台与服务)
- [机器人与 API](#机器人与-api)
- [残局库](#残局库)
- [数据集](#数据集)
- [人工智能与研究](#人工智能与研究)
  - [论文](#论文)
  - [项目](#项目)
  - [大模型评测](#大模型评测)
- [计算机视觉](#计算机视觉)
- [硬件](#硬件)
- [引擎评级与赛事](#引擎评级与赛事)
- [格式与协议](#格式与协议)
- [学习国际象棋编程](#学习国际象棋编程)

## 在线对弈

*与真人对弈的网站和应用。*

- [Lichess](https://lichess.org) - 免费、开源、无广告的对弈平台，支持各种用时、变体、研究和分析，另有[中文界面](https://lichess.org/?lang=zh-CN)。
- [Chess.com](https://www.chess.com) - 全球最大的国际象棋平台，涵盖对弈、谜题、课程、新闻和赛事直播，另有[中文版](https://www.chess.com/zh)。
- [World Chess](https://worldchess.com) - 国际棋联官方线上平台，可获得 FIDE 线上等级分和称号。
- [Internet Chess Club](https://www.chessclub.com) - 1995 年运营至今的老牌付费对弈服务器（ICC）。
- [Free Internet Chess Server](https://www.freechess.org) - 历史悠久的免费对弈服务器（FICS），支持众多经典桌面客户端。
- [PlayOK](https://www.playok.com/en/chess/) - 无需注册即可在浏览器中对弈。
- [Take Take Take](https://taketaketake.com) - 卡尔森参与创办的应用，可对弈、看比赛和复盘。

## 训练与提高

*帮助你提高棋力的网站和应用。*

### 战术

- [Lichess Puzzles](https://lichess.org/training) - 无限量免费战术题，支持主题训练、[Puzzle Storm](https://lichess.org/storm)、[Racer](https://lichess.org/racer) 和 [Streak](https://lichess.org/streak)。
- [Chess.com Puzzles](https://www.chess.com/puzzles) - 等级分战术题，以及 Puzzle Rush、Puzzle Battle 等模式。
- [ChessTempo](https://chesstempo.com) - 支持间隔重复的战术训练，另有残局、开局训练和棋谱库。
- [Blitz Tactics](https://blitztactics.com) - 限时快速识别战术模式的训练。
- [Listudy](https://listudy.org) - 免费的间隔重复训练，涵盖开局、战术和盲棋战术。
- [Lichess Coordinate Trainer](https://lichess.org/training/coordinate) - 棋盘坐标识别训练。

### 开局

- [Lichess Opening Explorer](https://lichess.org/analysis) - 分析棋盘，可查看任意局面的大师、Lichess 及个人对局统计。
- [Lichess Openings](https://lichess.org/opening) - 免费开局百科，附统计数据和示范对局。
- [OpeningTree](https://www.openingtree.com) - 根据任意 Lichess 或 Chess.com 棋手的对局生成开局树（[源码](https://github.com/openingtree/openingtree)）。
- [Chessbook](https://www.chessbook.com) - 开局谱构建与训练工具，聚焦你实战中最常遇到的着法。
- [Chess Opening Theory](https://en.wikibooks.org/wiki/Chess_Opening_Theory) - 维基教科书上由社区编写的免费开局理论。
- [ChessGames.com ECO Index](https://www.chessgames.com/chessecohelp.html) - 按 ECO 开局编码分类的棋谱。

### 残局

- [Lichess Practice](https://lichess.org/practice) - 关于将杀、关键残局等内容的互动练习。
- [Chess.com Endgames](https://www.chess.com/endgames) - 按难度分级的残局理论训练。
- [Endgame Trainer](https://endgametrainer.com) - 超过 6000 道理论残局练习。
- [Chess Endgame Training](https://chess-endgame-trainer.web.app) - 免费网页应用，与残局库和 Stockfish 对练残局。

### 课程与教学

- [Chess.com Lessons](https://www.chess.com/lessons) - 从入门到大师的系统视频课程。
- [Chessable](https://www.chessable.com) - 基于间隔重复的互动课程平台（多数课程收费）。
- [ChessMood](https://chessmood.com) - 特级大师主讲的视频课程与训练社区（收费）。
- [ChessDojo](https://www.chessdojo.club) - 按等级分划分的训练计划和学习社区。
- [Aimchess](https://aimchess.com) - 分析你的线上对局并生成个性化训练。
- [Noctie](https://noctie.ai) - 类人 AI 陪练，边下边指导。
- [DecodeChess](https://decodechess.com) - 用自然语言解释引擎着法的 AI 工具。
- [Chess Steps](https://www.chess-steps.com) - 荷兰“阶梯教学法”，全球教练广泛使用的六阶课程体系。
- [Chess Strategy Online](https://www.chessstrategyonline.com) - 面向进阶棋手的免费战略教程。

## 少儿与入门

*轻松入门国际象棋。*

- [Lichess Learn](https://lichess.org/learn) - 免费互动课程，讲解规则和基本战术。
- [ChessKid](https://www.chesskid.com) - 面向儿童的安全平台，提供对弈、课程和谜题。
- [ChessWorld](https://www.chessworld.io) - 游戏化的少儿学棋应用（原 ChessMatec），基于特级大师 Boris Alterman 的教学法。
- [Story Time Chess](https://storytimechess.com) - 用讲故事的方式教 3 岁以上儿童学棋的桌游。
- [Chessily](https://chessily.com) - 对新手友好的互动学习平台。

## 书籍

*按水平分级的经典与现代书籍。链接指向 [Open Library](https://openlibrary.org) 或免费版本。*

### 入门

- [Bobby Fischer Teaches Chess](https://openlibrary.org/works/OL6572297W) - Bobby Fischer 等著，《菲舍尔教你下国际象棋》，以程序化练习讲解将杀模式。
- [Logical Chess: Move by Move](https://openlibrary.org/works/OL16043919W) - Irving Chernev 著，逐步讲解 33 盘大师对局的每一步。
- [Chess Fundamentals](https://www.gutenberg.org/ebooks/33870) - 卡帕布兰卡著，1921 年的经典《国际象棋基础》，古登堡计划免费阅读。
- [1001 Chess Exercises for Beginners](https://openlibrary.org/works/OL28215716W) - Franco Masetti 与 Roberto Messa 著，分级战术练习。
- [Chess: 5334 Problems, Combinations and Games](https://openlibrary.org/works/OL19641960W) - 波尔加·拉斯洛著，包含大量一步杀、两步杀、三步杀的习题大全。

### 进阶

- [The Amateur's Mind](https://openlibrary.org/works/OL1806209W) - Jeremy Silman 著，剖析业余棋手常见的思维误区。
- [How to Reassess Your Chess](https://openlibrary.org/works/OL1806212W) - Jeremy Silman 著，通过“不平衡”评估局面。
- [Silman's Complete Endgame Course](https://openlibrary.org/works/OL1806211W) - Jeremy Silman 著，按等级分划分的残局教程。
- [The Woodpecker Method](https://openlibrary.org/works/OL26456631W) - Axel Smith 与 Hans Tikkanen 著，通过反复练习提升战术的“啄木鸟训练法”。
- [Pawn Structure Chess](https://openlibrary.org/works/OL3297355W) - Andrew Soltis 著，从常见兵型出发讲解计划。
- [Chess Structures: A Grandmaster Guide](https://openlibrary.org/works/OL21568498W) - Mauricio Flores Rios 著，现代兵型结构指南。
- [The Art of Attack in Chess](https://openlibrary.org/works/OL4069104W) - Vladimir Vuković 著，讲解攻王的经典著作。
- [Simple Chess](https://openlibrary.org/works/OL6473115W) - Michael Stean 著，清晰讲解局面性思想。

### 高级与经典

- [My System](https://openlibrary.org/works/OL4918564W) - 尼姆佐维奇著，《我的体系》，1925 年出版的局面理论奠基之作。
- [Think Like a Grandmaster](https://openlibrary.org/works/OL7983003W) - 科托夫著，《像特级大师一样思考》，计算与“变化树”的经典。
- [Zurich International Chess Tournament 1953](https://openlibrary.org/works/OL27997817W) - 布龙斯坦著，传奇赛事的对局集。
- [My 60 Memorable Games](https://openlibrary.org/works/OL2714658W) - 菲舍尔著，《我的 60 盘难忘对局》。
- [Dvoretsky's Endgame Manual](https://openlibrary.org/works/OL265702W) - 德沃列茨基著，残局理论的权威参考书。
- [Fundamental Chess Endings](https://openlibrary.org/works/OL16972394W) - Karsten Müller 与 Frank Lamprecht 著，全面的残局百科。
- [Endgame Strategy](https://openlibrary.org/works/OL9047079W) - Mikhail Shereshevsky 著，残局的战略原则。
- [Garry Kasparov on My Great Predecessors](https://openlibrary.org/works/OL3006223W) - 卡斯帕罗夫著，《我的伟大前辈》，多卷本的世界冠军史。
- [Grandmaster Preparation: Calculation](https://openlibrary.org/works/OL21179548W) - Jacob Aagaard 著，高强度的计算训练。
- [Game Changer](https://openlibrary.org/works/OL21643546W) - Matthew Sadler 与 Natasha Regan 著，解读 AlphaZero 的棋风及其启示。

### 免费公版书籍

- [Project Gutenberg Chess Shelf](https://www.gutenberg.org/ebooks/subject/1677) - 古登堡计划中所有公版国际象棋书籍。
- [Chess Strategy](https://www.gutenberg.org/ebooks/5614) - Edward Lasker 著，经典战略入门。
- [Chess and Checkers: The Way to Mastership](https://www.gutenberg.org/ebooks/4913) - Edward Lasker 著，面向进阶棋手的实用指南。
- [The Blue Book of Chess](https://www.gutenberg.org/ebooks/16377) - Howard Staunton 著，19 世纪的国际象棋手册。
- [The Exploits and Triumphs in Europe of Paul Morphy](https://www.gutenberg.org/ebooks/34180) - Frederick Milnes Edge 著，莫菲欧洲之旅的同时代记述。
- [Chess Generalship](https://www.gutenberg.org/ebooks/55278) - Franklin K. Young 著，借鉴军事思想的国际象棋理论。

## 视频

*值得一看的频道和演讲。*

### YouTube 频道

- [GothamChess](https://www.youtube.com/@GothamChess) - 国际大师 Levy Rozman 的教学、赛事回顾与娱乐视频。
- [agadmator's Chess Channel](https://www.youtube.com/@agadmator) - 经典与现代名局讲解。
- [GMHikaru](https://www.youtube.com/@GMHikaru) - 中村光的直播与回顾。
- [Daniel Naroditsky](https://www.youtube.com/@DanielNaroditskyGM) - 已故特级大师纳罗季茨基（1995-2025）的 speedrun 系列和讲座，极具教学价值。
- [Eric Rosen](https://www.youtube.com/@eric-rosen) - 国际大师 Eric Rosen 的趣味教学对局。
- [Chess Vibes](https://www.youtube.com/@ChessVibesOfficial) - 特级大师 Nelson Lopez 的概念教学，清晰易懂。
- [Hanging Pawns](https://www.youtube.com/@HangingPawns) - 深入的开局讲解。
- [John Bartholomew](https://www.youtube.com/@JohnBartholomewChess) - 长期连载的教学系列 Climbing the Rating Ladder。
- [Saint Louis Chess Club](https://www.youtube.com/@STLChessClub) - 讲座与顶级赛事直播。
- [ChessNetwork](https://www.youtube.com/@ChessNetwork) - 经典教学解说。
- [ChessBase India](https://www.youtube.com/@ChessBaseIndia) - 大型印度国际象棋媒体，赛事报道丰富。
- [Anna Cramling](https://www.youtube.com/@AnnaCramling) - 轻松有趣的对局和 Vlog。
- [FIDE](https://www.youtube.com/@FIDE_chess) - 国际棋联官方赛事直播。

### 演讲

- [Understanding Chess Mastery](https://www.youtube.com/watch?v=fPopQaY7Og4) - Jennifer Shahade 在 TEDxBaltimore 的演讲。
- [How Chess Can Revolutionize Learning](https://www.youtube.com/watch?v=A3yDvM8aplY) - Cody Pomeranz 在 TEDxYale 的演讲。
- [Working Backward to Solve Problems](https://www.youtube.com/watch?v=v34NqCbAA1c) - Maurice Ashley 讲述从国际象棋中学到的解题思路。
- [Don't Fear Intelligent Machines. Work with Them](https://www.ted.com/talks/garry_kasparov_don_t_fear_intelligent_machines_work_with_them) - 卡斯帕罗夫谈深蓝以及人机协作。

## 播客

*用耳朵听的国际象棋。*

- [Perpetual Chess Podcast](https://www.perpetualchesspod.com) - 每周采访顶尖棋手、教练和作者。
- [C-Squared Podcast](https://c2pod.com) - 特级大师卡鲁阿纳与 Chirila 每周畅谈棋坛。
- [The Chess Pit](https://www.chesspitpod.com) - 轻松幽默的英国每周国际象棋播客。

## 影视作品

*关于国际象棋及棋手的电影和剧集。*

- [The Queen's Gambit](https://en.wikipedia.org/wiki/The_Queen%27s_Gambit_(miniseries)) - 《后翼弃兵》，Netflix 迷你剧（2020），讲述虚构天才少女 Beth Harmon 的故事。
- [Searching for Bobby Fischer](https://en.wikipedia.org/wiki/Searching_for_Bobby_Fischer) - 《王者之旅》（1993），根据 Josh Waitzkin 的童年经历改编。
- [Pawn Sacrifice](https://en.wikipedia.org/wiki/Pawn_Sacrifice) - 《出线》（2014），讲述 1972 年菲舍尔对斯帕斯基之战。
- [Queen of Katwe](https://en.wikipedia.org/wiki/Queen_of_Katwe) - 《卡推女王》（2016），讲述乌干达棋手 Phiona Mutesi 的真实故事。
- [Magnus](https://en.wikipedia.org/wiki/Magnus_(2016_film)) - 纪录片（2016），记录卡尔森登上世界冠军之路。
- [Bobby Fischer Against the World](https://en.wikipedia.org/wiki/Bobby_Fischer_Against_the_World) - HBO 纪录片（2011），讲述菲舍尔的一生。
- [Game Over: Kasparov and the Machine](https://en.wikipedia.org/wiki/Game_Over:_Kasparov_and_the_Machine) - 纪录片（2003），讲述卡斯帕罗夫对阵深蓝。
- [Closing Gambit](https://vimeo.com/ondemand/closinggambit) - 纪录片（2018），讲述 1978 年科尔奇诺伊与卡尔波夫的世界冠军赛。
- [Brooklyn Castle](https://en.wikipedia.org/wiki/Brooklyn_Castle) - 纪录片（2012），讲述一支城市公立学校国际象棋队。
- [The Dark Horse](https://en.wikipedia.org/wiki/The_Dark_Horse_(2014_film)) - 《黑马》（2014），讲述新西兰国际象棋教练 Genesis Potini 的故事。
- [The Luzhin Defence](https://en.wikipedia.org/wiki/The_Luzhin_Defence) - 《防守》（2000），改编自纳博科夫的小说。

## 新闻、棋谱与等级分

*关注棋坛动态，查询棋谱和棋手信息。*

- [Lichess Broadcasts](https://lichess.org/broadcast) - 免费的重大赛事直播，附引擎分析。
- [Chess.com Events](https://www.chess.com/events) - 赛事直播与专题页（chess24 与 ChessBomb 的继任者）。
- [ChessBase News](https://en.chessbase.com) - 历史悠久的国际象棋新闻与分析。
- [The Week in Chess](https://theweekinchess.com) - TWIC，自 1994 年起每周发布新闻和免费 PGN 棋谱。
- [ChessGames.com](https://www.chessgames.com) - 带注释的大型棋谱库，社区活跃。
- [365Chess](https://www.365chess.com) - 棋谱数据库，包含棋手、赛事和开局浏览器。
- [Chessdom](https://www.chessdom.com) - 国际象棋新闻与实时对局。
- [New in Chess](https://www.newinchess.com/magazine) - 顶级特级大师参与撰写的权威国际象棋杂志。
- [FIDE Ratings](https://ratings.fide.com) - 国际棋联官方等级分和棋手档案。
- [2700chess](https://www.2700chess.com) - 世界顶尖棋手实时等级分。
- [Chess-Results](https://chess-results.com) - 数千场线下比赛的编排和成绩。

## 组织机构

*管理机构与各国棋协。*

- [FIDE](https://www.fide.com) - 国际棋联，国际象棋的国际管理机构；[FIDE 手册](https://handbook.fide.com)收录国际象棋规则。
- [Chinese Chess Association](https://cca.mindsports.org.cn) - 中国国际象棋协会官网。
- [US Chess](https://new.uschess.org) - 美国国际象棋联合会。
- [English Chess Federation](https://www.englishchess.org.uk) - 英格兰国际象棋联合会。
- [Chess Federation of Canada](https://www.chess.ca) - 加拿大国际象棋联合会。
- [European Chess Union](https://www.europechess.org) - 欧洲国际象棋联盟。
- [Saint Louis Chess Club](https://www.saintlouischessclub.org) - 美国顶级俱乐部，辛克菲尔德杯和美国锦标赛的举办方。

## 赛事

*重要的周期性赛事。*

- [FIDE World Championship](https://worldchampionship.fide.com) - 世界国际象棋冠军赛官方网站。
- [Candidates Tournament](https://en.wikipedia.org/wiki/Candidates_Tournament) - 决定世界冠军挑战者的八人候选人赛。
- [Chess Olympiad](https://en.wikipedia.org/wiki/Chess_Olympiad) - 两年一届的国家队团体赛。
- [Norway Chess](https://norwaychess.no) - 每年在斯塔万格举行的顶级超级赛。
- [Tata Steel Chess](https://tatasteelchess.com/en) - 塔塔钢铁赛，被誉为“国际象棋的温布尔登”，每年一月在维克安泽举行。
- [Grand Chess Tour](https://grandchesstour.org) - 包括辛克菲尔德杯在内的顶级巡回赛。
- [Freestyle Chess](https://www.freestyle-chess.com) - 卡尔森参与创办的顶级 Chess960（自由式）赛事。
- [Esports World Cup Chess](https://www.esportsworldcup.com/en/competitions/chess) - 电竞世界杯的国际象棋项目。

## 社区

*交流国际象棋的地方。*

- [r/chess](https://www.reddit.com/r/chess/) - Reddit 上最大的国际象棋版块。
- [r/chessbeginners](https://www.reddit.com/r/chessbeginners/) - 友好的新手提问版块。
- [Lichess Forum](https://lichess.org/forum) - Lichess 论坛，以及用于俱乐部的[战队](https://lichess.org/team)。
- [Chess.com Forums](https://www.chess.com/forum) - 大型综合国际象棋论坛。
- [Chess Stack Exchange](https://chess.stackexchange.com) - 关于规则、历史和战略的问答社区。
- [Lichess Discord](https://discord.gg/lichess) - Lichess 官方 Discord 服务器。

## 变体

*标准国际象棋之外的玩法。*

- [Lichess Variants](https://lichess.org/variant) - Chess960、Crazyhouse、Atomic、Antichess、山丘之王、三将、Horde 和 Racing Kings。
- [PyChess](https://www.pychess.org) - 免费变体服务器，支持中国象棋、将棋、泰国象棋、韩国象棋等数十种变体。
- [Chess.com Variants](https://www.chess.com/variants) - 包括四人棋和双人换子棋（Bughouse）在内的变体。
- [The Chess Variant Pages](https://www.chessvariants.com) - 童话象棋变体的百科全书式目录。
- [Chess960](https://en.wikipedia.org/wiki/Chess960) - 菲舍尔任意制象棋：底线棋子随机摆放。

## 排局与问题

*国际象棋排局艺术。*

- [YACPDB](https://www.yacpdb.org) - 大型开放排局数据库。
- [Meson](http://www.bstephen.me.uk/meson/) - 收录约 15 万个排局的数据库。
- [World Federation for Chess Composition](https://www.wfcc.ch) - 世界排局联合会，负责排局和解题锦标赛。
- [The Problemist](https://www.theproblemist.org) - 英国排局协会及其杂志。

## 通讯棋

*慢节奏、一步一步来的国际象棋。*

- [ICCF](https://www.iccf.com) - 国际通讯棋联合会。
- [SchemingMind](https://www.schemingmind.com) - 支持变体的通讯棋俱乐部和服务器。
- [Chess.com Daily](https://www.chess.com/play/online/daily) - 每步可用数天的回合制对局。

## 无障碍

*面向盲人和视障棋手的资源。*

- [Lichess Blind Mode](https://lichess.org/page/blind-mode-guide) - Lichess 读屏模式使用指南。
- [IBCA](https://ibca-info.org) - 国际盲人国际象棋协会。

## 中文资源

*中文国际象棋资源。*

- [国象联盟](https://www.chessease.net) - 国内主要的国际象棋平台，提供对弈、战术题、棋谱库和赛事。
- [弈战](https://www.ixiaqi.com) - 国际象棋、围棋、中国象棋的线上考级和比赛平台。
- [国象充电站](https://www.hellochess.cn) - 中文国际象棋学习网站，提供文章和书单推荐。
- [国家体育总局棋牌运动管理中心](https://www.sport.gov.cn/qpzx/) - 负责管理国际象棋、围棋、中国象棋等项目的国家机构。
- [国际象棋 - 维基百科](https://zh.wikipedia.org/wiki/%E5%9B%BD%E9%99%85%E8%B1%A1%E6%A3%8B) - 中文维基百科“国际象棋”词条。
- [Chess in China](https://en.wikipedia.org/wiki/Chess_in_China) - 国际象棋在中国的发展历史，包括[中国国际象棋甲级联赛](https://en.wikipedia.org/wiki/China_Chess_League)。

## 工具

*棋手的实用工具。*

### 分析与统计

- [Lichess Board Editor](https://lichess.org/editor) - 摆出任意局面进行分析，或[导入 PGN](https://lichess.org/paste)。
- [Chess.com Analysis](https://www.chess.com/analysis) - 分析棋盘、对局复盘和 PGN 编辑器。
- [Chesskit](https://chesskit.org) - 免费开源的 Stockfish 复盘工具（[源码](https://github.com/GuillaumeSD/Chesskit)）。
- [WintrChess](https://wintrchess.com) - 免费开源的复盘工具，带着法分类（[源码](https://github.com/WintrCat/wintrchess)）。
- [ChessMonitor](https://www.chessmonitor.com) - Lichess 和 Chess.com 对局的数据分析面板。
- [Lumichess](https://lumichess.com) - Chess.com 和 Lichess 对局的免费复盘和统计。

### 棋图与图片

- [Apronus Diagram Editor](https://www.apronus.com/chess/diagram/editor/) - 制作棋图和 GIF 动画。
- [Jin Chess Diagram Composer](https://www.jinchess.com/chessboard/composer/) - 经典的棋图生成器。
- [ChessboardImage](https://chessboardimage.com) - 根据 FEN 生成棋盘图片。
- [Chessvision.ai](https://chessvision.ai) - 从截图、书籍和视频中识别局面。
- [Chess Symbols in Unicode](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) - 国际象棋棋子的 Unicode 字符。
- [Wikimedia Commons Chess Pieces](https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent) - 自由授权的棋子图片。
- [Lichess Piece Sets](https://github.com/lichess-org/lila/tree/master/public/piece) - 数十套开放授权的 SVG 棋子。
- [Spiral Chess Set](https://www.thingiverse.com/thing:470700) - 可 3D 打印的棋子模型。

### 棋钟

- [ChessClock.org](https://chessclock.org) - 免费在线棋钟。

## 软件

*用于对弈、分析和管理棋谱的软件。*

### 桌面图形界面

- [En Croissant](https://github.com/franciscoBSalgueiro/en-croissant) - 现代化的跨平台分析与棋谱库工具（[官网](https://encroissant.org)）。
- [Nibbler](https://github.com/rooklift/nibbler) - UCI 引擎分析界面，针对 Leela 有专门功能。
- [Cute Chess](https://github.com/cutechess/cutechess) - 用于引擎对战的图形界面、命令行工具和库。
- [BanksiaGUI](https://www.banksiagui.com) - 免费的引擎赛事与分析界面。
- [Arena](http://www.playwitharena.de) - 历史悠久的免费 UCI/WinBoard 引擎界面。
- [Scid vs. PC](https://scidvspc.sourceforge.net) - 棋谱数据库与分析工具。
- [ChessX](https://github.com/Isarhamster/chessx) - 跨平台棋谱库与 PGN 工具。
- [Lucas Chess](https://github.com/lukasmonk/lucaschessR6) - 以训练为核心的界面，内置大量练习和引擎。
- [PyChess](https://github.com/pychess/pychess) - 支持 FICS 和 Lichess 的 GTK 桌面客户端。
- [XBoard](https://www.gnu.org/software/xboard/) - 经典的 GNU 图形界面，CECP 协议的参考实现。
- [Stockfish for Mac](https://github.com/daylen/stockfish-mac) - 原生 macOS 版 Stockfish 分析应用。
- [ChessBase](https://www.chessbase.com) - 业界标准的商业棋谱数据库软件（收费）。

### 移动端

- [Lichess Mobile](https://github.com/lichess-org/mobile) - 基于 Flutter 的 Lichess 官方开源应用。
- [DroidFish](https://github.com/peterosterlund2/droidfish) - 带引擎分析的 Android 应用。

### 终端

- [chess-tui](https://github.com/thomas-mauran/chess-tui) - Rust 编写的终端国际象棋，支持 Stockfish 和 Lichess。
- [cli-chess](https://github.com/trevorbayless/cli-chess) - Lichess 终端客户端，也支持离线对弈。
- [Gambit](https://github.com/maaslalani/gambit) - 在终端里下国际象棋。

## 引擎

*下国际象棋的程序。*

### 顶级引擎

- [Stockfish](https://github.com/official-stockfish/Stockfish) - 最强的开源引擎，采用 NNUE 评估（[官网](https://stockfishchess.org)）。
- [Leela Chess Zero](https://github.com/LeelaChessZero/lc0) - AlphaZero 风格的神经网络引擎（[官网](https://lczero.org)）。
- [Reckless](https://github.com/codedeliveryservice/Reckless) - Rust 编写的顶级 NNUE 引擎。
- [PlentyChess](https://github.com/Yoshie2000/PlentyChess) - 采用神经网络评估的顶级引擎。
- [Viridithas](https://github.com/cosmobobak/viridithas) - Rust 编写的超人水平 NNUE 引擎。
- [Obsidian](https://github.com/gab8192/Obsidian) - C++ 编写的强力 NNUE 引擎。
- [Stormphrax](https://github.com/Ciekce/Stormphrax) - 神经网络从零知识训练的引擎。
- [Integral](https://github.com/aronpetko/integral) - C++ 编写的强力神经网络引擎。
- [Alexandria](https://github.com/PGG106/Alexandria) - 强力的 NNUE 位棋盘引擎。
- [Berserk](https://github.com/jhonnold/berserk) - C 编写的一流引擎。
- [Ethereal](https://github.com/AndyGrant/Ethereal) - OpenBench 作者编写、文档完善的引擎。
- [Koivisto](https://github.com/Luecx/Koivisto) - 强力 NNUE 引擎。
- [Caissa](https://github.com/Witek902/Caissa) - C++ 编写的强力 NNUE 引擎。
- [Arasan](https://github.com/jdart1/arasan-chess) - 自上世纪 90 年代起持续开发的老牌引擎。

### 神经网络与拟人引擎

- [Maia Chess](https://github.com/CSSLab/maia-chess) - 基于 Lichess 对局训练的拟人神经网络（[官网](https://www.maiachess.com)）。
- [Maia-2](https://github.com/CSSLab/maia2) - 覆盖各水平段的统一拟人模型。
- [Patricia](https://github.com/Adam-Kulju/Patricia) - 刻意追求激进、热衷弃子的引擎。
- [ChessCoach](https://github.com/chrisbutner/ChessCoach) - 能生成自然语言解说的神经网络引擎。

### 变体引擎

- [Fairy-Stockfish](https://github.com/fairy-stockfish/Fairy-Stockfish) - Stockfish 衍生引擎，支持中国象棋、将棋、Crazyhouse 等众多变体。
- [CrazyAra](https://github.com/QueensGambit/CrazyAra) - 面向 Crazyhouse 等变体的深度学习 MCTS 引擎。

### 经典与教学引擎

- [Sunfish](https://github.com/thomasahle/sunfish) - 约 111 行 Python 实现的极简引擎。
- [GNU Chess](https://www.gnu.org/software/chess/) - 自由软件基金会的国际象棋引擎。
- [Crafty](https://github.com/MichaelB7/Crafty) - Robert Hyatt 的经典位棋盘引擎（镜像）。
- [Fruit](https://github.com/Warpten/Fruit-2.1) - Fabien Letouzey 编写、影响深远的开源引擎（镜像）。
- [Weiss](https://github.com/TerjeKir/weiss) - C 编写、代码简洁易读的引擎。
- [Andoma](https://github.com/healeycodes/andoma) - 小巧易读的 Python 引擎，适合学习 alpha-beta 搜索。
- [latrunculorum](https://github.com/benwr/latrunculorum) - 简单的 Python 国际象棋机器人。

### 商业引擎

- [Komodo Dragon](https://www.chessprogramming.org/Komodo) - 多次 TCEC 冠军，2026 年停止销售。
- [HIARCS](https://www.hiarcs.com) - 商业引擎及 HIARCS Chess Explorer 界面。
- [Shredder](https://www.shredderchess.com) - Stefan Meyer-Kahlen 开发的商业引擎和界面。
- [Fritz](https://shop.chessbase.com/en/categories/fritz) - ChessBase 出品的对弈与分析软件。

## 开发库

*着法生成、格式解析和棋盘渲染。*

### Python

- [python-chess](https://github.com/niklasf/python-chess) - Python 标准国际象棋库，支持着法生成、PGN、Polyglot、残局库和 UCI/XBoard 引擎。
- [stockfish](https://github.com/zhelyabuzhsky/stockfish) - 简洁的 Stockfish 调用封装。
- [Chessnut](https://github.com/cgearhart/Chessnut) - 简单的棋盘模型，支持 FEN 解析和合法着法生成。
- [fenparser](https://github.com/tlehman/fenparser) - 小型 FEN 解析器。

### JavaScript 与 TypeScript

- [chess.js](https://github.com/jhlywa/chess.js) - 着法生成与校验、FEN/PGN 支持和终局判断。
- [chessops](https://github.com/niklasf/chessops) - TypeScript 实现的国际象棋及变体规则，Lichess 在用。
- [kokopu](https://github.com/yo35/kokopu) - 国际象棋规则以及 FEN、PGN 读写。
- [pgn-parser](https://github.com/mliebelt/pgn-parser) - 将 PGN 解析为 JSON。
- [stockfish.js](https://github.com/nmrugg/stockfish.js) - 编译为 WebAssembly 的 Stockfish，可用于浏览器和 Node.js。
- [chess](https://www.npmjs.com/package/chess) - 基于代数记谱法的库，可校验局面并列出合法着法。

### 棋盘组件

- [chessground](https://github.com/lichess-org/chessground) - Lichess 的网页/移动端棋盘组件。
- [cm-chessboard](https://github.com/shaack/cm-chessboard) - 无依赖的 ES6 SVG 棋盘。
- [react-chessboard](https://github.com/Clariity/react-chessboard) - React 响应式棋盘组件。
- [vue3-chessboard](https://github.com/qwerty084/vue3-chessboard) - 基于 chessground 和 chess.js 的 Vue 3 棋盘。
- [chessboard.js](https://github.com/oakmac/chessboardjs) - 经典的独立 JavaScript 棋盘。
- [Lichess PGN Viewer](https://github.com/lichess-org/pgn-viewer) - Lichess 出品的可嵌入 PGN 查看器。
- [chess-board](https://github.com/laat/chess-board) - 根据 FEN 渲染局面的 Web Component。
- [flutter-chessground](https://github.com/lichess-org/flutter-chessground) - Lichess 出品的 Flutter 棋盘组件。

### Rust

- [shakmaty](https://github.com/niklasf/shakmaty) - 国际象棋及变体规则库，驱动 Lichess 的 Rust 服务。
- [cozy-chess](https://github.com/analog-hors/cozy-chess) - 快速的国际象棋及 Chess960 着法生成。
- [chess](https://github.com/jordanbray/chess) - 快速着法生成 crate。
- [Pleco](https://github.com/pleco-rs/Pleco) - Stockfish 的 Rust 重写版，可作库或引擎使用。
- [fen](https://github.com/ucarion/fen) - 带完善错误处理的 FEN 解析器。

### Go

- [CorentinGS/chess](https://github.com/CorentinGS/chess) - notnil/chess 的维护分支，支持位棋盘、PGN/FEN、UCI 和开局库。

### JVM

- [chesslib](https://github.com/bhlangonijr/chesslib) - Java 库，支持合法着法生成和 FEN/PGN 解析。
- [scalachess](https://github.com/lichess-org/scalachess) - Lichess 的 Scala 不可变国际象棋模型。

### C 与 C++

- [chess-library](https://github.com/Disservin/chess-library) - 快速的单头文件 C++ 国际象棋库。
- [Fathom](https://github.com/jdart1/Fathom) - 独立的 Syzygy 残局库查询库。
- [Gaviota Tablebases](https://github.com/michiguel/Gaviota-Tablebases) - Gaviota 残局库查询代码。

### 其他语言

- [Rudzoft ChessLib](https://github.com/rudzen/ChessLib) - C# 数据结构与着法生成。
- [dartchess](https://github.com/lichess-org/dartchess) - Lichess 出品的 Dart 国际象棋库。
- [chesskit-swift](https://github.com/chesskit-app/chesskit-swift) - 处理国际象棋逻辑的 Swift 包。
- [Chess.jl](https://github.com/romstad/Chess.jl) - Stockfish 联合作者 Tord Romstad 编写的 Julia 库。
- [chessIO](https://github.com/mlang/chessIO) - 带 UCI 前端的快速 Haskell 着法生成器。
- [chess](https://github.com/pioz/chess) - 快速的 Ruby 位棋盘库。

## 引擎开发

*构建、测试和调优引擎的工具。*

### 测试

- [OpenBench](https://github.com/AndyGrant/OpenBench) - 众多顶级引擎使用的分布式 SPRT 测试框架。
- [Fishtest](https://github.com/official-stockfish/fishtest) - Stockfish 的分布式测试框架（[在线实例](https://tests.stockfishchess.org)）。
- [fastchess](https://github.com/Disservin/fastchess) - 快速的引擎对战与 SPRT 命令行工具。
- [c-chess-cli](https://github.com/lucasart/c-chess-cli) - C 编写的轻量级命令行对战工具。
- [Stockfish Books](https://github.com/official-stockfish/books) - 用于引擎测试的开局库。

### 神经网络训练

- [bullet](https://github.com/jw1912/bullet) - Rust 机器学习库，是众多现代引擎训练 NNUE 的首选。
- [nnue-pytorch](https://github.com/official-stockfish/nnue-pytorch) - Stockfish 基于 PyTorch 的 NNUE 训练器。
- [Grapheus](https://github.com/Luecx/Grapheus) - 训练 NNUE 网络的 GPU 框架。
- [lczero-training](https://github.com/LeelaChessZero/lczero-training) - Leela Chess Zero 的网络训练代码。

### 调参与调试

- [texel-tuner](https://github.com/GediminasMasaitis/texel-tuner) - 通用的评估参数 Texel 调参器。
- [chess-tuning-tools](https://github.com/kiudee/chess-tuning-tools) - 基于贝叶斯优化的引擎参数调优。
- [perftree](https://github.com/agausmann/perftree) - 将你的着法生成器与 Stockfish 对比的 perft 调试器。
- [Stockfish WDL Model](https://github.com/official-stockfish/WDL_model) - 拟合胜/和/负模型以标准化评估值。

### 开局库与 PGN

- [PolyGlot](https://github.com/ddugovic/polyglot) - 开局库工具及 UCI 转 XBoard 适配器。
- [pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) - 搜索、过滤和转换 PGN 的命令行工具。

## 开源平台与服务

*在线国际象棋背后的开源基础设施。*

- [lila](https://github.com/lichess-org/lila) - Lichess 服务端，使用 Scala 编写。
- [lila-ws](https://github.com/lichess-org/lila-ws) - Lichess 的 WebSocket 服务。
- [fishnet](https://github.com/lichess-org/fishnet) - 为 Lichess 提供志愿者分布式 Stockfish 分析。
- [lila-openingexplorer](https://github.com/lichess-org/lila-openingexplorer) - Lichess 开局浏览器后端。
- [lila-tablebase](https://github.com/lichess-org/lila-tablebase) - Lichess 残局库服务。
- [lila-gif](https://github.com/lichess-org/lila-gif) - 将局面和对局渲染为图片及 GIF。
- [irwin](https://github.com/clarkerubber/irwin) - Lichess 的机器学习反作弊系统。
- [pychess-variants](https://github.com/gbtami/pychess-variants) - PyChess 变体网站的服务端。
- [Listudy](https://github.com/ArneVogel/listudy) - Elixir 编写的间隔重复训练服务。
- [Infinite Chess](https://github.com/Infinite-Chess/infinitechess.org) - 无限棋盘国际象棋的服务端。

## 机器人与 API

*将程序接入在线国际象棋。*

- [Lichess API](https://lichess.org/api) - Lichess 官方 REST 与流式 API，含 Bot、Board、残局库和开局浏览器接口。
- [lichess-bot](https://github.com/lichess-bot-devs/lichess-bot) - 连接 Lichess 机器人账号与 UCI/XBoard 引擎的官方桥接工具。
- [BotLi](https://github.com/Torom/BotLi) - 可高度配置的 Lichess 机器人桥接工具。
- [berserk](https://github.com/lichess-org/berserk) - Lichess API 官方 Python 客户端。
- [chariot](https://github.com/tors42/chariot) - Lichess API 的 Java 客户端。
- [Chess.com Published-Data API](https://www.chess.com/news/view/published-data-api) - Chess.com 只读公开 API，可获取棋手、对局和俱乐部数据。
- [chess.com](https://github.com/sarartur/chess.com) - Chess.com 公开 API 的 Python 客户端。
- [chess-web-api](https://github.com/andyruwruw/chess-web-api) - Chess.com 公开 API 的 JavaScript 封装。
- [Chess Challenge](https://github.com/SebLague/Chess-Challenge) - Sebastian Lague 的 C# 框架，用于编写迷你国际象棋机器人。

## 残局库

*少子局面的完美着法数据库。*

- [Syzygy Tables](https://syzygy-tables.info) - 查询七子 Syzygy 残局库的网页与 API。
- [Lichess Tablebase](https://tablebase.lichess.ovh) - 公开的残局库服务与下载镜像。
- [Syzygy Generator](https://github.com/syzygy1/tb) - Ronald de Man 编写的 Syzygy 残局库生成器。
- [Syzygy Bases](https://www.chessprogramming.org/Syzygy_Bases) - 标准 WDL/DTZ 残局库介绍。
- [Gaviota Tablebases Overview](https://www.chessprogramming.org/Gaviota_Tablebases) - 最多五子的压缩 DTM 残局库。
- [Lomonosov Tablebases](https://www.chessprogramming.org/Lomonosov_Tablebases) - 首个完整的七子 DTM 残局库。

## 数据集

*用于分析和机器学习的对局、谜题和评估数据。*

- [Lichess Open Database](https://database.lichess.org) - 所有 Lichess 等级分对局的月度 PGN 数据，另含谜题和评估数据。
- [Lichess on Hugging Face](https://huggingface.co/Lichess) - Parquet 格式的 Lichess 对局、谜题和局面评估数据。
- [lichess-org/chess-openings](https://github.com/lichess-org/chess-openings) - TSV 格式的开局名称、ECO 编码和着法。
- [Lichess Elite Database](https://database.nikonoel.fr) - 筛选出高等级分棋手的 Lichess 对局。
- [Lumbra's GigaBase](https://lumbrasgigabase.com) - 超大型免费棋谱库，涵盖线下和线上对局。
- [FICS Games Database](https://www.ficsgames.org) - 可下载的 FICS 对局存档。
- [TCEC Games](https://github.com/TCEC-Chess/tcecgames) - 历届 TCEC 的对局。
- [Leela Training Data](https://storage.lczero.org/files/training_data/) - Leela Chess Zero 公开的自对弈训练数据。
- [Chess Game Dataset](https://www.kaggle.com/datasets/datasnaek/chess) - Kaggle 上约 2 万盘 Lichess 对局的热门数据集。

## 人工智能与研究

*国际象棋与机器学习交叉领域的论文和项目。*

### 论文

- [AlphaZero](https://arxiv.org/abs/1712.01815) - 通过自对弈和通用强化学习算法掌握国际象棋与将棋。
- [MuZero](https://arxiv.org/abs/1911.08265) - 在 Atari、围棋、国际象棋和将棋中基于学习模型进行规划。
- [Acquisition of Chess Knowledge in AlphaZero](https://arxiv.org/abs/2111.09259) - 对 AlphaZero 所学概念的可解释性研究。
- [Aligning Superhuman AI with Human Behavior](https://arxiv.org/abs/2006.01855) - Maia 论文，研究如何预测人类着法。
- [Grandmaster-Level Chess Without Search](https://arxiv.org/abs/2402.04494) - 不依赖显式搜索、达到特级大师水平的 Transformer。
- [Evidence of Learned Look-Ahead in a Chess-Playing Neural Network](https://arxiv.org/abs/2406.00877) - 对 Leela 策略网络的可解释性研究。
- [ChessGPT](https://arxiv.org/abs/2306.09200) - 连接策略学习与语言模型。

### 项目

- [searchless_chess](https://github.com/google-deepmind/searchless_chess) - DeepMind 无搜索国际象棋的代码及 ChessBench 数据集。
- [Allie](https://github.com/ippolito-cmu/allie) - 与人类对齐、带自适应搜索的国际象棋 Transformer。
- [chess-transformers](https://github.com/sgrvinod/chess-transformers) - 训练 Transformer 下国际象棋。
- [chess_llm_interpretability](https://github.com/adamkarvonen/chess_llm_interpretability) - 探测下棋 GPT 内部的世界模型。
- [Neural Networks for Chess](https://github.com/asdfjkl/neural_network_chess) - 介绍 AlphaZero、Leela 和 NNUE 的免费书籍。
- [pgx](https://github.com/sotetsuk/pgx) - 基于 JAX 的向量化游戏环境（含国际象棋），用于强化学习。

### 大模型评测

- [Kaggle Game Arena](https://www.kaggle.com/game-arena) - 让大语言模型在国际象棋等游戏中对战的评测平台。
- [llm_chess](https://github.com/maxim-saplin/llm_chess) - 评测大模型与随机棋手及彼此对弈的基准。
- [llm-chess-puzzles](https://github.com/kagisearch/llm-chess-puzzles) - 用 Lichess 谜题评测大模型的基准。
- [chess_gpt_eval](https://github.com/adamkarvonen/chess_gpt_eval) - 评测 GPT 类模型与 Stockfish 对弈。

## 计算机视觉

*从图片和视频中识别棋盘和局面。*

- [tensorflow_chessbot](https://github.com/Elucidation/tensorflow_chessbot) - 从棋盘截图预测 FEN。
- [chesscog](https://github.com/georg-wolflein/chesscog) - 从实体棋盘照片识别局面。
- [LiveChess2FEN](https://github.com/davidmallasen/LiveChess2FEN) - 将实体棋盘的实时照片转换为 FEN。
- [fenify-3D](https://github.com/notnil/fenify-3D) - 从真实棋盘照片生成 FEN。
- [CameraChessWeb](https://github.com/Pbatch/CameraChessWeb) - 用摄像头记录线下对局并将 PGN 上传到 Lichess。

## 硬件

*电子棋盘、机器人和 DIY 项目。*

- [DGT](https://www.dgtprojects.com) - 标准比赛用电子棋盘和棋钟。
- [Chessnut](https://www.chessnutech.com) - Chessnut Air 与 Evo 电子棋盘。
- [Certabo](https://www.certabo.com) - RFID 电子棋盘。
- [Square Off](https://squareoffnow.com) - 会自动走子的机器人棋盘。
- [PicoChess](https://github.com/jromang/picochess) - 用树莓派和 DGT 棋盘打造独立的国际象棋电脑。
- [DGTCentaurMods](https://github.com/DGTCentaurMods/DGTCentaurMods) - DGT Centaur 的自定义固件和协议。
- [Play Online Chess with a Real Chess Board](https://github.com/karayaman/Play-online-chess-with-real-chess-board) - 借助摄像头用实体棋盘进行线上对局。
- [Chess-Robot](https://github.com/EDGE-tronics/Chess-Robot) - 基于机械臂、树莓派和 OpenCV 的下棋机器人。

## 引擎评级与赛事

*引擎之间的比较。*

- [CCRL](https://computerchess.org.uk/ccrl/4040/) - 多种用时下的计算机国际象棋评级列表。
- [CEGT](http://www.cegt.net) - CEGT 引擎评级列表。
- [TCEC](https://tcec-chess.com) - 顶级国际象棋引擎锦标赛，最具声望的引擎赛事。
- [Computer Chess Championship](https://www.chess.com/computer-chess-championship) - Chess.com 举办的持续性引擎赛事。
- [SPCC](https://www.sp-cc.de) - Stefan Pohl 的评级列表和 UHO 开局库。

## 格式与协议

*描述对局及与引擎通信的标准。*

- [UCI](https://backscattering.de/chess/uci/) - 通用国际象棋接口，标准的引擎通信协议。
- [CECP](https://www.gnu.org/software/xboard/engine-intf.html) - XBoard/WinBoard 使用的引擎通信协议。
- [PGN](https://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm) - 记录对局的可移植棋谱格式标准。
- [FEN](https://www.chessprogramming.org/Forsyth-Edwards_Notation) - 用一行文本描述局面的 FEN 记法。
- [EPD](https://www.chessprogramming.org/Extended_Position_Description) - 扩展局面描述，常用于测试集。
- [Polyglot Book Format](http://hgm.nubati.net/book_format.html) - Polyglot 开局库格式规范。
- [Algebraic Notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) - 记录着法的标准代数记谱法。
- [ICCF Numeric Notation](https://en.wikipedia.org/wiki/ICCF_numeric_notation) - 通讯棋使用的与语言无关的数字记谱法。
- [Descriptive Notation](https://en.wikipedia.org/wiki/Descriptive_notation) - 历史上的英语/西班牙语描述记谱法。
- [Perft Results](https://www.chessprogramming.org/Perft_Results) - 用于校验着法生成器的参考节点数。

## 学习国际象棋编程

*面向引擎作者的指南、教程和社区。*

- [Chess Programming Wiki](https://www.chessprogramming.org) - 计算机国际象棋百科全书，建议从[入门页面](https://www.chessprogramming.org/Getting_Started)开始。
- [TalkChess](https://talkchess.com) - 引擎开发者的主要论坛。
- [Coding Adventure: Chess](https://www.youtube.com/watch?v=U4ogK0MIzqk) - Sebastian Lague 用 C# 编写国际象棋引擎（[续集](https://www.youtube.com/watch?v=_vqlIPDR2TU)）。
- [Bitboard Chess Engine in C](https://www.youtube.com/watch?v=QUNP-UjujBM) - Code Monkey King 从零编写 BBC 引擎的视频系列（[代码](https://github.com/maksimKorzh/bbc)）。
- [VICE](https://github.com/bluefeversoft/vice) - 经典 VICE 视频教程系列的代码。
- [Rustic](https://rustic-chess.org) - 记录 Rustic 引擎构建过程的在线书籍。
- [CPW-Engine](https://github.com/nescitus/cpw-engine) - 为国际象棋编程维基编写的教学引擎。
- [TSCP](https://tckerrigan.com/Chess/TSCP/) - Tom Kerrigan 的简单国际象棋程序，经典学习材料。
- [Stockfish Docs](https://official-stockfish.github.io/docs/stockfish-wiki/Home.html) - Stockfish 官方文档，涵盖选项、编译和开发。
- [NNUE Explained](https://official-stockfish.github.io/docs/nnue-pytorch-wiki/docs/nnue.html) - 深入讲解 NNUE 架构和训练。

## 相关清单

*你可能也会喜欢的其他精选清单。*

- [Awesome](https://github.com/sindresorhus/awesome#readme) - Awesome 清单的清单。
- [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning#readme) - 机器学习框架、库和软件。
