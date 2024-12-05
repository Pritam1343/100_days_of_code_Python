# travel_log={
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"]
# }
# print(travel_log["France"][1])

travel_log={
    "France":{
        "Cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
    },
    "Germany":{
        "Cities_visited":["Stuttgart","Berlin"],
        "total_visits":5
    } 
}
print(travel_log["Germany"]["Cities_visited"][0])