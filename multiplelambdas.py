"""
pros = ["Michael", "Mary", "Ann", "Nick", "Dan", "Mark"]

distances = [12, 10, 19, 15, 5, 20]

travelPreferences = [12, 8, 25, 10, 3, 10]

# the output should be
#requestMatching(pros, distances, travelPreferences) = 
#["Michael", "Ann", "Dan", "Mary", "Nick"].


def requestMatching(pros,distances,travelPreferences):
    match=[]
    nonmatch=[]
    output=[]
    i=0
    while i<len(distances):
        if distances[i]<=travelPreferences[i]:
            match.append([pros[i],distances[i]])
        else:
            nonmatch.append([pros[i],distances[i]-travelPreferences[i]])
        i+=1
    match=sorted(match, key=lambda x:x[0])
    match=sorted(match, key=lambda x:x[1])
    print("match sorted is", match)
    nonmatch=sorted(nonmatch, key=lambda x: x[0])
    nonmatch=sorted(nonmatch, key=lambda x: x[1])
    print("nonmatch sorted is",nonmatch)
    for elem in match:
        output.append(elem[0])
    for elem in nonmatch:
        output.append(elem[0])
    print(output)
    if len(output)>5:
        return output[:5]
    else:
        return output
    
requestMatching(pros, distances, travelPreferences) CORRECT