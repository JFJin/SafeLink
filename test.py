from sklearn import svm
from urllib.parse import urlparse

link = "https://www.coolmath.com/"
domain_name = urlparse(link).netloc
scheme = urlparse(link).scheme
path = urlparse(link).path

print(domain_name)
print(scheme)
print(path)






def example():
    msg = ["https://www.coolmath.com/#main-content",
    "https://www.coolmathgames.com/",
    "https://www.coolmath.com/",
    "https://www.coolmath.com/prealgebra",
    "https://www.coolmath.com/algebra",
    "https://www.coolmath.com/precalculus-review-calculus-intro",
    "https://www.coolmath.com/0-cool-math-games-and-problems",
    "https://www.coolmath.com/reference/online-math-dictionary",
    "https://www.coolmath.com/math-anxiety-survival-guide",
    "https://www.coolmath4kids.com/",
    "https://www.coolmath.com/reference/geometry-trigonometry-reference",
    "https://www.coolmath.com/0-teacher-success-area-prealgebra-algebra-precalculus",
    "https://www.coolmathgames.com/",
    "https://www.coolmath.com/prealgebra",
    "https://www.coolmath.com/prealgebra/00-factors-primes",
    "https://www.coolmath.com/prealgebra/02-decimals",
    "https://www.coolmath.com/algebra",
    "https://www.coolmath.com/algebra/01-exponents",
    "https://www.coolmath.com/algebra/08-lines",
    "https://www.coolmath.com/",
    "https://www.bit.ly/badthings",
    "https://www.clicktobehacked.net/noob",
    "https://www.coolblox.com/hackerman",
    "https://www.coolmethgames.com/illegal",
    "https://www.coolmath.net/notcoolmath",
    "https://www.coolmath.poop/yes",
    "https://www.clicktokillyourself.com/hitman",
    "https://www.coolmath.com/pitbull/ninja/virus/yes/longname/longerwordthanlongname/yesbutno/iamoutofideas"
    ]

    links = msg
    domain = "www.coolmath.com"
    data = [
        [5,5,5,5,5],
        [2,2,2,2,2],
        [1,1,1,1,1],
        [2,3,4,2,2],
        [5,4,5,5,4],
        [5,1,5,4,4],
        [5,5,2,5,2],
        [5,1,5,1,4],
        [1,5,3,5,1],
        [5,2,5,1,3],

    ]

    s = ['safe','unsafe', 'unsafe','unsafe', 'safe', 'safe', 'unsafe','unsafe', 'unsafe', 'unsafe']


    rec_model = svm.SVC()
    rec_model.fit(data, s)

    badlinks = []
    for link in links:
        values = [bitly(link), redirect(link), blog(link), OOD(link, domain), end(link)]
        print(values)
        safe_link = rec_model.predict([values])
        data.append(values)
        s.append(safe_link[0])
        print (link, safe_link[0])
        if safe_link[0] == 'unsafe':
            badlinks.append(link)

    #safe_link = rec_model.predict([[8,1,20,8,1,2]])
    #return json.dumps(str(my_game))

    return badlinks

def redirect(link: str):
    if link.count("redirect") > 1:
        return 1
    if "redirect" in link:
        return 2
    return 5

def bitly(link: str):
    if "bit.ly" in link:
        return 1
    return 5

def blog(link: str):
    if "blog" in link:
        return 3
    return 5

def OOD(link: str, dom: str):
    name = dom.split('.')[1]
    if name in link:
        return 5
    return 1



def end(link: str):
    ending = urlparse(link).netloc[:-3]
    if checkEndings(ending) is not None:
        return checkEndings(ending)
    else:
        return 3




    # ending = link.split('.')
    # p1 = ending[-1]
    # p2 = ending[-2]

    # ans1 = checkEndings(p1[:3])
    # ans2 = checkEndings(p2[:3])
    # if ans1 is not None:
    #     return ans1
    # if ans2 is not None:
    #     return ans2
    # return 3

    #if p1[0:3] == 'gov':
        #return 5
    #if p1[0:3] == 'edu':
        #return 4
    #if p1[0:3] == 'net':
        #return 2
    #if p1[0:3] == 'com':
        #return 3
    #if p1[0:3] == 'org':
        #return 3
    #if p1[0:2] == 'io' or p1[0:2] == 'bz':
       #return 1
    #return 1

def checkEndings(s):
    if s == 'gov':
        return 5
    if s == 'edu':
        return 4
    if s == 'net':
        return 2
    if s == 'com':
        return 3
    if s == 'org':
        return 3
    if s == '.io' or s == '.bz':
        return 1
    return 1

def countdigits(link):
    count = 0
    for ch in link:
        if ch.isdigit():
            count += 1
    if count > 50:
        return 0
    elif count > 30:
        return 1
    elif count >= 20:
        return 3
    else:
        return 5


def length(link):
    count = len(link)
    if count > 100:
        return 1
    if count > 80:
        return 3
    else:
        return 5


print(countdigits('http://www.get5rich.com/home/id=7283473897972374234/how_to_get_f4m0us839423948394/about.html'))
print(length('http://www.get5rich.com/home/id=7283473897972374234/how_to_get_f4m0us839423948394/about.html'))

#print(example())