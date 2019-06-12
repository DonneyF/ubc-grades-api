stats_cat = ["average", "stdev", "high", "low", "pass", "fail", "withdrew", "audit", "other"]
grades_cat = ["0-9%", "10-19%", "20-29%", "30-39%", "40-49%", "<50%", "50-54%", "55-59%", "60-63%", "64-67%", "68-71%", "72-75%", "76-79%", "80-84%", "85-89%", "90-100%"]
yearsessions = ["1996S", "1996W", "1997S", "1997W", "1998S", "1998W", "1999S", "1999W", "2000S", "2000W", "2001S", "2001W", "2002S", "2002W", "2003S", "2003W", "2004S", "2004W", "2005S", "2005W", "2006S", "2006W", "2007S", "2007W", "2008S", "2008W", "2009S", "2009W", "2010S", "2010W", "2011S", "2011W", "2012S", "2012W", "2013S", "2013W", "2014S", "2014W", "2015S", "2015W", "2016S", "2016W", "2017S", "2017W", "2018S", "2018W"]
subjects = ["AANB", "ACAM", "ADED", "ADHE", "AFST", "AGEC", "AGRO", "AGSC", "ANAE", "ANAT", "ANSC", "ANTH", "APBI", "APPP", "APSC", "ARBC", "ARCH", "ARCL", "ARST", "ARTE", "ARTH", "ARTS", "ASIA", "ASIC", "ASTR", "ASTU", "ATSC", "AUDI", "BA", "BAAC", "BABS", "BAEN", "BAFI", "BAHC", "BAHR", "BAIM", "BAIT", "BALA", "BAMA", "BAMS", "BAPA", "BASC", "BASD", "BASM", "BATL", "BATM", "BAUL", "BIOC", "BIOE", "BIOF", "BIOL", "BMEG", "BOTA", "BRDG", "BUED", "BUSI", "CAPS", "CCFI", "CCST", "CDSC", "CDST", "CEEN", "CELL", "CENS", "CHBE", "CHEM", "CHIL", "CHIN", "CHML", "CICS", "CIVL", "CLCH", "CLST", "CNPS", "CNRS", "CNTO", "COEC", "COGS", "COHR", "COML", "COMM", "COMR", "CONS", "CPEN", "CPSC", "CRWR", "CSED", "CSIS", "CSPW", "CUST", "DANI", "DENT", "DERM", "DHYG", "DMED", "DPAS", "DRAM", "DSCI", "EADM", "ECED", "ECON", "EDCI", "EDCP", "EDST", "EDUC", "EECE", "ELEC", "EMBA", "EMER", "ENDS", "ENED", "ENGL", "ENPH", "ENVR", "EOSC", "EPSE", "ERTH", "ETEC", "EXCH", "FACT", "FDNS", "FEBC", "FHIS", "FILM", "FINA", "FIPR", "FISH", "FIST", "FMED", "FMPR", "FMSC", "FMST", "FNEL", "FNH", "FNIS", "FNLG", "FNSP", "FOOD", "FOPR", "FPEN", "FRE", "FREN", "FRSI", "FRST", "GBPR", "GEM", "GENE", "GEOB", "GEOG", "GEOL", "GEOP", "GEPA", "GERM", "GPP", "GREK", "GRS", "GRSJ", "GSAT", "HCEC", "HCEP", "HCET", "HEBR", "HECO", "HESO", "HGSE", "HIED", "HIND", "HINU", "HIST", "HKIN", "HMEC", "HMED", "HPB", "HUNU", "HXAH", "HXDR", "HXEC", "HXEN", "HXFL", "HXFR", "HXGM", "HXGY", "HXHI", "HXMA", "HXMU", "HXPC", "HXPH", "HXPS", "HXPY", "HXRE", "HXSP", "HXWR", "IAR", "IEST", "IGEN", "IHHS", "INDE", "INDO", "INDS", "INFO", "INLB", "ISCI", "ITAL", "ITST", "IWME", "JAPN", "JRNL", "KIN", "KORN", "LAIS", "LANE", "LARC", "LASO", "LAST", "LATN", "LAW", "LFS", "LIBE", "LIBR", "LING", "LLED", "LWS", "MAED", "MATH", "MDVL", "MECH", "MEDD", "MEDG", "MEDH", "MEDI", "MGMT", "MICB", "MIDW", "MINE", "MLED", "MMAT", "MMPE", "MRNE", "MTRL", "MUED", "MUSC", "NAME", "NEST", "NRSC", "NURS", "OBMS", "OBST", "OCCH", "OCGY", "OHS", "OMSS", "ONCO", "OPTH", "ORBI", "ORNT", "ORPA", "OSOT", "PAED", "PATH", "PCTH", "PERS", "PETE", "PHAR", "PHIL", "PHRM", "PHTH", "PHYL", "PHYS", "PLAN", "PLNT", "POLI", "POLS", "PORT", "PPEN", "PRIN", "PSYC", "PSYT", "PUNJ", "RADI", "READ", "RELG", "RES", "RGLA", "RGLT", "RHSC", "RMES", "RMST", "RSOT", "RSPT", "RUSS", "SANS", "SCAN", "SCED", "SCIE", "SEAL", "SLAV", "SOAL", "SOCI", "SOIL", "SOWK", "SPAN", "SPHA", "SPPH", "SSED", "STAT", "STS", "SURG", "SWED", "SWFS", "THTR", "TIBT", "TSED", "UDES", "UFOR", "URDU", "URO", "URST", "URSY", "VANT", "VISA", "VRHC", "WMST", "WOOD", "WRDS", "WRIT", "ZOOL"]

def section_dict_factory(cursor, row):
    d = {}
    d["grades"] = {}
    d["stats"] = {}
    for idx, col in enumerate(cursor.description):
        # Temporary. Need to use json1 plugin to nest results.
        if col[0] in grades_cat:
            d["grades"][col[0]] = row[idx]
        elif col[0] in stats_cat:
            d["stats"][col[0]] = row[idx]
        else:
            d[col[0]] = row[idx]
    return d

def basic_element_factory(cursor, row):
    # Returns only the element in the row
    for idx, col in enumerate(cursor.description):
        return row[idx]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        if row[idx] is not None: d[col[0]] = row[idx]
        #d[col[0]] = row[idx]
    return d