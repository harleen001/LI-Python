personal_details={"Name":"Harleen","Class":10,"Rollno":11}
academic_details={"Mathsmarks":50,"Chemistrymarks":90,"Englishmarks":80}
items_1=list(personal_details.items())
items_2=list(academic_details.items())
final_dictionary=dict(items_1+items_2)
print(final_dictionary)