import requests
from bs4 import BeautifulSoup

url = "https://coddy.tech"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

a=soup.find_all("a")
for i,item in enumerate(a):
    print(i+1,item.get_text(),"->",item["href"])
    print("\n")



'''output
2 Try HTML + CSS in the playground -> /playground/html


3 Learn -> /landing/html


4 Try JavaScript in the playground -> /playground/javascript


5 Learn -> /landing/javascript


6 Try Python in the playground -> /playground/python


7 Learn -> /landing/python


8 Try C++ in the playground -> /playground/cpp


9 Learn -> /landing/cpp


10 Try C in the playground -> /playground/c


11 Learn -> /landing/c


12 Try SQL in the playground -> /playground/sql


13 Learn -> /landing/sql


14 Learn -> /landing/css


15 Try C# in the playground -> /playground/csharp


16 Learn -> /landing/csharp


17 Try Java in the playground -> /playground/java


18 Learn -> /landing/java


19 Try GO in the playground -> /playground/golang


20 Learn -> /landing/go


21 Try PHP in the playground -> /playground/php


22 Learn -> /landing/php


23 Try R in the playground -> /playground/r


24 Learn -> /landing/r


25 Try Dart in the playground -> /playground/dart


26 Learn -> /landing/dart


27 Try Rust in the playground -> /playground/rust


28 Learn -> /landing/rust


29 Try Lua in the playground -> /playground/lua


30 Learn -> /landing/lua


31 Try Ruby in the playground -> /playground/ruby


32 Learn -> /landing/ruby


33 Try Swift in the playground -> /playground/swift


34 Learn -> /landing/swift


35 Try Verilog in the playground -> /playground/verilog


36 Learn -> /landing/verilog


37 Learn -> /landing/prompts


38 Try Terminal in the playground -> /playground/terminal


39 Learn -> /landing/terminal


40 Try TypeScript in the playground -> /playground/typescript


41 Learn -> /landing/typescript


42 Learn -> /landing/git


43 Learn -> /landing/docker


44 all courses -> /landing


45 BlogTutorials, guides, and stories from the Coddy team. -> /blog


46 DocsReference documentation for every supported language. -> /docs


47 PlaygroundWrite and run code in the browser, no setup required. -> /playground/python


48 AI AssistantPersonal AI tutor that explains code, debugs errors, and gives hints. -> /ai_assistant


49 ToolsFree utilities for developers - formatters, converters, and more. -> /tools


50 Embed EditorAdd a free, runnable code editor to your own site with one iframe. -> /embed


51 Cheat SheetsQuick-reference tables for the languages and tools you use. -> /cheat-sheets


52 CertificationsEarn shareable certificates by completing courses. -> /certifications


53 AboutLearn what Coddy is and the team behind it. -> /about


54 ContactGet in touch with support, partnerships, or press. -> /contact


55 PressLogos, brand colors, founder bios, and press contact. -> /press


56 CareersOpen roles, our mission, and what it’s like to work at Coddy. -> /careers


57 BusinessesCoddy for teams - onboard, train, and track engineers. -> /teams


58 AffiliatePromote Coddy and earn commissions on referrals. -> /affiliate


59 Coddy BuildBuild full-stack apps with AI - chat, preview, and publish. -> https://coddy.tech/build


60 START LEARNING -> /onboard


61 GET STARTED -> /onboard


62 I ALREADY HAVE AN ACCOUNT -> /login?l=1


63 ★4.9App Store(1K+) -> https://apps.apple.com/app/id6755648162


64 ★4.8Google Play(5K+) -> https://play.google.com/store/apps/details?id=tech.coddy.coddyapp


65 Python -> /landing/python


66 JavaScript -> /landing/javascript


67 TypeScript -> /landing/typescript


68 HTML -> /landing/html


69 CSS -> /landing/css


70 Java -> /landing/java


71 C++ -> /landing/cpp


72 SQL -> /landing/sql


73 C -> /landing/c


74 C# -> /landing/csharp


75 PHP -> /landing/php


76 Dart -> /landing/dart


77 Golang -> /landing/go


78 R -> /landing/r


79 Rust -> /landing/rust


80 Lua -> /landing/lua


81 Ruby -> /landing/ruby


82 Swift -> /landing/swift


83 Verilog -> /landing/verilog


84 AI Prompts -> /landing/prompts


85 Terminal -> /landing/terminal


86 Git -> /landing/git


87 Docker -> /landing/docker


88 Python -> /landing/python


89 JavaScript -> /landing/javascript


90 TypeScript -> /landing/typescript


91 HTML -> /landing/html


92 CSS -> /landing/css


93 Java -> /landing/java


94 C++ -> /landing/cpp


95 SQL -> /landing/sql


96 C -> /landing/c


97 C# -> /landing/csharp


98 PHP -> /landing/php


99 Dart -> /landing/dart


100 Golang -> /landing/go


101 R -> /landing/r


102 Rust -> /landing/rust


103 Lua -> /landing/lua


104 Ruby -> /landing/ruby


105 Swift -> /landing/swift


106 Verilog -> /landing/verilog


107 AI Prompts -> /landing/prompts


108 Terminal -> /landing/terminal


109 Git -> /landing/git


110 Docker -> /landing/docker


111 Python -> /landing/python


112 JavaScript -> /landing/javascript


113 TypeScript -> /landing/typescript


114 HTML -> /landing/html


115 CSS -> /landing/css


116 Java -> /landing/java


117 C++ -> /landing/cpp


118 SQL -> /landing/sql


119 C -> /landing/c


120 C# -> /landing/csharp


121 PHP -> /landing/php


122 Dart -> /landing/dart


123 Golang -> /landing/go


124 R -> /landing/r


125 Rust -> /landing/rust


126 Lua -> /landing/lua


127 Ruby -> /landing/ruby


128 Swift -> /landing/swift


129 Verilog -> /landing/verilog


130 AI Prompts -> /landing/prompts


131 Terminal -> /landing/terminal


132 Git -> /landing/git


133 Docker -> /landing/docker


134 See all courses → -> /landing


135 GET STARTED -> /onboard


136 Home -> /


137 About -> /about


138 Affiliate -> /affiliate


139 Businesses -> /teams


140 Press -> /press


141 Careers -> /careers


142 Coddy Build -> https://coddy.tech/build


143  -> https://www.instagram.com/coddy.tech/


144  -> https://www.facebook.com/coddylearn


145  -> https://www.linkedin.com/company/coddy-tech


146  -> https://www.tiktok.com/@coddy.tech


147  -> https://x.com/coddy_tech


148  -> https://www.youtube.com/@coddytech


149 All Courses -> /landing


150 Mobile App -> /apps


151 Blog -> /blog


152 Certifications -> /certifications


153 Reference -> /docs


154 Playground -> /playground/python


155 Tools -> /tools


156 Embed Editor -> /embed


157 Cheat Sheets -> /cheat-sheets


158 AI Assistant -> /ai_assistant


159 Contact -> /contact


160 FAQs -> /faqs


161 Python -> /landing/python


162 JavaScript -> /landing/javascript


163 TypeScript -> /landing/typescript


164 Java -> /landing/java


165 C++ -> /landing/cpp


166 C# -> /landing/csharp


167 SQL -> /landing/sql


168 HTML -> /landing/html


169 CSS -> /landing/css


170 C -> /landing/c


171 Golang -> /landing/go


172 PHP -> /landing/php


173 R -> /landing/r


174 Dart -> /landing/dart


175 Rust -> /landing/rust


176 Lua -> /landing/lua


177 Git -> /landing/git


178 Docker -> /landing/docker


179 Python -> /playground/python


180 JavaScript -> /playground/javascript


181 Java -> /playground/java


182 TypeScript -> /playground/typescript


183 C++ -> /playground/cpp


184 C -> /playground/c


185 C# -> /playground/csharp


186 SQL -> /playground/sql


187 Python -> /certification/python


188 JavaScript -> /certification/javascript


189 Java -> /certification/java


190 C++ -> /certification/cpp


191 C# -> /certification/csharp


192 SQL -> /certification/sqlite


193 HTML & CSS -> /certification/html


194 Go -> /certification/go


195 Rust -> /certification/rust


196 PHP -> /certification/php


197 JSON Formatter -> /tools/json-formatter


198 SQL Formatter -> /tools/sql-formatter


199 Regex Tester -> /tools/regex-tester


200 Markdown Editor -> /tools/markdown-editor


201 Base64 Encoder -> /tools/base64


202 URL Encoder -> /tools/url-encoder


203 JWT Decoder -> /tools/jwt-decoder


204 Diff Checker -> /tools/diff-checker


205 Browse all docs -> /docs


206 Python -> /docs/python


207 JavaScript -> /docs/javascript


208 Latest posts -> /blog


209 Software Development -> /blog/tag/software-development


210 Comparison -> /blog/tag/comparison


211 Privacy Policy -> /privacy


212 Terms -> /terms


213 Sitemap -> https://coddy.tech/sitemap.xml


214 Attributions -> /attributions  '''