closet = {
    "shirts": {
        "blue": 4,
        "black": 1,
        "white": 13,
        "flamingo-pink": 2
    },
    "pants": {
        "shorts": {
            "purple": 1,
            "red": 2,
            "flamingo-pink": 3
        },
        "jeans": {
            "denim": 8,
            "organic": 1
        }
    },
    "jackets": {}
}

# 1. There are 3 keys in the closet: shirts, pants, jackets

# 2.
print(closet["shirts"]["white"])

# 3.
print(closet["pants"]["shorts"]["flamingo-pink"])

# 4.
pink_shorts = closet["pants"]["shorts"]["flamingo-pink"]
pink_shirts = closet["shirts"]["flamingo-pink"]

if pink_shirts > pink_shorts:
    print("top")
else:
    print("bottom")