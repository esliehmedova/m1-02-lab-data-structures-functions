def check_keys(tickets):
    n=0
    for dictionary in tickets:
        if set(dictionary.keys())!=set(key_list):
            n=n+1
            return n
    return "All good" 

def invalid_records(tickets):
    m=0
    for i in tickets:
        values = i.values()
        if "nan" in values or "" in values:
            m=m+1
    return m 

def report_dict(tickets):
    rep_dict = {}
    rep_dict["first"] = cat_count
    rep_dict["second"] = cat_res_min_sum
    rep_dict["third"] = cat_avg
    rep_dict["forth"] = esc_rate_cat
    rep_dict["fifth"] = cust_count
    return rep_dict
