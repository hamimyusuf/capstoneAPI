import uuid, shortuuid

def makeId():
    uid = uuid.uuid4()
    s = shortuuid.encode(uid)
    shortid = s[:10]
    return shortid