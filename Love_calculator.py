def calculate_love_score(name1,name2):
    combined_names=(name1+name2).lower()
    t=combined_names.count("t")
    r=combined_names.count("r")
    u=combined_names.count("u")
    e=combined_names.count("e")
    true_count=t+r+u+e
    print(true_count)
    l=combined_names.count("l")
    o=combined_names.count("o")
    v=combined_names.count("v")
    e=combined_names.count("e")
    love_count=l+o+v+e
    print(love_count)
    love_score=(str(true_count)+str(love_count))
    print("your love score is",love_score)

calculate_love_score("poorvith","manya")    
    
    