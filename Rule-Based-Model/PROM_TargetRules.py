#
# List of target rules for nlp model

from medspacy.ner import TargetRule, TargetMatcher

target_rules = [
        # Oswestry
        TargetRule(literal="Oswestry", category="PROM-Measure", 
                   pattern=[
                       {"LOWER": {"in":['oswestry','odi']}}
                           ],
                   attributes={"measureType":"ODI"}
                  ),

        # Brief Pain Inventory
        TargetRule(literal="Brief Pain Inventory", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['bpi','bpisf']}}
                           ],
                  attributes={"measureType":"BPI"}
                  ),

        TargetRule(literal="Brief Pain Inventory", category="PROM-Measure", 
                   pattern=[
                            {"LOWER":"brief"},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"}, # This is needed to match optional space characters between words to account for line breaks
                           {"LOWER":{"IN":["pain","pn"]}},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                           {"LOWER":{"IN":["inventory","inv"]}}
                           ],
                  attributes={"measureType":"BPI"}
                  ),

        # PEG-3
        TargetRule(literal="Pain, Enjoyment, General Activity Scale", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['peg','peg3','peg 3']}}],
                  attributes={"measureType":"PEG"}
                  ),
        TargetRule(literal="Pain, Enjoyment, General Activity Scale", category="PROM-Measure", 
                   pattern=[
                           {"LOWER": {"IN":['pain','pn']}},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                           {"LOWER":"enjoyment"},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                           {"LOWER":"general"}
                   ],
                  attributes={"measureType":"PEG"}
                  ),   
        TargetRule(literal="Pain, Enjoyment, General Activity Scale", category="PROM-Measure", 
                   pattern=[
                           {"LOWER": {"IN":['pain','pn']}},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                           {"LOWER":"enjoyment"},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                           {"LOWER":"of"},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                           {"LOWER":"life"},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                           {"LOWER":"general"}
                   ],
                  attributes={"measureType":"PEG"}
                  ),   

        # Pain Disability Index
        TargetRule(literal="Pain Disability Index", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['pdi']}}],
                  attributes={"measureType":"PDI"}
                  ),
        TargetRule(literal="Pain Disability Index", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['pain','pn']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":['disability','dis']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                             {"LOWER": {"IN":['index','ind','in']}}],
                  attributes={"measureType":"PDI"}
                  ),
    
        # Pain Disability Questionnaire
        TargetRule(literal="Pain Disability Questionnaire", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['pdq']}}],
                  attributes={"measureType":"PDQ"}
                  ),
        TargetRule(literal="Pain Disability Questionnaire", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['pain','pn']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":['disability','dis']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                             {"LOWER": {"IN":["questionnaire","q","quest","ques","question"]}}],
                  attributes={"measureType":"PDQ"}
                  ),

        # DVPRS
        TargetRule(literal="DVPRS", category="PROM-Measure", 
                   pattern=[{"LOWER": "dvprs"},
                           ],
                  attributes={"measureType":"DVPRS"}
                  ),
        TargetRule(literal="DVPRS", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["defense","def"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": "and"},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["veterans","vets","vet"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": "rating"},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["scale","score"]}},
                           ],
                  attributes={"measureType":"DVPRS"}
                  ),
        TargetRule(literal="DVPRS", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["defense","def"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["veterans","vets","vet"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": "rating"},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["scale","score"]}},
                           ],
                  attributes={"measureType":"DVPRS"}
                  ),  
        TargetRule(literal="DVPRS", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["defense","def"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": "and"},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["veterans","vets","vet"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["scale","score"]}},
                           ],
                  attributes={"measureType":"DVPRS"}
                  ),

        TargetRule(literal="DVPRS", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["defense","def"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["veterans","vets","vet"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["scale","score"]}},
                           ],
                  attributes={"measureType":"DVPRS"}
                  ),

        # CPG Questionnaire
        TargetRule(literal="Chronic Pain Grade", category="PROM-Measure", 
                   pattern=[{"LOWER": "cpg"},
                           ],
                  attributes={"measureType":"CPG"}
                  ),
        TargetRule(literal="Chronic Pain Grade", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["chronic","chron","chrn","chronc","chrnic","chornic","chonric","chr"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["grade","grd"]}},
                           ],
                  attributes={"measureType":"CPG"}
                  ),

        # WHY Multidim Pain
        TargetRule(literal="Multidimensional Pain Inventory", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["whymdpi","mdpi","mpi"]}},
                           ],
                  attributes={"measureType":"MDPI"}
                  ),
        TargetRule(literal="Multidimensional Pain Inventory", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["multidimensional","multidim"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["inventory","inv","in","index"]}},
                           ],
                  attributes={"measureType":"MDPI"}
                  ),
        TargetRule(literal="Multidimensional Pain Inventory", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["multi","multi"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["dimensional","dim"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["inventory","inv","in","index"]}},
                           ],
                  attributes={"measureType":"MDPI"}
                  ),

        # short form
        TargetRule(literal="Short Form", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["sf36","sf12","shortform"]}},
                           ],
                  attributes={"measureType":"ShortForm"}
                  ),
        TargetRule(literal="Short Form", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["short","sh","shrt","s"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["form","frm","f"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LIKE_NUM":True},
                           ],
                  attributes={"measureType":"ShortForm"}
                  ),
        TargetRule(literal="Short Form", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["shortform","sf"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LIKE_NUM":True},
                           ],
                  attributes={"measureType":"ShortForm"}
                  ),
        TargetRule(literal="Short Form", category="PROM-Measure", 
                   pattern=[{"TEXT": {"REGEX":"^(?i)sf[0-9][0-9]"}}
                           ],
                  attributes={"measureType":"ShortForm"}
                  ),

        # Pain Global Rating of Change/Patient Global Impression of Change
        TargetRule(literal="Pain Global Rating of Change", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["pgcr","pgc","pgrc","pgroc","pgic"]}},
                           ],
                  attributes={"measureType":"PGRC"}
                  ),
        TargetRule(literal="Pain Global Rating of Change", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["pain","pn","patient","patients"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["global","glob"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["rating","impression","imp"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["of"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["change","chg"]}},
                           ],
                  attributes={"measureType":"PGRC"}
                  ),
        TargetRule(literal="Pain Global Rating of Change", category="PROM-Measure", 
                   pattern=[
                            {"LOWER": {"IN":["global","glob"]}},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["rating","imp","impression"]}},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["of"]}},
                           {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["change","chg"]}},
                           ],
                  attributes={"measureType":"PGRC"}
                  ),
        TargetRule(literal="Pain Global Rating of Change", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["pain","pn","patient","patients"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["global","glob"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["change","chg"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["rating","imp","impression"]}},
                           ],
                  attributes={"measureType":"PGRC"}
                  ),
        TargetRule(literal="Pain Global Rating of Change", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["global","glob"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["pain","pn","patient","patients"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["rating","impression","imp"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["of"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["change","chg"]}},
                           ],
                  attributes={"measureType":"PGRC"}
                  ),

        # PROMIS Measures
        TargetRule(literal="PROMIS", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["promis"]}},

                           ],
                  attributes={"measureType":"PROMIS"}
                  ),
        TargetRule(literal="PROMIS", category="PROM-Measure", 
                   pattern=[{"TEXT": {"REGEX":"^(?i)promis[0-9][0-9]?[a-z]?"}}
                           ],
                  attributes={"measureType":"PROMIS"}
                  ),

        # Roland Morris
        TargetRule(literal="Roland Morris Disability Questionnaire", category="PROM-Measure", 
                   pattern=[{"TEXT": {"REGEX":"^(?i)rmd[q]?"}}
                           ],
                  attributes={"measureType":"RMDQ"}
                  ),
        TargetRule(literal="Roland Morris Disability Questionnaire", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["roland","rolland","r"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["morris","moris","moriss","m"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["disability","dis"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["questionnaire","q","quest","ques","question"]}},
                           ],
                  attributes={"measureType":"RMDQ"}
                  ),
        TargetRule(literal="Roland Morris Disability Questionnaire", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["roland","rolland"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["morris","moris","moriss"]}},
                           ],
                  attributes={"measureType":"RMDQ"}
                  ),
        TargetRule(literal="Roland Morris Disability Questionnaire", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["rm"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["disability","dis"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["questionnaire","q","quest","ques","question"]}},
                           ],
                  attributes={"measureType":"RMDQ"}
                  ),
        TargetRule(literal="Roland Morris Disability Questionnaire", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["rm"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["disability","dis"]}},
                           ],
                  attributes={"measureType":"RMDQ"}
                  ),

        # Bournemouth Questionnaire (neck and low back)
        TargetRule(literal="Bournemouth", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["bournemouth","bbq","nbq"]}}, # I know this is susceptible to noise
                           ],
                  attributes={"measureType":"Bournemouth"}
                  ),
        TargetRule(literal="Bournemouth", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["back","neck"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["bournemouth","bourenmouth","bournmouth","bournmouthe","bournemouthe"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["questionnaire","q","quest","ques","question"]}},
                           ],
                  attributes={"measureType":"Bournemouth"}
                  ),
        TargetRule(literal="Bournemouth", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["bournemouth","bourenmouth","bournmouth","bournmouthe","bournemouthe"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["back","neck"]}},
                           ],
                  attributes={"measureType":"Bournemouth"}
                  ),
        TargetRule(literal="Bournemouth", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["back","neck"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["bournemouth","bourenmouth","bournmouth","bournmouthe","bournemouthe"]}},
                           ],
                  attributes={"measureType":"Bournemouth"}
                  ),
        TargetRule(literal="Bournemouth", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["bournemouth","bourenmouth","bournmouth","bournmouthe","bournemouthe"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["questionnaire","q","quest","ques","question"]}},
                           ],
                  attributes={"measureType":"Bournemouth"}
                  ),

        # Patient Specific Functional Scale
        TargetRule(literal="Patient Specific Functional Scale", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["psfs","pfs"]}},
                           ],
                  attributes={"measureType":"PSFS"}
                  ),
        TargetRule(literal="Patient Specific Functional Scale", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["patient","pt"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["specific","sp"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["functional","function","func","fun"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["scale","sc"]}},
                           ],
                  attributes={"measureType":"PSFS"}
                  ),
        TargetRule(literal="Patient Specific Functional Scale", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["patient","pt"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["functional","function","func","fun"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["scale","sc"]}},
                           ],
                  attributes={"measureType":"PSFS"}
                  ),

        # Keele Start back
        TargetRule(literal="Start Back", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["ksbs"]}},
                           ],
                  attributes={"measureType":"StartBack"}
                  ),
        TargetRule(literal="Start Back", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["start","st"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["back"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["screening","tool","questionnaire","scale"]}},
                           ],
                  attributes={"measureType":"StartBack"}
                  ),
        TargetRule(literal="Start Back", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["keele"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["start","st"]}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":["back"]}},
                           ],
                  attributes={"measureType":"StartBack"}
                  ),

        # Neck Disability Index or Neck Pain Disability Index
        TargetRule(literal="Neck Disability Index", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":["ndi","npdi"]}},
                           ],
                  attributes={"measureType":"NDI"}
                  ),
        TargetRule(literal="Neck Disability Index", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['neck']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":['disability','dis']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                             {"LOWER": {"IN":['index','ind','in']}}],
                  attributes={"measureType":"NDI"}
                  ),
        TargetRule(literal="Neck Disability Index", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['neck']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":['pain','pn']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":['disability','dis']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                             {"LOWER": {"IN":['index','ind','in']}}],
                  attributes={"measureType":"NDI"}
                  ),
        
        # Functional Rating Index/Scale (will not do a lowercase abbreviation because fri = friday)
        TargetRule(literal="Functional Rating Index", category="PROM-Measure", 
                   pattern=[{"LOWER": {"FUZZY":{"IN":['functional','func','function']}}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":['rating']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                             {"LOWER": {"IN":['index','ind','in','scale','scl']}}],
                  attributes={"measureType":"FRI"}
                  ),

        # Tampa Kinesiophobia Scale (Also will not add lowercase abbreviation, not specific)
        TargetRule(literal="Tampa Scale of Kinesiophobia", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['tampa']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"FUZZY":{"IN":['kinesiophobia']}}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                             {"LOWER": {"IN":['index','ind','in','scale','scl','score']}}],
                  attributes={"measureType":"TampaScale"}
                  ),
            TargetRule(literal="Tampa Scale of Kinesiophobia", category="PROM-Measure", 
                   pattern=[{"LOWER": {"IN":['tampa']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN":['index','ind','in','scale','scl','score']}},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"IN": ['of','for']},"OP":"?"},
                            {"LOWER": {"REGEX": "\s*"},"OP":"?"},
                            {"LOWER": {"FUZZY":{"IN":['kinesiophobia']}}}],
                  attributes={"measureType":"TampaScale"}
                  ),

    ]
