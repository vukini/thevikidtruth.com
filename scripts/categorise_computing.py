"""One-off: assign a `topics` category to every page in content/computing/."""
import re, pathlib
M = {
 "lisp": "picolisp pilasm pildb piltutorials plbox plio plnew pltutorial pilmachine pilchat pilhealth pillife pilnumbers pilquote pilsource picolispbyexample pilexamplesexamined findboxes withoutputtostring cardocar cdrdocdr carstylefn commonlisp clfunctions scheme racket r6rs emacslisp asml httpl subrl applyc balancec bigc extc flowc gcc htc httpgatec ioc lat1c mainc netc picoh sslc startc subrc symc tabc utf2c mkvers versh pmap upd simplyarrayarithmetic",
 "c-systems": "systemsprogramming 32bitcsource 64bitasmsource assemblylanguage cchars cfloats cints cops cprogramming cstandardlibrary cstrings csytanx gbddebugger identifier literals object storagelinkage tokens trigraphs digraphs unicodeinc rust ziglang odin vlang thecompiler makefile objdump",
 "javascript": "javascript jscontrolflow jsdatatypes jsevents jsfunctions jsobjects jsprototypalinheritance jsscope jsthree js3makingshapes jsvariable jskata nodejs",
 "python": "python pykeywords ipython numpy scipy intropygame pythonspacy pythonlibrariestoolsandlinks",
 "functional": "functional haskell haskellkata purescript lambdacalculus",
 "other-languages": "computerlanguages cuissmalltalk cuisterseguide gnusmalltalk pharo learnpharo objectsandmessagespharo forth fortran julia unity",
 "linux": "linux archlinux bash bashcase bashif bashreservewords bashvariables vikidsbashcookbook awk linuxinstrospection linuxprocessesandmemory linuxtools linuxtoolsandsoftware thelinuxprocessmanager simplelinuxconfig systemd pacman ncdu nmtui xrandr i3 burniso ubuntucommontask displaymodesandvirtualconsoles filesanddirectories regularexpressions regexplibrary keyboardconfig kmonad penti",
 "os-hardware": "os virtualization modernoperatingsystems theminixbook windows windowswsl apple coolhardware rasberrypi intelcpuarchitecture binary bciyh virtualbox vagrant datarecovery",
 "security": "computersecurity linuxsecurity firewalls applicationproxy circuitlevelfirewall ngfirewall packetfilteringfirewall statefullfirewall statelessfirewall arppoisoning dnspoisoning ettercap exploitation internetexploitation metasploit penetrationtesting wifipenetration malwaretypes honeypots idsips forensics encryption rainbowtables enumeration securenetworkarchitecture securingwebapps securityprogram icssecurity",
 "networking-web": "networking ipdatagrams ipv6 datagramencapsulation tls sshlogin telnetemail zncserver linode onlinevps seedbox webdevelopment appdev dropbox",
 "cs-theory": "computerscience algorithms datastructuresandalgorithms stacks databases machinelearning opendatascience krep",
 "tools": "git emacs emacsnotes dotemacs initorg vim vikidvim gotolinevim",
 "reading": "computingvideosandarticles webdevelopmentreadinglist learningonline computerstudyplan becomingaguru guru computingfreedom funkytechnology computing",
}
slug2cat = {s: c for c, ss in M.items() for s in ss.split()}
d = pathlib.Path(__file__).resolve().parent.parent / "content/computing"
missing = []
for f in sorted(d.glob("*.md")):
    if f.name == "_index.md": continue
    c = slug2cat.get(f.stem)
    if not c: missing.append(f.stem); continue
    t = f.read_text()
    fm_end = t.index("\n---", 3)
    fm = re.sub(r"(?m)^topics:.*\n(?:- .*\n)*", "", t[:fm_end + 1])
    fm = fm.rstrip("\n") + f"\ntopics:\n- {c}\n"
    f.write_text(fm + t[fm_end + 1:])
print("unmapped:", missing)
