
def voc_and_cons_count(string):
    vowels="aeiouAEIOU"
    v_count=0
    c_count=0
    for character in string:
        if character.isalpha():
            if character in vowels:
                v_count+=1
            else:
                c_count+=1    
    return v_count,c_count
v_count,c_count=voc_and_cons_count("iamanilyarlagadda") 
print(f"vowels count is {v_count}")   
print(f"consonants count is {c_count}")
