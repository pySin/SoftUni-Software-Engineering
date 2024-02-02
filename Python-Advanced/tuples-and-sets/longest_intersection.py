# Longest Intersection


n = int(input())

top_intersection = set()

for _ in range(n):
    range_1, range_2 = [range(int(x.split(",")[0]), int(x.split(",")[1]) + 1) for x in input().split("-")]
    # print(set(range_1), set(range_2))
    intersection = set(range_1) & set(range_2)
    if len(intersection) > len(top_intersection):
        top_intersection = intersection

intersection_values = ", ".join([str(a) for a in top_intersection])
print(f"Longest intersection is [{intersection_values}] with length {len(top_intersection)}")
