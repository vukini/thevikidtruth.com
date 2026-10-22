"""Assign a `topics:` category to wiki pages in each knowledge-base section.

Only the front matter is touched; page bodies are copied byte-for-byte.
Category metadata (titles, colours, intros) lives in data/topics/<section>.yaml.
Computing has its own script (categorise_computing.py). Substack posts in
content/writing/ are never touched by this script.
Usage: python3 scripts/categorise.py [section ...]
"""
import re, sys, pathlib

M = {
"mathematics": {
 "foundations": "03xxmathematicallogicandfoundations abstraction logic modusponens modustolens reflexivityrelation symmetryrelation transitivityrelation setrelations settheory thefoundationofmath zf categorytheory",
 "algebra": "abstractalgebra commutativerings fields group groups modulesalegbra multivariablepolynomialrings quotientgroups rings exterioralgebras",
 "linear-algebra": "affinetransformation innerproductspaces linearalgebra linearoperators tensors vectorspaces",
 "numbers-geometry": "numbertheory pythagoras topology dynamics 05xxcombinatorics",
 "math-physics": "qm relativity mathoncomputers",
 "overview": "00xxgeneral 01xxhistoryandbiography math mathmap",
},
"science": {
 "physics": "physics thelawsofphysics standardmodel electromagnetictheory energy",
 "life": "anatomy biology medicine psychology",
 "earth-society": "climate science networks",
},
"philosophy": {
 "philosophers": "aldoushuxely epicurus friedrichnietzsche jeremybentham jordanbpeterson ludwigamemoir ludwigwittgenstein richardrorty sentsan thalesofmiletos",
 "ideas": "ethics philosophicalterms rubric teleology",
 "physics": "philosophyinphysics philosophersofphysics",
 "overview": "philosophy philosophers2study",
},
"music": {
 "guitar": "guitar guitarchords guitarpractice guitartheory guitartutorials jazzguitar learnthefretboard openchords1 practicelessplaymore ukelele",
 "theory": "chordprogressions dmajor melodies musicalalphabet musicalkeys musictheory scales solfege triads",
 "songs": "aguadeestrellas amazinggrace amilliondreams babycaniholdyou elenorrigby eskawatakayway godrestyoumerrygentlemen lastkiss perfectedsheeran riptide threelittlebirds waterblessing songs2learn",
 "listening": "music playlist musicsoftware panflute",
},
"languages": {
 "spanish": "spanish advertencia numerales frases synergyspanish questions essence manipulation havingpossession apendicomaestro spanishvocab1 frasesenespa-ol lafamiliademaria nocashflow sparticle enbrasil2009 elfestivalwesak2019 afirmacionescientificasparalacuration spsongs lanegra spanishvideos",
 "french": "french frenchvocabulary italkicommunity1 mychildhood dezeroaun thekingssecret foundationsedge medicalinformationform",
 "esperanto": "esperanto learnesperanto uem unuaparto bonvenon esperantoscripts mornings1 spiritualwakeup citiloj esperantovortoj vortaro artikoloj suno tertremo egipto insulodelarozoj maldol-a-okolado trompoprovoj esperantolegajo daodejing bibilio verdabibilio sidarto launuaintervjuo lakvaraintervjuo picolispinstallation",
 "tokipona": "tokipona tokiponavocab",
 "swahili": "swahili sw101 swgrammar001 swvocab001 swphrases101 swreading101 swtext",
 "arabic": "arabic arabizi",
 "japanese": "japanese jpcolors",
 "hindi": "hindi",
 "mandarin": "mandrin",
 "learning": "languages howtolearnlanguages",
 "multilingual": "multilingual whatisdifficult timeinaday wakeupearly laruseducerf",
},
"essays": {
 "science": "afterphysics everettpicture hips hips1 hips6 pastandfuture pasthypo physicsandchance physicsandnarrative primitiveontology qmforthinkers quantummechandeveryday quantumreality thejazz understanding understandingtheuniverse worlddoesnotexist designinnature theinvisiblepyramid mapsoftime programmingtheuniverse theroadtoreality thephilosophyofphysics rogerpenrose immense acrackincreation yourbrainonparasites luewhat",
 "math-tech": "abookofsettheory anelementaryintroductiontothetheoryofprobablility anoutlineofsettheory anintroductiontothelanguageofcategorytheory basiccategorytheory burnmathclass divgradcurl graphtheoryasihaveknownit mathforphys nonlineardynamicsandchaos linearity scalefreenetwork linked afirstcourseinnetworktheory whichnumbersarereal cinanutshell expertcprogramming buildingmachinelearningsystemswithpython hackershandbook livelessons letoverlambda linuxadminhandbook linuxusbstack programminglinuxhackertoolsuncovered makingmusicwithcomputers principlesofpowersystems hetromation youarenotagadget thecsdetective significables",
 "society": "aconflictofvisions adultsintheroom capitalmarkets commodity cryptocurrencies dictators economics econpiketty fiat finance freemarkets generationzero gold magnacarta politics secretsofthetemple signals swarmwise theprize therighteousmind theupsideofinequality timepreference whatisconservatism worldstats thevalueweb thecontenttrap whyinformationgrows georgeorwell theroadtowiganpier ordinarymen shigerumizukishitler history halflifeoffacts homodeus",
 "spirit": "advaita atha breathwork doorsofperception holdingmybreath integralmeditation meditation rajayoga spiritual spritualnotes1 theyogasutras ugkrishnamurti thegnosticgospels n-odhana magik",
 "mind": "health stretchingscientifically whyeatingtoomuch selfhelp managment learning memorizeeverything thememorychalet thinking artthinking mapsofmeaning iamastrangeloop prometheusrising",
 "stories": "jaya krishna olympus sita immortality independence starwars wilderpeople where2invadenext scifi acanticleforliebowitz metamorphosis safeareagorazde renaissancemasters theplagueoffantasies thesilvereye louderthanwords playitagain videos themarvelousclouds",
 "notebook": "amibeingtoosubtle articles books booktemplate favourites glossary quotes vocab schadenfreude sclerotic environmentsanchor kidszone misc summingitup thephilosophybook thethirdplate",
},
}
root = pathlib.Path(__file__).resolve().parent.parent / "content"
for sec in (sys.argv[1:] or M):
    assert sec != "writing", "Substack posts are never edited"
    slug2cat = {s: c for c, ss in M[sec].items() for s in ss.split()}
    missing, n = [], 0
    for f in sorted((root / sec).glob("*.md")):
        if f.name == "_index.md": continue
        c = slug2cat.get(f.stem)
        if not c:
            if not re.search(r"(?m)^draft:\s*true", f.read_text()): missing.append(f.stem)
            continue
        t = f.read_text()
        fm_end = t.index("\n---", 3)
        fm = re.sub(r"(?m)^topics:.*\n(?:- .*\n)*", "", t[:fm_end + 1])
        new = fm.rstrip("\n") + f"\ntopics:\n- {c}\n" + t[fm_end + 1:]
        if new != t: f.write_text(new); n += 1
    print(sec, "updated", n, "unmapped public:", missing)
