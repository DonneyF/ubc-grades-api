stats_cat = ["average", "stdev", "high", "low", "pass", "fail", "withdrew", "audit", "other"]
grades_cat = ["0-9%", "10-19%", "20-29%", "30-39%", "40-49%", "<50%", "50-54%", "55-59%", "60-63%", "64-67%", "68-71%", "72-75%", "76-79%", "80-84%", "85-89%", "90-100%"]
yearsessions = ["1996S", "1996W", "1997S", "1997W", "1998S", "1998W", "1999S", "1999W", "2000S", "2000W", "2001S", "2001W", "2002S", "2002W", "2003S", "2003W", "2004S", "2004W", "2005S", "2005W", "2006S", "2006W", "2007S", "2007W", "2008S", "2008W", "2009S", "2009W", "2010S", "2010W", "2011S", "2011W", "2012S", "2012W", "2013S", "2013W", "2014S", "2014W", "2015S", "2015W", "2016S", "2016W", "2017S", "2017W", "2018S", "2018W"]

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

def arr_to_dict(arr, key):
    return {ele.pop(key):ele for ele in arr}